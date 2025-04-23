import sys
import math

def main():
    # 입력
    s0, X, M, D, K = map(int, sys.stdin.readline().split())

    # 주기길이는 M/gcd(X,M)이고, 이 수열에서 최대값은 (M - g + (s0 % g))
    g = math.gcd(X, M)
    r = s0 % g
    max_s = M - g + r

    # 모든 s_i가 0인 경우(별이 전혀 떨어지지 않음)
    if max_s == 0:
        print(0)
        return

    # 청소 없이 버틸 수 있는 최대 일수
    R = K // max_s

    # D일을 커버하기 위한 최소 청소 횟수
    # 초기 상태는 깨끗하므로 첫 구간 전 청소는 필요 없음
    cleans = (D - 1) // R
    print(cleans)

if __name__ == "__main__":
    main()