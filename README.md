# Test de connexion pour PHPTRAVELS

Ce dépôt contient un script `connexion.py` pour tester la connexion sur `https://phptravels.net` en utilisant Selenium + Chrome.

Prérequis
- Python 3.8+
- Google Chrome installé

Installation (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Exécution

1) Exécuter directement en passant les identifiants :

```powershell
python connexion.py --email "votre.email@example.com" --password "votre_mot_de_passe" --headless
```

2) Ou définir des variables d'environnement :

```powershell
$env:PHPTRAVELS_EMAIL = "votre.email@example.com"
$env:PHPTRAVELS_PASSWORD = "votre_mot_de_passe"
python connexion.py --headless
```

Notes
- Le script utilise `webdriver-manager` pour télécharger automatiquement le driver Chrome.
- Si vous souhaitez voir le navigateur, ne passez pas `--headless`.
- Les sélecteurs sont basés sur des attributs `name` (email/password) et un bouton `type=submit` ; adaptez-les si besoin.
