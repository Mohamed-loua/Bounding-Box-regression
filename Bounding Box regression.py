# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 20:56:38 2021

@author: BERETE Mohamed Loua
"""

from pyimagesearch import config
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os


#définir un accès jusqu'aux données et les images 
images_chemin = os.path.sep.join(["dataset", "images"])
box = os.path.sep.join(["dataset", "airplanes.csv"]) 

#Extraction de la localisation prédéfini des bounding box de la base de donnée airplanes
box_real = open(box).read().strip().split("\n")
print(box_real)

#Test pour comprendre le format des données de open cv
s = "image_0001.jpg"
image = os.path.sep.join([images_chemin,s])
images = cv2.imread(image)
print(load_img(image, target_size=(224,224)))

# Nous avons récupéré le numéro de l'image avec les coordonnées des bounding boxs adéquates, nous voulons maintenant extraire 
# et enregistrer uniquement les coordonnées des bounding boxs
for x in box_real[:]:
    x = x.split(",")
    nom_image , startX, startY ,endX ,endY = x
    #les coordonées des bounding box et leurs noms sont stockés des le variables que j'ai défini
    #Maintenant nous allons normaliser les coordonnées que nous avons extraite: d'abord il faut obtenir les dimensions de l'image
    image_path = os.path.sep.join([images_chemin,nom_image])
    
    #Avec open cv on récupère les dimensions de l'image
    image = cv2.imread(image_path)
    (h,w,d) = image.shape
    
    
    #Normalisation des données 
    startX = float(startX) / w
    endX = float(endX) / h
    startY = float(startY) / w
    endY = float(endY) / h
    
    #Conversion de l'image en array
    image = load_img(image_path, target_size = (224,224))
    image = img_to_array(image)
    data.append(image)
    targets.append([startX,endX,startY,endY]) 
    names.append(nom_image)
    
    #Test du bon fonctionnement du dictionnaire
print(targets[0])
# Conversion des données en array numpy et normalisation:
data = (np.array(data))/255
targets = np.array(targets)
