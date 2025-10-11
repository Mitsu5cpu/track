def check_dna_complement(strand1, strand2):
    """
    Check if two DNA strands are complementary and highlight anomalies
    """
    complement_map = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    
    # Check if strands are of equal length
    if len(strand1) != len(strand2):
        print("Error: Strands must be of equal length!")
        return
    
    print(f"Strand 1: {strand1}")
    print(f"Strand 2: {strand2}")
    print("Checking complementarity...")
    print()
    
    anomalies = []
    position_details = []
    
    for i in range(len(strand1)):
        base1 = strand1[i].upper()
        base2 = strand2[i].upper()
        
        expected_base2 = complement_map.get(base1, '?')
        
        if base2 == expected_base2:
            position_details.append(f"Position {i+1}: {base1} - {base2} ✓")
        else:
            position_details.append(f"Position {i+1}: {base1} - {base2} ✗ (expected {expected_base2})")
            anomalies.append(i)
    
    # Display all positions
    for detail in position_details:
        print(detail)
    
    print("\n" + "="*50)
    
    # Display strands with highlighted anomalies
    if anomalies:
        print("ANOMALIES DETECTED!")
        print(f"Number of anomalies: {len(anomalies)}")
        print(f"Anomaly positions: {[pos+1 for pos in anomalies]}")
        print()
        
        # Create highlighted output
        strand1_highlighted = ""
        strand2_highlighted = ""
        
        for i in range(len(strand1)):
            if i in anomalies:
                strand1_highlighted += f"[{strand1[i]}]"
                strand2_highlighted += f"[{strand2[i]}]"
            else:
                strand1_highlighted += strand1[i]
                strand2_highlighted += strand2[i]
        
        print("Strand 1 with anomalies highlighted:")
        print(strand1_highlighted)
        print("Strand 2 with anomalies highlighted:")
        print(strand2_highlighted)
    else:
        print("✓ Perfect complementarity! All base pairs match correctly.")

# Get input from user
print("DNA Strand Complementarity Checker")
print("=" * 40)
strand1 = input("Enter first DNA strand: ").upper()
strand2 = input("Enter second DNA strand: ").upper()

print("\n" + "="*50)
check_dna_complement(strand1, strand2)
