def xor_strings(s1, s2): #utilisation de la fonction xor 
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))

def chiffrement_CBC(plaintext, key, IV):
    # Divise le texte en blocs de la taille de la clé
    blocks = [plaintext[i:i + len(key)] for i in range(0, len(plaintext), len(key))]
    cipher_text = ''  # Variable pour stocker le texte chiffré
    prev_block = IV  # Initialise le bloc précédent avec l'IV

    for block in blocks:
        # Effectue l'opération XOR entre le bloc courant et le bloc précédent
        block = xor_strings(block, prev_block)
        # Effectue l'opération XOR entre le résultat précédent et la clé pour chiffrer le bloc
        cipher_block = xor_strings(block, key)
        cipher_text += cipher_block  # Ajoute le bloc chiffré au texte chiffré final
        prev_block = cipher_block  # Met à jour le bloc précédent pour le prochain tour de boucle

    return cipher_text  # Renvoie le texte chiffré

def dechiffrement_CBC(ciphertext, key, IV):
    # Divise le texte chiffré en blocs de la taille de la clé
    blocks = [ciphertext[i:i + len(key)] for i in range(0, len(ciphertext), len(key))]
    plain_text = ''  # Variable pour stocker le texte déchiffré
    prev_block = IV  # Initialise le bloc précédent avec l'IV

    for block in blocks:
        # Effectue l'opération XOR entre le texte chiffré et la clé pour récupérer le texte déchiffré
        decrypted_block = xor_strings(block, key)
        # Effectue l'opération inverse du chiffrement CBC pour obtenir le texte déchiffré
        plain_block = xor_strings(decrypted_block, prev_block)
        plain_text += plain_block  # Ajoute le bloc déchiffré au texte déchiffré final
        prev_block = block  # Met à jour le bloc précédent pour le prochain tour de boucle

    return plain_text  # Renvoie le texte déchiffré

# Exemple d'utilisation
plaintext = "Rayan"
key = "lacléderayan"
IV = "univderayan!"  

# Chiffre le texte en utilisant la fonction chiffrement_CBC
cipher_text = chiffrement_CBC(plaintext, key, IV)
print("Texte chiffré:", cipher_text)

# Déchiffre le texte chiffré en utilisant la fonction dechiffrement_CBC
decrypted_text = dechiffrement_CBC(cipher_text, key, IV)
print("Texte déchiffré:", decrypted_text)
