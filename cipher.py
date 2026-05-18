import random
import string
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
original_chars = chars.copy()
random.shuffle(chars) #chars
key = chars.copy() #shuffled chars

print("|".join(original_chars))
print("|".join(key))    

def encrypt(plain_text):
    cipher_text = ""
    for letter in plain_text:
        index = original_chars.index(letter)
        cipher_text += key[index]
    return cipher_text


def decrypt(cipher_text):
    plain_text = ""
    for letter in cipher_text:
        index = key.index(letter)
        plain_text += original_chars[index]
    return plain_text


def main():
    plain_text = input("Enter text to encrypt: ")
    encrypted_text = encrypt(plain_text)
    print("Encrypted text:", encrypted_text)
    decrypted_text = decrypt(encrypted_text)
    print("Decrypted text:", decrypted_text)

if __name__ == '__main__':
    main()