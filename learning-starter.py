#Course name: CMPUT 366
#Programming Assignment 3
#Author:    Yuwei Duan, Chongyang Ye
#Author Id:    1309121     1264608 
import mountaincar
from Tilecoder import numTilings, tilecode, numTiles
from Tilecoder import numTiles as n
from pylab import *

numRuns = 1
numEpisodes = 1000
alpha = 0.5/numTilings
gamma = 1
lmbda = 0.9
Epi = Emu = epsilon = 0
n = numTiles * 3
F = [-1]*numTilings
stepSum = zeros(numEpisodes)
returnsSum =zeros(numEpisodes)

def Policy(F,a,theta):
    Q=zeros(a)
    for a in range(a):
        for i in F:
            Q[a]+= theta[i+a*324]
    return Q

runSum = 0.0
for run in xrange(numRuns):
    theta = -0.01*rand(n)
    returnSum = 0.0
    for episodeNum in xrange(numEpisodes):
        G = 0
        #your code goes here (20-30 lines, depending on modularity)
        step=0.0
        s = mountaincar.init()
        trace=zeros(n)
        Q=zeros(3)
        while s is not None:
            step += 1
            tilecode(s[0],s[1],F)
            Q = Policy(F,3,theta)
            if rand() <= epsilon:
                action = randint(0,2)
            else:
                action = argmax(Q)
            r, sp = mountaincar.sample(s,action)
            delta=r-Q[action]
            G+=r
            for i in F: trace[i+action*numTiles] = 1
            if sp == None:
                theta += alpha*delta*trace
                break
            tilecode(sp[0],sp[1],F)
            delta += max(Policy(F,3,theta))
            theta += alpha * delta * trace
            trace=lmbda * trace *gamma
            s = sp
        
        
        print "Episode: ", episodeNum, "Steps:", step, "Return: ", G
        returnSum = returnSum + G
        stepSum[episodeNum]+=step/numRuns
        returnsSum[episodeNum]+= G/numRuns
    print "Average return:", returnSum/numEpisodes
    runSum += returnSum
print "Overall performance: Average sum of return per run:", runSum/numRuns        

def writeAve():
    fout = open('avgret.dat', 'w')
    for i in xrange(numEpisodes):
        fout.write(repr(i) + ' ' + repr(returnsSum[i]) + ' ' + repr(stepSum[i]))
        fout.write('\n')
    fout.close()

def writeF():
    fout = open('value', 'w')
    F = [0]*numTilings
    steps = 50
    for i in range(steps):
        for j in range(steps):
            tilecode(-1.2+i*1.7/steps, -0.07+j*0.14/steps, F)
            height = -max(Policy(F,3,theta))
            fout.write(repr(height) + ' ')
        fout.write('\n')
    fout.close()

writeF()
writeAve()