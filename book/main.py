from .fib import *
from .nucleotide_compressor import NucleotideCompressor

def start():
    #print([x for x in fib_gen(10)])
    compress_gene()


def compress_gene():
    gene = "CCGTTATATATATATAGCCATGGATCGATTATA"
    compressor = NucleotideCompressor(gene)
    print(compressor.bit_string)
    print(compressor)
