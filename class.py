class Sentence:
    def __init__(self, sentence): 
        self.sentence = sentence
    def givesentence(self, allcaps):
        if allcaps:
            return (self.sentence).upper()
        else:
            return (self.sentence)
    def numofwords(self):
        return len(self.sentence.split(' '))
    def numofcharacters(self):
        return len(self.sentence.replace(",", "").replace(" ", "").replace("?", "").replace(".", ""))
    def listofwords(self):
        return self.sentence.replace(",", "").replace("!", "").replace("?", "").replace(".", "").split(' ')
    def longestword(self):
       return max(self.listofwords(), key=len)
    def propersentence(self):
        return (self.sentence[0]).isupper() and (self.sentence[len(self.sentence)-1]=="." or self.sentence[len(self.sentence)-1]=="?" or self.sentence[len(self.sentence)-1]=="!")
    def createhistogram(self):
        dict = {
            'a':0,
            'b':0,
            'c':0,
            'd':0,
            'e':0,
            'f':0,
            'g':0,
            'h':0,
            'i':0,
            'j':0,
            'k':0,
            'l':0,
            'm':0,
            'n':0,
            'o':0,
            'p':0,
            'q':0,
            'r':0,
            's':0,
            't':0,
            'u':0,
            'v':0,
            'w':0,
            'x':0,
            'y':0,
            'z':0,
        }
        for letter in self.sentence.replace(",", "").replace("!", "").replace("?", "").replace(".", "").replace(" ", ""):
            if letter in dict:
                dict[letter] = dict[letter] + 1
        return dict
p1 = Sentence(input('enter a sentence'))
print('Sentance in capitals '+ p1.givesentence(allcaps=True))
print('Sentance in lower case '+ p1.givesentence(allcaps=False))
print (str(p1.numofwords()) + 'words in sentence')
print(p1.numofcharacters())
print(p1.longestword())
print(p1.listofwords())
print(p1.propersentence())
print(p1.createhistogram())
            
    
