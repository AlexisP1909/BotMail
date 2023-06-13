import json, ast, os
from datetime import datetime
from enum import Enum
from dateutil.relativedelta import relativedelta

periodeEntretienEnMois = 3

typeMateriel = {"borneSimple":"borne simple",
                "borneDouble": "borne double",
                "armoire": "armoire"}

# Obtenez le répertoire de travail actuel
repertoire_actuel = os.path.dirname(os.path.abspath(__file__))

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
        with open(JSONFile,"r", encoding="utf8") as file:
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
    departement=''.join(x for x in departement if x.isdigit())
    if len(departement) == 1: departement = f"0{departement}" # Si le département est composé d'un seul chiffre et est donné comme tel dans l'input, on ajoute un 0 devant   
    for region, depts in dictRegions.items():
        print(f"Departement cherché {departement} dans liste: {depts}")
        if departement in depts: return region
    
    print(f"ERROR : AUCUNE REGION TROUVEE POUR LE DEPT. \"{departement}\"")
    

def strToDate(strDate): return datetime.strptime(strDate, "%d/%m/%Y") #Fonction qui convertit une date de type "str" vers un format de type "date"

def diff_date(date1, date2): return relativedelta(date1, date2) #Fonction qui retourne la différence entre deux dates de type "date"

def parseInputData(data):
    """
    Fonction qui pour des données en entrée (data) renvoie une liste de parcs et la date de l'envoi des données
    """
    dateDonnees = data["dateDonnees"]
    dateDonneesFormate = strToDate(dateDonnees) # On convertit la date de "str" vers le type "date"
    parcs = data["parcs"] #Liste de dictonnaires, chaque dictionnaire est un parc
    for parc in parcs[:]: # Pour chaque parc (dans une liste copie)
        # La formule de la date de l'entretien prévu est : dateEntretien = dateMiseEnService + periodiciteEnMois*nbVisitesOrganisees
        date_entretien_organise = strToDate(parc["dateMiseEnService"])+ relativedelta(months=parc["periodiciteEnMois"]*(parc["nbVisitesOrganisees"]))
        if(dateDonneesFormate+relativedelta(months=periodeEntretienEnMois)>=date_entretien_organise and date_entretien_organise>=dateDonneesFormate):#Si la date de l'entretien organisé est entre aujourd'hui et dans periodeEntretienEnMois mois
            parc["urgence"] = Urgence.organise.value # La visite dans les periodeEntretienEnMois mois est organisée, elle est donc pas du tout urgente à prévoir
            parc["dateEntretien"] = date_entretien_organise
        else:# La visite dans les trois mois n'est pas organisée             
            # La formule de la date du prochain l'entretien est : dateEntretien = dateMiseEnService + periodiciteEnMois* (nbVisitesOrganisees+1)
            date_entretien = strToDate(parc["dateMiseEnService"])+ relativedelta(months=parc["periodiciteEnMois"]*(1+parc["nbVisitesOrganisees"])) # On détermine la date de l'intervention à venir
            parc["dateEntretien"] = date_entretien
            if(dateDonneesFormate>=date_entretien):# Si la date des données est plus tardive que la date de l'entretien
                parc["urgence"]=Urgence.dramatique.value #L'entretien est en retard
            elif(dateDonneesFormate+relativedelta(months=1)>=date_entretien): #Si la date de l'entretien est dans un mois (ou moins, mais pas en retard)
                parc["urgence"]=Urgence.urgent.value # L'entretien est considéré comme urgent
            elif(dateDonneesFormate+relativedelta(months=periodeEntretienEnMois)>=date_entretien): #Si la date de l'entretien est dans periodeEntretienEnMois mois (ou moins, mais pas sous 1 mois ou retard)
                parc["urgence"]=Urgence.pasUrgent.value # L'entretien est considéré comme pas urgent
            else: # L'entretien est dans plus de periodeEntretienEnMois mois
                parcs.remove(parc) # On ne considère pas l'entretien pour le rappel
    return parcs, dateDonneesFormate    

def trierParcs(donneesParcs):
    """
    Fonction qui trie une liste de parcs en un dictionnaire, en fonction des régions, des dates dates les plus récentes, et des régions avec le plus de 1/2 journées de travail
    ENTREE: donneesParcs (liste) Liste contenant différents parcs (devant contenir au moins les clés "departement", "dateEntretien", "urgence" et "nbDemiJoursTravail")
    SORTIE: dictParcsRange (dict) Dictionnaire des parcs rangés, et classés par régions (clé=région, valeur=liste de parcs)
    """
    dictParcs = {}
    for parc in donneesParcs: # Tri des parcs par région
        regionDuParc = findRegion(str(parc["departement"])) # On récupère la région du parc
        if regionDuParc in dictParcs.keys():# Si la région est déjà présente dans le dictionnaire des parcs
            dictParcs.get(regionDuParc).append(parc) # On ajoute le parc à sa région dans le dictionnaire
        else: # La région n'est pas encore présente dans le dictionnaire des parcs
            dictParcs[regionDuParc]=[parc] # On crée la région dans le doctionnaire et on y ajoute le parc
    for parcs in dictParcs.values(): # Tri des parcs par date croissantes pour chaque région
        parcs.sort(key=lambda x: x["dateEntretien"]) # Trier les parcs selon la date de l'entretien
        for i, parc in enumerate(parcs[:]):
            if parc["urgence"]==Urgence.organise.value: parcs.append(parcs.pop(i)) # Si un parc est d'urgence "organise" on l'ajoute à la fin de la liste
    listeTotaux = []
    i = 0
    for nomRegion, parcs in dictParcs.items():# Tri des régions selon celle qui a le plus de demi-journées de travail
        total = 0
        for parc in parcs: total+=int(parc["nbDemiJoursTravail"])
        listeTotaux.append((i, total))
        i+=1
    print("Liste du nouvel ordre", listeTotaux)
    ordreJoursTrav = [x[0] for x in sorted(listeTotaux, key=lambda tup: tup[1], reverse=True)]
    dictParcsRange = {list(dictParcs.keys())[i]:list(dictParcs.values())[i] for i in ordreJoursTrav}    
    print(dictParcsRange)
    return dictParcsRange
    
def createMaterielHTML(materiels):
    html = []
    for materiel, details in materiels.items():
        if details['nb']==0: continue
        nomMateriel = typeMateriel[materiel].replace('e','es') if int(details['nb'])>1 else typeMateriel[materiel]
        typeMatos = details['type'] if 'type' in details else ""
        html.append(f"{details['nb']} {nomMateriel} {typeMatos}")    
    return "<br>".join(html)

def createParkHTML(parc):
    infoSupDate = ""
    if parc['urgence']==Urgence.organise.value: infoSupDate = "<br>organisée"
    elif parc['urgence']==Urgence.dramatique.value: infoSupDate = "<br>en retard"
    nl = "\n"
    return f"""<tr>
                <td class=\"{parc['urgence']}\">{parc['dateEntretien'].strftime('%d %m %Y')} {infoSupDate}</td>
                <td>{createMaterielHTML(parc['materiel'])}</td>
                <td>{parc['nbDemiJoursTravail']} demi-journée(s) de travail</td>
                <td>{parc['nomEntreprise']}</td>
                <td>{"<br>".join(parc['contact'].values())}</td>
                <td>{parc['adresse'].replace(nl, ' ')}</td>
               </tr>"""

def createHTML(dicoParcs, dateDonnees, pathHTMLBrut):
    """
    Fonction qui crée l'HTML de l'email en récupérant le template "html_template.thml" et y ajoute les informations parsés
    ENTREE: dicoParcs (dict) Dictionnaire des parcs, rangé selon la région et l'importance
    SORTIE: html_final (str) L'HTML de l'email
    """
    with open(pathHTMLBrut,"r", encoding="utf8") as file:
        html_brut = file.read()
    htmlData = ""
    for region, parcs in dicoParcs.items(): 
        htmlData+=f"<tr><th colspan=\"6\">{region}</th></tr>"
        for parc in parcs: htmlData+=createParkHTML(parc)
    print("HTML créé", htmlData)
    html_final = html_brut.replace("<!-- INSERER TABLEAU -->", htmlData)
    html_final = html_final.replace("<!--DATE1-->", dateDonnees.strftime('%d %m %Y'))
    html_final = html_final.replace("<!--DATE2-->", (dateDonnees+ relativedelta(months=periodeEntretienEnMois)).strftime('%d %m %Y'))
    return html_final

def create_html_content(jsonFileName):
    """
    Fonction qui pour un nom de fichier JSON donné (qui doit être dans le même dossier que Editor.py) revoie l'HTML du mail correspondant
    ENTREE: jsonFileName (str) Le nom du fichier JSON contenant l'information (au format "nomDeFichier.json")
    SORTIE: html_content (str) L'html du contenu de mail sous forme de chaine de caractère 
    """
    donneesEntrees = readJSON(os.path.join(repertoire_actuel, jsonFileName))   # "Editor\\sample_ParserToEditor.json"
    listeParcs, dateDonnees = parseInputData(donneesEntrees)    
    dictParcsTrie = trierParcs(listeParcs)
    html_content = createHTML(dictParcsTrie, dateDonnees, os.path.join(repertoire_actuel, "html_template.html"))
    print(type(html_content))
    return html_content

refRegion(os.path.join(repertoire_actuel, "departements.json")) # On charge le dictionnaire des départements/régions dans la variable globale dictRegions
if __name__ == "__main__":
    html_content = create_html_content("data.json")
    print(html_content)