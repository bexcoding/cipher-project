'''
Title: Vigenere Cipher
Description: Encrypts a message using repeated Caesar Cipher
Developer: Alexander Beck
Email: beckhv2@gmail.com
Github: https://github.com/bexcoding

.....//\\......//\\......//\\......//\\......//\\......//\\......//\\....../
....//  \\....//  \\....//  \\....//  \\....//  \\....//  \\....//  \\....//
\..// /\ \\..// /\ \\..// /\ \\..// /\ \\..// /\ \\..// /\ \\..// /\ \\..//
\\// /  \ \\// /  \ \\// /  \ \\// /  \ \\// /  \ \\// /  \ \\// /  \ \\// /
 || | <> | || | <> |                                     > | || | <> | || |
 || | <> | || | <> | ||                          ||   // > | || | <> | || |
 /\  \  /  /\  \  /  ||                          ||  //   /  /\  \  /  /\  \
/  \  \/  /  \  \/   ||____       ___      ___   || //   /  /  \  \/  /  \
 <> | || | <> | ||   ||    \\   //   \\  //   \\ ||||    | | <> | || | <> |
 <> | || | <> | ||   ||     || ||____|| ||       || \\   | | <> | || | <> |
\  /  ||  \  /  ||   ||     || ||       ||       ||  \\  |  \  /  ||  \  /
 \/  //\\  \/  //\\  ||____//   \\___//  \\___// ||   \\ \\  \/  //\\  \/  /
    //..\\    //..\\                                      \\    //..\\    //
\  //....\\  //....\\  //....\\  //....\\  //....\\  //....\\  //....\\  //.
\\//......\\//......\\//......\\//......\\//......\\//......\\//......\\//..

'''

import string

CHARACTERS = string.ascii_lowercase
CHAR_LENGTH = len(CHARACTERS)


def encrypt(old_index, cipher_key):
    """
    int, int -> int
    takes the old index and adds it with the cipher key to get new index

    old_index: original index value from CHARACTERS
    cipher_key: value to shift original index by

    assumes: old_index and cipher_key >= 0 and <= (len(CHARACTERS) - 1)
    """
    new_index = old_index + cipher_key
    if new_index > (CHAR_LENGTH - 1):
        new_index -= CHAR_LENGTH
    return new_index


def decrypt(old_index, cipher_key):
    """
    int, int -> int
    takes the old index and subtracts from it the cipher key to get new index

    old_index: original index value from CHARACTERS
    cipher_key: value to shift original index by

    assumes: old_index and cipher_key >= 0 and <= (len(CHARACTERS) - 1)
    """
    new_index = old_index - cipher_key
    if new_index < 0:
        new_index += CHAR_LENGTH
    return new_index


def vigenere_cipher(message, mode, cipher_key):
    """
    str, str, int -> str
    adjusts the message with the key based on the mode chosen

    message: the message to be encrypted or decrypted
    mode: either "encrypt" or "decrypt"
    cipher_key: string that evaluates to several keys to shift original index

    assumes: mode will be either "encrypt" or "decrypt"
    """
    
    cipher_key = cipher_key.lower()
    current_cipher_index = 0
    new_message = []
    for letter in message:
        if letter.lower() in CHARACTERS:
            original_index = CHARACTERS.find(letter.lower())
            current_cipher_value = CHARACTERS.find(cipher_key[current_cipher_index])
            if mode == "encrypt":
                modified_index = encrypt(original_index, current_cipher_value)
            elif mode == "decrypt":
                modified_index = decrypt(original_index, current_cipher_value)
            if letter.isupper():
                new_message.append(CHARACTERS[modified_index].upper())
            else:
                new_message.append(CHARACTERS[modified_index])
        else:
            new_message.append(letter)
        current_cipher_index += 1
        if current_cipher_index >= len(cipher_key):
            current_cipher_index = 0
    return "".join(new_message)
