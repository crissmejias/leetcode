'''
Tenemos una lista de palabras, debemos agruparlas en listas de anagramas.

Ejemplo:

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
→ [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
'''

def group_anagrams(strs : list[str]) -> list[list[str]]:
    hashmap = {}
    for word in strs:
        sorted_str_list = sorted(word)
        sorted_str = "".join(sorted_str_list)
        hashmap.setdefault(sorted_str,[]).append(word)
    return list(hashmap.values())
        
print(group_anagrams([""]))                                    # [['']]
print(group_anagrams(["a"]))                                   # [['a']]
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]