NM = input().split(" ")
site_number = int(NM[0])
hope_find_pw = int(NM[1])

site_password = {}

for i in range(site_number):
    s_w = input().split(" ")
    site = s_w[0]
    password = s_w[1]

    site_password[site] = password

for i in range(hope_find_pw):
    site = input()
    print(site_password[site])

