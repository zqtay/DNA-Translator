def DNAtoAA(DNA):

  DNAtoAAdict = {"GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A","CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R","AAT":"N", "AAC":"N","GAT":"D", "GAC":"D","TGT":"C", "TGC":"C","CAA":"Q", "CAG":"Q","GAA":"E", "GAG":"E","GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G","CAT":"H", "CAC":"H","ATT":"I", "ATC":"I", "ATA":"I","ATG":"M","TTA":"L", "TTG":"L", "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L","AAA":"K", "AAG":"K","TTT":"F", "TTC":"F","CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P","TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S", "AGT":"S", "AGC":"S","ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T","TGG":"W","TAT":"Y", "TAC":"Y","GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V","TAA":"*", "TGA":"*", "TAG":"*"}

  DNA="".join(DNA.split()).upper()

  if len(DNA)%3 == 0:
    codons=[]
    i=0
    aa=[]
    while i < len(DNA):
      codons.insert(len(codons),DNA[i:i+3])
      i=i+3

    for codon in codons:
      aa.insert(len(aa),DNAtoAAdict[codon])
    
    return "".join(aa)
  else:
    print("DNA sequence incomplete!")


exampleDNA = "atgctg tcgtaa"

print(DNAtoAA(exampleDNA))