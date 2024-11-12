Voici un exemple de README pour votre projet de classification des maladies de la pomme de terre. Ce modèle inclut des sections expliquant l'utilisation de Postman et de FastAPI pour des tests concrets.

---

# Potato Disease Classification

Ce projet utilise un modèle de machine learning pour classifier les maladies des pommes de terre à partir d'images. En s'appuyant sur un dataset disponible sur [Kaggle](https://www.kaggle.com/), ce projet utilise FastAPI pour déployer le modèle et Postman pour effectuer des tests concrets.

## Description du Projet

Les maladies de la pomme de terre peuvent sérieusement affecter les récoltes et causer des pertes économiques majeures. Ce projet propose un modèle de classification des images de feuilles de pomme de terre afin de détecter les maladies et les prévenir. 

### Dataset

Le dataset utilisé pour entraîner ce modèle est disponible sur Kaggle. Il contient des images étiquetées en fonction des différentes maladies des pommes de terre. Les classes incluent, par exemple :
- Early blight
- Late blight
- Healthy

## Installation

1. **Cloner le dépôt** :
   ```
   git clone https://github.com/votre-nom-utilisateur/potato-disease-classification.git
   cd potato-disease-classification
   ```

2. **Installer les dépendances** :
   Assurez-vous d'avoir Python installé, puis utilisez `pip` pour installer les packages nécessaires :
   ```bash
   pip install -r requirements.txt
   ```

3. **Télécharger le dataset** :
   Téléchargez le dataset depuis Kaggle et placez-le dans le répertoire `data/`.

## Entraînement du Modèle

Le notebook `training.ipynb` contient toutes les étapes nécessaires pour le prétraitement des données, l'entraînement et l'évaluation du modèle.

- **Prétraitement** : Redimensionnement des images, mise à l'échelle.
- **Entraînement** : Entraînement d'un modèle de classification d'images.
- **Évaluation** : Calcul des performances du modèle avec une matrice de confusion et une précision.

Lancez le notebook pour entraîner le modèle :
```bash
jupyter notebook training.ipynb
```

## Déploiement avec FastAPI

Une fois le modèle entraîné, il est déployé en utilisant FastAPI pour permettre des prédictions en temps réel.

1. **Lancer le serveur FastAPI** :
   ```
   uvicorn app:app --reload
   ```

2. **Utiliser l'API** :
   - Le point de terminaison principal pour la classification des images est `POST /predict`.
   - Envoyez une image de feuille de pomme de terre au format `multipart/form-data`.

## Tests avec Postman

Vous pouvez utiliser [Postman](https://www.postman.com/) pour tester l'API FastAPI.

1. Ouvrez Postman et créez une nouvelle requête `POST` vers `http://127.0.0.1:8000/predict`.
2. Sous l'onglet **Body**, choisissez `form-data`.
3. Ajoutez une clé `file` de type `File` et téléchargez une image de feuille de pomme de terre pour le test.
4. Envoyez la requête et observez la réponse. La classification de l'image sera renvoyée sous forme de JSON.

## Structure du Projet

```
potato-disease-classification/
├── main.py                  # Fichier principal FastAPI pour déployer le modèle
├── training.ipynb          # Notebook pour entraîner et évaluer le modèle
├── models/                 # Dossier pour sauvegarder les modèles entraînés
├── data/                   # Dossier pour le dataset
└── requirements.txt        # Liste des dépendances du projet
```

## Ressources

- [Dataset Kaggle - Potato Disease](https://www.kaggle.com/) (trop volumineux pour l'envoyer dans mon depot)
- [Documentation de FastAPI](https://fastapi.tiangolo.com/)
- [Documentation de Postman](https://learning.postman.com/)

## Contributions

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une `issue` ou à soumettre une `pull request`.

---
