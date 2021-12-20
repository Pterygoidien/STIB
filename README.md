# STIB
Le dossier principal du projet est "STIB_Project_3" qui contient settings.py, urls.py
Les dossiers annexes sont des applications au sein du projet : 
  1. Main : contient les pages principales à afficher sur le site (index.html)
  2. Users : contient les modèles Users et les formulaires pour l'inscription, la connexion, déconnexion, ainsi que les pages/views pour voir les profiles utilisateurs. 
  3. Alerts : contient les modèles "Alertes", et les pages pour visualiser les alertes, voir une alerte en particulier, ajouter une alerte, voter une alerte
    3.1 L'alerte comporte deux modèles : Alert et AlertVote, chaque vote est liée à un compte utilisateur existant, de sorte qu'un utilisateur ne peut pas voter deux fois pour la même alerte. 
  4. Manager : interface administrateur, comportant les alertes, les stations et les lignes, ainsi que la gestion des profils utilisateurs.
  5. Transports : comporte simplement les modèles liés aux transports (Stations, Lignes, etc.)
  6. Stats : les statistiques en rapport aux différentes alertes
