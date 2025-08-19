matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Result = []

# for i in range(len(matrix)):
#     row = []
#     for j in range(len(matrix[i])):
#         row.append(matrix[j][i])
#     Result.append(row[::-1])    

# for row in Result:
#     print(row)


# optimal
n = len(matrix)

for i in range(n):
    for j in range(i+1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for row in matrix:
    row.reverse()     

for row in matrix:
    print(row)


