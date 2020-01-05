file=open("/root/Desktop/data.txt", "r")  #Ouverture du fichier des donnees brutes

lines=file.readlines() #Recuperation des donnees
file.close()

data=open("/root/Desktop/export.txt" ,"w") #Ouverture du fichier des donnees traitees

lines[0]=lines[0][11:26] #Traitement de la ligne 1
lines[0]=3600*int(lines[0][0:2])+60*int(lines[0][3:5])+int(lines[0][6:8])+int(lines[0][9:15])*1E-6
lines[-1]+='\n'

for k in range(1,len(lines)): #La dernière
    lines[k]=lines[k][11:26] #Traitement du reste des lignes
    lines[k]=3600*int(lines[k][0:2])+60*int(lines[k][3:5])+int(lines[k][6:8])+int(lines[k][9:15])*1E-6
    lines[k]-=lines[0] #Retranchement du la ligne 1
    data.write(str(lines[k])) #Ecriture dans le fichier d'export
    data.write('\n')

data.close()
