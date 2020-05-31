import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import random
import string

import pytesseract
from PIL import Image

import constants

filelist = ['current_route/'+file for file in os.listdir('current_route') if file.endswith('.png')]
images = [cv2.imread(img) for img in filelist]
#images = [cv2.cvtColor(img, cv2.COLOR_BGR2RGB) for img in images]

def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 10)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value

def findArrows(im):
    im_gray = cv2.cvtColor(im[:,:im.shape[1]//4], cv2.COLOR_BGR2GRAY)
    template = cv2.imread("templates/arrow_down.png", cv2.IMREAD_GRAYSCALE)
    m = cv2.matchTemplate(im_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.argmax(m)
    loc2 = m > 0.6

    fig, ax = plt.subplots(1, 3)
    ax[0].imshow(im)
    ax[1].imshow(m)
    ax[2].imshow(loc2)
    plt.show()

    return np.unravel_index(loc, m.shape)

def imageIcons(im):
    locs = [(259, 212), (259, 279), (259, 345), (259, 412), (259, 479),  (530, 212), (530, 279), (530, 345), (530, 412), (530, 479)]
    w = 40
    h = 40

    fig, ax = plt.subplots(5, 2)
    subs = []
    
    for i,(x,y) in enumerate(np.ndindex((5,2))):
        c = locs[i]
        sub = im[ c[1]:c[1]+h, c[0]:c[0]+w ]
        subs.append(sub)
        ax[x,y].imshow(sub)
    #plt.show()

    return subs

def islandNames(im):

    islandNames = []

    h = 24
    w = 180
    yoff = 207
    d = 66
    rois = [(18, yoff, w, h), (18, yoff + d*1, w, h), (18, yoff + d*2, w, h), (18, yoff + d*3, w, h), (18, yoff + d*4, w, h)]

    for (x,y,w,h) in rois:
        c = im[y:y+h, x:x+w, :]
        c = 255 - c
        #cv2.imshow("", c)
        #cv2.waitKey()
        txt = pytesseract.image_to_string(Image.fromarray(c), config="--oem 3 --psm 6")
        
        #idx = txt.find(" Island")
        #print(idx)
        #txt = txt[:idx]

        
        txt_verified, dst = constants.findClosestIsland(txt, max_chars = len(txt))
        if dst > 10:
            print(txt)
            print(txt_verified)
            exit(-1)

        #print(txt)
        #print(txt_verified)
        yield txt_verified

def islandNumbers(im):
    h = 24
    w = 180
    yoff = 227
    d = 66
    rois = [(18, yoff, w, h), (18, yoff + d*1, w, h), (18, yoff + d*2, w, h), (18, yoff + d*3, w, h), (18, yoff + d*4, w, h)]

    for (x,y,w,h) in rois:
        c = im[y:y+h, x:x+w, :]
        c = 255 - c
        txt = pytesseract.image_to_string(Image.fromarray(c), config="--oem 3 --psm 6")
        
        #print(txt)
        #cv2.imshow("", c)
        #cv2.waitKey()
        
        idx = txt.find(": ") + 2
        num = txt[idx:]
        yield int(num)

def itemNames(im):

    h = 20
    w = 180
    yoff = 210
    d = 66
    xoff = 310
    roisLeft = [(xoff, yoff, w, h), (xoff, yoff + d*1, w, h), (xoff, yoff + d*2, w, h), (xoff, yoff + d*3, w, h), (xoff, yoff + d*4, w, h)]


    xoff = 570
    h = 45
    w = 200
    roisRight = [(xoff, yoff, w, h), (xoff, yoff + d*1, w, h), (xoff, yoff + d*2, w, h), (xoff, yoff + d*3, w, h), (xoff, yoff + d*4, w, h)]

    for (x,y,w,h) in roisLeft + roisRight:
        c = im[y:y+h, x:x+w, :]
        c = 255 - c
        #cv2.imshow("", c)
        #cv2.waitKey()
        txt = pytesseract.image_to_string(Image.fromarray(c), config="--oem 3 --psm 6")
        txt_verified, dst = constants.findClosestItem(txt, max_chars = len(txt))

        """if dst > 10:
            print("ATTENTION") 
            print()

        print('"%s" -> "%s"' % (txt, txt_verified))"""
        yield txt_verified

def getNumberFromIcon(icon):
    
    
    
    sub = icon[20:35, 20:-1, :].astype(np.float)

    diff0 = abs(sub[:,:,0] - sub[:,:,1])
    diff1 = abs(sub[:,:,1] - sub[:,:,2])
    diff2 = abs(sub[:,:,2] - sub[:,:,0])
    avg_diff = 5 * (diff0+diff1+diff2) / 3.0
    
    sub = sub - np.dstack((avg_diff,avg_diff,avg_diff))
    sub[sub < 0] = 0
    cleaned = sub.astype(np.uint8)
    
    c = cv2.copyMakeBorder( cleaned, 0,20,20,20, cv2.BORDER_CONSTANT, value=(0,0,0))
    #c = cv2.repeat(cleaned, 1, 5)
    c = 255 - c

    

    c = cv2.resize(c, None, fx=5, fy=5)

    
    #print(c.shape)
    """print(sub[:,:,0])
    print(sub[:,:,1])
    print(sub[:,:,2])"""

    cv2.imwrite("digits/%s.png" % ''.join(random.choice(string.ascii_lowercase) for i in range(10)), c)
    
    
    txt = pytesseract.image_to_string(Image.fromarray(c), config="--oem 3 --psm 6 outputbase digits")



    if txt in ["", "-"]:
        txt = "1"

    #print(txt)
    
    """fig, ax = plt.subplots(1,6)
    ax[0].imshow(icon)
    ax[1].imshow(cleaned)
    ax[2].imshow(c)
    ax[3].imshow(c[:,:,0])
    ax[4].imshow(c[:,:,1])
    ax[5].imshow(c[:,:,2])
    plt.show()"""

    #exit(0)

    try:
        txt = int(txt)
    except:
        txt = 1

    return txt


exchanges = []
ISLAND = 0
NUM = 1
ITEM = 2
RES = 2



for im in images:
    image = im

    nums = [getNumberFromIcon(icon) for icon in imageIcons(image)]
    islands = [i for i in islandNames(image)]
    island_numbers = [i for i in islandNumbers(image)]
    items = [i for i in itemNames(image)]

    

    for i in range(5):
        print("%-20s x%-4d: %-40s x%-4d -> %-40s x%-4d" % (islands[i], island_numbers[i], items[i], nums[i], items[i + 5], nums[i + 5]))
        exchanges.append((islands[i], island_numbers[i], items[i], nums[i], items[i + 5], nums[i + 5]))
    
    print()

    #cv2.imshow("", image)
    #cv2.waitKey()

class Path:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.col = -1

    def __repr__(self): 
        return "%s %s %s" % (self.a, self.b, self.col) 

paths = []
for i in range(len(exchanges)):
    for j in range(len(exchanges)):
        if exchanges[i][ITEM + RES] == exchanges[j][ITEM]:
            paths.append(Path(exchanges[i][ISLAND], exchanges[j][ISLAND]))


def mark(p, c):
    p.col = c
    for x in paths:
        if x.col == -1:
            if p.a == x.b or p.b == x.a:
                mark(x, c)
        

c = 0
for p in paths:
    if p.col != -1:
        continue

    mark(p, c)
    c = c + 1
    
print(paths)
        
            



print(paths)

constants.drawMap(paths)

    
# save new icons
#cv2.imwrite("icons/%s.png" % ''.join(random.choice(string.ascii_lowercase) for i in range(10)), icon)


"""loc = findArrows(image)
print(loc)

sub = image[loc[0]:loc[0]+35, :loc[1]+15]
sub[sub < 100] = 0
cv2.imshow("", 255 - sub)
cv2.waitKey()

cv2.imwrite("txt.png", 255 - sub)"""

# txt = pytesseract.image_to_string(Image.fromarray(255 - sub), config="tessconf")

#print(pytesseract.image_to_data(Image.fromarray(255 - image)))
#print(txt)


#cv2.imshow("", images[0])
#cv2.waitKey()
