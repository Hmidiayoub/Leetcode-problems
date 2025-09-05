def spiralMatrix(n) :
    matrix = [[0 for _ in range(n)] for _ in range(n)] 
    half = n // 2
    offset, k = 0, 1
    value = 1
    while k <= half :
        for j in range(offset,n-1-offset) :
            print(f"value at {offset,j} = {value}")
            matrix[offset][j] = value
            value += 1
        for i in range(offset,n-1-offset) :
            print(f"value at {i,n-1-offset} = {value}")
            matrix[i][n-1-offset] = value
            value += 1
        for j in range(n-1-offset, offset,-1) :
            print(f"value at {n-1-offset,j} = {value}")
            matrix[n-1-offset][j] = value
            value += 1
        for i in range(n-1-offset,offset,-1) :
            print(f"value at {i,offset} = {value}")
            matrix[i][offset] = value
            value += 1
        offset += 1
        k += 1
    if n % 2 == 1 :
        matrix[half][half] = n * n
    return matrix
print(spiralMatrix(3))