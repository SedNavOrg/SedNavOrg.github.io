---
weight: 6
---
# Pilote automatique

1. # Pilote automatique

   1. ## Présentation du système

Le pilote automatique est la partie qui permet de barrer le bateau de manière autonome sans intervention humaine. Cela permet à l’utilisateur de tenir un cap ou un angle au vent de manière fiable tout en se reposant ou en faisant autre chose puisque le système agit sur la barre du bateau.

Pour mieux comprendre le fonctionnement du pilote automatique, voici ci-dessous un schéma des composants principaux de celui-ci : 

![][image1]

*Figure 40 : schéma des composants*

Le pilote automatique est composé de 3 cartes :

* Le compas (qui donne le cap du bateau)  
* La carte de contrôle (qui permet de visualiser les paramètres du pilote automatique)  
* La carte principale (qui agit sur le vérin et qui permet de barrer le bateau)

Voici ci-dessous une photo de l’ensemble de ces trois cartes qui forment le pilote automatique.

![][image2]

*Figure 41 :  les trois cartes montées*

Voici un zoom sur les trois cartes séparément ainsi que leurs composants : 

![][image3]

*Figure 42 :  Photo du montage du compas*

Détail des composants : 

* ALI : Amplificateur Linéaire Intégré  
* Résistances : réduire la tension avant l’ALI pour éviter la saturation ou pire, la rupture des composants  
* Câbles d’alimentation : alimenter les composants présents sur la carte  
* Accéléromètre : mesurer les flux magnétiques que l’on converti par la suite en cap 

![][image4]

*Figure 43 : Photo du montage de la carte de contrôle*

Détail des composants : 

* Ecran de contrôle : afficher les informations nécessaires pour configurer et contrôler le pilote automatique.  
* Câbles d’alimentation : alimenter la carte  
* Câbles pour transmettre les informations : transmettre l’appui sur une touche à la carte principale pour que l’Arduino puisse contrôler le pilote automatique  
* Touches de commande : commander le pilote avec des touches intuitives et pratiques d’utilisation (les touches sont tactiles)

![][image5]

*Figure 44 : Photo du montage de la carte principale*

Détail des composants : 

* ALI : Amplificateur Linéaire Intégré  
* Résistances : réduire la tension pour protéger des composants comme les ALI  
* Câbles connectés à la carte de commande : faire circuler l’alimentation et les informations de la carte   
* Câbles connectés au compas : idem que précédemment mais pour le compas  
* Câbles d’alimentation : alimenter la carte principale   
* Câbles connectés au moteur : alimenter le moteur et transmettre les informations pour piloter le moteur  
* Pont IBT2 : commander le moteur   
* Arduino Nano : piloter le Pont IBT2  
* Step-down regler : réguler la tension pour alimenter la carte  
* Raspberry PI0w : permettre la communication avec OpenCPN en Wi-Fi

* Thermorésistance : communiquer la température du pont pour lancer une alerte en cas de surchauffe

  2. ## Montage 

     1. ### Partie Hardware

Pour débuter le montage du pilote automatique, il faut commencer par la partie hardware. Pour cela, il vous faudra les différents éléments de montage (présents dans la partie : Liste du matériel nécessaire, partie pilote automatique).  
Il vous faudra également les outils suivants : 

* fer à souder (pour les composants électroniques)  
* tournevis plat de petite taille (pour les composants électroniques)  
* tournevis cruciforme (pour les composants électroniques)  
* pince coupante (pour dénuder du câble si besoin) 

Il n’y a pas vraiment d’ordre de montage des trois cartes, vous pouvez le faire dans l’ordre que vous préférez. Ici, nous avons classé les cartes de la plus rapide à la plus longue à réaliser. Pensez seulement à mettre correctement tous les composants et les câbles et de bien vérifier les soudures avant de mettre sous tension sous peine d’endommager certains composants. 

Recommandations pour les soudures : 

* Nous vous conseillons d’apprendre à souder avant d’essayer de le faire pour le pilote automatique et de vous entraîner  
* De plus, pour les composants principaux comme la carte arduino, le raspberry, l’accéléromètre… nous utilisons : 

  * Des connecteurs à pics : 

![][image6]  
*Figure 45 : connecteurs à pics*

* Des connecteurs à trous : 

![][image7]  
*Figure 46 : connecteurs à trous*

* Connecteurs de bornier : 

![][image7]  
*Figure 47 : connecteurs de bornier*

Cela permet de ne pas souder directement les composants sur la carte et donc de pouvoir les remplacer plus facilement en cas de dysfonctionnement. 

1. #### Compas

Pour rappel, le compas est l’outil qui permet de connaître le cap du bateau et de communiquer cette information avec la carte principale pour que le pilote automatique corrige le cap.  
Voici l’objectif final du montage :   
![][image8]

*Figure 48 : compas*

Il vous faut souder les composants suivants : 

| Emplacement sur la carte | Composant | Caractéristiques |
| :---- | :---- | :---- |
| J1 | 4 connecteurs de bornier  | Aucunes |
| R1, R2 | Résistance | 430 𝛀 |
| R3, R4 | Résistance | 4,7 k𝛀 |
| U1 | 2x4 connecteurs à trous I2C extender (passerelle I2C en français) Attention aux pattes, elles sont très fragiles | Aucunes P82B715 \+ Sockel |
| U2 | 1x4 connecteurs à pics Accéléromètre | Aucunes MPU 9250 oder 9255 ou IMU 9250 oder 9255 ICM20948 (actuellement) |

Remarques :

* Pour trouver les bonnes valeurs de résistance et le système utilisé voici une image explicative :   
  ![][image9]  
  *Figure 49 : source : [positron libre](https://www.positron-libre.com/cours/electronique/resistances/code-couleurs-resistances.php)*  
* Les résistances n’ont pas de sens, vous pouvez mettre la patte gauche à droite ou bien à gauche, cela ne changera en rien le fonctionnement de la résistance.  
* Le I2C extender par contre a un sens et il faut être vigilant. Il faut vérifier la documentation en fonctions des composants mais voici notre montage comme indication : 

![][image10]

*Figure 50 : sens du I2C*

On remarque le le point noir donne le sens, ici il est du côté de l’arrondi présent en dessous de U1

* Pour les quatre fils, il n’y a pas d’ordre non plus. Il faut juste que le fil branché au GND sur cette carte soit également branché au GND sur la carte principale (le montage sera détaillé dans la [partie 6.2.1.3](#carte-principale)) et de même pour les 3 autres fils. De manière générale dans les montages électriques et électroniques, les couleurs n’ont pas vraiment d’importance sauf pour le noir qui concerne les fils reliés à la masse et donc GND (ground) en anglais mais vous êtes bien entendus libres de mettre les couleurs que vous préférez.


  2. #### Carte de contrôle 

Pour rappel, la carte de contrôle permet de contrôler le pilote automatique sans l’IHM, de manière indépendante. L’écran sert à afficher les différents menus et le cap du compas (172 dans la figure ci-dessous). Les boutons permettent de naviguer dans les menus et de modifier les paramètres pour paramétrer le pilote automatique.

Voici l’objectif final du montage : 

![][image11]  
*Figure 51 : face recto de la carte de contrôle*

![][image12]  
*Figure 52 : face verso de la carte de contrôle*

Pour cela, il vous faudra souder les composants suivants : 

| Emplacement sur la carte | Composant | Caractéristiques |
| :---- | :---- | :---- |
| J1 | 1x7 connecteurs de bornier sur le verso | Aucunes |
| J2 | 1x8 connecteurs de bornier sur le verso | Aucunes |
| R1  | Résistance | 2,5 k𝛀 |
| U3 | 1x8 Connecteurs à broches Ecran LCD | Aucunes Jlx12864 |
| U1-U2,U4-U8 | 8x1x3 connecteurs à trous Touches tactiles | Aucunes TP223  |

Mêmes remarques que précédemment concernant les couleurs des fils et leur emplacement. 

De plus, comme les touches sont tactiles, nous vous conseillons de mettre des supports pour supporter les touches et éviter qu’elles ne s'abîment au fur et à mesure qu’on les manipule. 

![][image13]

*Figure 53 : supports*

Vous pouvez imprimer en 3D des cylindres (⌀ : 6 mm, hauteur : 9 mm), avant de le coller ou bien mettre des pions en bois. Le tout est de mettre un matériau isolant pour supporter les touches en porte à faux et éviter de les abîmer.

3. #### Carte principale  {#carte-principale}

La carte principale est celle qui centralise les informations et qui permet de contrôler la barre. De plus, le raspberry assure la communication avec l’IHM et permet donc l’échange d’informations entre celui-ci et le pilote automatique.  
Voici le montage final :   
![][image14]

*Figure 54 : carte principale*

Et voici une image pour voir les soudures en détails : 

![][image15]

*Figure 55 : soudures carte principale*

Pour cela il vous faudra souder les composants suivants : 

| Emplacement sur la carte | Composant | Caractéristiques |
| :---- | :---- | :---- |
| J1, J2, J3, J5, J7, J8 | Connecteurs de bornier | Aucunes |
| J6 | 2x4 connecteurs à pics | Aucunes |
| R1, R2  | Résistances | 430 𝛀  |
| R3, R4, R12 | Résistances | 4,7 k𝛀   |
| R5  | Résistance | 10 k𝛀  |
| R6 | Résistance | 5,6 k𝛀  |
| R7, R8  | Résistances | 120 k𝛀  |
| R9, R10 | Résistances | 47 k𝛀  |
| R11, R13  | Résistances | 22 k𝛀  |
| TH1 | Thermorésistance | 4,7 k𝛀 |
| U1  | 2x4 connecteurs à trous I2C Extender Attention aux pattes, elles sont très fragiles | Aucunes P82B715 \+ Sockel |
| U2, U3  | 2x2x7 connecteurs à trous Inverter Attention aux pattes, elles sont très fragiles | Aucunes Inverter 74HCT04 \+ Sockel |
| U4 | 2x20 connecteurs à trous Raspberry Pi Zero W | Aucunes |
| U5 | Vis écrou de support Pont IBT2 4 câbles entre le pont et la carte (en rouge sur la figure …) | Aucunes |
| U6 | 4x1 connecteurs à pics Step-Down Regler | Aucunes LM2596 4-35V |
| A1 | 2x15 connecteurs à trous Arduino Nano | Aucunes |

Remarques : 

* Pour la thermorésistance, une fois les soudures terminées et validées, vous pouvez installer le pont IBT2 et la thermistance avec de la pâte thermique entre les deux. Vous pouvez bien évidemment le faire quand vous le souhaitez mais il est plus simple de le faire une fois que vous n’aurez plus à manipuler la carte  
* Pour le Step-Down Regler, il vaut mieux le calibrer sur 5V avant utilisation  
* Même remarque pour le I2C extender que pour le compas concernant le sens de pose  
* Les Inverter ont un sens et il faut être vigilant. Il faut vérifier la documentation en fonctions des composants mais voici notre montage comme indication :

![][image16]

*Figure 56 : sens des inverter*

* Pour les différents câbles, vous devez brancher les mêmes câbles que ceux des cartes précédentes. Par exemple, le câble GND du compas doit être branché sur l’emplacement GND réservé au compas sur la carte. Voici une figure illustrant les différentes parties réservées pour les cartes :   
   ![][image17]  
  *Figure 57 : emplacement réservées de la carte*  
  


De gauche à droite : 

| Emplacement sur la carte | Port | Caractéristiques |
| :---- | :---- | :---- |
| J2 | Stb10 | \-10° sur le cap demandé |
| J2 | Stb1 | \-1° sur le cap demandé |
| J2 | Port1 | \+1° sur le cap demandé |
| J2 | Port10 | \+10° sur le cap demandé |
| J2 | Tack | Touche Tack |
| J2 | Select | Touche Select |
| J2 | Menue | Touche Menu |
| J2 | Auto | Touche Auto |
| J1 | DIN | DIN pour l’écran  |
| J1 | CLK | Clock pour l’écran |
| J1 | RST | Reset pour pour l’écran |
| J1 | DC | DC pour l’écran |
| J1 | CE | CE pour l’écran |
| J1 | 3.3V+ | \+3.3V pour l’écran |
| J1 | 3.3V- | \-3.3V pour l’écran |
| J3 | 3.3V+ | \+3.3V pour le compas |
| J3 | 3.3V- | \-3.3V pour le compas |
| J3 | SDA | SDA pour le compas |
| J3 | SCL | SCL pour le compas |
| J7 | 5V- | \-5V pour potentiomètre |
| J7 | Sense | retour du potentiomètre |
| J7 | 5V+ | \+5V pour potentiomètre |
| J5 | 12V- | \+12V alimentation |
| J5 | 12V+ | \-12V alimentation |
| J5 | SeaT | Connexion non utilisée par pypilot |
| J5 | \- | alimentation du moteur |
| J5 | \+ | alimentation du moteur |
| J5 | 12V+ | alimentation du vérin |
| J5 | 12V- | alimentation du vérin |
| J5 | SeaT | Connexion non utilisée par pypilot |
| J8 | Motor \- | alimentation du moteur |
| J8 | Motor \+ | alimentation du moteur |
| J8 | 12V- | alimentation du vérin |
| J8 | 12V+ | alimentation du vérin |

Remarques:

* Sur J5, les connexions : in 12V, In12+ et In Seat sont connectées directement sur le PCB respectivement à Out 12V-, Out12+ et Out Seat.

### 

2. ### Partie Software 

Pour ce qui est de la partie software, tous les codes proviennent de Github et peuvent y être téléchargés.  
Liens à ajouter  
Le matériel nécessaire pour effectuer tout cela, est le suivant : 

* un câble USB type A \- Micro USB pour alimenter le Raspberry Pi Zero et faire quelques tests  
* un câble USB type A \- Mini USB type B pour alimenter la carte Arduino Nano et téléverser les codes dessus  
* un lecteur de carte SD  
* une carte SD d’au moins 2 GB

  1. #### Raspberry Pi Zero

Dans ce passage nous détaillons le processus de connexion du pilote automatique à l’IHM.  
Cela permettra de centraliser les informations et de pouvoir contrôler le pilote automatique sur l’écran principal.  
Vous devez déjà avoir téléchargé pypilot sur l’IHM (partie 4.4).  
Le Raspberry Pi a le rôle d’ordinateur pour le pilote automatique, c’est lui qui transfère les informations au programme OpenCPN et qui gère les différentes informations reçues dans le pilote automatique en général (affichage sur l’écran LCD, données du compas, …). Il faut donc “flasher” le programme de base de cet ordinateur, qui est sous la forme d’une image sur la carte SD du Raspberry Pi.

Pour cela : 

* Téléchargez la dernière version de Tinypilot sur leur site : [https://pypilot.org/downloads/](https://pypilot.org/downloads/)   
* Décompressez l’archive qui a été téléchargée, ça sera l’image à transférer  
* Pour flasher l’image sur la carte SD, installez le logiciel raspberry Pi imager : [https://www.raspberrypi.com/software/](https://www.raspberrypi.com/software/)   
* Une fois le logiciel installé et les instructions de mise en route suivies, vous pouvez flasher l’image  
  * Sélectionnez le modèle de raspberry (ici le Raspberry Pi 0 W)  
  * Sélectionnez ensuite l’utilisation d’une image personnalisée comme OS, et allez chercher celle que vous venez de télécharger  
  * Vous pouvez maintenant choisir le stockage que vous souhaitez utiliser, et lancer l’écriture

Une fois que vous avez flashé l’image, insérez la carte SD dans le Raspberry PI Zero, puis  
Attendez ensuite une minute le temps que le Raspberry se lance correctement. Maintenant connectez-vous au réseau wifi “pypilot” qui devrait apparaître dans les réseaux disponibles, il n’y a pas besoin de mot de passe.

Ensuite dans votre navigateur, entrez l’adresse IP suivante dans la barre d’adresse : 192.168.14.1  
Cela devrait vous amener sur cette page du pilote automatique (remarque la langue et la couleur du fond peuvent être modifiée et donc différentes sur votre pilote automatique) :   
![][image18]  
*Figure 58 : page d’accueil pilote automatique*

Cette page web est essentielle car elle permet d'accéder à tous les paramètres du pilote automatique depuis un écran plus grand que l’écran LCD.   
En effet, si vous utilisez le pilote automatique de manière autonome, vous pouvez accéder à toutes les données et les paramètres sur cette page web (ce sont les mêmes menus que ceux afficher sur l’écran LCD).  
Ainsi pour les calibrations futures, vous pourrez passer par l’écran ou par ce site directement selon vos préférences.   
Allez dans l’onglet “Configuration”, puis cliquez sur le lien “Configure Wifi”, vous devez obtenir la page suivante :  
![][image19]  
*Figure 59 : page de configuration Wifi*

On observe ici le point d’accès qui a été créé ainsi que notre PC qui est connecté au réseau (c’est l’adresse IP 192.168.14.109) 

Il faut ensuite changer l’onglet de Master (AP) à Manage (client) cela signifie que le raspberry passe de manager du réseau à client et nous allons le configurer pour être Client du réseau créé par l’IHM comme sur la figure suivante :   
![][image20]  
*Figure 60 : configuration client*

Complétez les champs suivants : 

* SSID par celui configuré dans l’IHM (attention aux majuscules, il faut bien mettre exactement le même nom)   
* Client Clé par le code renseigné dans l’IHM (partie 4.2.5)  
* adresse du mode client avec une adresse IP compatible avec celles configurées dans l’IHM (partie 4.2.5) et notez l’adresse IP, on en aura besoin plus tard

Puis cliquez sur Submit, débranchez la carte du PC avant de la rebrancher sur la carte principale pour “reboot” la carte et valider l’opération.  
Dans OpenCPN (sur l’IHM) lancez le plugin pypilot et cliquez sur AP comme sur la figure suivante : 

![][image21]  
*Figure 61 : connexion pypilot*

Ensuite, entrez dans l’onglet Settings et noter l’adresse IP (celle configurée quelques lignes plus tôt) dans la barre comme sur la figure suivante : 

![][image22]  
*Figure 62 : connexion réussie*

Vous devriez avoir le bandeau vert après quelques secondes signifiant une réussite de l’opération. Si ce n’est pas le cas, il se peut que vous ayez fait une des erreurs suivantes : 

* Problème de carte SD du raspberry PI  
* Mauvaise adresse IP  
* Mauvaise configuration de pypilot  
* Mauvaise configuration du point d’accès de l’IHM (partie 4.2.5)

Reprenez les étapes précédentes ou renseignez vous sur le forum en cas de problème.

Une fois validé, vous pouvez observer le message : Connecté à OpenCPN sur l’écran LCD du pilote automatique dans le menu : settings \-\> control \-\> Wifi et les informations préalablement renseignées.  
Ceci clos la connexion entre le pilote automatique et l’IHM, maintenant toutes les informations trouvables sur le site web ou sur l’écran LCD se retrouve sur l’IHM (notamment le cap du compas et le cap désiré).

2. #### Arduino Nano

La carte arduino Nano a pour rôle d’envoyer les commandes au moteur en fonction des données reçues par le compas. Pour cela, il faut lui donner le programme qu’elle devra suivre.  
Afin de téléverser ce programme, vous pouvez télécharger l’IDE Arduino depuis leur page web, et suivre les étapes d’initialisation :  
[https://www.arduino.cc/en/software/](https://www.arduino.cc/en/software/)  
Une fois que le logiciel est installé, vous pouvez télécharger le programme à téléverser sur github, ainsi que les bibliothèques nécessaires :   
Lien temporaire pour les fichiers :   
[https://drive.google.com/file/d/1sLZdqL6ufFpdVWxDVSjmh9KC6vfXsYSw/view?usp=drive\_link](https://drive.google.com/file/d/1sLZdqL6ufFpdVWxDVSjmh9KC6vfXsYSw/view?usp=drive_link)

Une fois que vous avez téléchargé cette archive zip, vous pouvez la décompresser et mettre tous les fichiers dans le même dossier de votre ordinateur, puis renommer ce dossier “pypilotmotorcontrollerwithrudder”  
Vous pouvez maintenant ouvrir le fichier en .ino qui se trouve dans ce dossier avec le logiciel Arduino IDE  
Vérifier s’il faut ouvrir un workspace ou bien si le fichier .ino suffit

Vous pouvez maintenant connecter la carte arduino à votre ordinateur, choisir le modèle “Arduino Nano” dans Tools-\>Board-\>Arduino Nano, puis choisir le bon port dans Tools-\>Port  
(Pour connaître le bon port, il suffit de tester l’étape suivante et si elle renvoie une erreur, essayez avec un autre choix)

Vous pouvez maintenant téléverser le programme en cliquant sur le bouton avec la flèche vers la droite.  


[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,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
