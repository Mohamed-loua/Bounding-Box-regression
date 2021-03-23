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