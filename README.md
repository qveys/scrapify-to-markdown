# 🌐 Scrapify to Markdown

Web scraper that crawls websites and converts pages to Markdown format with real-time progress tracking.

## ✨ Features

- **Same-domain crawling**: Automatically discovers and follows internal links
- **Markdown conversion**: Converts HTML pages to clean Markdown files
- **Real-time progress**: Live dashboard with statistics and time tracking
- **Smart deduplication**: Avoids revisiting pages and handles URL normalization
- **Error handling**: Graceful error management with detailed statistics

## 🚀 Quick Start

### Installation

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Usage

```bash
python script.py
```

Enter the starting URL when prompted. The scraper will:
1. Crawl all pages on the same domain
2. Convert each page to Markdown
3. Save files in `markdown_pages_<domain>/`

## 📊 Progress Display

```
🔍 Page en cours d'analyse : https://example.com/page
🌀 15 liens trouvés sur cette page

|-----------------------|
|     🚀 Progression    |
|-----------------------|
| Converties |    245 |
| Restantes  |     38 |
| Visitées   |    123 |
| Erronées   |      2 |
| Parcourus  |   1057 |
|-----------------------|

⏱️  Temps écoulé : 02:34
```

## 🛠️ Technical Details

### Dependencies

- **requests**: HTTP requests handling
- **beautifulsoup4**: HTML parsing
- **markdownify**: HTML to Markdown conversion

### URL Filtering

The scraper automatically ignores:
- Query parameters (`?param=value`)
- URL fragments (`#section`)
- External domains
- Binary files (`.pdf`, `.jpg`, `.png`, `.gif`)

### File Naming

Files are named based on URL paths:
- `https://example.com/docs/guide` → `docs_guide.md`
- Duplicate paths get numbered suffixes: `page.md`, `page_1.md`, etc.

## 📁 Output Structure

```
markdown_pages_<domain>/
├── index.md
├── about.md
├── docs_getting-started.md
└── ...
```

Each file includes:
- Original URL as header
- Converted Markdown content

## 🎯 Example

```bash
$ python script.py
Entrez l'URL de départ: https://docs.flutter.dev
🎯 Démarrage du crawling de https://docs.flutter.dev
📁 Dossier de sortie: markdown_pages_docs_flutter_dev/
```

Results in 632+ Markdown files from Flutter documentation.

## 📝 License

MIT

