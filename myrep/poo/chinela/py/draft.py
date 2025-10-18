class Chinela:
    def __init__(elf, tamanho:int = 0):
        self.__tamanho :int = tamanho


    def set_tamanho (self, valor:int)->bool:
        if valor % 2 != 0 and  valor < 20 or valor >50 :
            print ("tamanho errado")
            return False
        self.__tamanho = valor
        return True

    def get_tamanho(self)-> int :
        return self.__tamanho 

    def __str__ (self):         
            return f"{self.__tamanho}"



def main():
    chinela= Chinela()
    while chinela.get_tamanho() == 0:
        valor = int(input("digite o tamanho da sua chinela!"))
        if chinela.set_tamanho(valor) == True:
            break 
  
    print ("compra com sucesso! tamanho da chinela: ", chinela.get_tamanho() )
    
main()            
