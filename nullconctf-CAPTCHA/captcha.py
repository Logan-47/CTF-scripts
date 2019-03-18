import sys
from PIL import Image
import cv2
import numpy as np
import os
import socket

# os.system('clear')
def identical(original1,charZ):
    difference = cv2.subtract(original1, charZ)
    b, g, r = cv2.split(difference)

    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        # print("The images are completely Equal")
        return True
    return False

decrypt = []


def solver(original1,decrypt):
    if identical(original1,charA):
        # print "its A"
        decrypt.append('A')
    elif identical(original1,charB):
        # print "Its B"
        decrypt.append('B')
    elif identical(original1,charC):
        # print "Its C"
        decrypt.append('C')
    elif identical(original1,charD):
        # print "Its D"
        decrypt.append('D')
    elif identical(original1,charE):
        # print "Its E"
        decrypt.append('E')
    elif identical(original1,charF):
        # print "Its F"
        decrypt.append('F')
    elif identical(original1,charG):
        # print "Its G"
        decrypt.append('G')
    elif identical(original1,charH):
        # print "Its H"
        decrypt.append('H')
    elif identical(original1,charJ):
        # print "Its J"
        decrypt.append('J')
    elif identical(original1,charI):
        # print "Its I"
        decrypt.append('I')
    elif identical(original1,charK):
        # print "Its K"
        decrypt.append('K')
    elif identical(original1,charL):
        # print "Its L"
        decrypt.append('L')
    elif identical(original1,charM):
        # print "Its M"
        decrypt.append('M')
    elif identical(original1,charN):
        # print "Its N"
        decrypt.append('N')
    elif identical(original1,charO):
        # print "Its O"
        decrypt.append('O')
    elif identical(original1,charP):
        # print "Its P"
        decrypt.append('P')
    elif identical(original1,charQ):
        # print "Its Q"
        decrypt.append('Q')
    elif identical(original1,charR):
        # print "Its R"
        decrypt.append('R')
    elif identical(original1,charS):
        # print "Its S"
        decrypt.append('S')
    elif identical(original1,charT):
        # print "Its T"
        decrypt.append('T')
    elif identical(original1,charU):
        # print "Its U"
        decrypt.append('U')
    elif identical(original1,charV):
        # print "Its V"
        decrypt.append('V')
    elif identical(original1,charW):
        # print "Its W"
        decrypt.append('W')
    elif identical(original1,charX):
        # print "Its X"
        decrypt.append('X')
    elif identical(original1,charY):
        # print "Its Y"
        decrypt.append('Y')
    elif identical(original1,charZ):
        # print "Its Z"
        decrypt.append('Z')



data=""
fopen = open('img.png','w+')
data =sys.argv[1]
# print "lenght of data: "+str(len(data))
data = data.strip()
# print "lenght of data: "+str(len(data))
imgdata = data.decode('hex')
fopen.write(imgdata)
fopen.close()


img = Image.open('img.png')
img2 = Image.open('img.png')
img3 = Image.open('img.png')
width, height = img.size
area1 = (0,0,width/4,height)
img = img.crop(area1)
img.save("img-1.png")
area2 = (width/4,0,width/2,height)
img2 = img2.crop(area2)
img2.save("img-2.png")
area3 = (width/2,0,width,height)
img3 = img3.crop(area3)
img3.save("img-3.png")
img4 = Image.open("img-3.png")
img5 = Image.open("img-3.png")
width1, height1 = img4.size
# area4 = (0,0,width/2,height)
area4 = (0,0,width1/2,height1)
img4 = img4.crop(area4)
img4.save("img-4.png")
area5 = (width1/2,0,width1,height1)
img5 = img5.crop(area5)
# img2 = img2.crop(area1)
img5.save("img-5.png")
# img2.save("crop3-2.png")


original1 = cv2.imread("img-1.png")
original2 = cv2.imread("img-2.png")
original3 = cv2.imread("img-4.png")
original4 = cv2.imread("img-5.png")

charA = cv2.imread("a.png")
charB = cv2.imread("b.png")
charC = cv2.imread("c.png")
charD = cv2.imread("d.png")
charE = cv2.imread("e.png")
charF = cv2.imread("f.png")
charG = cv2.imread("g.png")
charH = cv2.imread("h.png")
charJ = cv2.imread("j.png")
charK = cv2.imread("k.png")
charL = cv2.imread("l.png")
charM = cv2.imread("m.png")
charN = cv2.imread("n.png")
charO = cv2.imread("o.png")
charP = cv2.imread("p.png")
charQ = cv2.imread("q.png")
charR = cv2.imread("r.png")
charS = cv2.imread("s.png")
charT = cv2.imread("t.png")
charU = cv2.imread("u.png")
charV = cv2.imread("v.png")
charW = cv2.imread("w.png")
charX = cv2.imread("x.png")
charY = cv2.imread("y.png")
charZ = cv2.imread("z.png")
charI = cv2.imread("i.png")

solver(original1,decrypt)
solver(original2,decrypt)
solver(original3,decrypt)
solver(original4,decrypt)

finalthing = ''.join(decrypt)
print finalthing
