def compare(ref, seq):
    mutations = []
    i = j = 0
    pos = 1
    while i < len(ref) and j < len(seq):
        if ref[i].upper() != seq[j].upper():
            mutations.append((pos, ref[i].upper(), seq[j].upper(), 'substitution'))
        i += 1
        j += 1
        pos += 1
    while i < len(ref):
        mutations.append((pos, ref[i].upper(), '-', 'deletion'))
        i += 1
        pos += 1
    while j < len(seq):
        mutations.append((pos, '-', seq[j].upper(), 'insertion'))
        j += 1
        pos += 1
    return mutations

def summarize(mutations, length):
    for pos, ref_base, seq_base, mtype in mutations:
        print(f"{pos} {mtype.upper()} {ref_base}>{seq_base}")
    print(f"Total: {len(mutations)}")
    print(f"Ratio: {(len(mutations)/length)*100:.2f}%")

def main():
    ref = input().strip()
    seq = input().strip()
    mutations = compare(ref, seq)
    summarize(mutations, len(ref))

if __name__ == "__main__":
    main()
