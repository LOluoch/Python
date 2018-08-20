#Given two int values, return their sum. Unless the two values are the
#same, then return double their sum.

def sum_double(int1, int2):
  sum = int1 + int2
  if int1 == int2:
    sum= sum * 2
  return sum
