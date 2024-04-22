def count_words(text):
    text = text.split()
    diccionario ={}
    for i in text:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    return diccionario

def mas_repetida(diccionario):
    max_word = ""
    max_freq = 0
    for word, freq in diccionario.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq

cadena =str(input("Dame una cadena: "))

print(count_words(cadena))
print(mas_repetida(count_words(cadena)))