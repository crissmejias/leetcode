# Te dan dos strings `s` y `t` de la misma longitud.
# Devuelve True si son isomorfos (los caracteres se repiten la misma cantidad de veces)
# Solo se puede reemmplazar un caracter por otro, no se puede cambiar luego.

def isomorphic_strings(s: str, t: str) -> bool:
    hashmap = {}
    
