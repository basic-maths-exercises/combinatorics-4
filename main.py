
def permutations(n) : 
  if n==1 : return [[1]]
  base = permutations(n-1)
  allpermutes = [] 
  # Your code to generate all the permutations goes here
  
  return allpermutes
  

# No modifications are required from here onwards.  This code is just 
# used to test your implementation.
print( permutations(1) )
print( permutations(2) )
print( permutations(3) )
print( permutations(4) )
