NORMAL = [1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
FIGHTING= [1, 1, 2, 1, 1, 0.5, 0.5, 1, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 2]
FLYING= [1, 0.5, 1, 1, 0, 2, 1, 0.5, 1, 1, 1, 1, 0.5, 2, 1, 2, 1, 1, 1]
POISON = [1, 0.5, 1, 0.5, 2, 1, 0.5, 1, 1, 1, 1, 0.5, 1, 2, 1, 1, 1, 0.5]
GROUND= [1, 1, 1, 0.5, 1, 0.5, 1, 1, 1, 1, 2, 2, 0, 1, 2, 1, 1, 1]
ROCK=[0.5, 2, 0.5, 0.5, 2, 1, 1, 1, 2, 0.5, 2, 2, 1, 1, 1, 1, 1, 1]
BUG=[1, 0.5, 2, 1, 0.5, 2, 1, 1, 1, 2, 1, 0.5, 1, 1, 1, 1, 1, 1]
GHOST=[0, 0, 1, 0.5, 1, 1, 0.5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1]
STEEL=[0.5, 2, 0.5, 0, 2, 0.5, 0.5, 1, 0.5, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 1, 0.5]
FIRE=[1, 1, 1, 1, 2, 2, 0.5, 1, 0.5, 0.5, 2, 0.5, 1, 1, 0.5, 1, 1, 0.5]
WATER=[1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0.5, 0.5, 2, 2, 1, 0.5, 1, 1, 1]
GRASS=[1, 1, 2, 2, 0.5, 1, 2, 1, 1, 2, 0.5, 0.5, 0.5, 1, 2, 1, 1, 1]
ELECTRIC= [1, 1, 0.5, 1, 2, 1, 1, 1, 0.5, 1, 1, 1, 0.5, 1, 1, 1, 1, 1]
PSYCHIC=[1, 0.5, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 0.5, 1, 1, 2, 1]
ICE=[1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 1, 0.5, 1, 1, 1]
DRAGON=[1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0.5, 0.5, 0.5, 1, 2, 2, 1, 2]
DARK=[1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 0, 1, 1, 0.5, 2]
FAIRY=[1, 0.5, 1, 2, 1, 1, 0.5, 1, 2, 1, 1, 1, 1, 1, 1, 0, 0.5, 1]

types = [
    "NORMAL", "FIGHTING", "FLYING", "POISON", "GROUND", "ROCK",
    "BUG", "GHOST", "STEEL", "FIRE", "WATER", "GRASS",
    "ELECTRIC", "PSYCHIC", "ICE", "DRAGON", "DARK", "FAIRY"
]

arrays = {
    "NORMAL": NORMAL,
    "FIGHTING": FIGHTING,
    "FLYING": FLYING,
    "POISON": POISON,
    "GROUND": GROUND,
    "ROCK": ROCK,
    "BUG": BUG,
    "GHOST": GHOST,
    "STEEL": STEEL,
    "FIRE": FIRE,
    "WATER": WATER,
    "GRASS": GRASS,
    "ELECTRIC": ELECTRIC,
    "PSYCHIC": PSYCHIC,
    "ICE": ICE,
    "DRAGON": DRAGON,
    "DARK": DARK,
    "FAIRY": FAIRY
}

def defensive_combo():
    print(f"OPTIONS: {types}")

    raw = input("Insert two types separated by space:\n").upper().split()

    # Controllo input
    if len(raw) != 2:
        print("Error: you must insert exactly TWO types separated by space.")
        return

    t1, t2 = raw

    if t1 not in arrays or t2 not in arrays:
        print("Error: invalid type name.")
        return

    arr1 = arrays[t1]
    arr2 = arrays[t2]

    # Moltiplicazione elemento per elemento
    combo = [a*b for a, b in zip(arr1, arr2)]

    print("Resulting defensive array:")
    print(f"NORMAL: {combo[0]}\nFIGHTING: {combo[1]}\nFLYING: {combo[2]}")
    print(f"POSION: {combo[3]}\nGROUND: {combo[4]}\nROCK: {combo[5]}")
    print(f"BUG: {combo[6]}\nGHOST: {combo[7]}\nSTEEL: {combo[8]}")
    print(f"FIRE: {combo[9]}\nWATER: {combo[10]}\nGRASS: {combo[11]}")
    print(f"ELECTRIC: {combo[12]}\nPSYCHIC: {combo[13]}\nICE: {combo[14]}")
    print(f"DRAGON: {combo[15]}\nDARK: {combo[16]}\nFAIRY: {combo[17]}")

defensive_combo()
