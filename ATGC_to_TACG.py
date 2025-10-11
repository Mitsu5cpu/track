def dna_complement(sequence):
    translation_table = str.maketrans('ATGC', 'TACG')
    return sequence.upper().translate(translation_table)

dna_seq_mixed = "Replace this with input coding strand"

complement2 = dna_complement(dna_seq_mixed)


print(f"Original (mixed case): {dna_seq_mixed}")
print(f"Complement: {complement2}")
