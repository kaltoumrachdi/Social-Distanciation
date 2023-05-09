#!/usr/bin/env python
# coding: utf-8

# In[2]:


# on importe les modules dont on a besoin 
import cv2
from math import sqrt
import numpy as np 
#on lit la vidéo qui existe dans l'adresse passée à la fonction VideoCapture d'openCv 
cap=cv2.VideoCapture("C:/Users/azert/Desktop/projetMadani/Person.mp4")
#on donne à la variable body le modèle de l'objet qu'on souhaite chercher et détecter dans la vidéo en lui passant à la fonction CascadeClassifer 
body=cv2.CascadeClassifier("C:/Users/azert/anaconda3/Lib/site-packages/cv2/data/haarcascade_fullbody.xml")
#on parcourt chaque capture de la vidéo retournée pour y faire le traitement afin de détectre les personnes dans chaque capture 
while  1:

# on lit chaque capture avec la fonction read() en l'appliquant sur la capture 
    r,img=cap.read()
# on transforme l'image de l'espace en couleur vers le niveaux de gris pour une meuilleure détection 
    gray= cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# en utilisant la fonction detectMultiScale() on détecte les objets que leurs caractéristiques techniques sont contenues dans la variable body
    bd=body.detectMultiScale(gray,1.2,3)
#  on parcourt chaque quadriplet retourné par la fonction detectMultiScale() 
    for(x,y,w,h) in bd :
# on dessine un rectangle en utilisant le quadriplet retourné par la fonction detectMultiScale() en utilisant le point le plus haut gache de cordonnées (x,y) et le point le plus bas droit du rectangle qu'on calcule d'aprés (x,y) en utlisant la largeur et la hauteur du rectangle retournées aussi par la fonction detectMultiScale()
       cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1) 
#pour le quadriplet en cours de parcours on parcourt tous les autres quadriplets 
       for(x1,y1,w1,h1) in bd:
# ces variables sont pour calculer les cordonnées du centre de chaque rectangle    
             b=w/2
             c=h/2
             b1=w1/2
             c1=h1/2
#on calcule les distances entre chaque rectangle parcouru par rapport avec le rectangle parcouru du boucle qui contient cette boucle 
                
             d1=(x+b)-(x1+b1)
             d2=(y+c)-(y1+c1)
             d=sqrt((d1**2)+(d2**2))
# on transtype la distance d en une chaine de caractère pour l'afficher par la suite sur l'image                 
             a=str(d)
# on choisit le seuil qu'on va comparer la distance entre deux rectangles avec 
             N=400
# on transtype les variables calculées avant pour déterminer les cordonnées du centre du rectangle car on va les utliser pour dessine une ligne entre les centres des rectangles ,et la fonction line prends en paramètre un entier pas un float
             d=int(b)
             e=int(c)
             d1=int(b1)
             e1=int(c1)
# on choisit une font pour l'utiliser pour écrire la valeur de distance entre chaque deux rectangles 
             font=cv2.FONT_HERSHEY_SIMPLEX
# on affiche la distance entre chaque deux rectangles sur l'image 
             cv2.putText(img,a,(x,y),font,0.3,(255,255,255),1,cv2.LINE_AA)
# on étudie les cas pour la distance si elle est inférieure au seuil on dessine une ligne rouge entre les centres des deux rectangles sinon on fdessine une ligne bleue             
             if( d<N):
                      cv2.line(img,(x+d,y+e),(x1+d1,y1+e1),(0,0,255),3)
                      
             else: 
                      cv2.line(img,(x+d,y+e),(x1+d1,y1+e1),(255,0,0),3)
# on affiche l'image ou on a dessiné les lignes et affiché les valeurs de distances                     
    
             cv2.imshow("image",img)
# on affecte à la variable key un listener qui écoute les clics sur le clavier et qui fait une pause au cas de clic sur la clé p et sort si on clique surla clé q 
    key=cv2.waitKey(1)
    if  key == ord('q'):
        break 
    if key == ord('p') :
       cv2.waitKey(-1)
# on libère la valeur cap qui contient les captures de la vidéo 
cap.release()
# on détruit tous les fenetres img 
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




