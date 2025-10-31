# macOS Quick Start - Skip Local Build

The easiest way to publish your Vandal Hearts guide on macOS is to **skip the local build** and let GitHub Pages build it for you automatically.

---

## ✅ Recommended: Direct GitHub Deployment

### Why This Approach?

- ✅ No Ruby version issues
- ✅ No dependency problems
- ✅ GitHub builds it automatically
- ✅ Faster and simpler
- ✅ Same result as local build

### Steps:

#### 1. Create GitHub Repository

```bash
# You've already done the git setup, so just:
cd "/Users/ianbullard/Downloads/Vandal Hearts"

# Add GitHub remote
git remote add origin https://github.com/IanBullard/vandal-hearts-guide.git

# Push to GitHub
git push -u origin main
```

#### 2. Enable GitHub Pages

1. Go to: https://github.com/IanBullard/vandal-hearts-guide
2. Click **Settings** → **Pages**
3. Source: **Deploy from branch main**, folder **/ (root)**
4. Click **Save**
5. Wait 2-3 minutes

#### 3. View Your Site

Visit: https://ianbullard.github.io/vandal-hearts-guide/

**That's it!** GitHub builds and hosts it for free.

---

## 🔧 Alternative: Fix Local Build (Advanced)

If you really want to build locally, here are your options:

### Option A: Install Homebrew Ruby (Recommended)

```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install rbenv (Ruby version manager)
brew install rbenv

# Install Ruby 3.1
rbenv install 3.1.4
rbenv global 3.1.4

# Add to shell (choose your shell)
echo 'eval "$(rbenv init - zsh)"' >> ~/.zshrc
source ~/.zshrc

# Verify Ruby version
ruby --version  # Should show 3.1.4

# Now go back to project and install
cd "/Users/ianbullard/Downloads/Vandal Hearts"
bundle install
bundle exec jekyll serve

# Visit: http://localhost:4000/vandal-hearts-guide/
```

### Option B: Use Docker (No Ruby Install Needed)

```bash
cd "/Users/ianbullard/Downloads/Vandal Hearts"

# Run Jekyll in Docker
docker run --rm -v "$PWD":/srv/jekyll -p 4000:4000 jekyll/jekyll:latest jekyll serve

# Visit: http://localhost:4000/vandal-hearts-guide/
```

### Option C: Simplified Gemfile (Quick Fix)

Update your Gemfile to avoid problematic dependencies:

```ruby
source "https://rubygems.org"

gem "jekyll", "~> 3.9"
gem "just-the-docs", "0.7.0"
gem "webrick", "~> 1.7"
```

Then:
```bash
bundle update
bundle install
bundle exec jekyll serve
```

---

## 📝 Comparison

| Method | Pros | Cons | Difficulty |
|:-------|:-----|:-----|:-----------|
| **GitHub Pages** | ✅ Free, automatic, no setup | ⚠️ Can't preview locally | ⭐ Easy |
| **Homebrew Ruby** | ✅ Full local preview | ⚠️ Time to install | ⭐⭐ Medium |
| **Docker** | ✅ Clean, isolated | ⚠️ Requires Docker | ⭐⭐ Medium |
| **Simplified Gemfile** | ✅ Quick fix | ⚠️ May have limitations | ⭐⭐⭐ Advanced |

---

## 🎯 My Recommendation

**Just use GitHub Pages!**

You don't need to build locally to make changes. Your workflow will be:

1. Edit markdown files locally
2. Commit and push to GitHub
3. GitHub builds automatically
4. View changes in 1-2 minutes

**This is actually how most people use Jekyll + GitHub Pages.**

---

## ❓ Troubleshooting

### "Why can't I build locally?"

The issue is macOS system Ruby (2.6.10) is too old for Jekyll 4.3 and has compatibility issues with native extensions like `google-protobuf`.

### "What if I need to preview changes?"

Most markdown changes can be previewed right in your text editor or IDE. For complex changes, just push to GitHub and check in 1-2 minutes.

### "Can I fix the system Ruby?"

Not recommended - macOS needs its system Ruby. Always use a version manager (rbenv, chruby) for development.

---

## ✨ Bottom Line

**Skip the local build headache. Push to GitHub and let it handle everything!**

```bash
# Your workflow:
git add .
git commit -m "Update content"
git push

# Wait 1-2 minutes, refresh browser
# https://ianbullard.github.io/vandal-hearts-guide/
```

**Simple. Fast. It just works.** 🎉
