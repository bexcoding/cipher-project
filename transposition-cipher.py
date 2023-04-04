'''
Title: Transposition Cipher
Description: Encrypt a message by organizing code into rows and then combining
again by column
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
import math


ERROR_MESSAGE = "Error: Key must be between 2 and (message length / 2)"


def check_key_size(ckey, message_length):
    """
    int, int -> bool
    returns false if the ckey is not correct length and true otherwise
    
    ckey: cipher key for encryption or decryption
    message_length: length of the message that needs to be encrypted or
    decrypted
    
    assumes message_length >= 4
    """
    
    return ckey >= 2 and ckey <= (message_length / 2)
        

def encrypt(ckey, message):
    """
    int, str -> str
    returns an encrypted message that changes based on the key

    ckey: cipher key value
    message: the message to be encrypted

    assumes that ckey and message are the correct type of input
    assumes that message length >= 4
    """
    
    if not check_key_size(ckey, len(message)):
        return ERROR_MESSAGE
    message_list = [""] * ckey
    current_string = 0
    for character in message:
        message_list[current_string] += character
        current_string += 1
        if current_string > (ckey - 1):
            current_string = 0
    return "".join(message_list)


def decrypt(ckey, message):
    """
    int, str -> str
    returns a decrypted message that changes based on the key

    ckey: cipher key value
    message: the message to be decrypted

    assumes that ckey and message are the correct type of input
    assumes that message length >= 4
    """
    
    if not check_key_size(ckey, len(message)):
        return ERROR_MESSAGE
    columns = math.ceil(len(message) / ckey)
    message_list = [""] * columns
    current_column = 0
    #while use last column is true, characters will be added to last column
    use_last_column = True
    #last column length is how many characters the last column should accept
    last_column_length = len(message) % ckey
    for character in message:
        message_list[current_column] += character
        current_column += 1
        #if the last column has max characters, removes option to add to it
        #buried in second if statement to prevent continued decrement
        if use_last_column:
            if len(message_list[-1]) >= last_column_length:
                use_last_column = False
                columns -= 1
        if current_column >= columns:
            current_column = 0
    return "".join(message_list)