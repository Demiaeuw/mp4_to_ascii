# ASCII animated Project

This project allows you to convert a video into a sequence of ASCII images, save these images as .txt files, and then generate a C program to display these images as an animation in the terminal.

## Prerequisites

Make sure you have the following installed on your system:
- Python 3.x
- GCC (for compiling the C program)
- `ffmpeg` (for extracting frames from the video)

## Step 1: Installing `ffmpeg`

`ffmpeg` is a powerful tool for processing video and audio files. To install `ffmpeg` on your Linux system, follow the instructions below:

### On Ubuntu/Debian

Open a terminal and run the following commands:

```bash
sudo apt update
sudo apt install ffmpeg
```
### On Fedora

```bash
sudo dnf install ffmpeg
```

### On CentOS/RHEL

```bash
sudo yum install epel-release
sudo yum install https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm
sudo yum install ffmpeg ffmpeg-devel
```

### On Arch Linux

```bash
sudo pacman -S ffmpeg
```

## Step 2: Converting the Video to Frames

Place the video you want to convert in the Workbench folder of the current directory. Then, use the following command to extract frames from the video at a rate of 24 frames per second:

```bash
ffmpeg -i Workbench/votre_video.mp4 -vf "fps=24" frames/frame_%04d.png
```

This will create a `frames` folder containing the extracted frames as PNG files.

## Step 3: Running the First Python Script

The first Python script reads the video frames and generates `.txt` files containing the ASCII images. This script also creates a `frames_ascii` folder to store these files.

To run the script, make sure you are in the directory containing the Python script and the `frames` folder. Then, execute:

```bash
python3 ascii_video.py
```

This script will:
- Read each PNG frame in the `frames` folder.
- Convert each frame to ASCII art.
- Save each ASCII frame as a `.txt` file in the `frames_ascii` folder.

## Step 4: Running the Second Python Script

The second Python script generates a `play.c` file that contains a C function `play_vid()`. This function displays each ASCII frame in a loop to create an animation in the terminal.

To run this script, ensure you are in the same directory as the Python script, then execute:

```bash
python3 generate_play_c.py
```

This script will:
- Create a `play.c` file.
- Generate C functions for each ASCII frame.
- Create a `play_vid()` function that reads and displays each frame in a loop.

## Step 5: Compiling and Running the C Program

To compile the `play.c` file and run the ASCII animation, use the following commands:

```bash
gcc play.c -o play
./play
```

The ASCII animation will start displaying in the terminal.


---

---

---



# Projet d'Animation ASCII

Ce projet permet de convertir une vidéo en une séquence d'images ASCII, de sauvegarder ces images en fichiers `.txt`, puis de générer un programme C pour afficher ces images dans le terminal sous forme d'animation.

## Prérequis

Assurez-vous d'avoir les éléments suivants installés sur votre système :
- Python 3.x
- GCC (pour compiler le programme C)
- `ffmpeg` (pour extraire les frames de la vidéo)

## Étape 1 : Installation de `ffmpeg`

`ffmpeg` est un outil puissant pour traiter des fichiers vidéo et audio. Pour installer `ffmpeg` sur votre système Linux, suivez les instructions ci-dessous :

### Sur Ubuntu/Debian

Ouvrez un terminal et exécutez les commandes suivantes :

```bash
sudo apt update
sudo apt install ffmpeg
```

### Sur Fedora

```bash
sudo dnf install ffmpeg
```

### Sur CentOS/RHEL

```bash
sudo yum install epel-release
sudo yum install https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm
sudo yum install ffmpeg ffmpeg-devel
```

### Sur Arch Linux

```bash
sudo pacman -S ffmpeg
```

## Étape 2 : Conversion de la vidéo en frames

Placez la vidéo que vous souhaitez convertir dans le dossier `Workbench` du répertoire courant. Utilisez ensuite la commande suivante pour extraire les frames de la vidéo à une fréquence de 24 frames par seconde :

```bash
ffmpeg -i Workbench/votre_video.mp4 -vf "fps=24" frames/frame_%04d.png
```

Cela créera un dossier `frames` contenant les frames extraites sous forme de fichiers PNG.

## Étape 3 : Exécution du premier script Python

Le premier script Python lit les frames de la vidéo et génère des fichiers `.txt` contenant les images ASCII. Ce script crée également un dossier `frames_ascii` pour stocker ces fichiers.

Pour exécuter le script, assurez-vous que vous êtes dans le répertoire contenant le script Python et le dossier `frames`. Ensuite, exécutez :

```bash
python3 ascii_video.py
```

Ce script va :
- Lire chaque frame PNG dans le dossier `frames`.
- Convertir chaque frame en art ASCII.
- Enregistrer chaque frame ASCII sous forme de fichier `.txt` dans le dossier `frames_ascii`.

## Étape 4 : Exécution du second script Python

Le second script Python génère un fichier `play.c` qui contient une fonction C `play_vid()`. Cette fonction affiche chaque frame ASCII en boucle pour créer une animation dans le terminal.

Pour exécuter ce script, assurez-vous que vous êtes dans le même répertoire que celui du script Python, puis exécutez :

```bash
python3 generate_play_c.py
```

Ce script va :
- Créer un fichier `play.c`.
- Générer des fonctions C pour chaque frame ASCII.
- Créer une fonction `play_vid()` qui lit et affiche chaque frame en boucle.

## Étape 5 : Compilation et exécution du programme C

Pour compiler le fichier `play.c` et exécuter l'animation ASCII, utilisez les commandes suivantes :

```bash
gcc play.c -o play
./play
```

L'animation ASCII commencera à s'afficher dans le terminal.

