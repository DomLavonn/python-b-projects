class MadLibs:
    libs = {"noun": "Be careful not to vacuum the NOUN when you clean under your bed.",  "adjective": "Flip-flops are a staple of any summer wardrobe"}
    def __init__(self,grammer):
        self.grammer = grammer
        self.sentence = " "
        
    def showLib(self, word):
        if self.grammer == "noun":
            self.createLib(word, self.grammer)
            print(self.sentence)
        elif self.grammer == "adjective":
            self.createLib(word, self.grammer)
            print(self.sentence)
       
    def createLib(self, grammer_word, gram):
        if gram == "noun":
            self.sentence = self.libs.get("noun") + " " + grammer_word
        else:
            self.sentence = self.libs.get("adjective") + " " + grammer_word

        
        
def main():
    print("Hello! Welcome to MadLibs!!\nPlease pick your option? Noun or Adjective?\n")
    
    gram = input()
    
    gameWord = MadLibs(gram)
    
    word = input("Now pick you word (noun)!\n")
    
    gameWord.showLib(word)
    
    
    
    
    
    
    
    
    



if __name__ == "__main__":
    main()