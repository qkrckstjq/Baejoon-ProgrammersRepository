import re

# 패턴을 정규 표현식으로 정의
pattern = re.compile(r"(100+1+|01)+")

# 테스트 케이스 수 입력
T = int(input())

for _ in range(T):
    signal = input().strip()  # 각 테스트 케이스 전파 입력
    # 패턴에 매칭되면 "YES" 출력, 그렇지 않으면 "NO" 출력
    if pattern.fullmatch(signal):
        print("YES")
    else:
        print("NO")
