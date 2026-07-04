while True:
  while (choice := input('choose if upper (U), lower (L) or title (T)').lower()) not in ["l", "u", "t"]:
    print('error, reinsert the choice')
  match choice:
    case "l": print(input("insert text:\n").lower())
    case "t": print(input("insert text:\n").title())
    case "u": print(input("insert text:\n").upper())
