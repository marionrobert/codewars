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


# better solutions
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

#
def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]
