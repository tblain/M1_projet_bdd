def stratify(edb, idb):
    stratum = {}

    # init
    for d in edb:
        stratum[d] = 1

    for d in idb:
        stratum[d] = 1

    no_changes = False

    # stratification
    while(not no_changes):
        no_changes = True

        for l_pred in idb:
            for rule in idb[l_pred]:
                for r_pred in rule:
                    if r_pred[1]:
                        stratum[r_pred[0]]
                        new_val = max(stratum[l_pred], stratum[r_pred[0]] + 1)
                    else:
                        new_val = max(stratum[l_pred], stratum[r_pred[0]])

                    if new_val != stratum[l_pred]:
                        stratum[l_pred] = new_val
                        no_changes = False

    return stratum
