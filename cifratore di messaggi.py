import string

print("inserisci numero di volte in cui cifrare il testo:")
number_times = int(input())

for i in range(number_times):
    print('inserire testo:')
    text = str(input())
    alphabet = string.ascii_lowercase
    shifted = alphabet[1:] + alphabet[0] #parte da lal 2a lettera della stringa fino alla fine e aggiunge alla fine la 1a posizione(x 1 spiegazione migliore vedi documento python completo sul pc
    key = str.maketrans(alphabet, shifted)
    new_text = text.translate(key)
    print(new_text)
