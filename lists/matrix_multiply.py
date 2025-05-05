def multiply(list1, list2):
  if len(list1[0]) != len(list2):
    return 'matrix not possible'
  
  result = []

  for i in range(len(list1)):
    row = []
    for j in range(len(list1[0])):
      sum = 0

      for k in range(len(list2)):
        sum += list1[i][k] * list2[k][j]
      row.append(sum)
    result.append(row)

  return result

print(multiply([[1,1],[1,1]], [[1,1],[1,1]]))