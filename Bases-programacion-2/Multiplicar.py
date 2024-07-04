def multiplicacion_matrices(m1, m2):
    # Get the dimensions of the matrices
    rows_m1 = len(m1)
    cols_m1 = len(m1[0])
    rows_m2 = len(m2)
    cols_m2 = len(m2[0])
    
    # Ensure the matrices can be multiplied (columns of m1 must equal rows of m2)
    if cols_m1 != rows_m2:
        raise ValueError("Cannot multiply matrices: incompatible dimensions.")
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_m2)] for _ in range(rows_m1)]
    
    # Perform matrix multiplication
    for i in range(rows_m1):
        for j in range(cols_m2):
            for k in range(cols_m1):
                result[i][j] += m1[i][k] * m2[k][j]
    
    return result

# Example matrices
m1 = [[1, 2, 3],
      [4, 5, 6]]

m2 = [[1, 2], 
      [3, 3], 
      [5, 6]]

# Print the result of the multiplication
print(multiplicacion_matrices(m1, m2))

# Assertions to check correctness
assert(multiplicacion_matrices(m1, m2) == [[22, 26], [49, 59]])
