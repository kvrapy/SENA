
m = []
a = []#estudiantes
nt = []#notas
   

#-----------------------------------NOTAS---------------------
def nots():

  mi = int(input("cuantas notas desea ingresar?: "))
  
  t = []
  
  for i in range(0,mi) :
    
    print("ingresa la nota #",(i+1))
    n = input(">>")
    t.append(n)
    
  nt.append(t)
  


#-----------------------------------Capturar---------------------


def capt():
  print("################")
  print("#  INGRESAR    #")
  print("################")

  print("Cuantos alumnos desea ingresar ? : ")
  n = input(">>")
  n=int(n)

  for i in range(0,n):
    i = int(i)
    
  
    n = input("nombre : ")
    ap = input("apellido")
    tel = input("tel : ")
    nots() #para ingresar las notas
    l=[n,ap,tel,nt[i]]
    a.append(l)
    print(a[i])
    







#----------------------------eliminar estudiante------------------

def imprimirlista(lista,nombre):
    for i in range(0,len(lista)):
        print (nombre + "[" + str(i) + "]=" + str(lista[i]))

def eliminarele(lista, value):
    lista.remove(value)
    
def eliminar():  #esta es la combinacion de las 2 fun anteriores(principal)
  print("################")
  print("#  ELIMINAR    #")
  print("################")

  imprimirlista(a,"estudiante") 
  cn=int(input("Cual estudiante desea eliminar "))
  eliminarele(a,a[cn])
  imprimirlista(a,"estudiantes")
  

#-----------------------agregar-----------------------------
def agregar():
  print("################")
  print("# 1 ESTUDIANTE #")
  print("################")
  for i in range(0,1):
    i = int(i)
    n = input("nombre : ")
    ap = input("apellido")
    tel = input("tel : ")
    ns = nots() #para ingresar las notas
    l=[n,ap,tel,nt[i]]
    a.append(l)
    print(a[((i + len(a))) - 1])
    print(a)
  

#------------------imprimir estudiantes---------
def imprimir():
  print("################")
  print("#    LISTA     #")
  print("################")
  imprimirlista(a,"estudiantes")#se llama del bloque  eliminar
  
#-----------Eliminar NOTAS---------------------
def imp(lista):
    for i in range(0,len(lista)):
      print (lista[i][0] + "[" + str(i) + "]=" + str(lista[i][3]))
        
def eli(lista):
    del lista[::]        
def elimntas(): #principal
  print("################")
  print("#ELIMINAR NOTAS#")
  print("################")
  imp(a)
  v = int(input("cuale notas desea eliminar : "))
  de = a[v][3]
  eli(de)
  imp(a)



#-------------agregar notas-----------------
def agg(lista):
  mi = int(input("cuantas notas desea ingresar?: "))
  for i in range(0,mi) :
    print("ingresa la nota #",(i+1))
    n = input(">>")
    lista.append(n)
  
def agntas(): #principal
  print("##################")
  print("# AGREGAR  NOTAS #")
  print("##################")
  imp(a)#la funcion esta en eliminar notas
  print("a quien desea agregarle notas : ")
  o = int(input(">> "))
  de = a[o][3]
  agg(de)
  

def principal():
    opcion= 1
    while (opcion!= 7):
      
      
        print("################")
        print("#              #")
        print("#    MENU      #")
        print("#  PRINCIPAL   #")
        print("#              #")
        print("################")
        print("----MENU PRINCIPAL----")
        print("1.Ingresar Lista de estudiantes")
        print("2.Agregar estudiante")
        print("3.Eliminar estudiante")
        print("4.mostrar lista de estudiante")
        print("5.Agregar notas")
        print("6.Eliminar notas")
        print("7. Salir")
        print("Que deseas hacer?")
        opcion=int(input(">>"))
        if(opcion== 1):
            capt()
        elif(opcion== 2):
            agregar()
        elif(opcion== 3):
          eliminar()
            
        elif(opcion== 4):
          imprimir()
            
        elif(opcion== 5):
          agntas()
        elif (opcion== 6 ):
          elimntas()

        elif (opcion== 7):
            print("sallistes del programa")
        else:
            print("opcion mala")

#LLamando a la funcion principal

print(principal())  