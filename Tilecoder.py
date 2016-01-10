#Course name: CMPUT 366
#Programming Assignment 3
#Author:    Yuwei Duan, Chongyang Ye
#Author Id:    1309121     1264608 
numTilings = 4
numTiles=81*numTilings
    
def tilecode(x,y,tileIndices):
    # write your tilecoder here (5 lines or so)
    x+=1.2
    y+=0.07
    for i in range(numTilings):
        pos = int((x+i*0.2125/numTilings)/0.2125)
        vel = int((y+i*0.0175/numTilings)/0.0175)
        # get the tile number and populate the tileIndices vector
        tileIndices[i]=int(i*81+9*vel+pos)
        
    
def printTileCoderIndices(x,y):
    tileIndices = [-1]*numTilings
    tilecode(x,y,tileIndices)
    print 'Tile indices for input (',x,',',y,') are : ', tileIndices

#printTileCoderIndices(0.1,0.1)
#printTileCoderIndices(4.0,2.0)
#printTileCoderIndices(5.99,5.99)
#printTileCoderIndices(4.0,2.1)
    
