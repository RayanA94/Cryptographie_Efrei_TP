# Fonction pour effectuer l'opération XOR sur deux séquences de bytes
def xor_bytes(b1, b2):
    return bytes(a ^ b for a, b in zip(b1, b2))

# Fonction pour chiffrer un fichier en utilisant l'algorithme CBC
def chiffrement_CBC_fichier(file_in, file_out, key, IV):
    with open(file_in, 'rb') as f:
        plaintext = f.read()  # Lecture du contenu du fichier à chiffrer

    # Division du texte en blocs de la taille de la clé
    blocks = [plaintext[i:i + len(key)] for i in range(0, len(plaintext), len(key))]
    prev_block = IV.encode()  # Convertit le vecteur d'initialisation (IV) en bytes

    # Écriture du texte chiffré dans le fichier de sortie
    with open(file_out, 'wb') as f:
        for block in blocks:
            block = xor_bytes(block, prev_block)  # Opération XOR entre le bloc courant et le bloc précédent
            cipher_block = xor_bytes(block, key.encode())  # Opération XOR avec la clé pour chiffrer le bloc
            f.write(cipher_block)  # Écriture du bloc chiffré dans le fichier de sortie
            prev_block = cipher_block  # Mise à jour du bloc précédent pour le prochain tour de boucle

# Fonction pour déchiffrer un fichier chiffré en utilisant l'algorithme CBC
def dechiffrement_CBC_fichier(file_in, file_out, key, IV):
    with open(file_in, 'rb') as f:
        ciphertext = f.read()  # Lecture du contenu du fichier chiffré

    # Division du texte chiffré en blocs de la taille de la clé
    blocks = [ciphertext[i:i + len(key)] for i in range(0, len(ciphertext), len(key))]
    prev_block = IV.encode()  # Convertit le vecteur d'initialisation (IV) en bytes

    # Écriture du texte déchiffré dans le fichier de sortie
    with open(file_out, 'wb') as f:
        for block in blocks:
            decrypted_block = xor_bytes(block, key.encode())  # Opération XOR pour récupérer le texte déchiffré
            plain_block = xor_bytes(decrypted_block, prev_block)  # Opération inverse du chiffrement CBC
            f.write(plain_block)  # Écriture du bloc déchiffré dans le fichier de sortie
            prev_block = block  # Mise à jour du bloc précédent pour le prochain tour de boucle

# Fonction pour afficher le menu
def menu():
    print("1. Chiffrer un fichier")
    print("2. Déchiffrer un fichier")
    print("0. Quitter")
    choice = input("Choisissez une option : ")
    return choice

# Fonction principale pour exécuter le programme
def main():
    key = "Zw$Xq0+7i=9v%hN(2y@A!gE5lB&KcU#L*6TjPzRm3f1oCdV8DpYnHrM-IbS4JtF"
    IV = "wG0o)3R$c#I5.y+Y2vhU*4X@nFmL%T=PeJ8tBkK!lA1jM6q9rZsHpVdFiN7Ezbu"

    while True:
        choice = menu() 

        if choice == '1':
            file_to_encrypt = input("Entrez le nom du fichier à chiffrer : ")
            encrypted_file = input("Entrez le nom du fichier de sortie (chiffré) : ")
            chiffrement_CBC_fichier(file_to_encrypt, encrypted_file, key, IV)
            print(f"Le fichier a été chiffré dans '{encrypted_file}'.")

        elif choice == '2':
            encrypted_file = input("Entrez le nom du fichier chiffré : ")
            decrypted_file = input("Entrez le nom du fichier de sortie (déchiffré) : ")
            dechiffrement_CBC_fichier(encrypted_file, decrypted_file, key, IV)
            print(f"Le fichier déchiffré a été écrit dans '{decrypted_file}'.")

        elif choice == '0':
            print("Au revoir Le Roi du Monde t'es trop beau en + !")
            break

        else:
            print("Choix invalide. Veuillez saisir une option valide.")

if __name__ == "__main__":
    main()

#Fin du super code du GOAT Rayan ! 
