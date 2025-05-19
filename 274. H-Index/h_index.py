def h_index(citations):
    n = len(citations)
    temp = [0 for i in range(n+1)]
    
    for i in range(n):
        if citations[i] >= n:
            temp[n] +=1
        else:
            temp[citations[i]] +=1


    counter = 0
    for i in range(n,-1,-1):
        counter += temp[i]
        if counter >= i:
            return i
        



citations = [0, 0]
print(h_index(citations))