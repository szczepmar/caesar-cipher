def encryption(phrase, k):
    encrypted_text = ""
    for letter in phrase:
        char_id = ord(letter)
        if 65 <= char_id <= 90:
            char_id = ((((char_id - 65) + k) % 26) + 65)
            encrypted_text = encrypted_text + chr(char_id)
        elif 97 <= char_id <= 122:
            char_id = ((((char_id - 97) + k) % 26) + 97)
            encrypted_text = encrypted_text + chr(char_id)
        else:
            encrypted_text = encrypted_text + letter
    return encrypted_text


def decryption_with_step(phrase, k):
    decrypted_text = ""
    for letter in phrase:
        char_id = ord(letter)
        if 65 <= char_id <= 90:
            char_id = ((((char_id - 65) - k) % 26) + 65)
            decrypted_text = decrypted_text + chr(char_id)
        elif 97 <= char_id <= 122:
            char_id = ((((char_id - 97) - k) % 26) + 97)
            decrypted_text = decrypted_text + chr(char_id)
        else:
            decrypted_text = decrypted_text + letter
    return decrypted_text


def decryption_all_possibilities(phrase):
    for i in range(26):
        decrypted_text = ""
        for letter in phrase:
            char_id = ord(letter)
            if 65 <= char_id <= 90:
                char_id = ((((char_id - 65) - i) % 26) + 65)
                decrypted_text = decrypted_text + chr(char_id)
            elif 97 <= char_id <= 122:
                char_id = ((((char_id - 97) - i) % 26) + 97)
                decrypted_text = decrypted_text + chr(char_id)
            else:
                decrypted_text = decrypted_text + letter
        print(decrypted_text)


def test():
    text_file = open("tekst_jawny.txt", "r")
    lines = text_file.readlines()
    plain_list = []
    key_list = []
    encrypted_list = []
    positive = 0
    negative = 0
    for number in lines:
        plain_list.append(number.split("\t")[0])
        key_list.append(number.split("\t")[1])
        encrypted_list.append(number.split("\t")[2])
    encrypted_list_new = [number[:-1] for number in encrypted_list]
    key_list_new = [int(number) for number in key_list]
    for number in range(len(key_list_new)):
        if encrypted_list_new[number] == encryption((plain_list[number]), key_list_new[number]):
            positive += 1
        else:
            negative += 1
    print("Ilość pozytywnych szyfrowań wynosi = ", positive, "\nIlość negatywnych szyfrowań wynosi = ", negative)
    text_file.close()
