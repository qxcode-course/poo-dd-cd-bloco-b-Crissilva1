class Pessoa:
    def __init__(self, nome: str , idade:int):
        self.__nome = nome
        self.__idade = idade

    def get_Age (self)-> int:
        return self.__Age

    def get_name (self)-> str:
        return self.__name

    def __str__(self):
        return f"(self.__name):(self.__age)"

class Motoca:
    def __init__(self, potencia:int , tempo :int, cliente: Pessoa = None):
        self.__potencia : int = 1
        self.__tempo : int = 0                
        self.__cliente : Pessoa | None = "empty"
    
    def inserir(self, cliente : Pessoa)->bool:
        if self.__cliente != None:
           print ("fail: busy motorcycle")
           return False
        else:
            self.__cliente = cliente
            return True


    def remover (self, cliente : Pessoa)->None:
        if self.__cliente != None:
           print ("fail: busy motorcycle")
           return None
        aux: Pessoa = self.__cliente
        self.__cliente = None
        return aux

    def drive (self, time: int):
        if self.__tempo == 0:
         print("fail: buy time first")
        if self.__cliente == None:
         print ("fail: empty motorcycle") 
        if self.__age > 10:
           print ("fail: too old to drive")
        if self.__tempo <= 0:
            print ("fail: time finished after X minutes")

    def __str__(self):
        return f"(self.__potencia):(self.__tempo):(self.__pessoa)"



def main ():
    motoca = Motoca (None)
    while True :
        line : str = input ()
        print ("$" + line )
        args : list [str] = line.split (" ")
        if args[0] == "end":
            break
        if args [0] == "show":
            print (motoca)
        if args[0] == "enter":
            nome.args[1]
            idade.args(int[2])
            cliente= Pessoa (nome, idade)
            motoca.inserir(cliente)

main()            
        
