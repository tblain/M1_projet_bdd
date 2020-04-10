
def parsing(lines):
    """
    edb = ['Person']
    idb = {
        'Singleman' : [["Man", False], ["Husband", True]],
        'Predicat2' : [["NameOfPredicatOrEntity", "isNegated"]]
    }
    """
    edb = []
    idb = {}

    # skip TAG "% IDB"
    i = 1

    # parse entity
    # example: Person(pID,name,sex,married).
    while "% IDB" not in lines[i]:

        o = lines[i].split('(')
        edb.append(o[0])
        i += 1

    # skip TAG "% EDB"
    i += 1

    # parse predicat
    # example: Singleman(x) :- Man(x), not Husband(x).
    while i < len(lines):
        o = lines[i].split(":-")
        left = o[0].split("(")[0]
        right = remove_par(o[1])
        preds_right = []

        for p in right.split(","):
            # negated subgoal
            if "not" in p.split("(")[0]:
                preds_right.append(
                    [p.split("(")[0].split("not")[1].strip(), True])
            else:
                # nonnegated subgoal
                preds_right.append([p.split("(")[0].strip(), False])

        if left in idb:
            # list merge
            idb[left] += preds_right
        else:
            idb[left] = preds_right

        i += 1
    return edb, idb


def remove_par(string):
    # Man(x), not Husband(x)
    while ")" in string:
        right = string.rfind(")")
        left = string.rfind("(")
        string = string[0:left] + string[right+1: len(string)]
    return string
