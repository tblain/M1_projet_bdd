def stratify(edb, idb):
    stratum_dic = {}

    # init
    for d in edb:
        stratum_dic[d] = 1

    for d in idb:
        stratum_dic[d] = 1

    print(stratum_dic)

    no_changes = False

    max_level = 0

    # stratification
    while(not no_changes):
        no_changes = True

        for l_pred in idb:
            rule = idb[l_pred][0]
            for r_pred in rule:
                if r_pred[1]:
                    new_val = max(stratum_dic[l_pred], stratum_dic[r_pred[0]] + 1)
                else:
                    new_val = max(stratum_dic[l_pred], stratum_dic[r_pred[0]])

                if new_val != stratum_dic[l_pred]:
                    stratum_dic[l_pred] = new_val
                    max_level = max(max_level, new_val)
                    no_changes = False

    print("stratum_dic: ", stratum_dic)

    stratum = []
    for i in range(max_level):
        stratum.append([])

    for r in stratum_dic:
        if not r in edb:
            level = stratum_dic[r]
            stratum[level-1].append(r)
    
    return stratum