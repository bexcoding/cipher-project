'''
Title: Simple Substitution Cipher
Description: Cipher where each letter is mapped to another letter
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
import random


LETTERS = string.ascii_lowercase


def create_key():
    """
    () -> str
    generates a random cipher key, a string of letters 26 characters long
    """

    letter_list = list(LETTERS)
    random.shuffle(letter_list)
    return "".join(letter_list)


def check_key(ckey):
    """
    str -> bool
    checks if the given key is adequate/legal

    ckey: cipher key; string of 26 alphabet characters
    """
    
    ckey = ckey.lower()
    for character in ckey:
        if character not in LETTERS:
            return "Error: Key must use alphabet characters only"
    if len(ckey) != 26:
        return "Error: Key must be 26 characters long."
    elif len(ckey) != len(set(ckey)):
        return "Error: Key must not have any repeated characters."
    else:
        return "Pass: Key meets all criteria."


def encrypt(message, ckey):
    """
    str, str -> str
    returns an encrypted message

    message: the original message that needs to be encrypted
    ckey: cipher key; string of 26 alphabet characters
    """
    
    check = check_key(ckey)
    if check[0] == "E":
        return check
    new_message = []
    for character in message:
        if character.lower() in LETTERS:
            old_index = LETTERS.find(character.lower())
            new_character = ckey[old_index]
            if character.isupper():
                new_message.append(new_character.upper())
            else:
                new_message.append(new_character)
        else:
            new_message.append(character)
    return "".join(new_message)
        

def decrypt(message, ckey):
    """
    str, str -> str
    returns a decrypted message

    message: the original message that needs to be decrypted
    ckey: cipher key; string of 26 alphabet characters
    """

    check = check_key(ckey)
    if check[0] == "E":
        return check
    new_message = []
    for character in message:
        if character.lower() in LETTERS:
            old_index = ckey.find(character.lower())
            new_character = LETTERS[old_index]
            if character.isupper():
                new_message.append(new_character.upper())
            else:
                new_message.append(new_character)
        else:
            new_message.append(character)
    return "".join(new_message)