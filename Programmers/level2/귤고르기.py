#귤고르기
# https://school.programmers.co.kr/learn/courses/30/lessons/138476

"""
문제해결과정
1. counter 로 중복된 귤의 수를 셈 (most_common - counter 를 sorting 해주는 
2. k 를 삭제하면서 for loop 를 진행
3. 예외처리 - k 가 귤의 수와 같을 때에는 최소의 의미가 없으므로 set 의 길이로 처리
"""

def solution(k, tangerine):
    from collections import Counter
    if k == len(tangerine):
        return len(set(tangerine))
    else:
        tan_cnt = Counter(tangerine).most_common()
        keys_list = []
        for key, value in tan_cnt:
            k -= value
            keys_list.append(key)
            if k <= 0:
                return len(keys_list)
              

              
if __name__ == '__main__':
    k = 4
    tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
    answer = solution(k, tangerine)
    print(answer)
