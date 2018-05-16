"""#import urllib.request
import urllib

import time

price=99
while price > 4.74:
    time.sleep(900)
    page=urllib.request.urlopen("http://www.beans-r-us.biz/prices.html")
    text=page.read().decode("utf8")
    where=text.find('>$')
    start_of_price=where + 2
    end_of_price=start_of_price + 4
    price=float(text[ start_of_price:end_of_price ])
    
print("Buy!")

"""


"""
用函数来重用代码
"""
def make_smoothie():
    juice = raw_input("what juice would you like? ")
    fruit = raw_input("OK - and how about the fruit? ")
    print("Thank,Let's go!")
    print("Crushing the ice...")
    print("Blending the " + fruit)
    print("Now adding in the " + juice + "juice.")
    #print("Finished! There's your " + fruit + "and"  + juice + "smoothie!" )会报错，得按以下格式
    
    print("Finished! There's your " , fruit,"and"  , juice , "smoothie!" )
    
    
#点餐
print("Welcome to smoothie-matic 2.0")
another="Y"
while another == "Y":
    make_smoothie()
    another = raw_input('How about another(Y/N)?')
    
    