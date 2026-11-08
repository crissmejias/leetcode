nums = [1,2,3,4]

def solution(nums:list[int])->list[int]:
    new_array= []
    array_sum = 0
    for n in nums:
        array_sum += n
        new_array.append(array_sum)
    return new_array

