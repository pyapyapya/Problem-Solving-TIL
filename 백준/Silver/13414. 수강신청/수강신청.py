import sys
input = sys.stdin.readline

k, l = map(int, input().split(" "))
su_dict = {}

for idx in range(l):
    su = input().strip()
    su_dict[su] = idx
su_list = sorted(su_dict.items(), key=lambda x: x[1])
for k, v in su_list[:k]:
    sys.stdout.write(k + "\n")
