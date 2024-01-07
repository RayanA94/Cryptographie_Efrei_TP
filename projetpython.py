def xor_bytes(b1, b2):
    return bytes(a ^ b for a, b in zip(b1, b2))

def chiffrement_CBC_fichier(file_in, file_out, key, IV):
    with open(file_in, 'rb') as f:
        plaintext = f.read()

    blocks = [plaintext[i:i + len(key)] for i in range(0, len(plaintext), len(key))]
    cipher_text = b''
    prev_block = IV.encode()  

    with open(file_out, 'wb') as f:
        for block in blocks:
            block = xor_bytes(block, prev_block)
            cipher_block = xor_bytes(block, key.encode())
            f.write(cipher_block)
            prev_block = cipher_block

def dechiffrement_CBC_fichier(file_in, file_out, key, IV):
    with open(file_in, 'rb') as f:
        ciphertext = f.read()

    blocks = [ciphertext[i:i + len(key)] for i in range(0, len(ciphertext), len(key))]
    plain_text = b''
    prev_block = IV.encode()

    with open(file_out, 'wb') as f:
        for block in blocks:
            decrypted_block = xor_bytes(block, key.encode())
            plain_block = xor_bytes(decrypted_block, prev_block)
            f.write(plain_block)
            prev_block = block
           

# Exemple d'utilisation
file_to_encrypt = 'test.txt'
encrypted_file = 'fichier_chiffre.txt'
decrypted_file = 'fichier_dechiffre.txt'


# with open('fichier_chiffre.txt', 'rb') as f:
#    data = f.read()
#    for byte in data:
#        binary_representation = format(byte, '08b')
#        print(binary_representation, end=' ')



plaintext = ""
key = "Zw$Xq0+7i=9v%hN(2y@A!gE5lB&KcU#L*6TjPzRm3f1oCdV8DpYnHrM-IbS4JtF"
IV = "wG0o)3R$c#I5.y+Y2vhU*4X@nFmL%T=PeJ8tBkK!lA1jM6q9rZsHpVdFiN7Ezbu"

chiffrement_CBC_fichier(file_to_encrypt, encrypted_file, key, IV)
dechiffrement_CBC_fichier(encrypted_file, decrypted_file, key, IV)
