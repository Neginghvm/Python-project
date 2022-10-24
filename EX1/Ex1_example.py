def EX1_example(num_minutes):
  '''
  (int) -> int
  return the number of seconds there are in num_minutes minutes variable.
  example:
  >>> EX1_example(6)
  360
  '''
  
  if type(num_minutes)==int:
    seconds=num_minutes*60
    return(seconds)
  else:
    return"not found"
  
