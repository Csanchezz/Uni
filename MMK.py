import math 

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
        self.pw = 0.0
        # self.class = [ ]
    def makeP0(self):
        n= 0
        for x in range(self.servers+1):

            if x == self.servers: 
            
                response = (self.lambd/self.mu)**x/math.factorial(x) * self.servers * self.mu / (self.servers*self.mu-self.lambd)
                n = n+response
            else: 
                response = (self.lambd/self.mu)**x/math.factorial(x)
                n = n+response
        self.p0 = 1/n
        print("p0: ", self.p0)

    def getLQ(self):
        self.lq = (((self.lambd/self.mu)**self.servers * self.lambd * self.mu) / (math.factorial(self.servers-1)*(self.servers*self.mu-self.lambd)**2)) * self.p0

        # self.lq = self.lambd**2 / (self.mu*(self.mu-self.lambd))
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
    
    # update pn validate major or minor
    def getPN(self):
        div = 0.0
        if self.n  > self.servers:
            div= math.factorial(self.servers)*self.servers**(self.n-self.servers)
        else: 
            div = math.factorial(self.n)

        ldm = self.lambd/self.mu
         
        self.pn = (ldm)**self.n /(div)
        print("pn: ", self.pn)

    def getP0(self):
        self.p0 = 1-(self.lambd/self.mu)
        print("p0: ", self.p0)

    def getPW(self):
        self.pw = ((1/math.factorial(self.servers))*(self.lambd/self.mu)**self.servers)* ((self.servers*self.mu)/ (self.servers*self.mu)-self.lambd) * self.p0
        print("pw: ", self.pw)

    def makeall(self):
        print("*****for ", self.servers, " servers*****")
        self.makeP0()
        self.getLQ()
        self.getLS()
        self.getL()
        self.getWQ()
        self.getWS()
        self.getW()
        self.getPN()
        self.getPW()
        # self.getP0()
        

newq =  Queue( 1.5, 3, 1, 3)
newq.makeall()