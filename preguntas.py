"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


#Primer LAB
import csv

with open(r".\data.csv", 'r') as file:
  csvreader = csv.reader(file,delimiter='\t')
  data=[]    
  for row in csvreader:
      data.append(row)
  
file.close()

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma=0
    for lista in data:
        for number in lista[1]:
            suma=int(number)+suma
            
        
    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    letter_list=[]
    
    for lista in data:
        for letter in lista[0]:
            letter_list.append(letter)
        
    letter_list.sort()
    
    letter_set=set(letter_list)
    unique_list=(list(letter_set))
    unique_list.sort()
    
    tupple_list=[]
    for letter in unique_list:
        tupple=(letter,letter_list.count(letter))
        tupple_list.append(tupple)
        
    
    return tupple_list


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
 

    list_alf_num=[]
    for lista in data:
        row=[]
        for element in lista[0:2]:
            row.append(element)
        
        list_alf_num.append(row)
            
            
    list_alf_num.sort()
    letter=list_alf_num[0][0]
    suma=0 
    list_tupla=[]
    for lista in list_alf_num:
        if letter!=lista[0]:
            list_tupla.append((letter,suma))
            suma=0 
            letter=lista[0]
            
        suma=suma+int(lista[1])
        
    list_tupla.append((letter,suma))     
   
    
    return list_tupla


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    list_meses=[]
    for lista in data:
        date=lista[2]
        mes=date[5:7]
        list_meses.append(mes)
    
    list_meses.sort()
    
    mes=list_meses[0]
    suma=0 
    list_tupla=[]
    for lista in list_meses:
        if mes!=lista:
            list_tupla.append((mes,suma))
            suma=0 
            mes=lista
            
        suma=suma+1
        
    list_tupla.append((mes,suma))     
   
    
    return list_tupla


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    list_val=[]
    for lista in data:
        list_val.append([lista[0],lista[1]])
    
    list_val.sort()
    
    letter=list_val[0][0]
    list_tupla=[]
    mini=0
    maxi=0
    control_init=0
    for lista in list_val:
        if letter!=lista[0]:
            list_tupla.append((letter,maxi,mini))
            mini=int(lista[1])
            maxi=int(lista[1])
            letter=lista[0]
        
        if control_init==0:
            mini=int(lista[1])
            
        
        if maxi<int(lista[1]):
            maxi=int(lista[1])
        
        if mini>int(lista[1]) :
            mini=int(lista[1])
        
        control_init=control_init+1
            
            
    list_tupla.append((letter,maxi,mini))
            
       
        
 
        
    return list_tupla


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    
    dict_list=[]
    
    for lista in data:
        crrt_lista=lista[4].split(',')
        for element in crrt_lista:
            dict_list.append(element.split(':'))
     
    dict_list.sort()
    key=dict_list[0][0]
    
    
    list_tupla=[]
    mini=0
    maxi=0
    control_init=0
    for lista in dict_list:
        if key!=lista[0]:
            list_tupla.append((key,mini,maxi))
            mini=int(lista[1])
            maxi=int(lista[1])
            key=lista[0]
        
        if control_init==0:
            mini=int(lista[1])
            
        
        if maxi<int(lista[1]):
            maxi=int(lista[1])
        
        if mini>int(lista[1]) :
            mini=int(lista[1])
        
        control_init=control_init+1
            
            
    list_tupla.append((key,mini,maxi))
            
    """   
            """
        
 
            
            
    return list_tupla


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    list_n_l=[]
    lista_no=[]
    for lista in data:
        list_n_l.append([lista[1], lista[0]])
        if (lista[1] not in lista_no):
            lista_no.append(lista[1])
            
    lista_no.sort()
    
    list_letters=[]
 
    tuple_list=[]
    
    for numero in lista_no:
        for lista in list_n_l:
            if numero==lista[0]:
                list_letters.append(lista[1])
            
        tuple_list.append((int(numero),list_letters))
        list_letters=[]
    
      
    
    return tuple_list


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    list_n_l=[]
    lista_no=[]
    for lista in data:
        list_n_l.append([lista[1], lista[0]])
        if (lista[1] not in lista_no):
            lista_no.append(lista[1])
            
    lista_no.sort()
    
    list_letters=[]
 
    tuple_list=[]
    
    for numero in lista_no:
        for lista in list_n_l:
            if numero==lista[0] and lista[1] not in list_letters:
                list_letters.append(lista[1])
           
        list_letters.sort()
        tuple_list.append((int(numero),list_letters))
        list_letters=[]
    
    
    return tuple_list


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    dict_list=[]
    
    for lista in data:
        crrt_lista=lista[4].split(',')
        for element in crrt_lista:
            dict_list.append(element.split(':'))
     
    dict_list.sort()
    key=dict_list[0][0]
    
    mini=0
    maxi=0
    suma=0
    control_init=0
    claves={}
    key=dict_list[0][0]
    for lista in dict_list:
        if lista[0]==key:
            suma=suma+1
            claves[key]=suma
        
        elif lista[0]!=key:
            suma=1
            key=lista[0]
            claves[key]=suma
        
    
    return claves


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    list_tupla=[]
    for lista in data:
        letter=lista[0]
        long_4=len(lista[3].split(','))
        long_5=len(lista[4].split(','))
        list_tupla.append((letter,long_4,long_5))
        
    
    return list_tupla


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    
    letter_list=[]
    for lista in data:
        for l in lista[3].split(','):
            if l not in letter_list:
                letter_list.append(l)
    
    letter_list.sort()
    dicc={}
    suma=0
    
    for letter in letter_list:
        for lista in data:
            if letter in lista[3]:
                suma=suma+int(lista[1])
                
        dicc[letter]=suma
        suma=0
            
    
        
    return dicc


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    
    list_val=[]
    for lista in data:
        parts=lista[4].split(',')
        numbers=[]
        for parte in parts:
            numbers.append(int(parte.split(':')[1]))
        
        suma=sum(numbers)
            
            
        list_val.append([lista[0],suma])
        
    
    list_val.sort()
   
    dicc={}
    letter=''
    for key in list_val:
        if letter!=key[0]:
            letter=key[0]
            dicc[key[0]]=key[1]
        else:
            dicc[key[0]]=dicc[key[0]]+key[1]
     
            
        
    return dicc
