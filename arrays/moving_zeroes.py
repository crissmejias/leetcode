input = [0,1,0,3,12]

def solution(input:list[int]) -> list[int]:
    write = 0
    for i,n in enumerate(input):
        if n != 0:
            input[i], input[write] = input[write], input[i]
            write += 1
    return input 
print(solution(input))