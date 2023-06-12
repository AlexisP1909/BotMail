import openpyxl, json, ast
from datetime import datetime
from enum import Enum
from dateutil.relativedelta import relativedelta

periodeEntretienEnMois = 3

class Urgence(Enum):
    organise = "organise"
    pasUrgent = "pasUrgent"
    urgent = "urgent"
    dramatique = "dramatique"

def refRegion(pathDepartementRegions):
    """
    Fonction qui charge le contenu d'un fichier json (supposé contenir un dictionnaire) dans une variable globale dictRegions
    ENTREE: pathDepartementRegions (str) Path du fichier json contenant l'information
    SORTIE: Aucune (mais créatin de la varaible globale dictRegions contenant l'info extraite du fichier lu)
    """
    global dictRegions
    with open(pathDepartementRegions, "r", encoding="utf8") as file:
        dictRegions = ast.literal_eval(file.read())

def readJSON(JSONFile):
    """
    Fonction qui prend en entrée le path d'un fichier JSON et qui en sortie renvoie les informations qu'il contient
    ENTREE: JSONFile (str) Path du fichier JSON
    SORTIE: data (dict) Dictionnaire correspondant au contenu du fichier JSON lu
    """
    try:
        with open(JSONFile,"r") as file:
            data = json.load(file)
        #print(data)
        return data
        
    except:
        print("ERREUR LORS DE LA LECTURE DU FICHIER JSON")

def findRegion(departement):
    """
    Fonction qui pour un numéro de département donné renvoie le nom de sa région
    ENTREE: departement (str) numéro d'un département
    SORTIE: (str) Région du département donné en entrée
    """
    if len(departement) == 1: departement = f"0{departement}" # Si le département est composé d'un seul chiffre et est donné comme tel dans l'input, on ajoute un 0 devant   
    for region, depts in dictRegions.items():
        print(f"Departement cherché {departement} dans liste: {depts}")
        if departement in depts: return region
    
    print(f"ERROR : AUCUNE REGION TROUVEE POUR LE DEPT. \"{departement}\"")
    

def strToDate(strDate): return datetime.strptime(strDate, "%d/%m/%Y") #Fonction qui convertit une date de type "str" vers un format de type "date"

def diff_date(date1, date2): return relativedelta(date1, date2) #Fonction qui retourne la différence entre deux dates de type "date"

def parseInputData(data):
    """
    Fonction qui pour des données en entrée (data) 
    """
    dateDonnees = data["dateDonnees"]
    dateDonneesFormate = strToDate(dateDonnees) # On convertit la date de "str" vers le type "date"
    parcs = data["parcs"] #Liste de dictonnaires, chaque dictionnaire est un parc
    for parc in parcs[:]: # Pour chaque parc (dans une liste copie)
        parc["region"] = findRegion(str(parc["departement"])) # Ajout de la propriété "region"
        # La formule de la date de l'entretien prévu est : dateEntretien = dateMiseEnService + periodiciteEnMois*nbVisitesOrganisees
        date_entretien_organise = strToDate(parc["dateMiseEnService"])+ relativedelta(months=parc["periodiciteEnMois"]*(parc["nbVisitesOrganisees"]))
        if(dateDonneesFormate+relativedelta(months=periodeEntretienEnMois)>=date_entretien_organise and date_entretien_organise>=dateDonneesFormate):#Si la date de l'entretien organisé est entre aujourd'hui et dans periodeEntretienEnMois mois
            parc["urgence"] = Urgence.organise.value # La visite dans les periodeEntretienEnMois mois est organisée, elle est donc pas du tout urgente à prévoir
        else:# La visite dans les trois mois n'est pas organisée             
            # La formule de la date du prochain l'entretien est : dateEntretien = dateMiseEnService + periodiciteEnMois* (nbVisitesOrganisees+1)
            date_entretien = strToDate(parc["dateMiseEnService"])+ relativedelta(months=parc["periodiciteEnMois"]*(1+parc["nbVisitesOrganisees"])) # On détermine la date de l'intervention à venir
            if(dateDonneesFormate>=date_entretien):# Si la date des données est plus tardive que la date de l'entretien
                parc["urgence"]=Urgence.dramatique #L'entretien est en retard
            elif(dateDonneesFormate+relativedelta(months=1)>=date_entretien): #Si la date de l'entretien est dans un mois (ou moins, mais pas en retard)
                parc["urgence"]=Urgence.urgent # L'entretien est considéré comme urgent
            elif(dateDonneesFormate+relativedelta(months=periodeEntretienEnMois)>=date_entretien): #Si la date de l'entretien est dans periodeEntretienEnMois mois (ou moins, mais pas sous 1 mois ou retard)
                parc["urgence"]=Urgence.pasUrgent.value # L'entretien est considéré comme pas urgent
            else: # L'entretien est dans plus de periodeEntretienEnMois mois
                parcs.remove(parc) # On ne considère pas l'entretien pour le rappel

        #Code pour comparer deux dates
        """diffTemps = diff_date(date_entretien,dateDonneesFormate)
        print(f"Différence de temps entre les deux dates {dateDonneesFormate} et {date_entretien} : {diffTemps}")
        print(f"Différence en mois {diffTemps.years*12+diffTemps.months}")"""

    print(parcs)
    
def createMaterielHTML(materiels):
    for materiel in materiels:
        if

def createParkHTML(parc):
    pass


nomRegion = "PACA"
titreLigne = f"<tr><th colspan=\"4\">{nomRegion}</th></tr>"
print(titreLigne)

refRegion("Editor\\departements.json") # On charge le dictionnaire des départements/régions dans la variable globale dictRegions

if __name__ == "__main__":
    donneesEntrees = readJSON("Editor\\sample_ParserToEditor.json")    
    parseInputData(donneesEntrees)
    
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
