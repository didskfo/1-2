def solution(num):
    return sum([int(i) for i in str(num)])

# def solution(num):
#     num_sum = 0
#     for i in str(num):
#         num_sum += int(i)
#     return num_sum

print(solution(5923)) #19
print(solution(200)) # 2
print(solution(1234567890)) #45
print(solution(2364759387)) #54
