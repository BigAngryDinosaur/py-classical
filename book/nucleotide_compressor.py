
class NucleotideCompressor:

    def __init__(self, gene: str):
        self._compress(gene)

    def _compress(self, gene: str) -> int:
        self.bit_string = 1

        for nucleotide in gene:
            self.bit_string <<= 2

            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError(f"Invalid Nucleotide: {nucleotide}")

        return self.bit_string


    def _decompress(self) -> str:

        gene = ""

        for i in range(0, self.bit_string.bit_length() - 1, 2):

            bits: int = (self.bit_string >> i) & 0b11

            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError(f"Invalid bits: {bits}")

        return gene[::-1]


    def __str__(self) -> str:
        return self._decompress()
