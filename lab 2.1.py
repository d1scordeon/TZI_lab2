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

def decryption(string, key):
  cipher_text = []
  for i in range(len(string)):
      x = (ukr_alphabet.index(string[i]) -
           ukr_alphabet.index(key[i])) % 44
      cipher_text.append(ukr_alphabet[x])
  return ("".join(cipher_text))


if __name__ == "__main__":
    string = "ЙЇЇЛЩД18ЗБДЕЯШС"  # задане повідомлення
    keyword = "ДАЛЕМИЛ"  # заданий ключ
    key = generateKey(string, keyword)
    cipher_text = string
    print("Ciphertext :", cipher_text)
    print("Decrypted Text :", decryption(cipher_text, key))