import random

class client :
    def __init__(self):
        self.greeting = None
        
    def hello (self):
        f = open("Assets/data/client/hello/hello_st.txt")
        lines = f.readlines()
        f.close()
        words =[]
        for line in lines:
            line = line.rstrip("\n")
            words.append(line)
        w = random.choice(words)
        self.greeting = w
        with open("storys/story.txt","a") as f:
            f.write("client :" + self.greeting + "\n")
    def hwd (self):
        f = open("Assets/data/client/hello/hw.txt")
        lines = f.readlines()
        f.close()
        words =[]
        for line in lines:
            line = line.rstrip("\n")
            words.append(line)
        w = random.choice(words)
        self.hw = w
        with open("storys/story.txt","a") as f:
            f.write("client :" + self.hw + "\n")
    def tnks (self):
        f = open("Assets/data/client/hello/tnks.txt")
        lines = f.readlines()
        f.close()
        words =[]
        for line in lines:
            line = line.rstrip("\n")
            words.append(line)
        w = random.choice(words)
        self.tnks = w
        with open("storys/story.txt","a") as f:
            f.write("client :" + self.tnks + "\n")
            
    def gen_qt1 (self):
        f1 = open("Assets/data/client/question/asking_for_insurance/qt1.txt","r+")
        f2 = open("Assets/data/client/question/asking_about_insurance/qt1.txt","r+")
        f3 = open("Assets/data/client/question/declare_a_statement/qt1.txt","r+")
        
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        lines3 = f3.readlines()
        f1.close()
        f2.close()
        f3.close()
        words1 = []
        words2 = []
        words3 = []
        w = []
        for line1 in lines1 :
            line1 = line1.rstrip("\n")
            words1.append(line1)
        w.append(random.choice(words1))
        i = w[0]
        for line2 in lines2 :
            line2 = line2.rstrip("\n")
            words2.append(line2)
        w.append(random.choice(words2))
        j = w[1]
        for line3 in lines3 :
            line3 = line3.rstrip("\n")
            words3.append(line3)
        w.append(random.choice(words3))
        k = w[2]
        x = random.choice(w)
        self.qt1 = x
        #[rep=0"init", 1=car, 2=motorcycle, 3=camion, 4=cycle, 5=truck]
        #[tmp: 0=asking about, 1=asking for, 2=declare a statement]
        self.rep = 0
        if j in x :
            self.tmp = 0
        elif i in x:
            self.tmp = 1
            if "car" in x :
                self.rep = 1
            elif "motorcycle" in x:
                self.rep = 2
            elif "camion" in x :
                self.rep = 3
            elif "cycle" in x :
                self.rep = 4
            elif "truck" in x :
                self.rep = 5
        else :
            self.tmp = 2
        with open("storys/story.txt","a")  as f:
            f.write("client :" + self.qt1 +"\n")
        
