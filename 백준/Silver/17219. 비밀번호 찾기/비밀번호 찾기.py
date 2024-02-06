import sys

NM = sys.stdin.readline().split()
site_number = int(NM[0])
hope_find_pw = int(NM[1])

site_password = {}

for i in range(site_number):
    s_w = sys.stdin.readline().split()
    site = s_w[0]
    password = s_w[1].strip()  # 줄 바꿈 문자 제거

    site_password[site] = password

for i in range(hope_find_pw):
    site = sys.stdin.readline().strip()  # 줄 바꿈 문자 제거
    print(site_password[site])