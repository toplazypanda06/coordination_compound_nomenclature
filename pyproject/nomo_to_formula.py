import mysql.connector as sql
conn = sql.connect(host = "localhost", user = "root", password = "root", database = "elements")
cur = conn.cursor()

compound = 'diAmmine diChlorido Platinum (II) Chloride'
prefix_names = ["di", "tri", "tetra", "penta", "hexa","hepta","octa"]
f_split = compound.split()
ligand = []
l_god = []
jingalala = []
for i in range(0, len(f_split)):
    if "(" in f_split[i]:
        ligand.extend(f_split[0:i-1])


cur.execute("select ligand_name, ligand_symbol from ligands")

ligands_sql = cur.fetchall()
print(ligands_sql)

for i in prefix_names:
    for h in ligand:
        if i in h:
            jingalala.append([h, i])
print(jingalala)

for i in ligand:
    for b in ligands_sql:
        if b[0] in i:
            l_god.append(b[0])
suf_list = []
for i in range(0, len(ligands_sql)):
    x = ligands_sql[i][0][1]
    if len(jingalala[0]) == 2:
        for v in prefix_names:
            if v == jingalala[i][1]:
                suff = prefix_names.index(v)+2
                suf_list.append(suff)
print(suf_list)
print(l_god)

name = ""
for i in range(0, ligands_sql):
    if len(jingalala[i]) == 2:




