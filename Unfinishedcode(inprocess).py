def mainRoute(start_code, start_no, dest_code, dest_no):
  # NORTH
  if (start_code=='N'  or dest_code=='N') and (start_no< 9 or dest_no < 9):
      return True
  # EAST
  elif (start_code=='E' or dest_code=='E') and (start_no< 10 or dest_no < 10):
      return True
  # SOUTH
  elif (start_code=='S' or dest_code=='S') and (start_no< 9 or dest_no < 9):
      return True
  # WEST
  elif (start_code=='W' or dest_code=='W') and (start_no< 2 or dest_no < 2):
      return True
  else:
    return False


def mainFare(start_code, start_no, dest_code, dest_no):
  #Saphan Taksin - Wongwian Yai 16baht!
  if mainRoute(start_code, start_no, dest_code, dest_no)==True and (start_code=='S' and dest_code=='S') and (start_no==6,8 and dest_no ==6,8 ):
    return 16
  # MOCHIT - HAYAKLADPRAO FREE!!
  if mainRoute(start_code, start_no, dest_code, dest_no)==True and (start_code=='N' and dest_code=='N') and (start_no==9,8 and dest_no ==9,8 ):
    return 0
  elif mainRoute(start_code, start_no, dest_code, dest_no)==True and (start_code == dest_code):
    x = start_no - dest_no
    x=abs(x) 
    if x==1:
      return 16
    elif x==2:
      return 23
    elif x==3:
      return 26
    elif x==4:
      return 30
    elif x==5:
      return 33
    elif x==6:
      return 37
    elif x==7:
      return 40
    elif x>7:
      return 44
    else:
      return 'None'


def extentFare(start_code, start_no, dest_code, dest_no):
  # SAMRONG - KHEHA FREE!!
  if mainRoute(start_code, start_no, dest_code, dest_no)==False and(start_code=='E'and dest_code=='E') and (14<start_no<24 and 14<dest_no<24 ):
    return 0
  #E10-E14(BANG CHAK - BEARING 15 baht through the station) 
  elif mainRoute(start_code, start_no, dest_code, dest_no)==False and(start_code=='E'and dest_code=='E') and (9<start_no<15 and 9<dest_no<15 ):
    return 15
  # N9-N24(HA-YAEK-LADPRAO - KHUKHOT)
  elif mainRoute(start_code, start_no, dest_code, dest_no)==False and(start_code=='N'and dest_code=='N') and (8<start_no<25 and 8<dest_no<25 ):
    return 15
  # S9-S12 (PHO-NIMIT - BANGWA)
  elif mainRoute(start_code, start_no, dest_code, dest_no)==False and(start_code=='S'and dest_code=='S') and (8<start_no<13 and 8<dest_no<13 ):
    return 15


def totalFare():
  total = mainFare('N',8,'N',9) + extentFare('N',9,'N',13)
  return total

print(mainRoute('N',8,'N',9))
print(mainFare('N',8,'N',9))
print(extentFare('N',9,'N',13))
print (totalFare())
