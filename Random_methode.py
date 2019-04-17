import random


salut = ["hey", "hello", "yo", "wesh", "goodmorning"]

how_are_you = ["how are you", "how are you doing", "what's going on"]

with open ("hello_st.txt", "r") as myfile:
    data=myfile.read()


class random_sentense ():
    def __init__(self, bib):
        self.bib = bib
        self.sentense = random.choice(self.bib)
       

#####exemple###

sentense1 = random_sentense(data)

#sentense2 = random_sentense(how_are_you)

print(sentense1.sentense)

#print(sentense2.sentense)


