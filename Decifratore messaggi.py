import string
print('inserire numero volte in cui tradurre il testo:')
number_times = int(input())

for i in range(number_times):
    print('inserire testo:')
    text = input()
    alphabet = string.ascii_lowercase
    shift = alphabet[-1] + alphabet[:-1]
    key = str.maketrans(alphabet, shift)
    new_text = text.translate(key)
    print(new_text)
