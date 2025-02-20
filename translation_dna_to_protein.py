from Bio.Seq import Seq

def translate_dna_to_protein(dna_sequence):
    dna_seq = Seq(dna_sequence)
    protein_seq = dna_seq.translate()
    return str(protein_seq)

# Example: 21 nucleotide sequence (7 amino acids)
dna_sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
protein = translate_dna_to_protein(dna_sequence)
print(f"Protein sequence: {protein}")

Protein sequence: MAIVMGR*KGAR*
