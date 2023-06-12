import openpyxl, json

dateDonnees =""
parcs = []

def readJSON(JSONFile):
    with open(JSONFile,"r") as file:
        data = json.load(file)
    print(data)
    



nomRegion = "PACA"
titreLigne = "<tr><th colspan=\"4\">{}</th></tr>".format(nomRegion)
print(titreLigne)


readJSON("sample_ParserToEditor.json")
"""
datas = {
    "region":"PACA",
    


}
    [3,2,1],
    [6,5,4],
    [9,8,7]
]

for data in datas:
    materiel=""
    nbBornesSimples = data[0]
    nbBornesDoubles = data[1]
    nbArmoires = data[2]

    effectifs = [(nbBornesSimples, " borne simple"), (nbBornesDoubles, " borne double"), (nbArmoires, " armoire")]
    
    for index, (nb, texte) in enumerate(effectifs):
        if nb>0:
            if nb==1: materiel+=str(nb)+texte
            else: materiel+=str(nb)+texte.replace("e","es")
            if not index==len(effectifs)-1: materiel+="<br>"

    ligneInfo = "<tr><td class=\"pasUrgent\">Date 1</td><td>{}</td><td>Client 1</td><td>Adresse 1</td></tr>".format(materiel)
    print(ligneInfo)
"""
