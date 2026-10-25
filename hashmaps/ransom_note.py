# Tenemos dos strings, ransom_note y magazine. 
# Devolver True si podemos armar ransom_note con las letras de magazine y False si no.

def ransom_note(note : str, magazine : str) -> bool:
    hashmap = {}
    for char in magazine:
        hashmap[char] = hashmap.get(char,0) + 1
    for char in note:
        hashmap[char] = hashmap.get(char, 0) -1
        if hashmap[char] < 0:
            return False
    return True

print(ransom_note("note", "oten"))
print(ransom_note("this is a long note", "short magazine"))
print(ransom_note("ransom note", "this is a magazine that includes ransom note"))
print(ransom_note("note", ""))

print(ransom_note("aa", "ab"))     # False
print(ransom_note("a", "b"))       # False
print(ransom_note("", "abc"))      # True
