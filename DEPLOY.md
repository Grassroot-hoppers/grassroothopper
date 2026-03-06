# Getting Everything Online — Step-by-Step

*For Julien. Do these in order. Should take ~30 minutes.*

---

## Step 1: Create the Repo Under the Org

The org is already created at https://github.com/Grassroot-hoppers

1. Go to https://github.com/organizations/Grassroot-hoppers/repositories/new
2. Repository name: **grassroothopper** (URL becomes `github.com/Grassroot-hoppers/grassroothopper`)
3. Public repo
4. Don't initialize with README (you already have one)
5. Create the repo

## Step 2: Push the Code

From your terminal, inside the Grassroots Hopper folder:

```bash
# Add the new remote (keep the old one as a backup)
git remote rename origin old-origin
git remote add origin https://github.com/Grassroot-hoppers/grassroothopper.git

# Push everything
git push -u origin main
```

## Step 3: Enable GitHub Pages

1. Go to https://github.com/Grassroot-hoppers/grassroothopper/settings/pages
2. Under **Source**, select **GitHub Actions** (not "Deploy from a branch")
3. The workflow file (`.github/workflows/pages.yml`) is already in the repo — it'll deploy `website/` automatically on push
4. Wait 1-2 minutes for the first deploy

## Step 4: Set Up the Custom Domain (grassroothopper.com)

**In GitHub:**
1. Still on the Pages settings page
2. Under **Custom domain**, type `grassroothopper.com`
3. Click **Save**
4. Check **Enforce HTTPS** once it becomes available (takes a few minutes)

**At your domain registrar (for grassroothopper.com):**

Add these DNS records:

| Type | Name | Value |
|------|------|-------|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | Grassroot-hoppers.github.io |

These are GitHub's official IPs for Pages custom domains. The `CNAME` file in the `website/` folder is already set to `grassroothopper.com`.

## Step 5: Point the Other Domains (.org, .eu, .be)

For each of the other three domains, you have two options:

### Option A: DNS redirect (simplest)
At each registrar, set up a **URL redirect / forwarding** from the domain to `https://grassroothopper.com`. Most registrars have this built in.

| Domain | Redirect to |
|--------|-------------|
| grassroothopper.org | https://grassroothopper.com |
| grassroothopper.eu | https://grassroothopper.com |
| grassroothopper.be | https://grassroothopper.com |

### Option B: All domains serving the same site
If you want all four domains to show the site directly (no redirect), you'll need to:
1. Add each as a custom domain in GitHub Pages settings (one at a time, verify each)
2. Add the same A records and CNAME for each domain at its registrar

**Recommendation:** Start with Option A (redirects). It works immediately and you can upgrade later.

## Step 6: Verify It Works

After DNS propagation (5 minutes to 48 hours, usually fast):

- [ ] https://grassroothopper.com loads the initiative pitch deck
- [ ] https://grassroothopper.com/social-v2.html loads the Social Media V2 deck
- [ ] https://grassroothopper.com/david-retail.html loads the David Retail deck
- [ ] grassroothopper.org redirects to grassroothopper.com
- [ ] grassroothopper.eu redirects to grassroothopper.com
- [ ] grassroothopper.be redirects to grassroothopper.com
- [ ] HTTPS works (green lock)

## Step 7: (Optional) Archive the Old Repo

Once everything is live on the new org:

1. Go to https://github.com/raclettemeister/grassroothopper/settings
2. Scroll to **Danger Zone**
3. Click **Archive this repository**
4. Or: **Transfer** the repo to the Grassroot-hoppers org (preserves stars/issues)

---

## Quick Reference: What's Where

| URL | What it serves |
|-----|---------------|
| grassroothopper.com | Initiative pitch deck (index.html) |
| grassroothopper.com/social-v2.html | Social Media V2 pitch deck |
| grassroothopper.com/david-retail.html | David Retail pitch deck |
| github.com/Grassroot-hoppers/grassroothopper | The full repo (initiative + products + website) |

---

*Once this is live, you have a killer pitch URL to send to Rob Hopkins, Bonfire, CoopCycle, and anyone else.*
