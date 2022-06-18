
class Queue:
    def __init__(self, lambd, mu, n, servers):
        self.lambd = lambd
        self.mu = mu
        self.n = n
        self.servers = servers
        self.lq = 0.0
        self.ls = 0.0
        self.l = 0.0
        self.wq = 0.0
        self.ws = 0.0
        self.w = 0.0
        self.pn = 0.0
        self.p0 = 0.0
        # self.class = [ ]


    def getLQ(self):
       self.lq = self.lambd**2 / (self.mu*(self.mu-self.lambd))
       print("lq: ", self.lq)
    
    def getLS(self):
        self.ls = self.lambd/self.mu
        print("ls: ", self.ls)

    def getL(self):
        self.l  = self.lq + self.ls
        print("l: ", self.l)
        
    def getWQ(self):
        self.wq = self.lq/self.lambd
        print("wq: ", self.wq)

    def getWS(self):
        self.ws = 1/self.mu
        print("ws: ", self.ws)

    def getW(self):
        self.w  = self.ws + self.wq
        print("w: ", self.w)

    def getPN(self):
        ldm = self.lambd/self.mu
        self.pn = (ldm)**self.n /(1/(ldm))
        print("pn: ", self.pn)

    def getP0(self):
        self.p0 = 1-(self.lambd/self.mu)
        print("p0: ", self.p0)

    def makeall(self):
        self.getLQ()
        self.getLS()
        self.getL()
        self.getWQ()
        self.getWS()
        self.getW()
        self.getPN()
        self.getP0()
        

newq =  Queue( 1.5, 3, 1, 1)
newq.makeall()