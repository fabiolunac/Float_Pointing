import struct
import math

def f2mf(va: str, nbmant: int, nbexpo: int) -> int:
    f = float(va)
    
    if f == 0.0:
        return 1 << (nbmant + nbexpo - 1)
    
    # Converte float para representação IEEE 754 (bits)
    ifl = struct.unpack('!I', struct.pack('!f', f))[0]
    
    # Desempacotando IEEE 754
    s = (ifl >> 31) & 0x00000001
    e = ((ifl >> 23) & 0xFF) - 127 - 22
    m = ((ifl & 0x007FFFFF) + 0x00800000) >> 1
    
    # Sinal
    s = s << (nbmant + nbexpo)
    
    # Expoente
    e = e + (23 - nbmant)
    sh = 0
    
    while e < -math.pow(2, nbexpo - 1):
        e += 1
        sh += 1
    
    e = e & (int(math.pow(2, nbexpo)) - 1)
    e = e << nbmant
    
    # Mantissa
    if nbmant == 23:
        if ifl & 0x00000001:
            m += 1  # Arredonda
    else:
        sh = 23 - nbmant + sh
        carry = (m >> (sh - 1)) & 0x00000001
        m = m >> sh
        if carry:
            m += 1  # Arredonda
    
    return s + e + m



def mf2f(in_val: int , nbmant: int, nbexp: int) -> float:
    # Extraindo os campos da entrada
    s = (in_val >> (nbmant + nbexp)) & 1  # Sinal
    e = (in_val >> nbmant) & ((1 << nbexp) - 1)  # Expoente
    m = in_val & ((1 << nbmant) - 1)  # Mantissa

    # Convertendo a mantissa para signed
    sm = -m if s else m

    # Complemento a dois para o expoente
    if e & 0x80:  # Se o bit mais significativo (MSB) for 1, é negativo
        e_complemented = -((~e + 1) & 0xFF)
    else:
        e_complemented = e

    num_output = sm * math.pow(2, e_complemented)

    return num_output, sm, e_complemented

def read_file(path:str, nb_mantissa:int, nb_expo:int):

    values_out = []

    with open(path, "r") as file:
        data = [int(linha.strip(), 16)for linha in file]  # Remove espaços e quebras de linha


    for i in range(len(data)):
        values_out.append(mf2f(data[i], nb_mantissa, nb_expo))

    return values_out