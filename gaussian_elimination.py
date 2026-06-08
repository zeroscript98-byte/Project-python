

matrix =[
  [2, 1, -1,0],
  [1, -2, 2,10],
  [3, 3, 2,9]
  ]
def pivot_determiner():
  n=len(matrix)
  for pivot in range(n):
    for row in range(pivot+1,n): #rows under pivot
      factor=matrix[row][pivot]/matrix[pivot][pivot] #division factor
      for col in range(len(matrix[0])):
        matrix[row][col]=matrix[row][col]-factor*matrix[pivot][col]
        
def back_subtitutions():
  n=len(matrix)
  result=[]
  for i in range(n):
    result.append(0)
  for index in range(n-1,-1,-1): #bottom row
    vector_value=matrix[index][-1]
    for value in range(index+1,n): #to find the unknown number with the last variable
      vector_value -= matrix[index][value] * result[value]
    result[index] = vector_value / matrix[index][index]
  print(result)
  
pivot_determiner()
back_subtitutions()