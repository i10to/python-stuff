#Create a function which translates a given DNA string into RNA.
#for example:
#"GCAT"  =>  "GCAU"
#The input string can be of arbitrary length - in particular, it may be empty. 
#All input is guaranteed to be valid, i.e. 
#each input string will only ever consist of 'G', 'C', 'A' and/or 'T'.

def dna_to_rna(dna):
    if 'G' in dna or 'C' in dna or 'A' in dna or 'T' in dna:
        if 'T' in dna:
            dna = dna.replace('T','U') #the replace function is to change the values inside a variable

    else:
        return None
    
    return dna

