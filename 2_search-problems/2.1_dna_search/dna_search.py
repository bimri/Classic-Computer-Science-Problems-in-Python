"DNA search"

"""
Genes are commonly represented in computer software as a sequence of the characters
A, C, G, and T. Each letter represents a nucleotide, and the combination of
three nucleotides is called a codon. A codon codes for a specific amino acid that together with other amino acids can form a protein.
A classic task in bioinformatics software is to find a particular codon within a gene.
"""

# We can represent a nucleotide as a simple IntEnum with four cases.
from enum import Flag, IntEnum
from typing import Tuple, List

'''
Nucleotide is of type IntEnum instead of just Enum, because IntEnum gives us comparison
operators (<, >=, and so on) “for free.” Having these operators in a data
type is required in order for the search algorithms we are going to implement to be
able to operate on it. Tuple and List are imported from the typing package to
assist with type hints.
'''
Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))


'''
Codons can be defined as a tuple of three Nucleotides. A gene may be defined as a
list of Codons.
'''
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]           # type alias for codons
Gene  = List[Codon]                                         # type aliad for genes


'''
Typically, genes on the internet will be in a file format that contains a giant string representing
all of the nucleotides in the gene’s sequence.
'''
gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"

# We will also need a utility function to convert a str into a Gene.
def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):               # don't run off end!
            return gene 
        # initialize codon out of three nuncleotides
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)                  # add codon to gene
    return gene


"""
string_to_gene() continually goes through the provided str and converts its next
three characters into Codons that it adds to the end of a new Gene. If it finds that there
is no Nucleotide two places into the future of the current place in s that it is examining
(see the if statement within the loop), then it knows it has reached the end of an
incomplete gene, and it skips over those last one or two nucleotides.
"""
my_gene: Gene = string_to_gene(gene_str)


'Linear search'
'''
In effect, a linear search is the most simple, natural, and obvious way to
search for something. In the worst case, a linear search will require going through
every element in a data structure, so it is of O(n) complexity, where n is the number of
elements in the structure.
'''
def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    return False

acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
print(linear_contains(my_gene, acg))            # True
print(linear_contains(my_gene, gat))            # False


"""
NOTE This function is for illustrative purposes only. The Python built-in
sequence types (list, tuple, range) all implement the __contains__()
method, which allows us to do a search for a specific item in them by simply
using the in operator. In fact, the in operator can be used with any type that
implements __contains__(). For instance, we could search my_gene for acg
and print out the result by writing print(acg in my_gene).
"""


'Binary search'
'''
There is a faster way to search than looking at every element, but it requires us to
know something about the order of the data structure ahead of time. If we know that
the structure is sorted, and we can instantly access any item within it by its index, we
can perform a binary search. Based on this criteria, a sorted Python list is a perfect
candidate for a binary search.
'''
def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:                  # while there is still a search space
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False


my_sorted_gene: Gene = sorted(my_gene)
print(binary_contains(my_sorted_gene, acg))         # True
print(binary_contains(my_sorted_gene, gat))         # False
