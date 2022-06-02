"""one-time-pad is one of the encryption algoritms out there with a very large key space.
don't use it though. it's not secure"""

def one_time_pad(message, key):
    """encrypts/decripts the message using the key with the one time
    pad encryption mechanism. we assume all the characters in the message
    key are letters of the English alphabet. (this is a two way function
    it both encrypts and decrypts)"""
    if len(message) != len(key):
        raise Exception()
    # get the binary for the message
    message_binary_list = to_binary(message)
    # get the binary for the key
    key_binary_list = to_binary(key)
    # XOR them
    result_binary_list = []
    for i in range(len(key_binary_list)):
        result_binary = xor(message_binary_list[i], key_binary_list[i])
        result_binary_list.append(result_binary)
    # get the characters for the encrypted/decrypted
    character_list = []
    for binary in result_binary_list:
        character = chr(bin_to_int(binary))
        character_list.append(character)
    
    result = ''.join(character_list)

    # return
    return result

def to_binary(message):
    """takes in a string and returns a list of binaryies for each letter
    in the string"""
    binary_list = []
    for letter in message:
        binary = bin(ord(letter))[2:]
        while len(binary) < 8: # make sure the binary is 8 bits long
            binary = '0' + binary
        binary_list.append(binary)
    return binary_list


def xor(text_bin, key_bin):
    """does an XOR on two strings containing binary digits (0 and 1) and returns
    the result. we assume the text_bin and key_bin are of the same length."""
    result = ""
    for i in range(len(text_bin)):
        if text_bin[i] == key_bin[i]:
            result += '0'
        else:
            result += '1'
    return result


def bin_to_int(binary):
    integer = 0
    for i in reversed(range(len(binary))):
        integer += int(binary[i]) * 2**(len(binary)-(i+1))
    return integer

if __name__ == "__main__":
    message = "hey there"
    key = "!$@ú$*%#("
    print("message: {}".format(message))
    print("key: {}".format(key))
    print("\nencrypting ... ")
    cipher_text = one_time_pad("hey there", "!$@ú$*%#(")
    print("result:")
    print(cipher_text)
    print("\ndecrypring ...")
    plain_text = one_time_pad(cipher_text, key)
    print("result:")
    print(plain_text)
    # print(one_time_pad("hey there", "!$@ú$*%#("))     # encrypting
    # print(one_time_pad("IA9ÚPB@QM", "!$@ú$*%#("))       # decrypting
    # print(xor('101', '111'))
