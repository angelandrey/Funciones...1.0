def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(10, 10, c = 1, d = 1)