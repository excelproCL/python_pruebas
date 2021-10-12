#Crea directorios segun matriz
directorios=["Sede Antonio Varas","Sede Casa Central","Sede Alameda","Sede Alonso Ovalle","Sede Plaza Oeste","Sede Puente Alto","Sede Pirque","Sede San Carlos","Sede San Joaquin","Sede Valparaiso","Sede Educacion Continua","Sede Maipu","Sede Plaza Norte","Sede Plaza Vespucio","Sede San Bernardo","Sede Viña del Mar","Sede Melipilla"]
#define la carperta "Padre"
carpetaPadre="C:/Users/siste/OneDrive - Ematel SA/07A-DUOC/Mantencion Transformadores/"

import os

#carpeta=replace(carpeta'\',"'\\'")
#print(carpeta)
#itera lista
for i in directorios:
    #print(carpetaPadre+i)
    newCarpeta=carpetaPadre+i
    os.makedirs(newCarpeta,exist_ok=True)
#    print("C:\Users\siste\OneDrive - Ematel SA\07A-DUOC\Mantencion Transformadorescarpeta",i)'''
    
    
