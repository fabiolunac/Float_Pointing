from funcoes import f2mf, mf2f
import math

nbmant = 23
nbexpo = 8

# Numerador
Znti = [4.294341492410895e-23,
            2.410259936829204e-09,
                1.361884841455440e-08,
                    -4.120546556616038e-09,
                        -9.988893287934183e-09,
                            -1.906299572480522e-09,
                                -1.381565400439083e-11,
                                    -2.560176577052387e-17,
                                                            0]

# Denominador
Zdti = [1.444400000000000e-08,
          -4.944897983017996e-09,
              -8.723804374709209e-09,
                  -5.868442605271617e-10,
                      -3.124085233920797e-10,
                          -6.992432687036571e-11,
                              2.478522822801157e-10,
                                    -2.439636477041001e-13,
                                        8.276140953857137e-26]

b = [0] * (len(Znti) - 1)
a = [0] * (len(Znti) - 1)

a0 = Zdti[0]
Znti_norm = [b / a0 for b in Znti]
Zdti_norm = [a / a0 for a in Zdti]

print(Znti_norm)
print(Zdti_norm)

#Calculo do b
for i in range(0, len(Znti) - 1):
    b[i] = f2mf(Znti_norm[i], nbmant, nbexpo)

#Calculo do a
for i in range(0, len(Znti) - 1):
    a[i] = f2mf(Zdti_norm[i], nbmant, nbexpo)




# #Print
# print("------ b ------")
# for i in range(len(b)):
#     print(f"b_{i}: {hex(b[i])}")

# print("------ a ------")
# for i in range(len(a)):
#     print(f"a_{i+1}: {hex(a[i])}")