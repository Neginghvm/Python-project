def EX1_1(number):
   '''
  (int)-> int
    we give an int to the function and returns number+1
    example:
    >>> EX1_1(6)
    7
    '''
  if type(number)==int:
    v=number+1
    return v
  else:
    return "not found"
