from minhash.minhash_object import BaseMinHash
from minhash.shingle import BaseShingle


class TextMinHash(BaseMinHash):
    """
    Documentation can be found in the inherited class BaseMinHash
    """
    def __init__(self, shingles):
        super(TextMinHash, self).__init__(TextShingle, shingles)


class TextShingle(BaseShingle):
    """
    Documentation can be found in the inherited class BaseShingle
    """
    def __init__(self, shingle):
        super(TextShingle, self).__init__(shingle)
