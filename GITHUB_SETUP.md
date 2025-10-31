# GitHub Setup Instructions

Step-by-step guide to publish your Vandal Hearts guide to GitHub Pages.

---

## Prerequisites

✅ Git repository initialized (done!)
✅ Initial commit created (done!)
✅ GitHub account (create at [github.com](https://github.com) if needed)

---

## Step 1: Create GitHub Repository

1. **Go to GitHub** and sign in: https://github.com

2. **Click the "+" icon** in the top right corner → "New repository"

3. **Configure repository:**
   - **Repository name:** `vandal-hearts-guide`
   - **Description:** "Complete guide for Vandal Hearts (PlayStation, 1997)"
   - **Visibility:** Public (required for free GitHub Pages)
   - **DO NOT initialize with:**
     - ❌ README (we already have one)
     - ❌ .gitignore (we already have one)
     - ❌ License (optional, can add later)

4. **Click "Create repository"**

---

## Step 2: Connect Local Repository to GitHub

GitHub will show you setup instructions. Use the "push an existing repository" option:

```bash
cd "/Users/ianbullard/Downloads/Vandal Hearts"

# Add GitHub as remote (REPLACE 'yourusername' with your actual GitHub username!)
git remote add origin https://github.com/yourusername/vandal-hearts-guide.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

**Example with actual username:**
```bash
git remote add origin https://github.com/ianbullard/vandal-hearts-guide.git
git branch -M main
git push -u origin main
```

---

## Step 3: Update Configuration Files

Before the site will work correctly, you need to update two files with your actual GitHub username.

### 3a. Update _config.yml

Open `_config.yml` and find these lines:

```yaml
baseurl: "/vandal-hearts-guide" # Line 4
```
✅ This is correct if your repo is named `vandal-hearts-guide`

```yaml
aux_links:
  "View on GitHub":
    - "//github.com/yourusername/vandal-hearts-guide" # Line 31 - UPDATE THIS!
```

**Change `yourusername` to your actual GitHub username:**
```yaml
aux_links:
  "View on GitHub":
    - "//github.com/ianbullard/vandal-hearts-guide"
```

### 3b. Update README.md

Open `README.md` and find line 5:

```markdown
🎮 **[View the Live Guide](https://yourusername.github.io/vandal-hearts-guide/)** ← Update this after setup
```

**Change to your actual username:**
```markdown
🎮 **[View the Live Guide](https://ianbullard.github.io/vandal-hearts-guide/)**
```

### 3c. Commit and Push Changes

```bash
git add _config.yml README.md
git commit -m "Update GitHub username in config"
git push
```

---

## Step 4: Enable GitHub Pages

1. **Go to your repository** on GitHub:
   ```
   https://github.com/yourusername/vandal-hearts-guide
   ```

2. **Click "Settings"** tab (near top right)

3. **Click "Pages"** in the left sidebar

4. **Configure source:**
   - **Source:** Deploy from a branch
   - **Branch:** main
   - **Folder:** / (root)
   - **Click "Save"**

5. **Wait 2-3 minutes** for initial deployment

6. **Check deployment:**
   - Refresh the Pages settings page
   - You'll see: "Your site is live at https://yourusername.github.io/vandal-hearts-guide/"
   - Click the link to view your site!

---

## Step 5: Verify Everything Works

### Check the Site

Visit: `https://yourusername.github.io/vandal-hearts-guide/`

**Test these items:**

✅ Home page loads correctly
✅ Navigation sidebar appears
✅ Search box works
✅ Character pages load
✅ Walkthrough pages load
✅ Trials pages load
✅ Reference pages load
✅ "View on GitHub" link works
✅ Internal links work (click around!)

### Troubleshooting

**If the site doesn't load:**

1. **Check Actions tab** in GitHub repository
   - Look for "pages build and deployment" workflow
   - Should be green checkmark
   - If red X, click to see error details

2. **Verify _config.yml settings:**
   ```yaml
   remote_theme: just-the-docs/just-the-docs
   baseurl: "/vandal-hearts-guide"
   ```

3. **Check GitHub Pages settings:**
   - Settings → Pages
   - Should show "Your site is published at..."

4. **Wait a bit longer:**
   - First deployment can take 5-10 minutes
   - Subsequent updates are faster (1-2 minutes)

5. **Clear browser cache:**
   - Hard refresh: Ctrl+F5 (Windows) or Cmd+Shift+R (Mac)

---

## Step 6: Future Updates

When you make changes to the guide:

```bash
# Make your changes to files

# Stage changes
git add .

# Commit with a message
git commit -m "Description of your changes"

# Push to GitHub
git push

# Site will automatically rebuild in 1-2 minutes!
```

---

## Repository Structure on GitHub

Your repository will contain:

```
vandal-hearts-guide/
├── .gitignore               ✅ Committed
├── _config.yml              ✅ Committed
├── Gemfile                  ✅ Committed
├── README.md                ✅ Committed
├── index.md                 ✅ Committed
├── credits.md               ✅ Committed
├── characters/              ✅ Committed (12 files)
├── job-classes/             ✅ Committed (9 files)
├── walkthrough/             ✅ Committed (7 files)
├── trials/                  ✅ Committed (7 files)
├── reference/               ✅ Committed (5 files)
│
└── [NOT COMMITTED - Excluded by .gitignore]
    ├── .claude/             ❌ Local only
    ├── source/              ❌ Local only
    ├── TODO.md              ❌ Local only
    ├── CLAUDE.md            ❌ Local only
    └── *.txt files          ❌ Local only
```

---

## Optional: Custom Domain

If you want to use your own domain (like `vandal-hearts.com`):

1. **Buy a domain** from a registrar (Namecheap, Google Domains, etc.)

2. **Configure DNS:**
   - Add CNAME record pointing to: `yourusername.github.io`

3. **Update GitHub Pages settings:**
   - Settings → Pages
   - Custom domain: Enter your domain
   - Click Save
   - Enable "Enforce HTTPS" (after DNS propagates)

4. **Update _config.yml:**
   ```yaml
   url: "https://your-domain.com"
   baseurl: ""
   ```

---

## Optional: Add GitHub Actions Badge

Add a build status badge to your README.md:

```markdown
[![pages-build-deployment](https://github.com/yourusername/vandal-hearts-guide/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/yourusername/vandal-hearts-guide/actions/workflows/pages/pages-build-deployment)
```

---

## Summary

✅ **Step 1:** Created GitHub repository
✅ **Step 2:** Pushed code to GitHub
✅ **Step 3:** Updated config with your username
✅ **Step 4:** Enabled GitHub Pages
✅ **Step 5:** Verified site works
✅ **Step 6:** Know how to make updates

**Your site is live at:**
```
https://yourusername.github.io/vandal-hearts-guide/
```

**Share the link with fellow Vandal Hearts fans! 🎮⚔️**

---

## Getting Help

**If you encounter issues:**

1. **Check GitHub Pages documentation:**
   - https://docs.github.com/en/pages

2. **Check Just the Docs documentation:**
   - https://just-the-docs.github.io/just-the-docs/

3. **Common issues:**
   - Wrong baseurl → Fix in _config.yml
   - 404 errors → Check permalink paths
   - Theme not loading → Verify `remote_theme` setting
   - Build failures → Check GitHub Actions tab for errors

---

**Good luck! The Vandal Hearts community will appreciate your work! 🎉**
