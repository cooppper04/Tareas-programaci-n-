lista=[("nombre","valeria"),("edad",22),("profesion","matemtacias")]
diccionario=dict(lista)
print(diccionario)


#clave y valor
mi_diccionario={
    "valeria":"hola",
    "edad":22,
}
for valeria in mi_diccionario:
    print(valeria)

#contar los elementos en una lista
frecuencia={ "manzana":0,"pera":0,"piña":0,"naranja":0}
diccionario= ["manzana","pera","piña","manzana","pera","naranja",]
for elemento in diccionario:
    frecuencia[elemento]+= 1
print(frecuencia["manzana"])
print(frecuencia["pera"])
print(frecuencia["piña"])
print(frecuencia["naranja"])

#combinar diccionario
dic1={
    "a":10,
    "b":20,
}
dict2={
    "b":30,
    "c":40,
}
dic1.update(dict2)
print(dic1)

#valor maximo}
precios={
    "manzana":2.5,
    "banana":1.8,
    "naranja":3.0
}
valor_maximo=max(precios.values())
print(valor_maximo)

#convertir una lista de duplas en diccionario
lista_duplas=[("a",10),("b",20),("c",30)]
diccionario_n=dict(lista_duplas)
print(diccionario_n)

#promedio de un diccionario
notas={
    "matematicas": 8,
    "historia": 7,
    "ciencia": 9
}

              


        

        



