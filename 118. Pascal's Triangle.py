def pascal(numRow):
  out = []
  for i in range(numRow):
    if i == 0:
      out.append([1])
    elif i==1:
      out.append([1,1])
    else:
      temp = [1]
      for index in range(i-1):  
        if index +1 <len(out[i-1]):
          temp.append(out[i-1][index] +out[i-1][index+1])   
        if index +1 == len(out[i-1])-1:
          temp.append(1)
          out.append(temp)
  return out
