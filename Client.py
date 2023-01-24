import sys
from typing import  Dict

class Client:
    __name:str
    __adress:str
    __items_bought: dict[str,int]
    __bill:float
    def __init__(self,name:str="",adress:str="",__items_brought: dict[str,int],__bill:float):
        self.__name = name
        self.__adress = adress

        if __bill < 0:
            self.__bill = 0
        else:
            self.__bill = __bill
        if __items_brought.keys() < {0}:
            print("nieznana wartosc")
            sys.exit(-10)
        else:
            self.__items_bought = __items_brought
        if len(__items_brought) > 0 and __bill <=0:
            print("zla")
            sys.exit(-20)
    @property
    def name(self):
        return self.__name
    @property
    def adress(self):
        return self.__adress
    @property
    def items_brought(self):
        return self.__items_bought
    @property
    def bill(self):
        return self.__bill

    @name.setter
    def name(self,name:str):
        if name != type(str):
            print("zly typ")
        self.__name = name

    @adress.setter
    def adress(self, adress: str):
        if adress != type(str):
            print("zly typ")
        self.__name = adress

    @items_brought.setter
    def items_brought(self,value: dict[str,int]):
        if value.keys() < {0}:
            print("zly")
            sys.exit(-10)
        else:
            self.__items_bought = value
    @bill.setter
    def bill(self,bill:float):
        if bill < 0:
            print("zly")
        else:
            self.__bill = bill
    def discount(self):
        if self.__items_bought.keys() > {3}:
            return (self.__bill * 1.2)/100
        elif self.__bill > 200:
            return (self.__bill * 3.7)/100

    def __eq__(self, other)->bool:
        if self.__name == other.__name and self.__adress == other.__adress:
            return  True
        else:
            return False
