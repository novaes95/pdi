# -*- coding: utf-8 -*-
"""lendo img.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11I-1PEB8uf_2sFaH2k_XCzBciv4wQWV6
"""

!pip install gdal
!pip install rasterio

!pip install spectral

import tifffile as tif
import matplotlib.pyplot as plt
from spectral import imshow
import numpy as np

img = tif.imread('/content/L71221071_07120010720_DN.tif')

print (img)

img.shape
#representação linha coluna bandas

plt.imshow(img[:,:,0])
#plotar todas as linhas ( : ) e colunas, e a banda 1 - 0 pq python começa a contar do 0

plt.imshow(img[:,:,0],cmap='grey') 
#errei a banda de cores, o metodo lista as que existem

plt.imshow(img[:,:,0],cmap="Greys_r")

plt.imshow(img[:,:,3],cmap="Greys_r")
#plotar a banda 4

imshow(img,bands=(2,1,0))
#imshow do spctral fazendo composição de bandas 3,2,1
#apesar de simples e fácil, ele perde algumas informações no método de visualização como as coordenadas

from osgeo import gdal
#vizualizar na biblioteca gdal

img2 =gdal.Open('/content/L71221071_07120010720_DN.tif')

print (img2)
#n esta na estrutura do numpy que facilita o trabalho

imshow(img2)

img3 = img2.ReadAsArray()
imshow(img3)
#agora leu ma esta alguma coisa errada,

img3.shape
# esta com argumentos trocadas, antes lia linha/coluna/banda - desta forma esta banda/linha/coluna

img3 =img3.swapaxes(0,2)
#troca de lugar banda com coluna
img3 =img3.swapaxes(0,1)
#troca de lugar banda com coluna com linha
img3.shape
#agora a representação esta ok linha coluna banda

imshow(img3,bands=(2,3,1))

b1 = img2.GetRasterBand(1).ReadAsArray()
#outro metodo para ler bandas como array e usar numpy - atenção que o gdal
# foge da logica python e começa a contar bandas do 1

imshow(b1)

b2 = img2.GetRasterBand(2).ReadAsArray()
b4 = img2.GetRasterBand(4).ReadAsArray()
#bandas separadas mas estao lidas ok

stack = np.dstack([b1,b2,b4])
#stackando as bandas (só as 3 que selecionei)
stack.shape

imshow(stack,bands=(1,2,0))
#deu certo mas tb esta sem coordenadas

import rasterio
from rasterio.plot import show

rst = rasterio.open('/content/L71221071_07120010720_DN.tif')

print(rst)
#n veio como array bonitinho da numpy

show(rst,cmap='Greys_r')
#veio com as coordenadas UTM

b1  =rst.read(1)
b2  =rst.read(2)
b4  =rst.read(4)

stack2 = np.dstack([b1,b2,b4])

imshow(stack2,bands=(1,2,0))

with rasterio.open('/content/L71221071_07120010720_DN.tif') as rst:
  b1  =rst.read(1)
  b2  =rst.read(2)
  b4  =rst.read(4)
stack3 = np.dstack([b1,b2,b4])
#outro metodo usando with que roda o processo rasterio.open depois fecha para n deixar rastro na memoria

imshow(stack3,bands=(1,2,0))