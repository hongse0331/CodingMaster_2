def solution(answers):
    answer = []
    count = [0,0,0]
    answers = answers*8
    
    supo_1 = [1,2,3,4,5]*8
    supo_2 = [2,1,2,3,2,4,2,5]*5
    supo_3 = [3,3,1,1,2,2,4,4,5,5]*4
    
    for i in range(40):
        if answers[i] == supo_1[i]:
            count[0] += 1
        if answers[i] == supo_2[i]:
            count[1] += 1
        if answers[i] == supo_3[i]:
            count[2] += 1


    for i in range(3):
        if count[i] == max(count):
            answer.append(i+1)



    return answer