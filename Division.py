def Division():

  a  = int(input("enter any number"))

  b = int(input("enter any number"))
  try:
    c = a/b
  except:
    print('cant divide by zero')
  return c 
