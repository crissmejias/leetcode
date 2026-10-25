# Tenemos dos strings `s` y `t` y queremos devolver True en caso de que `t` tenga los mismos caracteres repetidos la misma cantidad de veces.

def valid_anagram(s : str, t : str) -> bool:
    conteos = {}
# Evaluamos que las longitudes de los str sean iguales.
    if len(s) != len(t):
        return False
# Sumamos y restamos en el conteo por cada elemento, si son iguales, quedará en 0.
    for char in s:
        conteos[char] = conteos.get(char, 0) + 1
    for char in t:
        conteos[char] = conteos.get(char,0) - 1
# Si algún elemento queda por debajo de 0, retorna False.
        if conteos[char] < 0:
            return False
    return True


print(valid_anagram("anagram", "nagaram"))  # True
print(valid_anagram("rat", "car"))          # False
print(valid_anagram("perro", "orre"))       # False (distinta longitud)
print(valid_anagram("", ""))                # True
print(valid_anagram("a", "a"))              # True
print(valid_anagram("a", "b"))              # False
print(valid_anagram("aab", "abb"))          # False (mismas letras, distinta cantidad)