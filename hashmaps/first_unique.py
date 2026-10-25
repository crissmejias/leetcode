# Te dan un string s. 
# Devuelve el índice del primer carácter que aparece una sola vez en todo el string. Si no hay ninguno, devuelve -1.

def first_unique(word : str) -> int:
    hashmap = {}
    for char in word:
        hashmap[char] = hashmap.get(char,0) + 1
    for i, char in enumerate(word):
        if hashmap[char] == 1:
            return i
    return -1

print(first_unique("lovingleetcode"))
print(first_unique("example"))
print(first_unique("aa"))
print(first_unique("z"))


