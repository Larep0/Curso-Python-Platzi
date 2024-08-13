# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
'''
edad=int ( input("Ingresa Edad: "))
if edad>=18:
    print (' Eres mayor de edad')
else:
    print (' No tienes la mayoria de edad')
'''


#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''
contra= "contrasena"
pas=(input("Ingresa tu Password ==>: "))
if contra == pas.lower():
    print ('Contrasena OK')
else:
    print('Contrasena incorrecta')
'''

#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

'''
print('
               Programa para dividir dos numeros
      Ingrese los datos solicitados a continuacion .... 
      
      ')
a=int (input (' Ingresa un numero a dividir==> '))
b=int (input (' Ingresa el divisor (debe ser distinto a 0)  ==> '))
if b==0:
    print(' No es posible realizar una division por cero')
else:
    div=a/b
    print (f'El resultado de la division es :{div}')

'''
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar
'''
print('
               Programa para identificar si un numero Entero es par
                    Ingrese los datos solicitados a continuacion .... 
        
      ')
print ('#'*70)

n=int (input(' Ingrese un numero entero ====>> '))
if n % 2 == 0:
    print ('#'*70)
    print (f'El numero {n} es PAR')
    print ('#'*70)
else:
    print ('#'*70)
    print (f'El numero {n} es IMPAR')
    print ('#'*70)
'''
#Programa basico cachipun

import random
opc = ['a', 'b', 'c']
round = 1
while True:
    print('*'*10)
    print('Ronda Numero', round)
    print('*'*10)

    print(''' ****   Vamos a jugar al cachipum ****
        Seleciona una de las siguientes opciones:
        a = PIEDRA
        b = PAPEL
        c = TIJERAS
        ''') 
    Pc = random.choice (opc)
    user= input('Selecciona tu opcion a,b,c   =====>>: ')
    user=user.lower()
    if not user in opc:
        print (f'Elejiste la opcion {user}')
        print (f'El PC a selecionado {Pc}')
    if user==Pc:
        print('Empatamiento')
    elif user=='a' and Pc == 'b':
        print(f'Gana el PC con la opcion {Pc} "PAPEL", superando al USUARIO con  {user} "PIEDRA"')
    elif user=='a' and Pc == 'c':
        print(f'Gana el USUARIO con la opcion {user} "PIEDRA", superando al PC con  {Pc} "TIJERAS"')
    elif user=='b' and Pc == 'a':
        print(f'Gana el USUARIO con la opcion {user} "PAPEL", superando al PC con  {Pc} "PIEDRA"')
    elif user=='b' and Pc =='c':
        print(f'Gana el PC con la opcion {Pc} "TIJERAS", superando al USUARIO con  {user} "PAPEL"')
    elif user=='c' and Pc=='a':
        print(f'Gana el PC con la opcion {Pc} "PIEDRA", superando al USUARIO con  {user} "TIJERAS"')
    elif user=='c' and Pc=='b':
        print(f'Gana el USUARIO con la opcion {user} "TIJERAS", superando al PC con  {Pc} "PAPEL"')
    else:
        print ('Elejiste PERDER  o no sabes leer')
    opcion=(input('Quieres intentarlo otraa vez ti? : (Y/N)  ====>: '))
    if opcion.upper() == 'N':
            print('HASTA LA PROXIMA CHAYANNE')
            break
    elif opcion.upper() =='Y':
            round+=1
            continue

#Prueba GITHUB remoto


#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
#Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
'''
print(' Analisis de edad e ingresos ')
edad=int((input('Ingresa tu edad ====>>> ')))

if edad>=16:
    ingreso=float((input('Ingresa tu remuneracion mensual ====>>> ')))
    if ingreso>=1000:
        print('Cumples con los requisitos para pagar tributo')
        tributo=float((ingreso*.10))
        print(f'Debes pagar el 10% el monto correspondienteses : {tributo}')
        print('Deposite en nuestra cta. corriente o en sucursales')
    else:
        print('Tu remuneracion es inferior a 1000 € no pagas tributo')
else:
    print('Para pagar tributo, debes cumplir con el rango de eadad minimo 16')'''

#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
#El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
#Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

'''nombre = input('Ingresa tu nombre===> ')
genero = input(' Ingresa tu genero:
               Para Mssculino, seleciona "M"
               Para Femenino,  selecciona "F"
              ')
if genero == "F":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
print(f'Tu grupo es  {grupo}')'''


#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
#Renta	Tipo impositivo
#Menos de 10000€	5%
#Entre 10000€ y 20000€	15%
#Entre 20000€ y 35000€	20%
#Entre 35000€ y 60000€	30%
#Más de 60000€	45%
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
'''
print ('CALCULO DE IMPUESTOS PARA LA EMPRESA')
print ('
       DETALLE:

       Menos de 10000€	5%
       Entre 10000€ y 20000€	15%
       Entre 20000€ y 35000€	20%
       Entre 35000€ y 60000€	30%
       Más de 60000€	45%
       ')

sueldo=float((input('Ingresa tu remuneracion mensual ==== > €')))
if sueldo<10000:
    tramo_uno=sueldo*.05
    print (f'El impuesto de este tramo de acuerdo a tu sueldo es: €{tramo_uno} ')
elif sueldo>10000 and sueldo<20000:
    tramo_dos=sueldo*.15
    print (f'El impuesto de este tramo de acuerdo a tu sueldo es: €{tramo_dos} ')
elif sueldo>20000 and sueldo<35000:
    tramo_tres=sueldo*.20
    print (f'El impuesto de este tramo de acuerdo a tu sueldo es: €{tramo_tres} ')
elif sueldo>35000 and sueldo<60000:
    tramo_cuatro=sueldo*.30
    print (f'El impuesto de este tramo de acuerdo a tu sueldo es: €{tramo_cuatro} ')
elif sueldo>60000:
    tramo_cinco=sueldo*.45
    print (f'El impuesto de este tramo de acuerdo a tu sueldo es: €{tramo_cinco} ')'''


#La pizzería Freddy and Fazber ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
#Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
#Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

'''print('  #### Bienvenidoa Freddy and Fazber Pizza ####
                
              
          ****Recuerda, todas incluyen Mozarella y Tomate**** ')
print('       ')
print('       ')
print('       ')
print('Actualmente tenemos dos tipos de Pizzas disponibles:')
print('       ')
print('       ')
print('             1 - Ricas Vegetarianas para Veganos')
print('             2 - No vegetarianas, para Carnivoros, como el Joaco')
print('       ')
print('       ')
opcion=input(' Seleciona una de las 2 opciones, diguitando 1 o 2 ===> :')
if opcion=='1':
    print('         Eljiste la Pizza vegetariana
          
          Ahora debes escoger uno de las siguientes ingredientes : ')
    print('       ')
    print(' Opcion A ====> PIMIENTO')
    print(' Opcion B ====> TOFU')
    veganop=input('Seleciona una alternativa A o B ===> : ')
    veganopMa=veganop.upper()
    if veganopMa=="A":
        print('Elejiste como tercer ingrediente especial : PIMIENTO')
        print ('Tu orden fue ingresada exitosamente, Preparando!!')
    elif veganopMa=="B":
        print('Elejiste como tercer ingrediente especial : TOFU')
        print ('Tu orden fue ingresada exitosamente, Preparando!!')
    else:
        print ('Debes seleccionar una alternativa valida (A o B) CTM : ')
elif opcion=='2':

    print('       "EL MACHO" Eejiste la Pizza No vegetariana
          
          Ahora debes escoger uno de las siguientes ingredientes : ')
    print('       ')
    print(' Opcion A ====> JAMON')
    print(' Opcion B ====> PEPERONI')
    print(' Opcion C ====> SALMON')
    carneop=input('Seleciona una alternativa A o B ===> : ')
    carneopMa=carneop.upper()
    if carneopMa=="A":
        print('Elejiste como tercer ingrediente especial : JAMON')
        print ('Tu orden fue ingresada exitosamente, Preparando!!')
    elif carneopMa=="B":
        print('Elejiste como tercer ingrediente especial : PEPERONI')
        print ('Tu orden fue ingresada exitosamente, Preparando!!')
    elif carneopMa=="C":
        print('Elejiste como tercer ingrediente especial : SALMON')
        print ('Tu orden fue ingresada exitosamente, Preparando!!')
    else:
        print ('Debes seleccionar una alternativa valida (A , B o C) CTM : ')
else:
    print ('Debes seleccionar una alternativa valida (1 o 2)')'''


#Pruebas de Index y Slicing STR
'''
tabla=str.maketrans("abcdefghij","1234567890")
texto=input('Ingresa una frase: ')
primera= texto[0] #Solo se imprime el caracter indicado en el STR
print (f'La primera letra de la frase es: {primera}')
ultima=texto [-1]
print (f'La ultima letra de la frase es: {ultima}')
invert=texto[::-1] #imprime al reves el texto
print (f'La frase invertida es: {invert}')
tamano=len(texto)
print (f'El tamanho de la frase es : {tamano} caracteres')
mayus=texto.upper()
print (f'El texto en mayusculas es : {mayus} ')
ceros=texto.zfill(20) #agrega ceros hasta completar la cantidad definida del STR
print (f'Rellena con ceros a la izquierda : {ceros}')
recorte=texto[5::] #Recorta desde la posicion definida al final (0 es el primer cat=racter)
print (f'Se imprimiran desde el caracter 5 al final : {recorte}')
tras=texto.translate(tabla)
print (f'La traduccion es: {tras}')'''

#Listas (Capitulo 19)
    #Puede ser modificada
    #Cada elemento esta separado por una coma
    #Puede contener todo tipo de datos STR, Bolean, Float. INT

'''numeros = [1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,10]
typos = ['Christian', 'German', 'Diego', 'Luis']
print(numeros)
print(typos)
print(type(numeros))
print(len(numeros))
print(numeros[0])#Solo se imprime el caracter indicado en la lista (igual que en los STR)
print(numeros.count(9)) # El metodo .count() cuenta cuantas veces un elemento esta en una lista
print(typos[3]) 
typos[0]= 'Maradona'
print(typos)
typos[1]= 'Alexis'
print(typos)
typos[2]= 'Pele'
print(typos)
typos[3]= 'Ronaldinho'
print(typos)
print('Joaquin Retamal'in typos) #Pregunta si dentro de la lista existe un elemento X (Devuelve un Bolean)
print(numeros[:3])
print(typos[:1])
print(typos[-1]) Muestra el ultimo elemento de la lista

# Metodos de Listas (capitulo 20)
    # append(): Añade un ítem al final de la lista.
    # clear(): Vacía todos los ítems de una lista.
    # extend(): Une una lista a otra.
    # count(): Cuenta el número de veces que aparece un ítem.
    # index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
    # insert(): Agrega un ítem a la lista en un índice específico.
    # pop(): Extrae un ítem de la lista y lo borra.
    # remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
    # reverse(): Le da la vuelta a la lista actual.
    # sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.

typos.append('Veronica')
print(typos)
#typos.remove('Alexis Alvarez')
print(typos)
#print (typos.index('Joaquin Retamal'))
typos.pop(3)
print(typos)
typos.reverse()
print(typos)
typos.pop()
print(typos)
'''


#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y 
# quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
'''
print('    @@@@   Juegos electronicos RAPAM   @@@@')
edad=int (input(' Ingresa tu edad ====> : '))
if edad<= 4:
    print ('################# Calculando #################')
    print (f' El costo de la entrada por {edad} años es gratuito')
    print (' Disfruta tu visiva')
elif edad>4 and edad<=18:
    print ('################# Calculando #################')
    print (f' El costo de la entrada por {edad} años es de 5€')
    print (' Disfruta tu visiva')
elif edad>18:
    print ('################# Calculando #################')
    print (f' El costo de la entrada por {edad} años es de 10€')
    print (' Disfruta tu visiva')
else:
    print('Digite una edad valida') '''

#Task
#Dado un numero entero n
# 1<= n <=100

#Si es impar, imprime Raro
#Si es par y en el rango inclusivo de 2 a 5, imprimir No Raro
#Si es par y está en el rango inclusivo de 6 hasta 20 , imprime Raro
#Si es par y mayor que 20 , imprimir No Raro

'''
n=int(input('=>>').strip())
if n>=1 and n <=100:
    if n % 2 != 0:
        print('Weird')
    elif n % 2 == 0 and n>=2 and n<=5:
        print('Not Weird')
    elif n % 2 == 0 and n>=6 and n<=20:
        print('Weird')
    elif n % 2 == 0 and n>20:
        print('Not Weird')
else:
    print('Chupala Shasstin')
'''
'''
#Task
#The provided code stub reads two integers, a and b, from STDIN.
#Add logic to print two lines. The first line should contain the result of integer division, a // b. The second line should contain the result of float division, a / b.
#No rounding or formatting is necessary.

a=int(input('').strip())
b=int(input('').strip())
entero= a // b
flot= a/b
print(entero)

print(flot)
'''

#Capitulo 28 Tuplas 
#Tuplas
#Estructura de datos inmutables que contiene una secuencia ordenada de elementos
# Tupla = (1, 2, 3, 4)

#Los elementos están separados por espacios luego de las comas
#Puede contener cualquier tipo de datos (STR, Float, Int, Bolean)
#Cada posición de la tupla tiene un índice
#Es inmutable y por lo tanto no puede ser modificada, lo que permite proteger mejor la data si no queremos que se modifique por error
# Acceder a un elemento
# Tupla = (”A”, “B”, “C”)
# Tupla [0] Indice a consultar (-1 siempre muestra el ultimo elemento de la Tupla)
# “A” Nos retorna el resultado de la posición 0 en la tupla
# Encontrar un elemento
# Tupla = (”A”, “B”, “C”)
# “A” in Tupla
#  True
# “Z” in Tupla
# False

#Metodos
#Buscar el Indice de un elemento
# Tupla = (”A”, “B”, “C”)
# Tupla.index(”A”)
# 0 Nos devuelve el indice del elemento que buscamos

# Numero de veces que un elemento aparece en la Tupla
# Tupla = (”A”, “B”, “C”)
# Tupla.count(elemento)
# Tupla.count(”B”)
# 1 Retorna el numero de veces del elemento en la Tupla
'''
Tupla=('Vola3', 'Vola6', 'Pendientes','1', '2','3')
print (Tupla)
print(Tupla[-1])
Mylista=list(Tupla) #Transforme mi Tupla a Lista, asi puedo editar, agregar, etc CRUD
print(Mylista)
print(Mylista[-1])
Mytupla=tuple (Mylista)
print(Mytupla)
'''


#Diccionarios. un diccionario en Python, es como un diccionario en la vida del día a día.
#Es decir, cada palabra tiene asociado un significado.
#Pues exactamente igual tenemos en Python, cada palabra, que llamaremos clave, tiene asociado un significado, que llamaremos valor. 
#Es decir, que un diccionario no es mas que un conjunto de parejas clave – valor. Los diccionarios en Python son un tipo de dato realmente muy potente.
#Indicar que si bien en el caso de un diccionario al uso, la clave (palabra que buscamos), siempre es una cadena de texto, en Python, la clave puede ser cualquier tipo de dato, 
#un entero, una cadena de texto.
#Incluso, es posible que el tipo de dato varíe, es decir, que para un elemento sea de un tipo y para otro elemento del diccionario, sea de otro tipo

#aprederemos sobre la estructura de los diccionarios, encontraremos una palabra y por ende su definición ==> en Python sería una llave (key), y su definición 
#los diccionarios siempre se definen entre llaves 

'''
my_dicc = { 'persona': 'niño',
  'nombre': 'nicolas',
  'genero':'masculino',
  'edad': '12 años',
  'Music':'Rock'}
print(my_dicc['nombre'])
print(my_dicc.get('apellidp')) #Igual que el anterior pero es mas usado porque en el caso de no esxitir la "llave" el programa no crachea y devuelve el valor NONE
print(type(my_dicc))

print(my_dicc.items()) #Devuelve entre tuplas () los resultados asociados
print(my_dicc.keys())
print(my_dicc.values())


#Los diccionarios, funcionan con el formato clave ===> valor (Eje: Nombre: Joaquin)
persona = { 'Nombre' : 'Joaquin',
           'Apellido' : ' Retamal',
           'Edad' : 10,
           'Rut' : '24.704.786-7',
           'Curso' : ' 4to Basico',
           'Escuela' : ' Chillan',
           'Asignaturas' : ['Matematicas','Lenguaje', 'Ingles']}
print (persona)
print (persona.items())
print (persona['Asignaturas'])
persona['Asignaturas'].append('Ciencias') #Como 'Asignaturas' es una lista, puedo emplear los mismos mecanismos (por ejemplo .append)
print (persona['Asignaturas'])

del persona ['Asignaturas'] #"del" se usa como funcion para borrar un calve dentro del diccionario
print (persona)
persona.pop("Escuela") #Otro mecanismo para eliminar una clave (Es necesario enviar el argumento para borrar a diferencia de las listas)
print (persona)
print (persona.keys()) #Devuelve una lista [] con Solo los claves o llaves
print (persona.items()) #Devuelve entre tuplas () los resultados asociados
'''

#Capitulo 33 Loop
#While
#Mientras la condicion se cumpla, el ciclo se repetira.
# while: cuando no nonozcas la cantidad de elementos a recorrer o la cantidad de iteraciones a realizar.

'''
numero = 0
while numero<10: 
    numero += 1
    print (numero)
'''
'''
numero = 0 
while numero < 20:
    numero += 1 
    if numero == 15:
        break #Rompe el ciclo de manera forzada
    print (numero)
'''
'''
numero = 0
while numero < 20:
    numero +=1
    if numero < 15:
        continue #En Python, la declaración "continue"
                # se utiliza dentro de un bucle (como while o for) para omitir el resto del código dentro del bucle para la iteración actual 
                # y pasar inmediatamente a la siguiente iteración del bucle 
    print (numero)
'''
'''
maximo = 10
multiplicador = 0
print('#### Plantilla para tablas de multiplicacion ####')
tabla =int(input(' Ingresa la tabla que deseas aprender =====>:'))
while multiplicador <= maximo:
    print (tabla, 'X' ,multiplicador, '===========>', tabla * multiplicador)
    multiplicador +=1
'''
# Capitula 34 "for"
# : for CO
# cuando conozas la cantidad de elementos a recorrer o el número de iteraciones a relaizar.
# El ciclo for en Python se utiliza para iterar sobre una secuencia (como una lista, tupla, cadena, conjunto o diccionario) 
# o cualquier otro objeto iterable. La sintaxis básica de un ciclo for es:

#for variable in iterable:
    # bloque de código

# variable: La variable que tomará el valor de cada elemento en la secuencia durante cada iteración del ciclo.
# iterable: La secuencia u objeto que se está iterando.
# bloque de código: El conjunto de instrucciones que se ejecutarán en cada iteración del ciclo.



#El siguiente ejemplo (en una Lista de actividades, encontrar la ultima tarea realizada y listar las pendientes)
'''
lista = ['Lavar Ropa','Planchar', 'Cocinar', 'Dormir', 'Estudiar']
print('Esta semana tenemos que realizar las siguientes actividades : ')
print (lista)
tarea = ( input ('De la lista anterior, Ingresa la ultima tarea realizada =====> : '))

# Variable para marcar si el elemento fue encontrado
encontrado = False

# Iterar sobre la lista con índice
for i, elemento in enumerate(lista):
    if elemento == tarea:
        encontrado = True
        # Imprimir los elementos restantes a partir del índice encontrado
        print(f"La tarea {tarea} fue encontrada con el índice {i} en la lista de actividades")
        print("Las siguientes Tareas aun estan pendientes por realizar :", lista[i+1:])
        if i+1 == None:
            print ('No hay tareas por realizar')
        break
if not encontrado:
    print(f"La tarea :{tarea} no es parte de la lista.")
'''
lista = ['Joaquin', 'Thiago', 'Cristobal','Michael']
Tupla = ('11','12','13','14','15')
dicc  = {
    'nombre' : 'Camisa',
    'Precio' : 100,
    'Stock' : 15
        }
'''
for i in dicc:
    print(i, '====>',dicc[i]) #aca recorro el diccionario 'i' imprimo una flecha y el mismo diccionario, como este ejemplo:  
     nombre ====> Camisa
        Precio ====> 100
        Stock ====> 15 
for i, value in dicc.items():
    print(i,'====>', value )'''
'''
gente = [
    {
        'nombre' : 'Luis',
        'edad' : 42,
        'genero' : 'Masculino'
    },
    {
       'nombre' : 'Joaquin',
        'edad' : 10,
        'genero' : 'Masculino'
    },
    {
       'nombre' : 'Romi',
        'edad' : 38,
        'genero' : 'Femenino' 
    }
]
for i in gente:
    print(i) #Sin formato
    print('nombre ===>',i['nombre']) 
    print('Edad =====>',i['edad'])
    print('Genero ===>',i['genero'])
'''
#En este desafío, se te proporcionará una lista de números llamada my_list. 
# Tu tarea es recorrer esta lista y utilizar un ciclo para seleccionar solo los números positivos. 
# Luego, debes agregar estos números a una nueva lista llamada new_list. Al final del ciclo, 
# debes imprimir los valores contenidos en new_list utilizando la función print.
# Por ejemplo, si la lista es [1, -1, 2, -2, 3, -3, 4, -4], 
# después de realizar las operaciones descritas, la lista new_list debería contener solo los números positivos, es decir, [1, 2, 3, 4].

'''
my_list = [1, -1, 2, -2, 3, -3, 4, -4, 69,-55,1001,-69]
new_list = []
nega =[]
print(f'Esta es la actual lista de numeros : {my_list}')
for positivos in my_list:
    if positivos > 0:
        new_list.append(positivos)
    elif positivos < 0:
        nega.append(positivos)

print(f'la nueva lista, solo con numeros positivos es : {new_list}')
print(f'Los numero negativos de la lista son  : {nega}')
'''

'''
matriz=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(matriz[0][2]) # Aca dentro de la matriz usando los mecanismos de Listas puedo identificar por posicion un elemento 

for filas in matriz:
    if 0 in filas:
        print('Si se encontro el elmento 0')
    elif 0 not in filas:
        print(' 0 no  pertenece a la fila')
    print (filas)
for filas in matriz:
    print (filas)
    for columnas in filas:
        print(columnas)
'''
        
      
