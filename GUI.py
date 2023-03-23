from tkinter import *
import funkcje

window = Tk()
window.title("Szyfr Cezara")
window.geometry("480x480")


def encryption_window():
    window_e = Toplevel()
    window_e.title("Szyfrowanie")
    window_e.geometry("480x480")

    text_lab = Label(window_e, text="Wprowadź tekst jaki chesz zaszyfrować")
    text_lab.pack(pady=10)

    plain_text_input = Entry(window_e)
    plain_text_input.pack(pady=10)

    key_lab = Label(window_e, text="Wprowadź cyfre z zakresu ( 1 - 26 ) jako klucz szyfrujący!")
    key_lab.pack(pady=10)

    key_input = Entry(window_e)
    key_input.pack(pady=10)

    def encrypt():
        encrypted_text = funkcje.encryption(plain_text_input.get(), int(key_input.get()))
        encrypt_label = Label(window_e, text=encrypted_text)
        encrypt_label.pack()

    encrypt_button = Button(window_e, text="Szyfruj", command=encrypt)
    encrypt_button.pack()

    button_encryption_exit = Button(window_e, text="Wyjście", command=window_e.destroy, fg='black')
    button_encryption_exit.pack(side="bottom", pady=20)


def decryption_key_window():
    window_d = Toplevel()
    window_d.title("Deszyfrowanie")
    window_d.geometry("480x480")

    encrypted_text_lab = Label(window_d, text="To jest okno szyfrowania wprowadź tekst i klucz!")
    encrypted_text_lab.pack(pady=20)

    encrypted_text_input = Entry(window_d)
    encrypted_text_input.pack(pady=10)

    key_lab = Label(window_d, text="Wprowadź cyfre z zakresu ( 1 - 26 ) jako klucz szyfrujący!")
    key_lab.pack(pady=10)

    key_input = Entry(window_d)
    key_input.pack(pady=10)

    def decrypt():
        decrypted_text = funkcje.decryption_with_step(encrypted_text_input.get(), int(key_input.get()))
        decrypt_label = Label(window_d, text=decrypted_text)
        decrypt_label.pack()

    decrypt_button = Button(window_d, text="Deszyfruj", command=decrypt)
    decrypt_button.pack()

    button_decryption_exit = Button(window_d, text="Wyjście", command=window_d.destroy, fg='black')
    button_decryption_exit.pack(side="bottom", pady=20)


def decryption_keyless_window():
    window_da = Toplevel()
    window_da.title("Deszyfrowanie bez klucza")
    window_da.geometry("480x720")

    encrypted_text_lab = Label(window_da, text="To jest okno szyfrowania wprowadź tekst")
    encrypted_text_lab.pack(pady=10)

    encrypted_text_input = Entry(window_da)
    encrypted_text_input.pack(pady=10)

    def decrypt_all():
        for i in range(26):
            decrypted_text = funkcje.decryption_with_step(encrypted_text_input.get(), i)
            decrypt_label = Label(window_da, text=decrypted_text)
            decrypt_label.pack()

    decrypt_button = Button(window_da, text="Deszyfruj", command=decrypt_all)
    decrypt_button.pack()

    button_decryption_exit = Button(window_da, text="Wyjście", command=window_da.destroy, fg='black')
    button_decryption_exit.pack(side="bottom", pady=20)


button_encryption = Button(window, text="Szyfrowanie", command=encryption_window, fg='red')
button_encryption.pack(pady=45)

button_decryption_key = Button(window, text="Deszyfrowanie", command=decryption_key_window, fg='green')
button_decryption_key.pack(pady=45)

button_decryption_keyless = Button(window, text="Deszyfrowanie bez klucza", command=decryption_keyless_window, fg='blue')
button_decryption_keyless.pack(pady=45)

button_exit = Button(window, text="Wyjście", command=window.destroy, fg='black')
button_exit.pack(pady=45)

window.mainloop()
