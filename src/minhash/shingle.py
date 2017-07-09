class MinHashShingle(object):
    """
    This class represents a "Shingle" as described in "On the Resemblance and Containment of Documents"
    by A. Z. Broder, Proc. Compression Complex. Seq. 1997, pp. 21-29, 1997.

    A Shingle is a sequence of elements taken from an object in order to generate
    a min-Hash signature for that object.

    Example:
        For the text object (document): "The dog and the cat are friends",
        a Shingle in the length of 4 (also called "the 4-Shingle") can be:
        "The dog and the"
        It is recommended to split the document to overlap k-Shingles, and
        then to use all the Shingles in order to generate the min-Hash signature
        for the document. In our case, the 4-Shingling for our sentence will be:
        "The dog and the"
        "dog and the cat"
        "and the cat are"
        "the cat are friends"
        Each such Shingle should be hashed by n hash functions (to be used
        to construct a min-Hash signature in the length of n)
    """

    def __init__(self):
        pass

    def hash(self, hashing_manager):
        """
        Every Shingle must "know" how to hash it self. Due to the fact that every
        Shingle can be extracted from a different type of object (it can be text,
        bytes, photo pixels, etc.), every this function should be implemented
        differently for each input type.
        :param hashing_manager: The hashing_manager can be used as a hash functions source.
        :return: a list in the length of n (where n is the number of hash functions returned
        by the the hashing_manager) of the hash values calculated for that feature, cell i
        contains the value calculated by the i-th hash function.
        """
        raise NotImplementedError


class BaseShingle(MinHashShingle):
    """
    This class is a basic implementation of the MinHashShingle object, and can be used
    as a base (or abstract) class for specific implementations (for simple input
    types, like text documents, no changes for this class are required, therefore,
    one can use this class or inherit it without overwriting it)
    """
    def __init__(self, shingle):
        """
        Initiating a new BaseShingle instance for a given Shingle extracted from input object
        :param shingle: A Shingle that was extracted from the input object
        """
        super(BaseShingle, self).__init__()
        self.shingle = shingle

    def hash(self, hashing_manager):
        """
        Documentation can be found in the inherited function
        MinHashShingle.hash(hashing_manager)
        """
        # Convert the shingle into numeric value
        hashed = abs(int(hash(self.shingle)))
        # Initiate the list of hash values to return
        shingle_signature = []

        # Each hash function is constructed out of 3 prime numbers, and defined as:
        # h(hashed) = ((s * (prime_number_1 ^ 2)) + (s * prime_number_2 ^ 2)) mod prime_number_3
        # where prime_number_3 is fixed for all n hash functions (also called here 'base_prime'
        for prime_tuple in hashing_manager.prime_tuples:
            shingle_signature.append(
                int(
                    (
                        hashed * prime_tuple[0] ^ 2 +
                        hashed * prime_tuple[1]
                    ) % hashing_manager.base_prime)
            )

        return shingle_signature
