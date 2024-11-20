class flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+"("+self.meaning+")"
flash = []
print("Welcome")
while(True):
    word = input("enter the name")
    meaning = input("Enter a meaning")
    flash.append(flashcard(word,meaning))
    option = int(input("Enter 0 for adding more or else 1"))
    if (option):
               break
    print("Your Flahcard")
    for i in flash:
         print(">",i)
