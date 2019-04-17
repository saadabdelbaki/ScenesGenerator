import random
class agent :
    def __init__(self):
        self.greeting = None
        
    def hello (self):
        f = open("Assets/data/insurer/hello/hello_st.txt","r+")
        lines = f.readlines()
        f.close()
        words = []
        for line in lines:
            line = line.rstrip("\n")
            words.append(line)
        w = random.choice(words)
        list_of_greetings = ["morning ", "good morning ", "good afternoon ", "good evening ", "evening"]
        for i in list_of_greetings : 
            if i == w:
                self.greeting = "Hey"
            else : 
                self.greeting = w
        with open("storys/story.txt","a") as f:
            f.write("agent :" + self.greeting + "\n")
    def hwdr (self):
        f = open("Assets/data/insurer/hello/hwdr.txt")
        lines = f.readlines()
        f.close()
        words =[]
        for line in lines:
            line = line.rstrip("\n")
            words.append(line)
        w = random.choice(words)
        self.hwdr = w
        with open("storys/story.txt","a") as f:
            f.write("agent :" + self.hwdr + "\n")
    
    def qt1(self, tmp, rep):
        self.tmp = tmp
        self.rep = rep
        if tmp == 0: #asking about insurance
            f = open("Assets/data/insurer/question/asking_about_insurance/qt1.txt","r+")
            lines = f.readlines()
            f.close()
            words = []
            for line in lines :
                line = line.rstrip("\n")
                words.append(line)
            self.qt1 = random.choice(words)

        
        elif tmp == 1: #asking for insurance
            if rep == 1: # car
                f = open("Assets/data/insurer/question/asking_for_insurance/car/qt1.txt","r+")
                lines = f.readlines()
                f.close()
                words = []
                for line in lines :
                    line = line.rstrip("\n")
                    words.append(line)
                self.qt1 = random.choice(words)
            elif rep == 2: #motorcycle
                f = open("Assets/data/insurer/question/asking_for_insurance/motorcycle/qt1.txt","r+")
                lines = f.readlines()
                f.close()
                words = []
                for line in lines :
                    line = line.rstrip("\n")
                    words.append(line)
                self.qt1 = random.choice(words)
            elif rep == 3:#camion
                f = open("Assets/data/insurer/question/asking_for_insurance/camion/qt1.txt","r+")
                lines = f.readlines()
                f.close()
                words = []
                for line in lines :
                    line = line.rstrip("\n")
                    words.append(line)
                self.qt1 = random.choice(words)
            elif rep == 4: #cycle
                f = open("Assets/data/insurer/question/asking_for_insurance/cycle/qt1.txt","r+")
                lines = f.readlines()
                f.close()
                words = []
                for line in lines :
                    line = line.rstrip("\n")
                    words.append(line)
                self.qt1 = random.choice(words)
            else:#truck
                f = open("Assets/data/insurer/question/asking_for_insurance/truck/qt1.txt","r+")
                lines = f.readlines()
                f.close()
                words = []
                for line in lines :
                    line = line.rstrip("\n")
                    words.append(line)
                self.qt1 = random.choice(words)
            
        elif tmp == 2 : #declare a statement
            f = open("Assets/data/insurer/question/declare_a_statement/qt1.txt","r+")
            lines = f.readlines()
            f.close()
            words = []
            for line in lines :
                line = line.rstrip("\n")
                words.append(line)
            self.qt1 = random.choice(words)
        with open("storys/story.txt","a") as f:
            f.write("agent :" + self.qt1 + "\n")
