def EX1_5(age):
  '''
  the program should display a message indicating whether the person is an infant, a child, a teenager, or an adult.
  example:
  >>>ex1_5(18)
  teenager
  '''
  
  if age<=1 and age>0:
    return "infant"
  if age>1 and age<13:
    return "child"
  if age>=13 and age<20:
    return "teenager"
  if age>=20:
    return "adult"
  else:
    return "not found"
