# Prédiction de la pathogénicité des mutations du gène BRCA2

## Description
Ce projet vise à développer un modèle prédictif classant les mutations du gène BRCA2 comme pathogènes (associées à des maladies) ou bénignes (sans effet). L'objectif est d'aider les cliniciens à interpréter les variants génétiques et à prioriser les mutations pour des études expérimentales.

## Données
- Source : [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/) pour les variants BRCA2 annotés.
- Séquence de référence : [UniProt ID P51587](https://www.uniprot.org/uniprot/P51587)
- Prétraitement : génération des séquences mutées, encodage BERT et ajout des propriétés biochimiques (hydrophilicité).

## Méthodes
- Encodage des séquences avec ProtBERT pour obtenir des embeddings contextuels.
- Intégration de propriétés biochimiques (hydrophilicité selon Kyte-Doolittle).
- Modèle : réseau de neurones dense (512 → 128 neurones, activation ReLU), couche de sortie sigmoïde.
- Fonction de coût : entropie croisée binaire, optimiseur Adam, 300 époques, batch size = 32.

## Évaluation
- Métriques : précision, rappel, F1-score, AUROC, AUPR.
- Visualisations : matrice de confusion, t-SNE pour explorer les clusters.

## Résultats attendus
- Modèle entraîné capable de prédire la pathogénicité des mutations avec haute précision.
- Insights sur les mutations perturbant la fonction des protéines.
- Base extensible pour d'autres gènes (ex. BRCA1, PTEN).

## Livrables
- Scripts Python : extraction, prétraitement, entraînement et évaluation.
- Notebook Jupyter documentant la démarche.
- Modèle entraîné (.pkl).
- Graphiques et analyses des performances.

## Installation et utilisation
1. Cloner le repository :
   ```bash
   git clone https://github.com/reinabarry142/BRCA2_Pathogenicity.git
