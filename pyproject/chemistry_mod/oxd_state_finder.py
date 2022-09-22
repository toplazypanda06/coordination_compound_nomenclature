import mysql.connector as sql
from chemistry_mod import divison_work
def oxd_finder(compound):
    conn = sql.connect(host = "localhost", user = "root", password = "root", database = "elements")
    cur = conn.cursor()
    compound = "[ Pt (NH3)2 Cl2 ] -2"
    col = divison_work.division(compound)
    ligands = col[0]
    ligand_name = col[1]
    CM = col[2]
    oxd_state_ligand = []
    mul_oxd = []
    total_state = col[4]
    state1 = 0



    for i in ligand_name:
        lig = i[0:-1]
        cur.execute("select oxd_state from ligands where ligand_symbol = '{}'".format(lig))
        oxd_state = cur.fetchall()
        oxd_state_ligand.append(oxd_state[0][0] * int(i[-1]))

    cur.execute("select elmt_name from element where elmt_symbol = '{}'".format(CM))
    C_name = cur.fetchall()


    for i in oxd_state_ligand:
        state1 += i
    state_CM = total_state - state1

    return[oxd_state_ligand, total_state, state_CM]
