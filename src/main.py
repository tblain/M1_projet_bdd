from parser import parsing
import preprocessor
from stratification import stratify

if __name__ == "__main__":
    text_file = open("../data/test1", "r")
    lines = text_file.readlines()

    # parsing des lignes
    edb, idb = parsing(lines)

    print(edb)
    print(idb)

    # # stratification
    strats = stratify(edb, idb)

    # # affichage du resultat
    print(strats)