#8- Argumentos arbitrarios de palabras clave, **kwargs

def my_function(**chico):
  print("El historial de "+""+chico["fname"]+" "+ chico["lname"]+" "+"Es bueno")

my_function(fname = "Angel", lname = "Andrey")
