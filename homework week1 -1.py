def A(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return A(n-1) + A(n-2) 
print A(10)