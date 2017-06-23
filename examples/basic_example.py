from geneblocks import BlocksFinder
from geneblocks.biotools import reverse_complement, random_dna_sequence

C1, A, B, C2, C3, D, E, F = [random_dna_sequence(100 * L) for L in range(1, 9)]

sequences = {
    "a": C1 + A + C2,
    "b": B + D + C2 + C3,
    "c": E + C1 + C2,
    "d": C2 + C1 + F + C3,
    "e": C3 + reverse_complement(C2 + C1)
}

blocks_finder = BlocksFinder(sequences)
axes = blocks_finder.plot_common_blocks()
axes[0].figure.savefig("basic_example.png", bbox_inches="tight")
