#6- Si no sabe cuántos argumentos se pasarán a su función, agregue un * antes del nombre del parámetro en la definición de la función.
#De esta manera, la función recibirá una tupla de argumentos y podrá acceder a los elementos en consecuencia:
#Si se desconoce el número de argumentos, agregue un * antes del nombre del parámetro:
def my_function(*kids):
  print("El es mi amigo " + kids[0])
my_function("Alan", "tito", "Andrey")

def my_function(*kids):
  print("Este es mi amigo " + kids[1])
my_function("Alan", "tito", "Andrey")

def my_function(*kids):
  print("este soy yo :) " + kids[2])
my_function("Alan", "tito", "Andrey")

def my_function(*kids):
  print("estos somos todos juntos :) " + kids[0] + kids[1] + kids[2])
my_function("Alan" " ", "tito" " ", "Andrey")







