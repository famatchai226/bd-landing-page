import re

with open('../kera-landing-page/index.html', encoding='utf-8') as f:
    h = f.read()

# ---- URLs ----
kera_url = 'https://baltazar.mymaketou.store/fr/products/acces-prive-et-discret-des-videos-dune-influenceuse/checkout'
bd_url = 'https://baltazar.mymaketou.store/fr/products/veut-tu-14838-pdf-bd-hentai-pour-homme-mature-/checkout'
h = h.replace(kera_url, bd_url)

# ---- Meta title & description ----
h = h.replace(
    "Accès Privé et Discret — Vidéos d'une Influenceuse | Baltazar",
    "Pack +14 838 BD Hentaï pour Homme Mature | Baltazar"
)
h = h.replace(
    "Accédez aux vidéos privées d'une influenceuse qui a fait le buzz. Canal Télégram privé et sécurisé. Offre exclusive et discrète via Baltazar.",
    "Accédez à notre collection exclusive de +14 838 BD hentaï en PDF pour homme mature et discret. Téléchargement immédiat via Baltazar."
)

# ---- Navbar ----
h = h.replace('href="#" class="nav-logo">KERA<span>TILWE</span>', 'href="#" class="nav-logo">BD<span>HENTAI</span>')
h = h.replace('>🔥 Acheter maintenant<', '>📚 Obtenir le Pack<')

# ---- Hero badge ----
h = h.replace('🔥 Promo Exclusive — Durée Limitée', '🔥 Offre Exclusive — +14 838 BD PDF')

# ---- Hero title ----
h = h.replace(
    "<em>Accès Privé et Discret</em><br />\n            aux Vidéos d'une Influenceuse<br />\n            qui a fait le Buzz 🔥",
    "<em>Pack +14 838 BD Hentaï</em><br />\n            pour Homme Mature et Discret<br />\n            Téléchargement Immédiat 📚"
)

# ---- Hero description ----
h = h.replace(
    "Toutes les vidéos sont déjà enregistrées dans le canal. Accès instantané via un\n            <strong>canal Télégram sécurisé</strong> — 100% privé,\n            livré dans votre email dès le paiement.",
    "Plus de <strong>14 838 BD hentaï en PDF</strong> pour homme mature — collection complète livrée directement par email dès le paiement. 100% discret."
)

# ---- CTA button ----
h = h.replace("J'en profite maintenant", "📚 J'obtiens le Pack")

# ---- Prices (hero) ----
h = h.replace('7&nbsp;700 FCFA', '13&nbsp;000 FCFA')
h = h.replace('10&nbsp;000 FCFA', '25&nbsp;768 FCFA')
h = h.replace('−23&nbsp;%', '−50&nbsp;%')

# ---- Anonymat note ----
h = h.replace(
    "recevoir le lien. Vous pouvez utiliser un\n              <strong>pseudonyme</strong> lors du paiement pour rester anonyme.",
    "recevoir vos fichiers PDF. Vous pouvez utiliser un <strong>pseudonyme</strong> lors du paiement pour rester anonyme."
)

# ---- Trust badges ----
h = h.replace('<span class="trust-icon">⚡</span> Accès instantané</span>', '<span class="trust-icon">⚡</span> Livraison immédiate</span>')
h = h.replace('<span class="trust-icon">📩</span> Lien par email</span>', '<span class="trust-icon">📩</span> Fichiers par email</span>')

# ---- Carousel images -> bd.jpg ----
for i in range(6):
    h = h.replace(f'./assets/hero caroussel/{i}.jpeg', './assets/bd.jpg')

# ---- Video section ----
h = h.replace(
    "Regarde cette video pour eviter de perdre du\n          temps",
    "Découvrez un aperçu de votre future collection"
)
h = h.replace('./assets/video/kera 7700.mp4', './assets/video/bd.mp4')
h = h.replace(
    "Regardez cette courte vidéo\n          pour comprendre le processus d'achat étape par étape.",
    "Regardez cette courte vidéo pour découvrir un aperçu de notre collection exclusive de BD adultes."
)

# ---- Stats strip ----
h = h.replace(
    '<span class="strip-number">🔥</span>\n        <span class="strip-label">Influenceuse Buzz</span>',
    '<span class="strip-number">14 838</span>\n        <span class="strip-label">BD Hentaï PDF</span>'
)
h = h.replace(
    '<span class="strip-label">Privé &amp; Discret</span>',
    '<span class="strip-label">Discret &amp; Légal</span>'
)
h = h.replace(
    '<span class="strip-label">Accès Instantané</span>',
    '<span class="strip-label">Livraison Immédiate</span>'
)
h = h.replace(
    '<span class="strip-number">+1&nbsp;850</span>\n        <span class="strip-label">Membres satisfaits</span>',
    '<span class="strip-number">+2 100</span>\n        <span class="strip-label">Clients satisfaits</span>'
)

# ---- What you get header ----
h = h.replace(
    "Un lien d'accès au canal Télégram contenant l'intégralité des vidéos de l'influenceuse.",
    "Un fichier ZIP contenant +14 838 BD hentaï en PDF, livré directement dans votre email."
)

# ---- Offer cards ----
h = h.replace(
    '<div class="offer-icon red">🎬</div>\n          <p class="label-upper" style="color: var(--primary); margin-bottom: 0.4rem;">Vidéos Exclusives</p>\n          <p class="title-lg">Toutes les vidéos</p>\n          <p class="offer-value">Valeur : <span>25 000 FCFA</span></p>\n          <p class="body-md" style="margin-top: 0.75rem; font-size:0.9rem;">\n            Toutes les vidéos de l\'influenceuse qui a fait le buzz — déjà enregistrées dans le canal.\n          </p>',
    '<div class="offer-icon red">📚</div>\n          <p class="label-upper" style="color: var(--primary); margin-bottom: 0.4rem;">Collection BD</p>\n          <p class="title-lg">+14 838 BD Hentaï PDF</p>\n          <p class="offer-value">Valeur : <span>25 768 FCFA</span></p>\n          <p class="body-md" style="margin-top: 0.75rem; font-size:0.9rem;">\n            Collection massive de BD hentaï pour adultes en PDF haute qualité — prête à télécharger.\n          </p>'
)
h = h.replace(
    '<div class="offer-icon gold">🔐</div>\n          <p class="label-upper" style="color: var(--secondary); margin-bottom: 0.4rem;">Accès Privé</p>\n          <p class="title-lg">Canal Sécurisé</p>\n          <p class="offer-value">Valeur : <span>7 700 FCFA</span></p>\n          <p class="body-md" style="margin-top: 0.75rem; font-size:0.9rem;">\n            Canal Télégram privé, 100% discret. Aucune trace sur ton téléphone visible par tes proches.\n          </p>',
    '<div class="offer-icon gold">📧</div>\n          <p class="label-upper" style="color: var(--secondary); margin-bottom: 0.4rem;">Livraison Sécurisée</p>\n          <p class="title-lg">Email 100% Discret</p>\n          <p class="offer-value">Valeur : <span>Inclus</span></p>\n          <p class="body-md" style="margin-top: 0.75rem; font-size:0.9rem;">\n            Livraison par email sécurisé. Aucune trace visible. Paiement avec pseudonyme possible.\n          </p>'
)
h = h.replace(
    '<div class="offer-icon dark">♾️</div>\n          <p class="label-upper" style="color: var(--on-surface-variant); margin-bottom: 0.4rem;">Accès Permanent</p>\n          <p class="title-lg">Accès à Vie</p>\n          <p class="offer-value">Valeur : <span>5 000 FCFA</span></p>\n          <p class="body-md" style="margin-top: 0.75rem; font-size:0.9rem;">\n            Une fois payé, tu gardes l\'accès au canal de façon permanente. Aucun abonnement.\n          </p>',
    '<div class="offer-icon dark">♾️</div>\n          <p class="label-upper" style="color: var(--on-surface-variant); margin-bottom: 0.4rem;">Propriété Complète</p>\n          <p class="title-lg">Fichiers à Vie</p>\n          <p class="offer-value">Valeur : <span>Inclus</span></p>\n          <p class="body-md" style="margin-top: 0.75rem; font-size:0.9rem;">\n            Une fois téléchargé, les fichiers t\'appartiennent. Aucun abonnement, aucune limite.\n          </p>'
)

# ---- Value callout ----
h = h.replace(
    '>30 000 FCFA<span\n              style="font-size:0.85rem; font-weight:400; color:var(--on-surface-variant);"> de contenu</span></p>',
    '>25 768 FCFA<span\n              style="font-size:0.85rem; font-weight:400; color:var(--on-surface-variant);"> de contenu</span></p>'
)
h = h.replace(
    '>7 700\n            FCFA</p>\n          <p style="font-size:0.85rem; color:var(--on-surface-variant); text-decoration:line-through;">10 000 FCFA</p>',
    '>13 000\n            FCFA</p>\n          <p style="font-size:0.85rem; color:var(--on-surface-variant); text-decoration:line-through;">25 768 FCFA</p>'
)

# ---- Why section -> adapt for BD ----
h = h.replace('Pourquoi Télégram ?', 'Pourquoi notre Pack ?')
h = h.replace('Ta vie privée,<br />notre priorité absolue', 'La plus grande collection<br />de BD adultes disponible')
h = h.replace(
    '100% Sécurisé</strong> — Télégram ne divulgue\n                jamais tes informations personnelles, contrairement à WhatsApp.',
    '+14 838 BD PDF</strong> — La plus grande collection de BD hentaï disponible à ce prix en Afrique francophone.'
)
h = h.replace(
    "Anonymat garanti</strong> — Tu peux même\n                utiliser un surnom lors du paiement. Nous ne voulons pas connaître ton identité.",
    "PDF haute qualité</strong> — Tous les fichiers sont en haute résolution, lisibles sur mobile, tablette ou PC."
)
h = h.replace(
    "Protection de tes proches</strong> — Plus\n                besoin de laisser WhatsApp exposé. Le canal Télégram est isolé et sécurisé.",
    "Livraison immédiate</strong> — Reçois ton fichier ZIP dans ta boîte email en moins de 5 minutes après paiement."
)
h = h.replace(
    "Livraison instantanée</strong> — Dès le\n                paiement validé, tu reçois le lien d'accès par email en quelques secondes.",
    "Prix imbattable</strong> — 13 000 FCFA pour +14 838 BD, soit moins de 1 FCFA par fichier. Introuvable ailleurs."
)
h = h.replace(
    "⚠️ <em>Si tu utilises un iPhone, accède via l'application Safari pour te connecter à Télégram.</em>",
    "⚠️ <em>Assurez-vous d'avoir de l'espace de stockage disponible sur votre appareil pour le pack complet.</em>"
)
h = h.replace(
    "Bon on se retrouve dans le\n            canal ! 🤜🏼🤛🏼",
    "Profite de la collection dès aujourd'hui ! 📚🔥"
)
h = h.replace(
    "Une fois ton paiement validé, tu seras automatiquement redirigé vers notre canal privé où\n              toutes les vidéos de l'influenceuse t'attendent.",
    "Une fois ton paiement validé, tu recevras un email avec le lien de téléchargement du pack complet de +14 838 BD hentaï en PDF."
)

# ---- Testimonials ----
h = h.replace('+1850 membres<br />nous font déjà confiance', '+2 100 clients<br />nous font déjà confiance')
h = h.replace(
    "J'ai reçu le lien en moins de 2 minutes après le paiement. Les vidéos sont toutes\n            là, je recommande à 100%.",
    "J'ai reçu le lien de téléchargement en 3 minutes. Le pack est énorme, des milliers de BD de qualité. Je recommande à 100%."
)
h = h.replace(
    "Franchement j'étais sceptique au départ, mais tout fonctionne parfaitement. La\n            discrétion est au rendez-vous et le contenu est top.",
    "J'étais sceptique mais j'ai tenté. Le fichier ZIP est arrivé rapidement et la qualité des BD est vraiment bonne."
)
h = h.replace(
    "Le contenu est exactement ce qui était annoncé. Toutes les vidéos de\n            l'influenceuse sont bien présentes. Télégram c'est vraiment pratique 👌",
    "Incroyable collection ! Plus de 14 000 fichiers comme promis. La livraison par email est simple et discrète 👌"
)
h = h.replace(
    'Rejoins la communauté de <strong style="color:var(--primary);">1850 membres\n            satisfaits</strong> et profite dès maintenant.',
    'Rejoins les <strong style="color:var(--primary);">2 100 clients satisfaits</strong> et accède à la collection dès maintenant.'
)

# ---- FAQ ----
h = h.replace('Comment est-ce que je reçois les vidéos ?', 'Comment est-ce que je reçois les fichiers ?')
h = h.replace(
    "Après ton paiement, tu reçois un PDF par email contenant le lien d'invitation au canal Télégram privé.\n            Toutes les vidéos de l'influenceuse y sont déjà enregistrées.\n            Assure-toi de saisir ton adresse email correctement lors de la commande.",
    "Après ton paiement, tu reçois un email avec le lien de téléchargement du pack ZIP (+14 838 BD hentaï PDF).\n            Assure-toi de saisir ton adresse email correctement lors de la commande."
)
h = h.replace(
    "Oui, totalement. Nous utilisons Télégram car il ne partage aucune information personnelle.\n            Tu peux même utiliser un surnom lors du remplissage de tes informations de paiement.\n            Nous ne cherchons pas à te connaître, seulement à te livrer le contenu.",
    "Oui, totalement. Tu peux utiliser un pseudonyme lors du paiement.\n            La livraison se fait par email et le contenu est un simple fichier ZIP — rien de visible sur ton téléphone."
)
h = h.replace("C'est quoi cette influenceuse qui a fait le buzz ?", "Combien de fichiers y a-t-il exactement ?")
h = h.replace(
    "Une influenceuse a fait le buzz dernièrement avec ses vidéos. Toutes ses vidéos ont été enregistrées dans\n            notre canal Télégram privé. Passe au paiement TOUT DE SUITE pour ne pas rater cette promo.",
    "Le pack contient exactement +14 838 fichiers PDF de BD hentaï. Assure-toi d'avoir de l'espace de stockage disponible sur ton appareil."
)
h = h.replace(
    "Une fois que tu rejoins le canal Télégram, tu y as accès de façon permanente.\n            Le contenu reste disponible aussi longtemps que le canal est actif.",
    "Une fois téléchargés, les fichiers t'appartiennent définitivement. Tu peux les transférer sur tous tes appareils sans limite."
)
h = h.replace("Je suis sur iPhone, est-ce compatible ?", "Les fichiers sont-ils compatibles avec tous les appareils ?")
h = h.replace(
    "Oui ! Si tu utilises un iPhone, utilise l'application <strong>Safari</strong> pour te connecter\n            à ton compte Télégram et accéder au canal.",
    "Oui ! Les fichiers PDF sont compatibles avec tous les appareils : Android, iPhone, PC, Mac, tablette. Compatible avec toute visionneuse PDF."
)

# ---- CTA section ----
h = h.replace("Prêt à accéder aux vidéos<br />de l'influenceuse ?", "Prêt à accéder à +14 838<br />BD Hentaï en PDF ?")
h = h.replace("Accès instantané · Paiement sécurisé · 100% Discret", "Téléchargement immédiat · Paiement sécurisé · 100% Discret")
h = h.replace(
    '<span class="cta-price-now">7 700 FCFA</span>\n        <span class="cta-price-old">10 000 FCFA</span>',
    '<span class="cta-price-now">13 000 FCFA</span>\n        <span class="cta-price-old">25 768 FCFA</span>'
)
h = h.replace('🛒 Acheter Maintenant — 7 700 FCFA', '📚 Obtenir le Pack — 13 000 FCFA')
h = h.replace(
    "votre lien Télégram. Vous pouvez utiliser un <strong>pseudonyme</strong> lors du paiement pour préserver votre\n        anonymat.",
    "votre lien de téléchargement. Vous pouvez utiliser un <strong>pseudonyme</strong> lors du paiement pour préserver votre anonymat."
)

# ---- Upsell section ----
old_upsell = '        <!-- Upsell 1 : Collection Baltazar -->\n        <div style="background: white; border-radius: 2rem; padding: 2.5rem; box-shadow: 0 10px 40px rgba(0,0,0,0.05); display: flex; align-items: center; gap: 2.5rem; flex-wrap: wrap; text-align: left;">\n          <img src="https://balta.famatchai226.workers.dev/assets/hero%20caroussel/0.jpeg" alt="Collection Balta" style="width: 120px; height: 120px; object-fit: cover; border-radius: 1.5rem; box-shadow: 0 10px 20px rgba(0,0,0,0.15); border: 2px solid white;">\n          <div style="flex: 1; min-width: 280px;">\n            <h3 class="title-lg" style="margin-bottom: 0.5rem; color: var(--on-surface);">Collection Premium Baltazar</h3>\n            <p class="body-md" style="font-size: 0.95rem; margin-bottom: 1.5rem;">Ne vous contentez pas d\'une seule influenceuse. Accédez à notre canal massif contenant plus de 2000 vidéos exclusives.</p>\n            <a href="https://balta.famatchai226.workers.dev/" class="btn-primary" style="animation: none;">Voir l\'offre Premium &rarr;</a>\n          </div>\n        </div>\n\n        <!-- Upsell 2 : BD Hentai -->\n        <div style="background: white; border-radius: 2rem; padding: 2.5rem; box-shadow: 0 10px 40px rgba(0,0,0,0.05); display: flex; align-items: center; gap: 2.5rem; flex-wrap: wrap; text-align: left;">\n          <img src="./assets/bd.jpg" alt="Collection BD Adulte" style="width: 120px; height: 120px; object-fit: cover; border-radius: 1.5rem; box-shadow: 0 10px 20px rgba(0,0,0,0.15); border: 2px solid white;">\n          <div style="flex: 1; min-width: 280px;">\n            <h3 class="title-lg" style="margin-bottom: 0.5rem; color: var(--on-surface);">Pack +14 838 BD &amp; Mangas pour Adultes</h3>\n            <p class="body-md" style="font-size: 0.95rem; margin-bottom: 1.5rem;">Découvrez notre collection exclusive de bandes dessinées pour adultes. Un accès immédiat à des milliers d\'histoires inédites.</p>\n            <a href="https://baltazar.mymaketou.store/products/veut-tu-14838-pdf-bd-hentai-pour-homme-mature-/checkout" class="btn-secondary" style="animation: none;" target="_blank" rel="noopener">Voir l\'offre BD &rarr;</a>\n          </div>\n        </div>'

new_upsell = '        <!-- Upsell 1 : Collection Kera -->\n        <div style="background: white; border-radius: 2rem; padding: 2.5rem; box-shadow: 0 10px 40px rgba(0,0,0,0.05); display: flex; align-items: center; gap: 2.5rem; flex-wrap: wrap; text-align: left;">\n          <img src="https://kera.famatchai226.workers.dev/assets/hero%20caroussel/0.jpeg" alt="Collection Kera" style="width: 120px; height: 120px; object-fit: cover; border-radius: 1.5rem; box-shadow: 0 10px 20px rgba(0,0,0,0.15); border: 2px solid white;" onerror="this.src=\'./assets/bd.jpg\'">\n          <div style="flex: 1; min-width: 280px;">\n            <h3 class="title-lg" style="margin-bottom: 0.5rem; color: var(--on-surface);">Accès Privé — Vidéos d\'une Influenceuse</h3>\n            <p class="body-md" style="font-size: 0.95rem; margin-bottom: 1.5rem;">Accédez aux vidéos privées d\'une influenceuse qui a fait le buzz. Canal Télégram sécurisé et 100% discret. 7 700 FCFA.</p>\n            <a href="https://baltazar.mymaketou.store/fr/products/acces-prive-et-discret-des-videos-dune-influenceuse/checkout" class="btn-primary" style="animation: none;" target="_blank" rel="noopener">Voir l\'offre Vidéos &rarr;</a>\n          </div>\n        </div>\n\n        <!-- Upsell 2 : Collection Balta -->\n        <div style="background: white; border-radius: 2rem; padding: 2.5rem; box-shadow: 0 10px 40px rgba(0,0,0,0.05); display: flex; align-items: center; gap: 2.5rem; flex-wrap: wrap; text-align: left;">\n          <img src="https://balta.famatchai226.workers.dev/assets/hero%20caroussel/0.jpeg" alt="Collection Baltazar" style="width: 120px; height: 120px; object-fit: cover; border-radius: 1.5rem; box-shadow: 0 10px 20px rgba(0,0,0,0.15); border: 2px solid white;" onerror="this.src=\'./assets/bd.jpg\'">\n          <div style="flex: 1; min-width: 280px;">\n            <h3 class="title-lg" style="margin-bottom: 0.5rem; color: var(--on-surface);">Collection Premium Baltazar — +2000 Vidéos</h3>\n            <p class="body-md" style="font-size: 0.95rem; margin-bottom: 1.5rem;">Ne vous contentez pas d\'une seule influenceuse. Accédez à notre canal massif contenant plus de 2000 vidéos exclusives.</p>\n            <a href="https://balta.famatchai226.workers.dev/" class="btn-secondary" style="animation: none;">Voir l\'offre Premium &rarr;</a>\n          </div>\n        </div>'

h = h.replace(old_upsell, new_upsell)

# ---- Float bar ----
h = h.replace(
    '🔥 Promo : <strong>7 700 FCFA</strong> au lieu de 10 000 FCFA',
    '🔥 Pack BD : <strong>13 000 FCFA</strong> au lieu de 25 768 FCFA'
)
h = h.replace("J'achète 🛒", "J'obtiens 📚")

# ---- Remove Vercel scripts ----
h = h.replace('  <script defer src="/_vercel/insights/script.js"></script>\n  <script defer src="/_vercel/speed-insights/script.js"></script>\n', '')
h = h.replace('\n  <script>\n  window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };\n</script>\n<script defer src="/<unique-path>/script.js"></script>', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(h)

print(f'Done! {len(h)} bytes written to index.html')
