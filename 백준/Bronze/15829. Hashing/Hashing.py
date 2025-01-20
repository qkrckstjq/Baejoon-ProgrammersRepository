# 입력 처리
L = int(input())  # 문자열 길이
string = input().strip()  # 해시를 계산할 문자열

# 상수값
r = 31
M = 1234567891

# 해시 계산
hash_value = 0
power = 1  # r^i 값을 저장

for i in range(L):
    char_value = ord(string[i]) - 96  # 'a'를 1로 변환
    hash_value = (hash_value + char_value * power) % M
    power = (power * r) % M  # r^i 값을 갱신하며 모듈러 연산

print(hash_value)
