file=open("~/Desktop/co2.csv", "r")  #Ouverture du fichier des données brutes

lines=file.readlines() #Récupération des données
file.close()

data=open("~/Desktop/export.csv" ,"w") #Ouverture du fichier des données traitées

lines[0]=lines[0][11:26] #Traitement de la ligne 1
lines[0]=3600*int(lines[0][0:2])+60*int(lines[0][3:5])+int(lines[0][6:8])+int(lines[0][9:15])*1E-6
lines[-1]+='\n'

data.write('Temps (s), Concentration (ppm), Température (°C)'+'\n') #En-tête

for k in range(1,len(lines)):
    CO2_T_values=str(lines[k][26:]) #Sauvegarde des données
    lines[k]=lines[k][11:26] #Traitement du reste des lignes
    lines[k]=3600*int(lines[k][0:2])+60*int(lines[k][3:5])+int(lines[k][6:8])+int(lines[k][9:15])*1E-6
    lines[k]-=lines[0] #Retranchement de la ligne 1
    ckValue=int(lines[k]) #Variable test valeur
    if ckValue%2==1: #Test de la parité de ckValue
        print('Impair')
    data.write(str(round(lines[k]))+CO2_T_values) #Copie dans le fichier d'export

data.close()
