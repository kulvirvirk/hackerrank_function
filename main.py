# Problem description: 
# https://www.hackerrank.com/challenges/write-a-function/problem 

def is_leap(year):

  # First method; works but unnecessarily long 
  # leap = False
  # if year % 4 == 0:
  #   leap = True
  #   if year % 100 == 0 and year % 400 != 0:
  #     leap = False

  # else: leap == False
  # return leap

 # second method; way more elegent.
 # because we are just returning True or False 
  return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


year = int(input('Enter year: '))

print(is_leap(year))