class Camel_Case:
    def __init__(self, word:str):
         self.word = word
         
    def __str__(self):
        return f"{self.word}"
    
    def printData(self):
        print(f"{saya.word}")
        print(f"{saya.word}".split(" "))
        print(f"{saya.word}".title())
        
    
saya = Camel_Case("saya pengusaha sukses")
saya.printData()
 
