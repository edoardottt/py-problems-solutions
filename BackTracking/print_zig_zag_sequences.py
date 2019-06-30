#BACKTRACKING PRINT SEQUENCES WITH Xi<Xi+1>Xi+2 or Xi>Xi+1<Xi+2 FOR i<n-2
print("BACKTRACKING PRINT SEQUENCES WITH Xi<Xi+1>Xi+2 or Xi>Xi+1<Xi+2 FOR i<n-2")
T = [0,0,0]
def zigzag(n,i):
    if(i==n): # finished string, print it
        print(T)
    else:
        if(i==0): # if first value I can put into {0,1,2}
            for j in range(3):
                T[i] = j
                zigzag(n,i+1)
        elif(i==1): # in the second I can put {0,1,2} - precedent element(0)
            for j in range(3):
                if (T[i-1]!= j):
                    T[i] = j
                    zigzag(n,i+1)
        else:
            pre = T[i-2] 
            if (pre<T[i-1]): # if it is less than the precedent
                for j in range(n):
                    if(j<T[i-1]): # putting lower value than precedent
                        T[i] = j
                        zigzag(n,i+1)
            else: # se è maggiore del precedente
                for j in range(n):
                    if(j>T[i-1]): # putting higher value than precedent
                        T[i] = j
                        zigzag(n,i+1)
zigzag(3,0)