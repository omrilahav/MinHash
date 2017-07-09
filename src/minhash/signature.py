from __future__ import division


class MinHashSignature(object):
    """
    This class represents a min-Hash signature
    """
    def __init__(self, signature_size):
        """
        Initating a new instance of MinHashSignature
        :param signature_size: The size of the min-Hash signature
        """
        self.signature_size = signature_size
        # Initiate the min-Hash signature to be a list in length [signature_size] where each cell
        # contains the value "infinity"
        self.signature = [float("inf") for i in range(0, signature_size)]

    def generate(self, shingles, hashing_manager):
        """
        Generate a min-Hash signature for some input object that is represented by the given shingles
        which were extracted from it.
        :param shingles: The Shingles that were extracted from the input object
        :param hashing_manager: Can be used as a hash functions source
        :return:
        """
        for shingle in shingles:
            # Generate [self.signature_size] length list of values calculated by hashing the Shingle
            # with [self.signature_size] hash functions
            shingle_signature = shingle.hash(hashing_manager)
            # Update the object min-Hash signature with the new Shingle-signature
            self.update_signature(shingle_signature)

    def update_signature(self, shingle_signature):
        """
        For the min-Hash signature to be "min"-Hash, it should contains only the minimum
        value each hash function calculated for the entire Shingles set. Therefore, with
        every additional Shingle being hashed [self.signature_size] times with [self.signature_size]
        hash functions, only the hash values which are smaller than all the other hash
        values (for each specific hash function) calculated until now (for other Shingles)
        will be inserted into the object's min-Hash signature (overwriting older values)
        :param shingle_signature: A list of [self.signature_size] hash values, calculated by [self.signature_size]
        hash functions. The hash value calculated by the i-th hash function is stored in the i-th cell.
        :return: None
        """
        for i in range(0, self.signature_size):
            if shingle_signature[i] < self.signature[i]:
                self.signature[i] = shingle_signature[i]

    def calculate_jaccard_coefficient(self, other_signature):
        """
        The Jaccard index, also known as Intersection over Union and the Jaccard similarity coefficient,
        is a statistic used for comparing the similarity and diversity of sample sets.
        The Jaccard coefficient measures similarity between finite sample sets, and is defined as the size
        of the intersection divided by the size of the union of the sample sets.
        (https://en.wikipedia.org/wiki/Jaccard_index)
        This function calculates the Jaccard coefficient of two min-Hash signatures, the one currently
        represented by
        :param other_signature:
        :return:
        """
        similar = float(0)
        total = float(0)

        try:
            for i in range(0, self.signature_size):
                if self.signature[i] == other_signature.signature[i]:
                    similar += 1

                total += 1
        except IndexError:
            return 0

        return float(similar / total)
