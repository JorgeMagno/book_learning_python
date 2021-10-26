#1
#def is_prime(n, i = 2): 
  
    # Base cases 
#    if (n <= 2): 
 #       return True if(n == 2) else False
  #  if (n % i == 0): 
   #     return False
    #if (i * i > n): 
     #   return True 
  
    # Check for next divisor 
    #return is_prime(n, i + 1) 
  
  
# Driver Program 
#print('is_prime(3):', is_prime(3)) #
#print('is_prime(7):', is_prime(7)) #
#print('is_prime(9):', is_prime(9)) #
#print('is_prime(23):', is_prime(23))

def triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = triangle(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
    return result

triangle = triangle(10)
for row in triangle:
	print(row)
