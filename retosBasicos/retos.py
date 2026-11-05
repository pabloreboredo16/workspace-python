def area_marco(ancho, alto, grosor):
    area_total = ancho * alto
    area_hueco = (ancho - 2 * grosor) * (alto - 2 * grosor)
    return area_total - area_hueco
print(area_marco(10, 8, 1))

mi_array = [1, 2, 3, 4, 5]
print(mi_array[2])

def se_solapan(primera, segunda):
    inicio1, fin1 = primera
    inicio2, fin2 = segunda
    
    return inicio1 < fin2 and inicio2 < fin1
print(se_solapan((9, 12), (11, 14)))
print(se_solapan((9, 11), (11, 13)))

def variaciones(lecturas):
    resultados = []
    for i in range(1, len(lecturas)):
        resultados.append(lecturas[i] - lecturas[i - 1])
    return resultados
print(variaciones([10, 13, 8, 8]))

# NO FUNCIONA EL TEST
numero = "33"
numero_entero = int(numero)
print(numero_entero)

# NO FUNCIONA EL TEST
usuarios = {"Juan", "Ana", "Carlos", "Maria", "Carlos"}
usuarios.add("Luis")
usuarios.remove("Carlos")
print(usuarios)

