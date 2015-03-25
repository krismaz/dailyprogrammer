#Nim 0.10.2
import strutils, future, tables

var
    input =  stdin.readLine.split #Slight preprocessing
    lookup = initTable[string, string] (64)
    chars =  {"A":"T", "T":"A", "G":"C", "C":"G"}.toTable()

echo input.map((x:string) =>chars[x]).join " " #Well that's nice


const #Glorious dataz
    codons ="Ala   GCT, GCC, GCA, GCG-Leu   TTA, TTG, CTT, CTC, CTA, CTG-Arg   CGT, CGC, CGA, CGG, AGA, AGG-Lys   AAA, AAG-Asn   AAT, AAC-Met   ATG-Asp   GAT, GAC-Phe   TTT, TTC-Cys   TGT, TGC-Pro   CCT, CCC, CCA, CCG-Gln   CAA, CAG-Ser   TCT, TCC, TCA, TCG, AGT, AGC-Glu   GAA, GAG-Thr   ACT, ACC, ACA, ACG-Gly   GGT, GGC, GGA, GGG-Trp   TGG-His   CAT, CAC-Tyr   TAT, TAC-Ile   ATT, ATC, ATA-Val   GTT, GTC, GTA, GTG-STOP   TAA, TGA, TAG"

for line in codons.split "-": #Build table from string, to avoid sting searching
    var 
        ss = line.split "   " #I really should let the the compiler do the by common subexpression
    for result in ss[1].split ", ":
        lookup[result] = ss[0]

for i in countup(0, input.len-3, 3): #Do codon lookup
    stdout.write lookup[ input[i] & input[i+1] & input[i+2]], " "