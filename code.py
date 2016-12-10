
import win32api, win32con
import random
from PIL import ImageGrab,ImageOps
from numpy import *
import os
import time

x_pad = 5
y_pad = 100

x1_pad = 556
y1_pad = 416

#RENAME TO PERC
class Cord:
    def perc_perc(x,y):
        x = int(x*x1_pad)
        y = int(y*y1_pad)
        return (x,y)

    f_shrimp =   perc_perc(0.07,0.71)
    f_rice =  perc_perc(0.131 ,0.71)
    f_nori =   perc_perc(0.072,0.819)
    f_roe =  perc_perc(0.135  ,0.813)
    f_salmon =   perc_perc(0.043,0.935)
    f_unagi =  perc_perc(0.128 ,0.921)

    phone = perc_perc(0.91,0.755)

    menu_toppings = perc_perc(0.838, 0.5687)

    t_shrimp = perc_perc(0.77, 0.459)
    t_unagi = perc_perc(0.8759, 0.4375)
    t_nori = perc_perc(0.89388, 0.57211)
    t_roe = perc_perc(0.89388, 0.57212)
    t_salmon = perc_perc(0.7859, 0.716346)
    t_exit = perc_perc(0.88589, 0.6899)

    mat = perc_perc(0.329, 0.7173)
    menu_rice = perc_perc(0.824, 0.615)
    buy_rice = perc_perc(0.8579, 0.584)

    delivery_norm = perc_perc(0.767, 0.611)

def screenGrab():
    


    box = (5, 100, 558, 515)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_capture__' + str(int(time.time())) + '.png')
    #return im


#Base: 556 x 416
def startGame():
    Click(perc_perc(.5,.4))
    time.sleep(.1)
    Click(perc_perc(.5,.8))
    time.sleep(.1)
    Click(perc_perc(.9,.9))
    time.sleep(.1)
    Click(perc_perc(.5,.8))
    time.sleep(.1)
    Click(perc_perc(0.9, 0.95))
    time.sleep(.1)
    Click(perc_perc(0.484, 0.7716))


def clear_tables():
    Click(perc_perc(0.149, 0.4279))
    
    Click(perc_perc(0.2968, 0.4375))
    Click(perc_perc(0.455, 0.4278))
    Click(perc_perc(0.6277, 0.6375))
    Click(perc_perc(0.781, 0.42788))
    Click(perc_perc(0.937, 0.4326))
    time.sleep(1)

def buyFood(food):
    mousePos(Cord.phone)
    mousePos(Cord.menu_toppings)
    mousePos(Cord.t_shrimp)
    mousePos(Cord.t_nori)
    mousePos(Cord.t_roe)
    mousePos(Cord.t_salmon)
    mousePos(Cord.t_unagi)
    mousePos(Cord.t_exit)
     
    mousePos(Cord.menu_rice)
    mousePos(Cord.buy_rice)
     
    mousePos(Cord.delivery_norm)

def makeFood(food):
    if ( food == 'caliroll' ):
        print ("make caliroll")
        Click(Cord.f_rice)
        sleepp()
        Click(Cord.f_nori)
        sleepp()
        Click(Cord.f_roe)
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
    elif( food == 'onigiri' ):
        print ("make onigiri")
        Click(Cord.f_rice)
        sleepp()
        Click(Cord.f_rice)
        sleepp()
        Click(Cord.f_nori)
        sleepp()
        time.sleep(.1)
        foldMat()

    ##SLEEP NOT NEEDED?##
        sleepp()
        
        time.sleep(1.5)
    elif( food == 'gunkan'):
        Click(Cord.f_rice)
        sleepp()
        Click(Cord.f_nori)
        sleepp()
        Click(Cord.f_roe)
        sleepp()
        Click(Cord.f_roe)
        sleepp()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
        

def foldMat():
    Click(Cord.mat)


#Mouse Clicking functions
#Once
#Holds
def sleepp():
    time.sleep(.05 + 0.05*random.random())
def Click(cord):
    mousePos(cord)
    leftClick()
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print( "Clicord_percent()ck.")

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print ('left Down')
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print ('left release')

#MOVEMENT
def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))
     
##




def cord_perc():
    x,y = win32api.GetCursorPos()
    x = (x-x_pad)/x1_pad
    y = (y-y_pad)/y1_pad
    print(x,y)
          
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print (x,y)
def perc_getter():
    for i in range(6):
        time.sleep(1.2)
        print (cord_perc())
def cord_getter():
    for i in range(6):
        time.sleep(1.2)
        print (get_cords())

def perc_perc(x,y):
    x = int(x*x1_pad)
    y = int(y*y1_pad)
    return (x,y)
    
##############_______________________________##############


def main():
    pass



if __name__ == '__main__':
    main()

