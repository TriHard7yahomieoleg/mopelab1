import random

a0 = 1
a1 = 4
a2 = 3
a3 = 2
n = 20
y = [0] * 8
x1 = [0] * 8
x2 = [0] * 8
x3 = [0] * 8
for i in range(8):
    x1[i] = round(random.random() * n, 2)
    x2[i] = round(random.random() * n, 2)
    x3[i] = round(random.random() * n, 2)
    y[i] = round(a0 + a1 * x1[i] + a2 * x2[i] + a3 * x3[i], 2)
x01 = round((max(x1) + min(x1)) / 2, 2)
x02 = round((max(x2) + min(x2)) / 2, 2)
x03 = round((max(x3) + min(x3)) / 2, 2)
dx1 = round(x01 - min(x1), 2)
dx2 = round(x02 - min(x2), 2)
dx3 = round(x03 - min(x3), 2)
Xn1 = [round((x1[i] - x01) / dx1, 2) for i in range(8)]
Xn2 = [round((x2[i] - x02) / dx2, 2) for i in range(8)]
Xn3 = [round((x3[i] - x03) / dx3, 2) for i in range(8)]
Yet = a0 + a1 * x01 + a2 * x02 + a3 * x03
for i in range(8):
    print(
        "{:<6} {:<6} {:<6} {:<12} {:<5} {:<9} {:<6} {:<9} {:<6} {:<9} {:<6} {:<9}".format(
            i + 1,
            x1[i],
            x2[i],
            x3[i],
            "Y"+str(i+1)+":",
            y[i],
            "Xn1" + "-"+str(i + 1) + ":",
            round(Xn1[i], 2),
            "Xn2" + "-"+str(i + 1) + ":",
            round(Xn2[i], 2),
            "Xn3" + "-"+str(i + 1) + ":",
            round(Xn3[i], 2),
        )
    )
print("\n{:<5} {:<5} {:<5} {:<5}".format("x0", x01, x02, x03))
print("{:<5} {:<5} {:<5} {:<5}\n".format("dx", dx1, dx2, dx3))
print("y: "+str(y))
print("\nY_et = "+str(Yet))
Ymax=round(max(y),2)
print("Y_max = "+str(Ymax))
i = y.index(max(y))
print("Index_y = " + str(i+1))
print(x1[i], x2[2], x3[i])
print(round(Xn1[i], 4), round(Xn2[i], 4),  round(Xn3[i], 4))
