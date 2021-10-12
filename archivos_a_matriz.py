#listar archivo a una matriz
import os
directorioRaiz="C:\\Users\\siste\\OneDrive - Ematel SA\\Datos adjuntos\\03_RRHH\\00_Carpetas de Personal"
listado=os.listdir(directorioRaiz)
print(listado)#Crea directorios segun matriz
#directorios=["Sede Antonio Varas","Sede Casa Central","Sede Alameda","Sede Alonso Ovalle","Sede Plaza Oeste","Sede Puente Alto","Sede Pirque","Sede San Carlos","Sede San Joaquin","Sede Valparaiso","Sede Educacion Continua","Sede Maipu","Sede Plaza Norte","Sede Plaza Vespucio","Sede San Bernardo","Sede Viña del Mar","Sede Melipilla"]
#define la carperta "Padre"
#carpetaPadre="C:/Users/siste/OneDrive - Ematel SA/07A-DUOC/Mantencion Transformadores/"



#carpeta=replace(carpeta'\',"'\\'")
#print(carpeta)
#itera lista
for i in listado:
    carpeta=directorioRaiz+"\\"+i
    print(carpeta+"\n")
    os.listdir(carpeta)
    #newCarpeta=carpetaPadre+i
    #os.makedirs(newCarpeta,exist_ok=True)
#    print("C:\Users\siste\OneDrive - Ematel SA\07A-DUOC\Mantencion Transformadorescarpeta",i)'''
    