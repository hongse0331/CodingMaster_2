def solution(arr):

    answer = []

    for i in range(len(arr)):

        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])
    
    return answer

a= solution([1,1,3,3,0,1,1])
b= solution([4,4,4,3,3])

print(a)
print(b)