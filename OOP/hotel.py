#定义一个类来计算旅馆租房费用。
#__init__()构造器对一些实例属性进行初始化。
#calcTotal()方法决定每日总的租房费用还是计算全部的租房费。

class HotelRoomCalc(object):
    'hotel room rate  calculator'

    def __init__(self,rt,sales=0.085,rm=0.1):
        """Hotel room calc default arguments:
          sales tax == 8.5% and room tax ==10%"""
        self.salesTax=sales
        self.roomTax=rm
        self.roomRate=rt

    def calcTotal(self,days=1):
        'Calculate total;default to daily rate'
        daily = round((self.roomRate * (1 + self.roomTax + self.salesTax)),2)
        return float(days) * daily

sfo=HotelRoomCalc(299)  #实例化
sfo.calcTotal()          #日租金
sfo.calcTotal(2)         #2天的租金
