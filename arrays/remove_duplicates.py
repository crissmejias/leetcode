nums = [0, 0, 1, 1, 1, 2, 2, 3]

def solution(nums:list[int]) -> int:
    write = 1
    for i,read in enumerate(nums):
        if read != nums[write-1]:
            nums[write] = read
            write += 1
    return write
print(solution(nums))


