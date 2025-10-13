class Camiseta:
    def __init__(self, tamanho:str = ""):
        self.__tamanho : str = tamanho


    def set_tamanho(self, valor : str ):
        if valor == "PP" :
            self.__tamanho = valor
        elif valor == "P" :
            self.__tamanho = valor  
        elif valor == "M" :
            self.__tamanho = valor
        elif valor == "G" :
             self.__tamanho = valor
        elif valor == "GG" :
             self.__tamanho = valor
        elif valor == "XG" :
             self.__tamanho = valor

        else:
            print (f"error , {valor} não é um tamanho valido")
            print ("tamanhos validos, são: PP, P, M, G , GG ,XG")

    def get_tamanho(self)-> str:
        return self.__tamanho 

    def __str__ (self):         
        return f"{self.__tamanho}"
     

def main():
    camiseta = Camiseta()
    while camiseta.get_tamanho() == "":
        valor = (input("escolha o tamanho da sua camiseta!"))
        camiseta.set_tamanho(valor)
  
    print ("camiseta escolhida! tamanho da camisa: ", camiseta.get_tamanho() )
    
main()            
