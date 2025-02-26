import struct
import math

def f2mf_v1(va: str, nbmant: int, nbexpo: int) -> int:
    """
    Função para converter um número float para o formato digital de ponto flutuante,
    suporta 32 e 16 bits
    """

    f = float(va)
    nbits = nbmant + nbexpo + 1
    
    if f == 0.0:
        return 1 << (nbmant + nbexpo - 1)
    
    # Converte float para representação IEEE 754 (bits)
    if(nbits == 16):
        ifl = struct.unpack('>H', struct.pack('>e', f))[0]
        mant_ref = 10

    elif(nbits == 32):
        ifl = struct.unpack('!I', struct.pack('!f', f))[0]
        mant_ref = 23


    # Desempacotando IEEE 754
    s = (ifl >> (nbmant + nbexpo)) & 0x1  # Bit de sinal
    e = ((ifl >> nbmant) & ((1 << nbexpo) - 1)) - ((1 << (nbexpo - 1)) - 1) - (nbmant - 1)  # Expoente ajustado
    m = ((ifl & ((1 << nbmant) - 1)) + (1 << nbmant)) >> 1  # Mantissa ajustada

    # # Sinal
    s = s << (nbmant + nbexpo)
    
    # # Expoente
    e = e + (mant_ref - nbmant)
    sh = 0
    
    while e < -math.pow(2, nbexpo - 1):
        e += 1
        sh += 1
    
    e = e & (int(math.pow(2, nbexpo)) - 1)
    e = e << nbmant
    
    # Mantissa
    if nbmant == mant_ref:
        if ifl & 0x1:
            m += 1  # Arredonda
    else:
        sh = mant_ref - nbmant + sh
        carry = (m >> (sh - 1)) & 0x1
        m = m >> sh
        if carry:
            m += 1  # Arredonda
    
    return s + e + m

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



def mf2f(val: int , nbmant: int, nbexpo: int) -> float:
    """
    Função para converter o formato de ponto flutuante digital para float
    """
    
    s = (val >> (nbmant + nbexpo)) & 0x1
    e = (val >> nbmant) & ((1 << nbexpo) - 1)
    m = val & ((1 << nbmant) - 1)

    if e & (1 << nbexpo - 1):
        e_complemented = -((~e + 1) & (1 << nbexpo) - 1)
    else:
        e_complemented = e

    value = math.pow(-1, s) * m * math.pow(2, e_complemented)

    return value

def read_file(path:str, nb_mantissa:int, nb_expo:int):

    values_out = []

    with open(path, "r") as file:
        data = [int(linha.strip(), 16)for linha in file]  # Remove espaços e quebras de linha


    for i in range(len(data)):
        values_out.append(mf2f(data[i], nb_mantissa, nb_expo))

    return values_out
