'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici
  if n < 2:
    return False
  
  for i in range(2,n//2+1):
    if n%i == 0:
      return False
  
  return True
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
  produs = 1
  for element in lst:
    produs *= int(element)
  
  return produs

  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
  while x != y:
    if x>y:
      x-=y
    else:
      y-=x
  
  return x
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici

  rest = -1
  while rest != 0:
    rest = x%y
    x=y
    y=rest
  
  return x
  
  
  
def main():
  # interfata de tip consola aici

  isrunning = True

  while isrunning:
    problema = input("Scrie numarul problemei!\n")

    if problema == "1":
      print("Ai ales problema unu: Verificam daca n este un numar prim.")
      numar = int(input("Scrie numarul n: "))
      if is_prime(numar):
       print(f"Numarul {numar} este prim")
      else:
        print(f"Numarul {numar} nu este numar prim")
    
    elif problema == "2":
      print("Ai ales optiunea 2: Produsul numerelor din lista")
      lista = []
      n = int(input("Scrie numarul de elemente din lista."))

      for i in range(n):
        elem = int(input("Scrie elementul din lista."))
        lista.append(elem)
      
      print(f"Produsul elementelor din lista este {get_product(lista)}")
    
    elif problema == "3":
      print("Ai ales obtiunea 3: Aflarea cmmdc-ului a doua numere.")
      x = int(input("Scrie primul numar: "))
      y = int(input("Scrie al doilea numar: "))
      print("Metoda 1: cmmdc cu scaderi repetate.")
      print(get_cmmdc_v1(x,y))

      print("Metoda 2: cmmdc cu modulo.")
      print(get_cmmdc_v2(x,y))
    
    elif problema == 'x':
      isrunning = False

    else:
      print("Ai ales o obtiune grsita, incearca din nou!")
      
if __name__ == '__main__':
  main()
