"""
to resize every image in folders orange_cats and croissants
"""
from skimage.util import random_noise
from PIL import Image,ImageOps
import os
import numpy as np



def resize_image(path,pixel_size):
    #print(path)   
    for item in os.listdir(path):
        try:
            imgpath=os.path.join(path,item)
            img=Image.open(imgpath)
            img=img.resize(pixel_size,Image.ANTIALIAS)
            img.save(imgpath)
        except:
            print("Error occurred: ", imgpath)



def scale_image(path,area,pixel_size):
    for item in os.listdir(path):
        try:
            imgpath=os.path.join(path,item)
            img=Image.open(imgpath)
            cropped=img.crop(area)
            cropped=cropped.resize(pixel_size,Image.ANTIALIAS)
            cropped.save(os.path.join(path,"scaled_"+item))
        except:
            print("Error occurred: ", imgpath)

"""
to mirror an image horizontally (*2 total img number)
"""
def mirror_image(path):
    for item in os.listdir(path):
        try:
            imgpath=os.path.join(path,item)
            img=Image.open(imgpath)
            mirror_img=ImageOps.mirror(img)
            mirror_img.save(os.path.join(path,"mirror_"+item))
        except:
            print("Error occurred: ", imgpath)
        

"""
to rotate an image certain degrees (*16 total )
""" 
def rotate_image(path,degree):
    for item in os.listdir(path):
        try:
            imgpath=os.path.join(path,item)
            img=Image.open(imgpath)
            rotate_img=img.rotate(degree)
            rotate_img.save(os.path.join(path,str(degree)+"_"+item))

        except:
            print("Error occurred: ", imgpath)


            
"""
below is to add noise to the images but it's not necessarily needed
"""

"""
to create gaussian noise for images (*2 total)
"""


def gauss_noise_image(path):
    for item in os.listdir(path):
        try:
            imgpath=os.path.join(path,item)
            img=Image.open(imgpath)
            
            arr=np.array(img)
            noisy_arr=random_noise(arr,mode='gaussian', seed=None, clip=True)
            noisy_arr=(noisy_arr*255).astype(np.uint8)
            noisy_img = Image.fromarray(noisy_arr)

            noisy_img.save(os.path.join(path,"gauss_"+item))

        except:
            print("Error occurred: ", imgpath)




"""
below to create speckle noise for images (*2 total)
"""

def sp_noise_image(path):
    for item in os.listdir(path):
        try:
            imgpath=os.path.join(path,item)
            img=Image.open(imgpath)
            
            arr=np.array(img)
            noisy_arr=random_noise(arr,mode='s&p', seed=None, clip=True)
            noisy_arr=(noisy_arr*255).astype(np.uint8)
            noisy_img = Image.fromarray(noisy_arr)

            noisy_img.save(os.path.join(path,"s&p_"+item))

        except:
            print("Error occurred: ", imgpath)


    
