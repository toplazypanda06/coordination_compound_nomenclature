#def nomenclature_coordination_compund():
import mysql.connector as sql
from chemistry_mod import divison_work, oxd_state_finder
conn = sql.connect(host = "localhost", user = "root", password = "root", database = "elements")
cur = conn.cursor()
compound = "[ Pt (NH3)2 Cl2 ] Cl"
prefix_names = ["di", "tri", "tetra", "penta", "hexa","hepta","octa"]
c_split = compound.split()
print(c_split)
god_cond = False
for i in c_split[-1]:
    if i.isalnum():
        god_cond = True
if god_cond == True:
    C_split = c_split[0:-1]
else:
    C_split = c_split
CM = c_split[1]
ligands = []
ligands_name = []
final_name = []
outer = None

oxd_list = oxd_state_finder.oxd_finder(compound)


if len(C_split) > 4:
    for i in range(2, len(C_split)-1):
        ligands.append(C_split[i])

for i in ligands:
    a = ""
    if "(" in i or ")" in i:
        for x in i:
            if x != "(" and x != ")":
                a+=x
    else:
        a = i       
    ligands_name.append(a)

#cur.execute("select elmt_name from element where elmt_symbol = '{}'".format(CM))
#CM_name = cur.fetchall()
#final_name.append(CM_name)

for i in ligands_name:
    cur.execute("select ligand_name from ligands where ligand_symbol = '{}'".format(i[0:(len(i)-1)]))
    name = cur.fetchall()
    if len(name) != 0:
        if i[-1] in "123456789":
            prefix = prefix_names[int(i[-1])-2]
        final_name.append(prefix + name[0][0]) 
m = ""
cur.execute("select elmt_name from element where elmt_symbol = '{}'".format(CM))
C_name = cur.fetchall()


"""for i in range(0, len(compound)):
    if compound[i] == "]" and compound[i] != compound[-1]:
        if (i-(len(compound)-1)) > 2 and compound[i+2].isalpha():
            outer = cur.execute("select elmt_name from element where elmt_symbol = '{}'".format(compound[i+2:len(compound)]))
            print(outer)"""
cond = False
for i in c_split[-1]:
    if i.isalpha():
        cond = True

CM_state = divison_work.division(compound)
if cond == True:
    cur.execute("select elmt_name from element where elmt_symbol = '{}'".format(c_split[-1]))
    outer = cur.fetchall()
for y in final_name:
    m += y + " "
if oxd_list[-1] != 0:
    finale = m + C_name[0][0] + ' (' + "I" * oxd_list[-1] + ")"+' '
if outer != None:
    out = outer[0][0][0:-2] + 'de'
    finale += out


print(finale)#nomenclature_coordination_compund()
"""
drop the s.no column
reverse nomelcature
VBT"""