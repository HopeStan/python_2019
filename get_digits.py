def get_digits(num):
  list_of_int = []
  if num is 0:
     return_tuple = (0,)
  while num != 0:
    list_of_int = [num%10]+list_of_int
    num //= 10
    return_tuple = tuple(list_of_int)
  return return_tuple

 
print(get_digits(int(input())))
