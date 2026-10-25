# Tenemos una lista de números y un target. Debemos devolver los índices de los números que sumados nos devuelvan el target
nums = [2,7,11,15]
target = 9
# Respuesta esperada [0,1]
def two_sum(nums : list[int], target : int):
    nums_dict = {}
    for i, num in enumerate(nums):
        complement =  target - num
        if complement in nums_dict:
            return [nums_dict[complement], i]
        nums_dict[num] = i
    return None

print(two_sum(nums, target))
# [0,1]

print(two_sum([3,3],6))
# [0,1]

print(two_sum([3,2,4],6))
# [1,2]