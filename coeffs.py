from funcoes import f2mf
import math

nbmant = 23
nbexpo = 8

Zn1 = [-0.0030]
Zd1 = [1.0000, -0.9978]

Zn2 = [0.7264,    0.4282]
Zd2 = [1.0000,    1.0489,    0.2886]

Zn3 = [-3.2489,   -0.3488]
Zd3 = [1.0000,   -0.0280,    0.1635]

Zn4 = [2.5889]
Zd4 = [1.0000,   -0.3644]

Zn5 = [-0.0635]
Zd5 = [1.0000,   -9.8459e-04]

Zn6 = [1.0494e-04]
Zd6 = [1.0000,   -3.3924e-13]

def inverter_primeiro_bit(num: int, num_bits: int) -> int:
    mask = 1 << (num_bits - 1)  # Cria uma máscara com o primeiro bit ligado
    return num ^ mask  # Inverte o primeiro bit com XOR

# Conversao
b0_1 = f2mf(Zn1[0], nbmant, nbexpo)
a1_1 = f2mf(Zd1[1], nbmant, nbexpo)
a1_1neg = inverter_primeiro_bit(a1_1, 32)

b0_2 = f2mf(Zn2[0], nbmant, nbexpo)
b1_2 = f2mf(Zn2[1], nbmant, nbexpo)
a1_2 = f2mf(Zd2[1], nbmant, nbexpo)
a2_2 = f2mf(Zd2[2], nbmant, nbexpo)
a1_2neg = inverter_primeiro_bit(a1_2, 32)
a2_2neg = inverter_primeiro_bit(a2_2, 32)

b0_3 = f2mf(Zn3[0], nbmant, nbexpo)
b1_3 = f2mf(Zn3[1], nbmant, nbexpo)
a1_3 = f2mf(Zd3[1], nbmant, nbexpo)
a2_3 = f2mf(Zd3[2], nbmant, nbexpo)
a1_3neg = inverter_primeiro_bit(a1_3, 32)
a2_3neg = inverter_primeiro_bit(a2_3, 32)

b0_4 = f2mf(Zn4[0], nbmant, nbexpo)
a1_4 = f2mf(Zd4[1], nbmant, nbexpo)
a1_4neg = inverter_primeiro_bit(a1_4, 32)

b0_5 = f2mf(Zn5[0], nbmant, nbexpo)
a1_5 = f2mf(Zd5[1], nbmant, nbexpo)
a1_5neg = inverter_primeiro_bit(a1_5, 32)

b0_6 = f2mf(Zn6[0], nbmant, nbexpo)
a1_6 = f2mf(Zd6[1], nbmant, nbexpo)
a1_6neg = inverter_primeiro_bit(a1_6, 32)

# Print dos coeficientes

print("\n-------- IIR 1 coeffs --------")
print("b0:  " + hex(b0_1))
print("a1:  " + hex(a1_1))
print("-a1: " + hex(a1_1neg))

print("\n-------- IIR 2 coeffs --------")
print("b0: " + hex(b0_2))
print("b1: " + hex(b1_2))
print("a1: " + hex(a1_2))
print("a2: " + hex(a2_2))
print("-a1: " + hex(a1_2neg))
print("-a2: " + hex(a2_2neg))

print("\n-------- IIR 3 coeffs --------")
print("b0: " + hex(b0_3))
print("b1: " + hex(b1_3))
print("a1: " + hex(a1_3))
print("a2: " + hex(a2_3))
print("-a1: " + hex(a1_3neg))
print("-a2: " + hex(a2_3neg))

print("\n-------- IIR 4 coeffs --------")
print("b0: " + hex(b0_4))
print("a1: " + hex(a1_4))
print("-a1: " + hex(a1_4neg))

print("\n-------- IIR 5 coeffs --------")
print("b0: " + hex(b0_5))
print("a1: " + hex(a1_5))
print("-a1: " + hex(a1_5neg))

print("\n-------- IIR 6 coeffs --------")
print("b0: " + hex(b0_6))
print("a1: " + hex(a1_6))
print("-a1: " + hex(a1_6neg))

# valor, mantissa, expoente = mf2f(a1_1, nbmant, nbexpo)

# print(f"Mantisssa (int): {int(mantissa)}")
# print(f"Expoente: {expoente}")
# print(f"Valor de Retorno: {mantissa * math.pow(2, expoente)}")

