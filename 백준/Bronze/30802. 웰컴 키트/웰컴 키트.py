N = int(input())
S, M, L, XL, XXL, XXXL = map(int, input().split())
T, P = map(int, input().split())

total_tshirt_bundles = 0
for demand in [S, M, L, XL, XXL, XXXL]:
    total_tshirt_bundles += (demand // T) + (1 if demand % T != 0 else 0)

max_pen_bundles = N // P
remaining_pens = N % P

print(total_tshirt_bundles)
print(max_pen_bundles, remaining_pens)
