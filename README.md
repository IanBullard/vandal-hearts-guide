# Vandal Hearts Complete Guide

A comprehensive guide and FAQ collection for **Vandal Hearts** (PlayStation, 1997), consolidating information from six classic FAQs into a modern, searchable format.

🎮 **[View the Live Guide](https://ianbullard.github.io/vandal-hearts-guide/)**

## 🎮 About Vandal Hearts

Vandal Hearts is a tactical role-playing game developed by Konami for the Sony PlayStation. This guide combines strategies, battle data, character information, and secrets from multiple community-created FAQs into one searchable, easy-to-navigate website.

## 📚 What's Included

This guide covers:

- **12 Playable Characters** - Backgrounds, stats, and strategies
- **8 Job Class Paths** - Detailed analysis and recommendations
- **40+ Story Battles** - Turn-by-turn strategies
- **6 Trials of Toroah** - Optional challenges for Ash's ultimate class
- **Complete Item Database** - Weapons, armor, spells, and secrets
- **Act-by-Act Walkthrough** - Full story progression guide

## 🚀 Quick Start

### Prerequisites

- Ruby 2.7+ (check with `ruby --version`)
- Bundler (`gem install bundler`)

### Installation

1. Navigate to this directory:
   ```bash
   cd "/Users/ianbullard/Downloads/Vandal Hearts"
   ```

2. Install dependencies:
   ```bash
   bundle install
   ```

3. Run the development server:
   ```bash
   bundle exec jekyll serve
   ```

4. Open your browser to:
   ```
   http://localhost:4000
   ```

### Building for Production

To generate static HTML files:

```bash
bundle exec jekyll build
```

Files will be generated in the `_site/` directory.

## 📁 Site Structure

```
vandal-hearts-guide/
├── _config.yml              # Jekyll configuration
├── Gemfile                  # Ruby dependencies
├── index.md                 # Home page
│
├── characters/              # Character guides
│   ├── index.md
│   ├── ash-lambert.md
│   ├── clint-picard.md
│   └── ...
│
├── job-classes/             # Job class analysis
│   ├── index.md
│   ├── hero.md
│   ├── knight.md
│   └── ...
│
├── walkthrough/             # Story progression
│   ├── index.md
│   ├── act-1/
│   ├── act-2/
│   └── ...
│
├── battles/                 # Battle-specific strategies
│   ├── index.md
│   └── ...
│
├── trials/                  # Trials of Toroah guides
│   ├── index.md
│   ├── nova.md
│   ├── earth.md
│   └── ...
│
├── items/                   # Equipment and items
│   ├── weapons.md
│   ├── armor.md
│   └── consumables.md
│
├── reference/               # Quick reference tables
│   ├── spells.md
│   ├── enemy-data.md
│   └── secrets.md
│
└── credits.md               # FAQ author attribution
```

## 🎨 Theme

This site uses [Just the Docs](https://just-the-docs.github.io/just-the-docs/), a modern documentation theme with:

- ✅ Built-in search functionality
- ✅ Automatic navigation generation
- ✅ Mobile-responsive design
- ✅ Dark/light mode toggle
- ✅ Syntax highlighting
- ✅ Automatic table of contents

## 🛠️ Customization

### Changing the Color Scheme

Edit `_config.yml`:

```yaml
color_scheme: dark  # Options: "light" or "dark"
```

### Adding New Pages

1. Create a new Markdown file in the appropriate directory
2. Add front matter:
   ```yaml
   ---
   layout: default
   title: Page Title
   parent: Parent Section
   nav_order: 1
   ---
   ```
3. Write content in Markdown

### Navigation Order

Control page order with `nav_order` in front matter:

```yaml
nav_order: 1  # Lower numbers appear first
```

## 📝 Content Sources

This guide consolidates information from six FAQ authors:

| Author | Focus | Version | Year |
|:-------|:------|:--------|:-----|
| **Jeff Chan (Atom Edge)** | Character & Job Class Guide | 4.0 | 2002 |
| **Lancel0t** | Walkthrough & Strategy | 0.9a | 1997 |
| **Shotgunnova** | Comprehensive FAQ | - | - |
| **Syonyx** | Detailed Guide | - | - |
| **Richard Uyeyama** | Battle Data & Reference | 1.1 | 1997 |
| **Wolverine Inc.** | Perfect Battle Tactics | - | 1997 |

All original FAQ files are preserved in the root directory (`*.txt` files).

## 🚢 Deployment Options

### GitHub Pages (Recommended)

1. **Create a new GitHub repository** named `vandal-hearts-guide`
2. **Push this project** (see instructions below)
3. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Source: Deploy from branch `main`, folder `/ (root)`
   - Click Save
4. **Wait 2-3 minutes** for deployment
5. **Site will be live at:** `https://yourusername.github.io/vandal-hearts-guide/`
6. **Update _config.yml** with your GitHub username (see setup instructions below)

### Netlify (Free)

1. Create account at [netlify.com](https://www.netlify.com/)
2. Connect to your GitHub repository
3. Build command: `jekyll build`
4. Publish directory: `_site`
5. Deploy!

### Manual Hosting

Build the site and upload the `_site/` directory to any web server.

## 🐛 Troubleshooting

### Bundler errors

```bash
bundle update
bundle install
```

### Jekyll won't start

Check Ruby version:
```bash
ruby --version  # Should be 2.7 or higher
```

### Changes not appearing

Force rebuild:
```bash
bundle exec jekyll clean
bundle exec jekyll serve
```

## 📜 Copyright & License

- **Game Content**: © Konami Co., Ltd. All rights reserved.
- **FAQ Content**: © Respective authors (see credits)
- **This Compilation**: Assembled for educational and archival purposes

Original FAQs were distributed freely in the gaming community (1997-2002). This project preserves and organizes that community knowledge.

## 🤝 Contributing

Found an error or want to add content?

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📧 Contact

Questions or suggestions? Open an issue on GitHub or contact the maintainer.

## 🙏 Acknowledgments

Special thanks to:
- All six FAQ authors for their incredible work
- The Vandal Hearts community
- Konami for creating this classic game
- The Just the Docs theme developers

---

**Happy strategizing! 🎮⚔️**
