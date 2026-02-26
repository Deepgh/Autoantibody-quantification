import os
import matplotlib.pyplot as plt
import numpy as np
from tifffile import imread
from scipy.ndimage import gaussian_filter 

directory = 'E:/Blimp1Slides/X_Week8_40X/'
files = os.listdir(directory)
fls = []
for f in files:
    a=f.replace("_ch00","")
    fls.append(a)
fls = [k for k in fls if k.split("_")[-1]=="RAW.tif"]
file = fls[9] # change the number 0,1 ... for next file
file = file.replace(".tif","")

nuclear_path = directory + file + '_ch00.tif'
auto_path = directory + file + '_ch01.tif' 

nuc_th = 7000 #nuclear thershold value
tiss_th = 800 #tissue thershold value
nuc_sigma = 2
tiss_sigma = 3
blur_sigma = 500

image = imread(nuclear_path)
nucleus = gaussian_filter(image, nuc_sigma)
nucleus_mask = np.where(nucleus > nuc_th,1,0)
plt.imshow(nucleus_mask)
plt.title("nucleus")
plt.show()
plt.clf()

tissue = gaussian_filter(image,tiss_sigma)
tissue_mask = np.where(tissue> tiss_th,1,0)
plt.imshow(tissue_mask)
plt.title("tissue")
plt.show()
plt.clf()

only_tissue = tissue_mask - nucleus_mask
only_tissue = np.where(only_tissue<0,0,only_tissue)
plt.imshow(only_tissue)
plt.title("only tissue")
plt.show()
plt.clf()

print(file)
print("mask values nuclei: " + str(np.unique(nucleus_mask)))
print("mask values tissue: " + str(np.unique(tissue_mask)))
print("mask values only tissue: " + str(np.unique(only_tissue)))

autoAb = imread(auto_path)
blur = gaussian_filter(autoAb,blur_sigma)
plt.imshow(blur)
plt.title("blur")
plt.show()
plt.clf()
autoAb = autoAb/blur
plt.imshow(autoAb)
plt.title("autoAb")
plt.show()
plt.clf()
autoAb = 65535*(autoAb/np.max(autoAb))
auto_nucleus = np.sum(nucleus_mask*autoAb, dtype = np.int64)
auto_cyto = np.sum(only_tissue*autoAb, dtype = np.int64) 

print("Total intensity Nucleus: "+str(auto_nucleus))
print("Total intensity Cytoplasm: "+str(auto_cyto))

only_nucleus_area = np.sum(nucleus_mask, dtype = np.int64)
only_cytoplasm_area = np.sum(only_tissue, dtype = np.int64)

#Calculating the mean intensities
nucelus_mean_intensity = float(auto_nucleus/only_nucleus_area)
only_cytoplasm_mean_intensity = float(auto_cyto/only_cytoplasm_area)
print(nucelus_mean_intensity/ only_cytoplasm_mean_intensity)

print('Nucleus MI ' +str(nucelus_mean_intensity))
print('Cytoplasm MI ' + str(only_cytoplasm_mean_intensity))