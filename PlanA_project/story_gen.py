from Assets.data.client.client import client
from Assets.data.insurer.agent import agent




#####make story function######
def story() :
    client1 = client()
    client1.hello()
    agent1 = agent()
    agent1.hello()
    client1.hwd()
    agent1.hwdr()
    client1.tnks()
    client1.gen_qt1()
    agent1.qt1(client1.tmp, client1.rep)
    print("you'll find the story in storys directory")

story()
##########



