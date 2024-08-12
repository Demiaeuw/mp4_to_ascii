import os

OUTPUT_C_FILE = "play.c"
ASCII_FRAMES_DIR = "frames_ascii"

# Fonction pour générer le contenu de la fonction C pour afficher les frames
def generate_c_function_for_frame(frame_number, frame_content):
    function_name = f"printFrame{frame_number}"
    frame_lines = frame_content.split("\n")
    
    c_function = f"void {function_name}() {{\n"
    for line in frame_lines:
        # Échapper les guillemets et ajouter chaque ligne du fichier en tant que ligne de printf
        c_function += f'    printf("{line.replace(\'"\', \'\\\"\')}\\n");\n'
    c_function += "}\n\n"
    
    return c_function

# Génération du contenu pour play.c
def generate_play_c():
    with open(OUTPUT_C_FILE, "w") as c_file:
        # Écrire les includes et les fonctions de base
        c_file.write('#include <stdio.h>\n')
        c_file.write('#include <unistd.h> // Pour utiliser la fonction usleep()\n\n')
        
        c_file.write('void clearScreen() {\n')
        c_file.write('    // Pour les systèmes UNIX\n')
        c_file.write('    printf("\\033[H\\033[J");\n')
        c_file.write('}\n\n')
        
        # Initialiser le compteur de frames
        frame_number = 1
        function_calls = ""
        
        # Parcourir les fichiers dans le répertoire frames_ascii
        for filename in sorted(os.listdir(ASCII_FRAMES_DIR)):
            if filename.startswith("ascii_frame_") and filename.endswith(".txt"):
                # Lire le contenu du fichier
                with open(os.path.join(ASCII_FRAMES_DIR, filename), "r") as frame_file:
                    frame_content = frame_file.read()
                
                # Générer la fonction C pour cette frame
                c_function = generate_c_function_for_frame(frame_number, frame_content)
                c_file.write(c_function)
                
                # Ajouter l'appel à la fonction dans la boucle principale
                function_calls += f"        clearScreen();\n"
                function_calls += f"        printFrame{frame_number}();\n"
                function_calls += f"        usleep(200000); // Attente de 200 millisecondes\n\n"
                
                # Incrémenter le compteur de frames
                frame_number += 1
        
        # Générer la fonction play_vid
        c_file.write('void play_vid() {\n')
        c_file.write('    while(1) { // Boucle infinie\n')
        c_file.write(function_calls)
        c_file.write('    }\n')
        c_file.write('}\n\n')
        
        # Générer la fonction main qui appelle play_vid
        c_file.write('int main() {\n')
        c_file.write('    play_vid();\n')
        c_file.write('    return 0;\n')
        c_file.write('}\n')

# Appel de la fonction pour générer le fichier C
generate_play_c()

