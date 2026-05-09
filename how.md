# BD Landing Page — Instructions de déploiement

## Structure du projet
```
bd-landing-page/
├── index.html
├── assets/
│   ├── bd.jpg              ← image hero / upsell
│   ├── moyens-paiement.png
│   └── proofs/             ← captures de témoignages
```

## Git — Premier push
```bash
cd bd-landing-page
git init
git add .
git commit -m "init: bd-landing-page"
git remote add origin https://github.com/TON_COMPTE/bd-landing-page.git
git push -u origin main
```

## Cloudflare Pages
1. Dashboard Cloudflare → **Pages** → **Create a project**
2. Connecter le repo GitHub `bd-landing-page`
3. Framework preset : **None**
4. Build command : *(laisser vide)*
5. Build output directory : `/` (racine)
6. Déployer !

## Cloudflare Web Analytics
Remplacer `VOTRE_TOKEN_ICI` dans `index.html` par le token fourni dans le dashboard Cloudflare.
