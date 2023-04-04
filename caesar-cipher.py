'''
Title: Caesar Cipher
Description: Takes a message and key and adjusts the message by the key's value
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

CHARACTERS = (string.ascii_lowercase + " " + string.digits +
              string.ascii_uppercase)
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


def caesar_cipher(message, mode, cipher_key):
    """
    str, str, int -> str
    adjusts the message with the key based on the mode chosen
    
    message: the message to be encrypted or decrypted
    mode: either "encrypt" or "decrypt"
    cipher_key: value to shift original index by
    
    assumes: cipher_key >= 0 and <= (len(CHARACTERS) - 1)
             mode will be either "encrypt" or "decrypt"
    """
    if cipher_key < 0 or cipher_key > (CHAR_LENGTH - 1):
        return f"ERROR: cipher key must be between 0 and {CHAR_LENGTH - 1}."
    new_message = ""
    for letter in message:
        if letter in CHARACTERS:
            original_index = CHARACTERS.find(letter)
            if mode == "encrypt":
                modified_index = encrypt(original_index, cipher_key)
            elif mode == "decrypt":
                modified_index = decrypt(original_index, cipher_key)
            new_message += CHARACTERS[modified_index]
        else:
            new_message += letter
    return new_message