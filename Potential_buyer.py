from Client import Client
import sys


class Potential_buyer(Client):
    __discount_limit:float

    def __init__(self, name: str = "", adress: str = "", __items_brought: dict[str, int], __bill: float,__discount_limit:float = 100):
        super().__init__(name,adress,__items_brought,__bill)
        if __discount_limit < 100:
            print("zla")
            sys.exit(-10)
        else:
            self.__discount_limit = __discount_limit

    @property
    def discount_limit(self):
        return self.__discount_limit
    @discount_limit.setter
    def discount_limit(self,discount_limit:float):
        if discount_limit != type(int):
            print("zle")
        elif discount_limit < 100:
            print("zle")
        else:
            self.__discount_limit = discount_limit
    def is_potential_buyer(self)->bool:
        if self.items_brought.keys() > {3}:
            if (self.bill * 1.2)/100 >self.__discount_limit:
                return True
            else:
                return False
        elif self.bill > 200:
            if (self.bill * 1.2)/100 >self.__discount_limit:
                return True
            else:
                return False
        else:
            return False


