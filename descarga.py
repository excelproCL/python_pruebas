import requests
url="https://www.python.org/static/img/python-logo@2x.png"
myfile=requests.get(url)
open ("C:/Users/siste/OneDrive - Academia de Derecho y Ciencias/Programacion/Python/Pruebas/imagen.png", "wb").write(myfile.content)
#javascript:generaXLS();
#https://docs.python-requests.org/en/latest/
#https://likegeeks.com/es/descargar-archivos-usando-python/