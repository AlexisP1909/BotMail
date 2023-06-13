from openpyxl import load_workbook
import pandas as pd
import datetime
import json
# Load the Excel workbook
wb = load_workbook('PlanningSandbox.xlsx')

#Variables 
NuméroLigneEnTetes = 2
NomC_Entreprise = "Entreprise"
NomC_BornesSimpl = "Bornes Simples"
NomC_BornesDoubles = "Bornes Doubles"
NomC_Armoires = "Armoires"
NomC_NbDemiJournees = "Nombre de demi-journées"
NomC_Adresse = "Adresse"
NomC_Departement = "Département"
NomC_Contact = "Contact"
NomC_DateMiseEnService = "Date de mise en service"
NomC_Periodicite = "Périodicité en mois"
NomC_VisiteOrganisee = "Visite Organisée?"

# Select the worksheet
feuille = wb['Clients']

# Create an empty list to store the evaluated values
data = []

# Iterate over rows and columns to get evaluated values
for row in feuille.iter_rows(values_only=True):
    row_values = []
    for cell in row:
        evaluated_value = cell
        row_values.append(evaluated_value)
    data.append(row_values)

# Create a Pandas DataFrame from the data
df = pd.DataFrame(data)
nb_lignes, nb_colonnes = df.shape

#Initialisation des Variables des numéros de colonnes
numC_Entreprise=-1
numC_Adresse=-1
numC_Departement=-1
numC_BornesSimpl=-1
numC_BornesDoubles=-1
numC_Armoires=-1
numC_=-1
numC_Contact=-1
numC_DateMiseEnService=-1
numC_Periodicite=-1
numC_VisiteOrganisee = []

#Parcourt la ligne des en-têtes pour trouver les colonnes relatives aux informations souhaitées
for i in range(0,nb_colonnes) :
    if df.iloc[NuméroLigneEnTetes,i] is not None:
            if df.iloc[NuméroLigneEnTetes,i].lower()==NomC_Entreprise.lower() : #teste la correpondance sans prendre en compte les majuscules
                numC_Entreprise = i #stocke le numéro de la colonne
            elif df.iloc[NuméroLigneEnTetes,i].lower()==NomC_BornesSimpl.lower() :
                numC_BornesSimpl=i
            elif df.iloc[NuméroLigneEnTetes,i].lower()==NomC_BornesDoubles.lower() :
                numC_BornesDoubles=i
            elif df.iloc[NuméroLigneEnTetes,i].lower()==NomC_Armoires.lower() :
                numC_Armoires=i
            elif df.iloc[NuméroLigneEnTetes,i].lower()==NomC_NbDemiJournees.lower() :
                numC_NbDemiJournes=i
            elif df.iloc[NuméroLigneEnTetes,i].lower()==NomC_Adresse.lower() :
                numC_Adresse = i
            elif df.iloc[NuméroLigneEnTetes,i].lower()==NomC_Departement.lower() :
                numC_Departement=i
            elif df.iloc[NuméroLigneEnTetes,i].lower()==NomC_Contact.lower() :
                numC_Contact = i
            elif df.iloc[NuméroLigneEnTetes,i].lower()==NomC_DateMiseEnService.lower() :
                numC_DateMiseEnService = i
            elif df.iloc[NuméroLigneEnTetes,i].lower()==NomC_Periodicite.lower() :
                numC_Periodicite = i
            elif df.iloc[NuméroLigneEnTetes,i].lower()==NomC_VisiteOrganisee.lower() :
                numC_VisiteOrganisee.append(str(i))#stocke chaque numéro de colone relevé

#Création des listes et dictionnaires globaux
EnvoiJSON = {}
date = str(datetime.datetime.today().strftime("%d/%m/%Y"))
EnvoiJSON["dateDonnees"] = date
ListesParcs = []
for i in range(3,nb_lignes):
    #Initialisation des Variables de données
    NbVisitesOrganisees = 0

    #Variables pour la lisibilité et traitement
    Entreprise = df.iloc[i,numC_Entreprise]

    BornesSimpl = str(df.iloc[i,numC_BornesSimpl]).split(" ",1)
    BornesDoubles = str(df.iloc[i,numC_BornesDoubles]).split(" ",1)
    Armoires = str(df.iloc[i,numC_Armoires]).split(" ",1)

    NbDemiJournees = df.iloc[i,numC_NbDemiJournes]

    Adresse = df.iloc[i,numC_Adresse]
    Departement = df.iloc[i,numC_Departement]

    Contact = df.iloc[i,numC_Contact].split()

    DateMiseEnService = df.iloc[i,numC_DateMiseEnService]
    Periodicite = df.iloc[i,numC_Periodicite]
    for j in range(0,len(numC_VisiteOrganisee)-1):
        NbVisitesOrganisees +=1
    #Création des sous-sous-dictionnaires
    DictionnaireContact = {}
    if len(Contact)>0 :
        DictionnaireContact["prenom"] = Contact[0]
        if len(Contact)>1 :
            DictionnaireContact["nom"] = Contact[1]
            if len(Contact)>2 :
                     DictionnaireContact["telephone"] = Contact[2]
                     if len(Contact)>3 :
                        DictionnaireContact["email"] = Contact[3]


    DictionnaireBorneSimple = {}
    if(len(BornesSimpl)>0):
        DictionnaireBorneSimple["nb"] = BornesSimpl[0]
        if(len(BornesSimpl)>1):
          DictionnaireBorneSimple["type"] = BornesSimpl[1]
   
    DictionnaireBorneDouble = {}
    if(len(BornesDoubles)>0):
        DictionnaireBorneDouble["nb"] = BornesDoubles[0]
        if(len(BornesDoubles)>1):
            DictionnaireBorneDouble["type"] = BornesDoubles[1]
    
    DictionnaireArmoires = {}
    if(len(Armoires)>0):
        DictionnaireArmoires["nb"] = Armoires[0]
        if(len(Armoires)>1):
            DictionnaireArmoires["type"] = Armoires[1]

    DictionnaireMateriel = {}
    DictionnaireMateriel["borneSimple"]=DictionnaireBorneSimple
    DictionnaireMateriel["borneDouble"]=DictionnaireBorneDouble
    DictionnaireMateriel["armoire"]=DictionnaireArmoires
    #Dictionnaire Parc
    DictionnaireParc = {}
    DictionnaireParc["departement"] = Departement
    DictionnaireParc["dateMiseEnService"] = str(DateMiseEnService.strftime("%d/%m/%Y"))
    DictionnaireParc["periodiciteEnMois"] = Periodicite
    DictionnaireParc["nbVisitesOrganisees"] = NbVisitesOrganisees
    DictionnaireParc["nbDemiJoursTravail"] = NbDemiJournees
    DictionnaireParc["contact"] = DictionnaireContact
    DictionnaireParc["materiel"] = DictionnaireMateriel
    DictionnaireParc["nomEntreprise"] = Entreprise
    DictionnaireParc["adresse"] = Adresse

    ListesParcs.append(DictionnaireParc)

EnvoiJSON["parcs"] = ListesParcs
out_file = open("data.json", "w")
json.dump(EnvoiJSON,out_file)