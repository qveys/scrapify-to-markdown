import os
import requests
import sys
import time
import threading
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from markdownify import markdownify as md

def is_same_domain(base_url, test_url):
    """Vérifie si les deux URLs appartiennent au même domaine."""
    base_domain = urlparse(base_url).netloc
    test_domain = urlparse(test_url).netloc
    return base_domain == test_domain

def get_all_links(url, base_url, stats):
    """Récupère tous les liens de la page qui appartiennent au même domaine."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = set()
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            full_url = urljoin(url, href)
            # Ignorer les liens avec des query parameters ou des ancres
            if '?' in full_url or '#' in full_url:
                continue
            
            # Normaliser l'URL en supprimant le "/" final (sauf pour la racine)
            if full_url.endswith('/') and len(urlparse(full_url).path) > 1:
                full_url = full_url[:-1]
            
            if is_same_domain(base_url, full_url) and not full_url.endswith(('.pdf', '.jpg', '.png', '.gif')):
                links.add(full_url)
        
        stats['links_found'] += len(links)
        return links
    except Exception as e:
        stats['errors'] += 1
        return set()

def save_as_markdown(url, output_dir, stats):
    """Sauvegarde le contenu de l'URL en Markdown."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        html = response.text
        markdown = md(html)
        parsed_url = urlparse(url)
        
        # Créer un nom de fichier basé sur le chemin de l'URL
        path = parsed_url.path.strip('/').replace('/', '_') or 'index'
        base_filename = f"{output_dir}/{path}.md"
        
        # Créer le dossier parent si nécessaire
        os.makedirs(os.path.dirname(base_filename), exist_ok=True)
        
        # Vérifier si le fichier existe et créer un nom unique si nécessaire
        filename = base_filename
        counter = 1
        while os.path.exists(filename):
            name_part = base_filename[:-3]  # Enlever .md
            filename = f"{name_part}_{counter}.md"
            counter += 1
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# {url}\n\n{markdown}")
        
        stats['pages_converted'] += 1
        return True
    except Exception as e:
        stats['errors'] += 1
        return False

def clear_screen():
    """Efface l'écran et remet le curseur en haut."""
    os.system('clear' if os.name == 'posix' else 'cls')

def display_progress(current_url, links_found, stats, start_time):
    """Affiche le progrès dans un format structuré."""
    # Effacer l'écran
    clear_screen()
    
    # Affichage de la page en cours
    print(f"🔍 Page en cours d'analyse : {current_url}")
    print(f"🌀 {links_found} liens trouvés sur cette page")
    print()
    
    # Tableau de progression
    print("|-----------------------|")
    print("|     🚀 Progression    |")
    print("|-----------------------|")
    print(f"| Converties |   {stats['pages_converted']:6d} |")
    print(f"| Restantes  |   {stats['remaining']:6d} |")
    print(f"| Visitées   |   {stats['already_visited']:6d} |")
    print(f"| Erronées   |   {stats['errors']:6d} |")
    print(f"| Parcourus  |   {stats['links_found']:6d} |")
    print("|-----------------------|")
    print()
    print()
    
    # Temps écoulé
    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print(f"⏱️  Temps écoulé : {minutes:02d}:{seconds:02d}")
    print()

def crawl(url, base_url, output_dir, start_time):
    """Parcourt itérativement les liens du même domaine."""
    visited = set()
    queue = [url]  # Queue des URLs à traiter
    stats = {'pages_converted': 0, 'remaining': 0, 'links_found': 0, 'errors': 0, 'already_visited': 0}
    
    while queue:
        current_url = queue.pop(0)  # Prendre la première URL de la queue
        
        # Marquer comme visitée AVANT de vérifier
        visited.add(current_url)
        
        # Traiter la page
        save_as_markdown(current_url, output_dir, stats)
        links = get_all_links(current_url, base_url, stats)
        
        # Ajouter les nouveaux liens à la queue (en évitant les doublons)
        new_links = []
        for link in links:
            if link not in visited and link not in queue:
                new_links.append(link)
            elif link in visited:
                stats['already_visited'] += 1
        
        queue.extend(new_links)
        
        # Ordonner la queue par ordre alphabétique
        queue.sort()
        
        # Mise à jour des statistiques
        stats['remaining'] = len(queue)
        
        # Affichage du progrès
        display_progress(current_url, len(links), stats, start_time)
        time.sleep(0.5)  # Pause pour voir l'affichage
    
    return stats

if __name__ == "__main__":
    start_url = input("Entrez l'URL de départ: ").strip()
    
    # Créer un dossier parent basé sur l'URL de base
    parsed_start_url = urlparse(start_url)
    domain_name = parsed_start_url.netloc.replace('www.', '').replace('.', '_')
    output_directory = f"markdown_pages_{domain_name}"
    os.makedirs(output_directory, exist_ok=True)
    
    print(f"🎯 Démarrage du crawling de {start_url}")
    print(f"📁 Dossier de sortie: {output_directory}/")
    print("=" * 60)
    input("Appuyez sur Entrée pour commencer...")
    
    start_time = time.time()
    stats = crawl(start_url, start_url, output_directory, start_time)
    
    end_time = time.time()
    clear_screen()
    print("=" * 60)
    print(f"🎉 Crawling terminé en {end_time - start_time:.2f} secondes!")
    print("=" * 60)
    print(f"📊 Statistiques finales:")
    print(f"   • Pages converties: {stats['pages_converted']}")
    print(f"   • Liens trouvés: {stats['links_found']}")
    print(f"   • Pages déjà visitées: {stats['already_visited']}")
    print(f"   • Erreurs: {stats['errors']}")
    print(f"📁 Fichiers sauvegardés dans: {output_directory}/")
