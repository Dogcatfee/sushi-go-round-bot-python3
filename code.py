
import win32api, win32con
import random
from PIL import ImageGrab,ImageOps
from numpy import *
import os
import time

from msvcrt import getch

#USE raw_cords() to get top left and bottom right of window
x_pad = 9
y_pad = 103

x1_pad = 1199 - x_pad
y1_pad = 1000 - y_pad

#RENAME TO PERC
class Cord:
    def perc_perc(x,y):
        x = int(x*x1_pad)
        y = int(y*y1_pad)
        return (x,y)
    
    phone = perc_perc(0.91,0.755)

    menu_toppings = perc_perc(0.86916, 0.56889)


    #mat = perc_perc(0.329, 0.7173)
    mat = perc_perc(0.3025, 0.8366666666666667)
    menu_rice = perc_perc(0.824, 0.615)
    buy_rice = perc_perc(0.8579, 0.6000)

    delivery_norm = perc_perc(0.767, 0.611)
    delivery_norm_rice = perc_perc(0.805,0.607)


def perc_perc(x,y):
    x = int(x*x1_pad)
    y = int(y*y1_pad)
    return (x,y)
def re_perc(x,y):
    x = float(x/x1_pad)
    y = float(y/y1_pad)
    return (x,y)

tABS = {
    'shrimp' : perc_perc(0.721667, 0.42666),
    'unagi'  : perc_perc(0.861667, 0.425556),
    'nori'   : perc_perc(0.7225, 0.546667),
    'roe'    : perc_perc(0.86667, 0.57333),
    'salmon' : perc_perc(0.7275, 0.68),
    'menu_rice': perc_perc(0.824, 0.615),
    't_exit'   : perc_perc(0.9375, 0.72)
    }

lABS ={
    'shrimp': perc_perc(0.07,0.71),
    'rice'  : perc_perc(0.131 ,0.71),
    'nori'  : perc_perc(0.072,0.819),
    'roe'   : perc_perc(0.135  ,0.813),
    'salmon': perc_perc(0.043,0.935),
    'unagi' : perc_perc(0.128 ,0.921)
    }

foodOnHand = {'shrimp': 5,
                  'rice': 10,
                  'nori': 10,
                  'roe': 10,
                  'salmon': 5,
                  'unagi': 5}
basefood = foodOnHand

start_menues = ((perc_perc(.5,.4)), (perc_perc(.5,.8)),
                (perc_perc(.9,.93)), (perc_perc(.5,.8)))
tables = ((perc_perc(0.149, 0.4279)),(perc_perc(0.2808333, 0.4278)),
          (perc_perc(0.4408, 0.4275)),(perc_perc(0.61, 0.42788)),
          (perc_perc(0.781, 0.42788)), (perc_perc(0.937, 0.4326)))


blanks = {'seat one': 7621,
          'seat two': 9488,
          'seat three': 11085,
          'seat four': 6698,
          'seat five': 11188,
          'seat six' : 9003 }

        
seats = {"seat one": (perc_perc(0.5133333333333333, 0.13111111111111112),
                      (perc_perc(0.6125, 0.15333333333333332))),
         
         "seat two": ((perc_perc(0.6708333333333333, 0.13111111111111112)),
                    (perc_perc(0.77, 0.15333333333333332))),
         
         "seat three": ((perc_perc(0.8291666666666667, 0.13111111111111112)),
                    (perc_perc(0.9283333333333333, 0.15333333333333332))),
         
         "seat four": ((perc_perc(0.03833333333333333, 0.13111111111111112)),
                    (perc_perc(0.1375, 0.15333333333333332))),
         
         "seat five": ((perc_perc(0.19916666666666666, 0.13111111111111112)),
                    (perc_perc(0.295, 0.15333333333333332))),
         
         "seat six":  ((perc_perc(0.355, 0.13111111111111112)),
                    (perc_perc(0.45416666666666666, 0.15333333333333332)))}

bseats = {"seat one": ((46,118),
                     (165,138)),
         "seat two": ((239, 118),
                        (354, 138)),
         "seat three": ((426,118),
                        (545,138)),
         "seat four": ((805,118),
                        (924,138)),
         "seat five": ((616,118),
                       (735,138)),
         "seat six":  ((995,118),
                       (1114, 138))}

sushiSeats = {'seat one': ((3593, 'onigiri'), (3647, 'gunkan'), (3977, 'caliroll'), (3695, 'salmonroll'), (4142, 'shrimpsushi')),
              'seat two': ((3263, 'onigiri'), (3317, 'gunkan'), (3647, 'caliroll'), (3365, 'salmonroll'), (3812, 'shrimpsushi')),
              'seat three': ((3529, 'onigiri'), (3520, 'gunkan'), (3850, 'caliroll'), (3441, 'salmonroll'), (4015, 'shrimpsushi')),
              'seat four': ((3593, 'onigiri'), (3647, 'gunkan'), (3977, 'caliroll'), (3695, 'salmonroll'), (4142, 'shrimpsushi')),
              'seat five': ((3593, 'onigiri'), (3647, 'gunkan'), (3977, 'caliroll'), (3695, 'salmonroll'), (4142, 'shrimpsushi')), 
              'seat six': ((3657, 'onigiri'), (3393, 'gunkan'), (3723, 'caliroll'), (3568, 'salmonroll'), (3888, 'shrimpsushi')),
              
}

def screenGrab():
    
    box = (x_pad,y_pad,x1_pad+x_pad, y_pad+y1_pad)
    im = ImageGrab.grab(box)
    #im.show()
    #im.save(os.getcwd() + '\\full_capture__' + str(int(time.time())) + '.png')
    return im


def startGame():
    for i in start_menues:
        Click(i)
        time.sleep(.1)    


def clear_tables():

    for i in tables:
        Click(i)
        sleepp()
        print(i)

def checkFood():
    for i, j in foodOnHand.items():   
        if( i == 'nori' or i == 'rice' or i == 'roe' ):
            if( j <= 4 ):
                print ( '%s is low and replenish' % i)
                buyFood(i)
        elif( i == 'salmon' or i == 'shrimp'):
            if( j<= 3 ):
                print ( '%s is low and refill' % i)
                buyFood(i)

def buyFood(name):
    print("buy" + str(name))

    Click(Cord.phone)
    SloClick(Cord.phone)

    if ( name == 'rice' ):
        
        SloClick(tABS['menu_rice'])
        s = screenGrab()
        if (s.getpixel(Cord.buy_rice) !=  (127, 127, 127)):
            print ('rice avail')
            SloClick(Cord.buy_rice)
            foodOnHand['rice'] += 10
            #time.sleep(.5)
            SloClick(Cord.delivery_norm_rice)
            #time.sleep(2.5)
        else:
            print( 'no ' + name)
            SloClick(tABS['t_exit'])
            time.sleep(2)
            buyFood(name)
            
    elif ( name == 'salmon' or name == 'shrimp'):
        SloClick(Cord.menu_toppings)
        s = screenGrab()
        if ( s.getpixel(tABS[name]) != (109, 123, 127)):
            print (name + 'avail')
            SloClick(tABS[name])
            foodOnHand[name] += 5
            SloClick(Cord.delivery_norm)
        else:
            print( 'no ' + name)
            SloClick( tABS['t_exit'])
            time.sleep(2)
            buyFood(name)
    else:
        SloClick(Cord.menu_toppings)
        s = screenGrab()
        if ( s.getpixel(tABS[name]) != (109, 123, 127)):
            print (name + 'avail')
            SloClick(tABS[name])
            foodOnHand[name] += 10
            SloClick(Cord.delivery_norm)
        else:
            print( 'no ' + name)
            SloClick( tABS['t_exit'])
            time.sleep(2)
            buyFood(name)


 






def ingreed(name):
    print("make" + str(name))

    for i in name:
        
    
        foodOnHand[i] -= 1
        Click(lABS[i])
        sleepp()
        
    foldMat()


caliroll = ('rice', 'nori','roe')
onigiri = ('rice', 'rice' , 'nori')
gunkan = ('rice', 'nori', 'roe', 'roe')
salmonroll = ('rice', 'nori' , 'salmon' , 'salmon')
shrimpsushi = ('rice', 'nori', 'shrimp' , 'shrimp')    

    
def makeFood(food):
    if ( food == 'onigiri' ):

         ingreed(onigiri)
         
         
    if (  food == 'caliroll' ):

        ingreed(caliroll)

    elif ( food == 'gunkan' ):

        ingreed(gunkan)
            
    elif ( food == 'salmonroll'):

        ingreed(salmonroll)
    elif ( food == 'shrimpsushi'):

        ingreed('shrimpsushi');
        






def get_seat(seat):
        p1,p2 = seat
        x,y = p1
        x1, y1 = p2
        
        box = (x+x_pad, y+y_pad, x1+x_pad, y1+y_pad )
        im = ImageOps.grayscale(ImageGrab.grab(box))
        #im = ImageGrab.grab(box)
        a = array(im.getcolors())
        a = a.sum()
    
        #im.save(os.getcwd() + '\\'  + str(int(a)) + "-" + str(int(5*random.random())) + '.png')
        return (a)

def has_key(map, seat):
    for i in seat:
        if(map == i[0]):
            
            return True
        else:
            print( i[0])
    return False

def res():
    foodOnHand = basefood

#Retrieve index
def foody(foods, s):
    for i in range(len(foods)):
        if((foods[i][0] - 60 )<= s <= (foods[i][0] + foods[i][0] - 60)):
            return(i)

#makeFood based on input name
def comparator(name):
    s = get_seat(seats[name])
    #Check Map to see if matches Blank
    
    if(s != blanks[name]):
        print('test')
        #Check Map against known values to make food
        if(has_key(s, sushiSeats[name])):
            #print('y')
            num = foody(sushiSeats[name], s)
            makeFood(sushiSeats[name][num][1])
    
    

def check_bubs():
    checkFood()
    #Get Map of location
    #s1 = get_seat(seats['seat one'])
    #Compare Map to Blank spot
    #if (s1 != Blank.seat_1):
    #Compare Map to Known spots
    comparator ('seat one')
            
    clear_tables()

    comparator('seat two')

     
        
    checkFood()

    comparator('seat three')

     
    
    clear_tables()

    comparator('seat four')

     
    checkFood()
    comparator('seat five')

     

    comparator('seat six')

    clear_tables()

     
            
        
        

def foldMat():
    Click(Cord.mat)
    time.sleep(.5)
    clear_tables()
    time.sleep(.5)
    checkFood()
    time.sleep(2)


#Mouse Clicking functions
#Once
#Holds
def sleepp():
    time.sleep(.01 + 0.01*random.random())
def Click(cord):
    mousePos(cord)
    #time.sleep(.6)
    leftClick()
def SloClick(cord):
    x,y = cord
    mousePos((int(x/3), int(y/3)))
    time.sleep(.2)
    mousePos((int(x/2), int(y/2)))
    mousePos(cord)
    time.sleep(.2)
    #leftClick()

    time.sleep(.1)

    leftClick()
    time.sleep(.1)
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
def raw_cords():
    x,y = win32api.GetCursorPos()
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

def sleight():
    for i in range(15):
        rando = int(3 * random.random())
        seat_getter(seats)
        #checkFood()
        if( rando == 3):
            makeFood('onigiri')
            makeFood('caliroll')
        elif( rando == 2):
            makeFood('caliroll')
            makeFood('gunkan')
        elif( rando <= 1):
            makeFood('gunkan')
            makeFood('onigiri')
        if(i%2):
            seat_getter(seats)
            clear_tables()
        checkFood()
        time.sleep(2)
        
        

def speed():
    startGame()
    sleight()
    

def kick():
    startGame()
    while(True):
        check_bubs()
        seat_getter(seats)
        time.sleep(3)
        #s = screenGrab()
        
        #if(s.getpixel(Cord.mat) != (155, 145, 53)):
        #    Click(Cord.mat)



def seat_getter(data):
for i in data:
 
        x,y = data[i][0]
        x1, y1 = data[i][1]
        
        box = (x+x_pad, y+y_pad, x1+x_pad, y1+y_pad )
        im = ImageOps.grayscale(ImageGrab.grab(box))
        im = ImageGrab.grab(box)
        a = array(im.getcolors())
        a = a.sum()
    
        im.save(os.getcwd() + '\\' + i + str(int(a)) + "-" + str(int(5*random.random())) + '.png')
        print (i)


#SIX: 115
#FIVE: 115
#FOUR: 115
#THREE: 115
#TWO: 115
#ONE: 115






def main():
    pass



if __name__ == '__main__':
    main()

