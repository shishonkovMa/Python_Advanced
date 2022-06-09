stra, strb = input().split(), input().split()

print(*list(map(lambda x: int(stra[x]) ^ int(strb[x]), range(len(stra)))))

# stra, strb = ''.join(input().split()), ''.join(input().split())
#
# print(*[int(a, 16) ^ int(b, 16) for a, b in zip(stra, strb)])