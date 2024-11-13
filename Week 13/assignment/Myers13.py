from random import randint
from typing import Tuple

nucleotides = ("A", "T", "C", "G")
complement_dict = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

def count_nucleotides(sequence):
    # (A_count, T_count, C_count, G_count)
    return sequence.count("A"), sequence.count("T"), sequence.count("C"), sequence.count("G")

def find_complement(sequence):
    return tuple(complement_dict[item] for item in sequence)

def slice_dna(sequence, start, end):
    return sequence[start:end]

def gc_content(sequence):
    counts = count_nucleotides(sequence)
    g_c_count = counts[2] + counts[3]
    total = sum(counts)
    return (g_c_count / total) * 100

def mutate(sequence):
    random_index = randint(0, len(sequence) - 1)
    ar = list(sequence)
    ar[random_index] = nucleotides[randint(0, len(nucleotides) - 1)]
    return tuple(ar)


def main():
    # generates a random dna sequence for testing
    dna_sequence = tuple(nucleotides[randint(0, 3)] for i in range(20))

    print("Sequence: ", dna_sequence)
    print("")
    print("Counts: (A, T, C, G): ", count_nucleotides(dna_sequence))
    print("Complement: ", find_complement(dna_sequence))
    print("Sliced DNA (1-3): ", slice_dna(dna_sequence, 1, 4))
    print("GC content: ", gc_content(dna_sequence))
    print("Mutated: ", mutate(dna_sequence))
    print("")
    print("Original Sequence: ", dna_sequence)
if __name__ == "__main__":
    main()