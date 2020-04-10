from parser import parsing
# import preprocessing
# import stratification

if __name__ == "__main__":
    text_file = open("../data/test1", "r")
    lines = text_file.readlines()

    # parsing des lignes
    edb, idb = parsing(lines)

    print(edb)
    print(idb)

    # # preprocessing sur les lignes parsees
    # preprocess_data = preprocessing.preprocess(parsed)

    # # stratification
    # strats = stratification.stratification(preprocess_data)

    # # affichage du resultat
    # print(strats)
