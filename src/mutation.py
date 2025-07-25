def apply_mutation(sequence, protein_change):
    three_to_one = {
        'Ala':'A','Arg':'R','Asn':'N','Asp':'D','Cys':'C',
        'Gln':'Q','Glu':'E','Gly':'G','His':'H','Ile':'I',
        'Leu':'L','Lys':'K','Met':'M','Phe':'F','Pro':'P',
        'Ser':'S','Thr':'T','Trp':'W','Tyr':'Y','Val':'V',
        'Sec':'U','Pyl':'O','Asx':'B','Glx':'Z','Xle':'J','Ter':'*'
    }

    def convert(aa):
        if len(aa) == 1:
            return aa.upper()
        return three_to_one.get(aa.capitalize(), None)

    match = re.match(r'p\.([A-Za-z]{1,3})(\d+)([A-Za-z]{1,3})', protein_change)
    if not match:
        return None

    aa_orig, pos_str, aa_new = match.groups()
    pos = int(pos_str) - 1
    orig_aa = convert(aa_orig)
    new_aa = convert(aa_new)

    if orig_aa is None or new_aa is None:
        return None
    if pos >= len(sequence):
        return None
    if sequence[pos] != orig_aa:
        # Warn but still try to apply the mutation
        print(f"Warning: expected {orig_aa} at position {pos+1}, found {sequence[pos]}")

    return sequence[:pos] + new_aa + sequence[pos+1:]