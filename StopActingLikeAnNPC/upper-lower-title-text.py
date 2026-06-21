while True:
  a = input('insert text')
  while (choice := input('choose if upper (U), lower (L) or title (T)').lower()) not in ["l", "u", "t"]:
    print('error, reinsert the choice')
  match choice:
    case "l": print(a.lower())
    case "t": print(a.title())
    case "u": print(a.upper())
