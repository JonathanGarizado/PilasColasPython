# pila
pila = []
pila.append(True)
pila.append(1)
pila.append(2)
pila.append("Manzana")
print(pila)
variable_temporal =pila.pop()
print(pila)
print(variable_temporal)

# colas
cola = []
cola.append(True)
cola.append(1)
cola.append(2)
cola.append("Manzana")
print(cola)
vari = cola.pop(0)
print(cola)
print(vari)

# Diccionario
Tupla = ("Lucas","Juana","Juan Carlos","Karen","Viviana","Jhoan","Lorenzo","Ivan","Lina","Paola")

Lista = ["Cuaderno","Frutas","lapiceros","celular","portatil","parapente","gafas","pan de lorenzo"]

Años = (1996,1982,1976,1984,1954,1976,1895,1972,1980)

Informacion = {} # dict()
# Informacion = {'Nombre':Tupla, 'Compras':Lista, 'Años': Años}
Informacion['Nombre'] = Tupla
Informacion['Compras'] = Lista
Informacion['Años'] = Años
# print(Informacion)

lista_keys = []
for keys in Informacion:
  lista_keys.append(keys)
  print(keys)

for keys in Informacion:
  print(Informacion[keys])
# print(Informacion['Nombre'])

# Listas de listas
Lista_principal = []
Lista_principal.extend([Tupla,Lista,Años])
# print(Lista_principal)

def extraer(Diccionario,llave,Nombre):
  for iterador in range(len(Diccionario[llave])):
    if Diccionario[llave][iterador] == Nombre:
      lista_keys = []
      for keys in Diccionario:
        if keys != llave:
          lista_keys.append(keys)
      lista_keys.sort()
      # print(lista_keys)
      lista_requerida = []
      for item in lista_keys:
        lista_requerida.append(Diccionario[item][iterador])

  return lista_requerida

lista_requerida = extraer(Informacion,'Nombre','Karen')

# print(lista_requerida)


Informacion['años'] = [1234,1235,1236,1379,1052]

Informacion['Compras'][4]='Caja'
# print(Informacion['Compras'])

del Informacion['años']

# ejemplo de pop en una lista del diccionario

Informacion['Compras'].pop()
# print(Informacion['Compras'])

# Diccionario
Dicc = {}
Dicc["123456"] = {"Nombre":"Juan","Edad":20,"Tipo de sandre":"O+","Compras":"Frutas"}

print(Dicc)

print(Dicc['123456']['Tipo de sandre'])





##################################################

#############################################