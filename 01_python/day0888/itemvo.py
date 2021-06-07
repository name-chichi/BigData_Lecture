# itemvo.py  Model 역할을 하는 Class
class ItemVO:
    def __init__(self,id,name,price,regdate):
        self.__id = id;
        self.__name = name;
        self.__price = price;
        self.__regdate = regdate;
    def __str__(self):
        return '%d, %s, %f, %s' % (self.__id,self.__name,self.__price,self.__regdate);
    def getId(self):
        return self.__id;

    def getName(self):
        return self.__name;
    def setName(self, name):
        self.__name = name;
    def getPrice(self):
        return self.__price;
    def setPrice(self, price):
        self.__price = price;
    def getRegdate(self):
        return self.__regdate;
    def setRegdate(self, regdate):
        self.__regdate = regdate;








