# my solution
def find_outlier(integers):
  numbers_of_pairs = 0
  numbers_of_impairs = 0

  for n in integers :
    if n % 2 == 0:
      numbers_of_pairs += 1
    else:
      numbers_of_impairs += 1

  if numbers_of_impairs == 1:
    for n in integers :
      if n % 2 != 0 :
        return n
  else :
    for n in integers :
      if n % 2 == 0:
        return n

