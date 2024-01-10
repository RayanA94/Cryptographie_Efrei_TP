# Fonction pour effectuer l'opération XOR sur deux séquences de bytes
def xor_bytes(b1, b2):
    return bytes(a ^ b for a, b in zip(b1, b2))

# Fonction pour chiffrer un fichier en utilisant l'algorithme CBC
def chiffrement_CBC_fichier(fichier_entre, fichier_sortie, key, IV):
    with open(fichier_entre, 'rb') as f:
        texteneutre = f.read()  # Lecture du contenu du fichier à chiffrer

    # Division du texte en blocs de la taille de la clé
    blocks = [texteneutre[i:i + len(key)] for i in range(0, len(texteneutre), len(key))]
    prev_block = IV.encode()  # Convertit le vecteur d'initialisation (IV) en bytes

    # Écriture du texte chiffré dans le fichier de sortie
    with open(fichier_sortie, 'wb') as f:
        for block in blocks:
            block = xor_bytes(block, prev_block)  # Opération XOR entre le bloc courant et le bloc précédent
            cipher_block = xor_bytes(block, key.encode()) 
            f.write(cipher_block)  
            prev_block = cipher_block  

# Fonction pour déchiffrer un fichier chiffré en utilisant l'algorithme CBC
def dechiffrement_CBC_fichier(fichier_entre, fichier_sortie, key, IV):
    with open(fichier_entre, 'rb') as f:
        textechiffre = f.read()

    blocks = [textechiffre[i:i + len(key)] for i in range(0, len(textechiffre), len(key))]
    texte_neutre = b''
    prev_block = IV.encode()

    with open(fichier_sortie, 'wb') as f:
        for block in blocks:
            decrypted_block = xor_bytes(block, key.encode())  # Déchiffrement avec la clé
            plain_block = xor_bytes(decrypted_block, prev_block)  # Opération inverse du chiffrement CBC
            f.write(plain_block)
            prev_block = block


# Fonction pour afficher le menu
def menu():
    print("1. Chiffrer un fichier")
    print("2. Déchiffrer un fichier")
    print("0. Quitter")
    choice = input("Choisissez une option : ")
    return choice

# Fonction principale pour exécuter le programme
def main():
    key = "aB3cD#9z*2FgH1P"
    IV = "xY@6!vQ%5sG2&ZL"


    while True:
        choice = menu() 

        if choice == '1':
            fichier_a_chiffre = input("Entrez le nom du fichier à chiffrer : ")
            fichier_chiffrer = input("Entrez le nom du fichier de sortie (chiffré) : ")
            chiffrement_CBC_fichier(fichier_a_chiffre, fichier_chiffrer, key, IV)
            print(f"Le fichier a été chiffré dans '{fichier_chiffrer}'.")

        elif choice == '2':
            fichier_chiffrer = input("Entrez le nom du fichier chiffré : ")
            fichier_dechiffrer = input("Entrez le nom du fichier de sortie (déchiffré) : ")
            dechiffrement_CBC_fichier(fichier_chiffrer, fichier_dechiffrer, key, IV)
            print(f"Le fichier déchiffré a été écrit dans '{fichier_dechiffrer}'.")

        elif choice == '0':
            print("Au revoir Le GOAT !")
            break

        else:
            print("Choix invalide. Veuillez saisir une option valide.")

if __name__ == "__main__":
    main()

#Fin du super code du GOAT Rayan ! 
