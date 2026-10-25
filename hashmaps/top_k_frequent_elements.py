'''
Tenemos una lista de nums y un entero `k`, 

Devolver los k elementos que más se repiten en cualquier orden.

Ejemplo:
nums = [1, 1, 1, 2, 2, 3], k = 2  →  [1, 2]

'''

def top_k_frequent(nums : list[int],k : int) -> list[int]:
    # Iteramos por cada elemento de la lista y lo agregamos como key al hashmap
    hashmap = {}
    for num in nums:
        hashmap[num] = hashmap.get(num,0) + 1 # Sumaremos uno por cada vez que lo encontremos
    sorted_hashmap = sorted(hashmap, key=hashmap.get,reverse=True) # Ordenamos el hashmap por el orden del value (devuelve una lista)
    return sorted_hashmap[:k] # Hacemos un slice de la lista hasta el valor `k` 

print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))   # [1, 2]
print(top_k_frequent([1], 1))                  # [1]
print(top_k_frequent([4, 4, 4, 5, 5, 6], 1))   # [4]
print(top_k_frequent([1, 2, 3], 3))            # [1, 2, 3] (todos con conteo 1, cualquier orden)
print(top_k_frequent([-1, -1, 2], 1))          # [-1] (negativos también valen)
print(top_k_frequent([7, 7, 8, 8, 9], 2))      # [7, 8] o [8, 7]