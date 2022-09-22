def division(compound):
    c_split = compound.split()
    ligands = []
    ligands_name = []
    god_cond = False
    total_state = None
    for i in c_split[-1]:
        if i.isalnum():
            god_cond = True
    if god_cond == True:
        C_split = c_split[0:-1]
    else:
        C_split = c_split
    if len(C_split) > 4:
        for i in range(2, len(C_split) - 1):
            ligands.append(C_split[i])

    for i in ligands:
        a = ""
        if "(" in i or ")" in i:
            for x in i:
                if x != "(" and x != ")":
                    a += x
        else:
            a = i
        ligands_name.append(a)
    cond = False
    if c_split[-1] != "]":
        for i in c_split[-1]:
            if i.isalpha():
                cond = True
        if cond == False:
            total_state = int(c_split[-1])
    else:
        total_state = 0
    return[ligands, ligands_name, C_split[1], c_split, total_state]
