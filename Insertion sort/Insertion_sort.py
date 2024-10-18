import random
def randomlist():
    nums = []
    for i in range(0,100000):
        n = random.randint(1,99)
        nums.append(n)
    return (nums)


def insertionsort():
    nlist = randomlist()
    
    for i in range(1, len(nlist)):
        
        currentval = nlist[i]
        
        
        position = i
        
        while position > 0 and nlist[position - 1] > currentval:
            
            nlist[position] = nlist [position - 1]
            position -= 1
            
            nlist[position] = currentval
            
    return nlist
print(insertionsort())


