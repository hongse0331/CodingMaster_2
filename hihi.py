def solution(s):
    answer = ''
    
    
    i = len(s)//2
     
    if (len(s) % 2) == 0:
        s[i:i+2] = answer
    elif (len(s) % 2) == 1:
        s[i] = answer 
    
    
    return answer

a = solution("abcde")

print(a)