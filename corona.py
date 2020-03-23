__author__ = "Hugo Drakeskär | 2020"

convertions = """
TTT F
TTC
TTA L
TTG
CTT
CTC
CTA
CTG
ATT I
ATC
ATA
ATG M
GTT V
GTC
GTA
GTG
TCT S
TCC
TCA
TCG
CCT P
CCC
CCA
CCG
ACT T
ACC
ACA
ACG
GCT A
GCC
GCA
GCG
TAT Y
TAC
TAA $
TAG
CAT H
CAC
CAA Q
CAG
AAT N
AAC
AAA K
AAG
GAT D
GAC
GAA E
GAG
TGT C
TGC
TGA $
TGG W
CGT R
CGC
CGA
CGG
AGA
AGG
AGT S
AGC
GGT G
GGC
GGA
GGG
"""
c_dict = {}
prev_acid = ""
for conv in convertions.split("\n"):
    combo = conv[:3]
    if len(conv) > 4:
        lett = conv[4:]
        prev_acid = lett
    elif len(combo) == 0:
        continue
    else:
        lett = prev_acid
    c_dict[combo] = lett

formatted_origin = ""
origin = open("./covid19_dna.txt", "r").read()
for dna_row in origin.split("\n"):
    letters = dna_row.split(" ")
    for dna_chunk in letters:
        if not any(char.isdigit() for char in dna_chunk) and dna_chunk != " ":
            formatted_origin += dna_chunk.upper()

formatted_origin = formatted_origin[2:]


def decode(dna, offset=0):
    dna = dna[offset:]
    acids = []
    chunks = [dna[x: x + 3] for x in range(len(dna)) if x % 3 == 0]
    acid = ""
    for i, chunk in enumerate(chunks):
        if len(chunk) == 3:
            if chunk in ["TAA", "TGA", "TAG"]:
                try:
                    index_m = acid.index("M")
                    true_acid = acid[index_m:]
                    if len(true_acid) < 40:
                        continue
                    start_index = i*3+4-len(true_acid)*3-(1-offset)
                    acids.append([start_index, true_acid])
                except:
                    pass

                acid = ""
            else:
                acid += c_dict[chunk]
    return acids

text0 = decode(formatted_origin, 0)
text1 = decode(formatted_origin, 1)
text2 = decode(formatted_origin, 2)
all_text = text0+text1+text2
all_text.sort()
h=0
