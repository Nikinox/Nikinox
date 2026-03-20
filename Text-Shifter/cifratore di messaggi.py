import string
answer=""
choose=""
print("insert yes if you want to use this tool")
answer=input().lower()
while answer != "yes" and answer != "no":
    print("error, insert again the answer")
    answer = input().lower()
    if answer=="no":
        quit
    while answer=="yes":
        print("Insert enc for encrypting a message, insert dec for decrypting a message encrypted")
        choose=input().lower()
        while choose != "enc" and choose != "dec":
            print("error, insert again the option")
        if choose=="enc":
            print('inserire testo:')
            text = str(input())
            alphabet = string.ascii_lowercase
            shifted = alphabet[1:] + alphabet[0] #real:encrypted=a:b
            key = str.maketrans(alphabet, shifted)
            new_text = text.translate(key)
            print(new_text)
        if choose=="dec":
            print('insert text:')
            text = input()
            alphabet = string.ascii_lowercase
            shift = alphabet[-1] + alphabet[:-1]#encrypted:real=b:a
            key = str.maketrans(alphabet, shift)
            new_text = text.translate(key)
            print(new_text)
        print("Do you want to use again this tool? insert yes or no")
        answer=input().lower()
        while answer != "yes" and answer != "no":
            print("error, insert again the answer")
            answer = input().lower()
        if answer=="no":
            break
