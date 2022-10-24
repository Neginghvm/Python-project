def EX1_6(rom_num):
  '''
  this program shows the ROMAN NUMERAL version of the number,if the number is outside the range of 1 through 10 the program returns an error message ( tis is not correct )
  example:
  >>>EX1_6(5)
  V
  '''
  if rom_num==1:
    return "I"
  elif rom_num==2:
    return "II"
  elif  rom_num==3:
    return "III"
  elif  rom_num==4:
    return "IV"
  elif  rom_num==5:
    return "V"
  elif rom_num==6:
    return "VI"
  elif rom_num==7:
    return "VII"
  elif rom_num==8:
    return "VIII"
   elif rom_num==9:
     return "IX"
  elif rom_num==10:
    return "X"
  else:
    return "this is not correct"
