#Exercício 1
n1 = [108.304,100.827,67.992]
ca1 = [108.477,100.389,69.362]
c1 = [109.907,100.555,69.817]
o1 = [110.821,100.799,69.027]


n2 = [107.670,101.359,70.074]
ca2 = [108.477,100.389,69.362]
c2 = [109.513,101.011,68.450]
o2 = [110.667,100.572,68.425]


soma = (n1[0]-n2[0])**2+(n1[1]-n2[1])**2+(n1[2]-n2[2])**2
soma = soma+(ca1[0]-ca2[0])**2+(ca1[1]-ca2[1])**2+(ca1[2]-ca2[2])**2
soma = soma+(c1[0]-c2[0])**2+(c1[1]-c2[1])**2+(c1[2]-c2[2])**2
soma = soma+(o1[0]-o2[0])**2+(o1[1]-o2[1])**2+(o1[2]-o2[2])**2


rmsd = ((1/4)*soma)**1/2
print("\nO valor de RMSD é:",rmsd)

#Exercício 2

seqA = "ATGATCTCGTAATTAACCGGAATTTTGGGCC"
#Saída esperada: 41.93

tam = len(seqA)
qtde = seqA.count("C")
qtde = qtde+seqA.count("G")
perc = (qtde/tam)*100
print("Percentual A:", perc)

seqB = "GGCCTTAAGTTTAACCCGGAATTTAAAGGCCCCAAA"
#Saída esperada: 44.44 

tam = len(seqB)
qtde = seqB.count("C")
qtde = qtde+seqB.count("G")
perc = (qtde/tam)*100
print("Percentual B:", perc)