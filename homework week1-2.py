def A(n):
    sum = 0
    for i in range (1,n+1):
        for j in range (1,i+1):
            sum += j
    return sum       
print A(5)