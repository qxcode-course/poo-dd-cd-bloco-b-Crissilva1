class Grafite:
    VALID_THICKNESS=[0.3, 0.5, 0.7]
    VALID_HARDNESS=["HB", "2B", "4B", "6B"]

    def __init__(self, size:int, thickness:float, hardness:str):
        self.__size:int=size
        self.__tickness:float=thickness
        self.__hardness:str= hardness
    
    def get_size(self)->int:
        return self.__size

    def get_thickness(self)->float:
        return self.__thickness

    def get_hardness(self)->str:
        return self.__hardness

    def set_size(self,size:int):
        self.__size=size

    def __str__(self)->str:
        return f"{self.__size}:{self.__thickness}:{self.__hardness}"
    
class Lapiseira:
    def __init__(self, thickness:float):
        self.__ponta:Grafite | None = None
        self.__thickness:float = tickness

    def get_ponta(self)->Grafite:
        return self.__ponta
    
    def hasGrafite(self)->bool:
        if self.__ponta is None:
            return False
        else:
            return True

    def insert(self,grafite:Grafite):
        if self.__ponta != None:
            print ("fail: ja existe grafite")
            return
        self.__ponta = grafite

    def __str__(self)->str:
        return f"{self.__thickness}"

    def remove(self)->Grafite|None:
        if self.__ponta is None:
            return None
        aux=self.__ponta
        self.__ponta=None
        return aux

    def writePage(self):
        

   


