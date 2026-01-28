---
title: IHM
weight: 4
---
# Interface Homme Machine
1. # Interface Homme Machine

   1. ## Présentation du système

L’Interface Homme-Machine (IHM) constitue le point central d’interaction entre l’utilisateur et le système de navigation. Elle permet de visualiser en temps réel la position du bateau, le cap, ainsi que les données issues de l’anémomètre et du pilote automatique.

*Figure 2: rôle de l’IHM dans le système*

D’un point de vue logiciel, l’IHM repose sur Signal K, qui assure la centralisation et la distribution des données entre les différents sous-systèmes. OpenCPN agit comme interface graphique principale pour la navigation et le pilotage.

Pour la partie matérielle, tout ordinateur compatible avec OpenPlotter peut être utilisé. Néanmoins, l’ensemble du système a été développé et validé sur Raspberry Pi 4, configuration que nous recommandons. Un écran, un clavier et une souris sont nécessaires pour la configuration initiale.

2. ##  Montage 

   1. ### Installation d’OpenPlotter

L’installation d’OpenPlotter nécessite un second ordinateur afin de préparer la carte SD.  
Télécharger l’image officielle d’OpenPlotter depuis le site officiel, puis utiliser un logiciel de flashage tel que [Balena Etcher](https://etcher.balena.io/).  
Insérer la carte SD dans le Raspberry Pi, connecter les périphériques (écran, clavier, souris), puis démarrer le système. Lors du premier lancement, configurer la langue, le clavier et la connexion internet. Une connexion internet est indispensable pour la suite de l’installation.

2. ### Installation et mise à jour des applications

Allez dans le panneau en haut à droite.  
A moins d’être précisé autrement, l’installation des applications sera faite via l’application Settings (accessible depuis le bouton en haut à gauche). Dans Settings, cliquer sur Add sources puis sur add candidates. Si à un moment ultérieur vous avez besoin de mettre à jour une application, re-cliquez sur add candidates pour avoir les mises à jour.

*Figure 3 : Applications disponibles dans OpenPlotter*

3. ### Installation de Signal 

Dans settings, installez *Signal K installer* :  
Une fois cet *installer* installé, vous pouvez vous connecter au serveur de Signal K en vous connectant ainsi :   
Ouvrir Chromium (ou Firefox) et tapez [https://localhost:3000](https://localhost:3000) dans la barre d’adresse.  
Vous pouvez aussi utiliser ceci (insérer lien vers executable quand je l’aurait mis sur le github de SedNav), qui lance automatiquement le serveur de Signal K.

Une fois connecté, vous avez une demande pour créer un compte administrateur, Notez les bien quelque part \!

4. ### Installation d’OpenCPN

Comme précédemment, installez OpenCPN via settings:  
Sur l’installer, cliquez sur *check versions*, puis dans *install*, sélectionnez la version *Backport* (c’est celle la plus à jour)

*Figure 4 : Installer d’OpenCPN*

Une fois OpenCPN installé, il faut connecter OpenCPN au serveur Signal K : allez dans *Options* puis dans *Connection* et dans la section *“configure a new connection”*, sélectionnez network.  
Comme protocole, choisissez Signal k, comme adresse *Localhost* et comme port *3000*. Laissez l’option automatic server discovery décochée (voir figure ci-dessous).

*Figure 5 : connexion entre OpenCPN et Signal K*

Vous pouvez de plus commencer à préparer la connexion au pilote automatique en installant le plugin pypilot.

5. ### Mise en place du Hotspot

Vous avez à votre disposition 2 solutions : 

* Pour installer le hotspot, le point d'accès wifi, vous pouvez utiliser cet installateur (insérer lien vers exécutable pour installer hotspot quand je l’aurais mis sur github).

* Dans le panneau de configuration DU Wifi, en haut à droite :   
  Dans Advanced Options \> Create Wireless Hotspot \> Create New Wi-Fi Hotspot (photo)  
  Créer le réseau Wifi :   
* Choisir le nom, le mot de passe (wifi security)  
* Dans Advanced Options \> Edit Connections   
* Sélectionner le réseau créé (photo)

* Sélectionner :   
  * Band: B/G (2.4 GHz)  
  * Channel: 6 (2437 MHz)

Une fois cela fait, nous vous invitons à installer le reste des systèmes et à revenir ici une fois cela fait.

3. ## Connexion avec l’Anémomètre

Dans Signal K \> Panneau de gauche \> Server \> Data connections \> Add connection

Sélectionnez: 

* DataType: NMEA 0183 (dépend de la doc de l’anémomètre)

(type de donnée envoyée)

* Enabled: Yes  
* ID: 

(ID de la connexion dans Signal K)

* NMEA 0183 Source: TCP Client  
* Host: *windsendor-0.local* (*Dépend du capteur*)  
* Port: 6666 (*Dépend du capteur*)  
* Cocher *Validate Checksum*

Pour afficher les données:  
Dans SIgnal K \> Webapps \> instrumentpanel  
   
(Photo du bouton à cliquer)  
→ Les différents modes s’affichent 

4. ## Préparation de la connexion avec le pilote automatique

Le plugin pypilot permet d’intégrer le pilote automatique à OpenCPN.  
Installer le plugin dans OpenCPN: Options \> Plugins.  
La liste des différents Plugins apparaît, Sélectionner Pypilot et cocher Enabled.

Dorénavant la partie IHM est prête à se connecter avec le pilote automatique mais pour cela encore faut-il avoir le pilote automatique (c’est la partie 5). A la fin, une fois le pilote automatique monté, il sera possible de le connecter avec OpenCPN et l’IHM pour centraliser les données.   
