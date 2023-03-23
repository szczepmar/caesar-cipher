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


while True:
    choice = int(input("\nWybierz co chcesz zrobić (cyfra)\n"
                       "1. Szyfrowanie\n"
                       "2. Deszyfrowanie\n"
                       "3. Wszystkie opcje deszyfrowania\n"
                       "4. Test \n"
                       "5. Wyjście\n"))
    if choice == 1:
        plain_text = input("Podaj tekst, który chcesz zaszyfrować: ")
        key = int(input("Podaj długość kroku do zaszyfrowania tekstu: "))
        print("Tak wygląda twoja zaszyfrowana wiadomość: " + encryption(plain_text, key))
    elif choice == 2:
        encrypted_message = input("Podaj tekst, który chcesz odszyfrować: ")
        key = int(input("Podaj długość kroku do zaszyfrowania tekstu: "))
        print("Tak wygląda wiadomość, którą chciałeś odszyfrować: " + decryption_with_step(encrypted_message, key))
    elif choice == 3:
        encrypted_message = input("Podaj tekst, który chcesz odszyfrować: ")
        print("To są wszystkie możliwości wiadomości, którą chciałeś odszyfrować \n")
        decryption_all_possibilities(encrypted_message)
    elif choice == 4:
        # Tekst do sprawdzenia z eportalu miał 10 poprawnie zaszyfrowanych i 2 niepoprawnie
        test()
    elif choice == 5:
        exit()
