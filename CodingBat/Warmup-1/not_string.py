#Given a string, return a new string where "not " has been added to the
#front. However, if the string already begins with "not", return the
#string unchanged.

def not_string(str):
  prefix = 'not '
  if str[:3] != prefix:
    return prefix + str
  else:
    return str
#80% correct, still needs work
