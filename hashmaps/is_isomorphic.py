# Te dan dos strings `s` y `t` de la misma longitud.
# Devuelve True si son isomorfos (los caracteres se repiten la misma cantidad de veces)
# Solo se puede reemmplazar un caracter por otro, no se puede cambiar luego.

def is_isomorphic(s: str, t: str) -> bool:
    hashmap_s = {}
    hashmap_t = {}
    for char_s, char_t in zip(s, t):
        hashmap_s[char_s] = hashmap_s.get(char_s,char_t)
        hashmap_t[char_t] = hashmap_t.get(char_t,char_s)
        if hashmap_s[char_s] != char_t or hashmap_t[char_t] != char_s:
            return False
    return True
# Los del enunciado
print(is_isomorphic("egg", "add"))        # True
print(is_isomorphic("foo", "bar"))        # False (regla 1)
print(is_isomorphic("paper", "title"))    # True
print(is_isomorphic("badc", "baba"))      # False (regla 2)
print(is_isomorphic("a", "a"))            # True
print("-------------------")
# Para probar cada regla por separado
print(is_isomorphic("aabb", "abab"))      # False (regla 1: la 'a' va a 'a' y luego a 'b')
print(is_isomorphic("aa", "ab"))          # False (regla 1)
print(is_isomorphic("ab", "aa"))          # False (regla 2: 'a' y 'b' van a la misma)
print("-------------------")

# Bordes
print(is_isomorphic("", ""))              # True
print(is_isomorphic("abc", "abc"))        # True (cada una a sí misma)
print(is_isomorphic("ab", "ba"))          # True (intercambio)
print(is_isomorphic("abca", "zbxz"))      # True (la 'a' se repite y siempre da 'z')
print(is_isomorphic("abca", "zbxy"))      # False (la 'a' da 'z' y luego 'y')