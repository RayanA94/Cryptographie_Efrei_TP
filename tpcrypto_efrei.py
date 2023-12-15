def xor_strings(s1, s2):
    """Fonction pour effectuer l'opération XOR entre deux chaînes, en se limitant à la longueur de la plus courte."""
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))

def chiffrement_CBC(plaintext, key, IV):
    blocks = [plaintext[i:i + len(key)] for i in range(0, len(plaintext), len(key))]
    cipher_text = ''
    prev_block = IV

    for block in blocks:
        block = xor_strings(block, prev_block)
        cipher_block = xor_strings(block, key)
        cipher_text += cipher_block
        prev_block = cipher_block

    return cipher_text

def dechiffrement_CBC(ciphertext, key, IV):
    blocks = [ciphertext[i:i + len(key)] for i in range(0, len(ciphertext), len(key))]
    plain_text = ''
    prev_block = IV

    for block in blocks:
        decrypted_block = xor_strings(block, key)
        plain_block = xor_strings(decrypted_block, prev_block)
        plain_text += plain_block
        prev_block = block

    return plain_text

# Exemple d'utilisation
plaintext = "Rayan"
key = "lacléderayan"
IV = "randomIV"  # Choisissez un IV approprié

cipher_text = chiffrement_CBC(plaintext, key, IV)
print("Texte chiffré:", cipher_text)

decrypted_text = dechiffrement_CBC(cipher_text, key, IV)
print("Texte déchiffré:", decrypted_text)
