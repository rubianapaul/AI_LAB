import random
def main():
    room=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
    proom=perceive()
    count=0
    for i in range(4):
        if(i%2==0):
            for j in range(4):
                display(proom,i,j)
                if(proom[i][j]==1):
                    print("Cleaning the tile: ",(i,j))
                    count=count+1
                    proom[i][j]=0
        else:
            for j in range(4):
                k=3-j
                display(proom,i,k)
                if(proom[i][k]==1):
                    print("Cleaning the tile: ",(i,k))
                    count=count+1
                    proom[i][k]=0
    print("ROOM CLEANED!")
    print("Efficiency = ",(float)(count/16)*100)

def perceive():
    room=[]
    for i in range(4):
        temp=[]
        for j in range(4):
            p=random.randint(0,1)
            temp.append(p)
        room.append(temp)
    return room
def display(room,m,n):
    print("______________________")
    for i in range(4):
        for j in range(4):
            if(i==m and j==n):
                print("[",room[i][j],"]",end='')
            else:
                print(" ",room[i][j]," ",end='')
        print("")
    
                
main()
