'''
Title: Reverse Cipher
Description: Cipher that displays a message in reverse order.
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


def reverse_cipher(message):
    """
    str -> str
    returns a message that is the reverse of the input message
    
    message: a str that the user wants reversed
    assumes that the input is of the correct type
    """
    new_message = ""
    i = len(message) - 1
    while i >= 0:
        new_message += message[i]
        i -= 1
    return new_message


def reverse_without_punctuation(message):
    """
    str -> str
    returns a message that is the reverse of the input message with no
    punctuation and with all letters lowercase
    
    message: a str that the user wants reversed
    assumes that the input is of the correct type
    """
    new_message = ""
    i = len(message) - 1
    while i >= 0:
        if message[i] in string.ascii_letters:
            new_message += (message[i]).lower()
        i -= 1
    return new_message