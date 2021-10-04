import os
import cv2

Nombre_carpeta = 'Fotos de Video'
Ubicacion_carpeta = 'C:/Users/PC/TrabajosPython' #Cambia a la ruta donde hayas almacenado Data
Carpeta = Ubicacion_carpeta + '/' + Nombre_carpeta

if not os.path.exists(Carpeta):
	print('Carpeta creada: ',Carpeta)
	os.makedirs(Carpeta)

cap = cv2.VideoCapture('prueba/videoprueba.mp4')
n_imagen= 0

while (cap.isOpened()):
    ret,frame = cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if ret == False:
        break
    #cv2.imwrite(Carpeta +'frame' + str(n_imagen) + '.png', frame)
    cv2.imwrite(Carpeta + '/frame_{}.png'.format(n_imagen),frame)
    n_imagen +=1

    if n_imagen>=10:
        break






