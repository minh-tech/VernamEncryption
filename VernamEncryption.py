import string


def cipherVernam(plain_text, one_time_pad, start):
    """
        Encrypt plain text using Vernam cipher
        Input:
            plain_text
            one_time_pad
            start: the number that begins alphabet
                Ex: A = 0, B = 1, ... , Z = 25 => start = 0
                Ex: A = 1, B = 2, ... , Z = 26 => start = 1
    """
    # Remove white spaces in text
    plain_text = plain_text.replace(" ", "")
    one_time_pad = one_time_pad.replace(" ", "")

    # Create two dictionaries for alphabet and number
    alphabet_list = list(string.ascii_lowercase)
    alphabet_key = dict((letter, i) for i, letter in enumerate(alphabet_list, start=start))
    number_key = dict((value, key) for key, value in alphabet_key.items())

    print("Alphabet :", alphabet_key)
    print("Number   :", number_key)

    # Change alphabet to number
    plain_text_value = [alphabet_key[char] for char in plain_text]
    one_time_pad_value = [alphabet_key[char] for char in one_time_pad]

    # Calculate the sum of each pair-value, subtract 26 if the sum equal or more than (26 + start)
    sum_value = []
    for x, y in zip(plain_text_value, one_time_pad_value):
        x_plus_y = x + y
        while x_plus_y >= (26 + start):
            x_plus_y = x_plus_y - 26
        sum_value.append(x_plus_y)

    # Show result
    print("Plain text       :", [" %s" % s for s in plain_text])
    print("Plain text values:", ["%02d" % n for n in plain_text_value])
    print("1-time pad       :", [" %s" % s for s in one_time_pad])
    print("1-time pad values:", ["%02d" % n for n in one_time_pad_value])
    print("Sum values       :", ["%02d" % n for n in sum_value])

    # Cipher text be convert from number to character
    cipher_text = ''.join([number_key[value] for value in sum_value])
    print("Cipher text:", cipher_text)


if __name__ == "__main__":
    plain_text = "what people call intelligence just boils down to curiosity"
    one_time_pad = "idhs pdofhw wifh sjdkfyrkfopd wejd bhuds sode bd qwertfdsw"
    start = 0
    cipherVernam(plain_text, one_time_pad, start)
    start = 1
    cipherVernam(plain_text, one_time_pad, start)
