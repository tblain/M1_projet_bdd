from parsere import parsing
import preprocessor
from stratification import stratify

if __name__ == "__main__":
    inputfilename = "test1"
    text_file = open(f"../data/{inputfilename}", "r")
    lines = text_file.readlines()

    # parsing des lignes
    edb, idb = parsing(lines)

    # print(edb)
    # print(idb)

    # # stratification
    strats = stratify(edb, idb)

    # # affichage du resultat
    print(strats)

    with open(f"../output/{inputfilename}", "w") as f:
        for idx, rules in enumerate(strats):
            rls = ""
            for r in rules:
                rls += r.replace("'", "") + " "
            rls = rls.strip()
            f.write(f"{idx} : {rls}\n")
