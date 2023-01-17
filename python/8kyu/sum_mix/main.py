# my solution
def sum_mix(arr):
  # transform array of all numbers
  new_array = []
  for n in arr:
    new_array.append(int(n))
  # print(new_array)
  return sum(new_array)

# better solution
def sum_mix(arr):
    return sum(map(int, arr))
