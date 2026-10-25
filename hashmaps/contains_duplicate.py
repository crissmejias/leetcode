# Tenemos una lista nums. Devolver true si algún valor aparece al menos dos veces y False si todos son distintos.

def contains_duplicate(nums : list[int]) -> bool:
    nums_set= set()
    for num in nums:
        if num in nums_set:
            return True
        nums_set.add(num)
    return False

# Pruebas
print(contains_duplicate([1,2,3,1,5]))
# True

print(contains_duplicate([1,2,3,4,5]))
#False

print(contains_duplicate([]))
#False