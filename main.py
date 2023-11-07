ukr_alphabet = "АБВГҐДЕЄЖЗИЇЙКЛМНОПРСТУФХЦЧШЩЬІЮЯ_0123456789"

# Функція, що генерує гамму для кирилиці
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

# Функція, що повертає шифр
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ukr_alphabet.index(string[i]) +
             ukr_alphabet.index(key[i])) % 44
        cipher_text.append(ukr_alphabet[x])
    return("" . join(cipher_text))

# Функція, що повертає оригінальний текст
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ukr_alphabet.index(cipher_text[i]) -
             ukr_alphabet.index(key[i]) + 44) % 44
        orig_text.append(ukr_alphabet[x])
    return("" . join(orig_text))


if __name__ == "__main__":
    string = "АСВААН_25000_БОЛ"  # задане повідомлення
    keyword = "БІЛОВИД"         # заданий ключ
    key = generateKey(string, keyword)
    cipher_text = cipherText(string, key)
    print("Ciphertext :", cipher_text)
    print("Original/Decrypted Text :", originalText(cipher_text, key))
