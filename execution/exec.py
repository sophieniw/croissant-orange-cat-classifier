#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 12:42:24 2019

@author: sophie
"""

import os
'''
!!!
changing working directory to the classifier directory
you will have a different path to your classifier directory
so you need to change the path to your own path
''' 
os.chdir("/Users/sophie/croissant-or-cat-classifier/") 

import image_process
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import models,layers,optimizers
from PIL import Image,ImageOps


'''
!!!
path of croissant pictures folder 
You need to change this path to your croissants folder path
'''
patho='/Users/sophie/croissant-or-cat-classifier/croissants/'
image_process.data_augmentation(patho,(50,50))
cro_set=image_process.img_to_arr(patho)
cro_set.shape


'''
You need to change this path to your orange_cats folder path
'''
pathc='/Users/sophie/croissant-or-cat-classifier/orange_cats/'
image_process.data_augmentation(pathc,(50,50))
cat_set=image_process.img_to_arr(pathc)
cat_set.shape


#0 as croissant; 1 as orange cat
label_croissant=[]
for i in range(len(cro_set)):
    label_croissant.append(0)

label_cat=[]
for i in range(len(cat_set)):
    label_cat.append(1)
    
np.array(label_croissant)
np.array(label_cat)

print(len(label_croissant))
print(len(label_cat))



training_images=np.concatenate((cro_set[:30000],cat_set[:30000]),axis=0)
training_images.shape
training_labels=np.concatenate((label_croissant[:30000],label_cat[:30000]),axis=0)
training_labels.shape



test_images=np.concatenate((cro_set[30000:],cat_set[30000:]),axis=0)
test_labels=np.concatenate((label_croissant[30000:],label_cat[30000:]),axis=0)

print(test_images.shape)
print(test_labels.shape)




#below to create a model for data training
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu',
                        input_shape=(50, 50, 3),data_format="channels_last"))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))



model.compile(loss='binary_crossentropy',
              optimizer=optimizers.RMSprop(lr=1e-4),
              metrics=['acc'])

history = model.fit(training_images,training_labels,
                    epochs=30,batch_size=128,
                    validation_data=(test_images, test_labels))

print(model.summary())

history_dict = history.history


acc = history_dict['acc']
val_acc = history_dict['val_acc']
epochs = range(1, len(acc) + 1)


plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Acc')
plt.legend()
plt.show()


#below to test image in the model to see if it's a croissant or a cat
#build a function to test multiple images

def test_img(path):
    img=Image.open(path)
    img=img.resize((50,50))
    arr=np.array(img)
    arr=np.expand_dims(arr,axis=0)
    return (model.predict(arr))


'''
!!!
You would need to use your own path with the test images
'''
path="/Users/sophie/croissant-or-cat-classifier/test_img/test_img"
#scores=[]
for item in os.listdir(path):
    try:
        imgpath=os.path.join(path,item)
        score=test_img(imgpath)
        print(item,score)
        
        #scores.append(score)
    except:
        print('Error: ', score)
    



    