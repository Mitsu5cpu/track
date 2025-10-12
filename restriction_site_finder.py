def find_genetic_patterns(sequence, pattern):
    """Find all occurrences of a genetic pattern in DNA sequence"""
    positions = []
    pattern = pattern.upper()
    sequence = sequence.upper()
    
    # Validate that pattern contains only valid DNA nucleotides
    valid_nucleotides = {'A', 'T', 'G', 'C'}
    if not all(nuc in valid_nucleotides for nuc in pattern):
        return None, "Error: Restriction site contains invalid DNA nucleotides"
    
    if len(pattern) == 0:
        return None, "Error: Restriction site cannot be empty"
    
    if len(pattern) > len(sequence):
        return None, "Error: Restriction site is longer than DNA sequence"
    
    for i in range(len(sequence) - len(pattern) + 1):
        if sequence[i:i+len(pattern)] == pattern:
            positions.append(i)
    
    return positions, None

def main():
    print("DNA Restriction Site Finder")
    print("=" * 40)
    
    # Get input from user
    dna_sequence = input("Enter DNA sequence: ").strip()
    restriction_site = input("Enter restriction site to find: ").strip()
    
    if not dna_sequence:
        print("Error: DNA sequence cannot be empty")
        return
    
    if not restriction_site:
        print("Error: Restriction site cannot be empty")
        return
    
    # Find restriction enzyme sites
    sites, error = find_genetic_patterns(dna_sequence, restriction_site)
    
    if error:
        print(f"\n{error}")
        return
    
    # Display results
    print("\n" + "=" * 50)
    print("RESULTS:")
    print(f"DNA Sequence: {dna_sequence}")
    print(f"Sequence length: {len(dna_sequence)} bases")
    print(f"Restriction Site: {restriction_site}")
    print(f"Restriction site length: {len(restriction_site)} bases")
    print(f"Restriction sites found at positions: {sites}")
    print(f"Number of sites found: {len(sites)}")
    
    # Show the sequence with highlighted sites
    if sites:
        print(f"\nSequence with '{restriction_site}' sites highlighted:")
        highlighted_sequence = ""
        last_pos = 0
        
        for pos in sites:
            # Add sequence before the restriction site
            highlighted_sequence += dna_sequence[last_pos:pos]
            # Add highlighted restriction site
            highlighted_sequence += "[" + dna_sequence[pos:pos+len(restriction_site)] + "]"
            last_pos = pos + len(restriction_site)
        
        # Add remaining sequence
        highlighted_sequence += dna_sequence[last_pos:]
        print(highlighted_sequence)
    else:
        print(f"\nNo restriction sites '{restriction_site}' found in the DNA sequence.")

# Run the program
if __name__ == "__main__":
    main()
