"""Main module."""

def count_gc(seq):
    """Count GC content in a sequence."""
    seq = seq.upper()
    return (seq.count('G') + seq.count('C')) / len(seq)
