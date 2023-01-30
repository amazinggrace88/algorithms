# 크기가 작은 부분 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/147355

"""
# 문제 해결 과정
- 문자열의 길이를 p 라고 설정을 하고, for loop 로 풀었음
"""
## first try : +4점 ! Yay
def solution(t, p):
    count = 0
    len_p = len(p)
    for i in range(0, len(t)-len(p)+1):
        if t[i:i+len_p] <= p:
            count += 1
    return count

  
# 아주 짧게 .. 
def solution(t, p):
    return len([t[i:i+len(p)] for i in range(0, len(t) - len(p) + 1) if t[i:i+len(p)] <= p])
