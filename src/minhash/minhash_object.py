from minhash.signature import MinHashSignature


class MinHashObject(object):
    """
    The min-Hash object represents an input object which we want to generate a
    min-Hash signature for
    """
    def __init__(self):
        pass

    def get_signature(self, signature_size, hashing_manager):
        """
        This function responsible to generate (if required) the min-Hash signature
        for the given object and return it.
        :param signature_size: The size of the min-Hash signature.
        :param hashing_manager: The hashing_manager can be used as a hash functions source.
        :return: A min-Hash signature of the input object in the length of signature_size.
        """
        raise NotImplementedError


class BaseMinHash(MinHashObject):
    """
    This class is a basic implementation of the MinHashObject, and can be used
    as a base (or abstract) class for specific implementations (for simple input
    types, like text documents, no changes for this class are required, therefore,
    one can use this class or inherit it without overwriting it)
    """
    def __init__(self, shingles_type, shingles):
        """
        Initiating a new BaseMinHash instance
        :param shingles: A list of Shingles extracted from the input object, which
        are transformed into MinHashShingle instances
        """
        super(BaseMinHash, self).__init__()
        self.shingles = []
        for shingle in shingles:
            self.shingles.append(shingles_type(shingle))
        self.signature = None

    def get_signature(self, signature_size, hashing_manager):
        """
        Documentation can be found in the inherited function
        MinHashObject.get_signature(signature_size, hashing_manager)
        """
        if self.signature is None:
            self.signature = MinHashSignature(signature_size)
            self.signature.generate(self.shingles, hashing_manager)

        return self.signature
