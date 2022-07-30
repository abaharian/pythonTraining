class info:
    def __init__(self, char):
        self.wins = 0
        self.loses = 0
        self.draws = 0
        self.goalout = 0
        self.goalin = 0
        self.name = char
    def addgoalout(self, n):
        self.goalout += n
    def addgoalsin(self, n):
        self.goalin += n
    def addwins(self):
        self.wins += 1
    def addloses(self):
        self.loses += 1
    def adddraws(self):
        self.draws += 1

    def isLessThan(self, other):
        if(self.score() < other.score()):
            return True
        elif(self.score() > other.score()):
            return False
        if(self.wins < other.wins):
            return True
        elif(self.wins > other.wins):
            return False
        elif(self.name[0] > other.name[0]):
            return True
        return False

    def score(self):
        return (self.wins * 3 + self.draws)

    def print(self):
        print(self.name, " wins:", self.wins, " , loses:", self.loses, " , draws:", self.draws, ' , goal difference:', self.goalout-self.goalin, " , points:", self.score())

def resultReader(result, first, second):
    listr = result.split('-')
    g1 = int(listr[0])
    g2 = int(listr[1])
    first.addgoalout(g1)
    first.addgoalsin(g2)
    second.addgoalout(g2)
    second.addgoalsin(g1)

    if(g1>g2):
        first.addwins()
        second.addloses()
    elif(g2>g1):
        first.addloses()
        second.addwins()
    else:
        first.adddraws()
        second.adddraws()

def sortList(tl):
    for i in range(0,4):
        for j in range(i+1,4):
            if(tl[i].isLessThan(tl[j])):
                swap(tl,i,j)

def swap(teamlist, i, j):
    temp = teamlist[i]
    teamlist[i] = teamlist[j]
    teamlist[j] = temp


iran = info('Iran')
portugal = info('Portugal')
spain = info('Spain')
moroco = info('Morocco')

inp = input()
resultReader(inp, iran, spain)
inp = input()
resultReader(inp, iran, portugal)
inp = input()
resultReader(inp, iran, moroco)
inp = input()
resultReader(inp, spain, portugal)
inp = input()
resultReader(inp, spain, moroco)
inp = input()
resultReader(inp, portugal, moroco)

teamlist =[iran, portugal, spain, moroco]

sortList(teamlist)

for i in range(4):
    teamlist[i].print()
