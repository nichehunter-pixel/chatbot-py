# Chatbot Python avec l'API VoidAI

Petit chatbot en ligne de commande écrit en Python, utilisant l’API `chat/completions` de VoidAI.

Le script permet de :

- choisir un modèle parmi une liste prédéfinie ;
- définir un prompt système au démarrage ;
- discuter avec le modèle directement dans le terminal ;
- conserver l’historique de la conversation pendant l’exécution.

## Prérequis

- Python 3
- le module `requests`

Installation de la dépendance :

```bash
pip install requests
