import math

# print("result:" + math.exp(0))

print("math.exp(-45.17) : ", math.exp(-45.17))
# 《人工智能导论》P142
w = 0.1
am = 0.6931
yi = 1
gm = 1
Z = (math.exp(-am) * 8 + math.exp(am) * 2) * 0.1
wrong = 0.1 * math.exp(-am) / Z
right = 0.1 * math.exp(am) / Z
print("Z: %.4f" % Z)
print("wrong: %.4f" % wrong)
print("right: %.4f" % right)

print("-----")

mit_a1 = 0.5 * math.log(((1 - 0.3) / 0.3))
print("mit_a1 : %.4f" % mit_a1)

mit_zm = math.exp(-mit_a1) * 7 + math.exp(mit_a1) * 3
print("mit_zm : %.4f" % mit_zm)
mit_zm2 = 0.1*math.exp(-mit_a1) * 7 + 0.1*math.exp(mit_a1) * 3
print("mit_zm2 : %.4f" % mit_zm2)

mit_wrong_1 = 0.1*math.exp(-mit_a1) / mit_zm2

mit_right_1 = 0.1*math.exp(mit_a1) / mit_zm2

print("mit_wrong_1 : %.8f" % mit_wrong_1)
print("mit_right_1 : %.8f" % mit_right_1)

mit_err2 = mit_wrong_1 * 3
print("mit_err2 : %.8f" % mit_err2)

mit_a2 = 0.5 * math.log((1 -mit_err2) / mit_err2)
print("mit_a2 : %.6f" % mit_a2)

