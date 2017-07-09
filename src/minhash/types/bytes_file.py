from minhash.minhash_object import BaseMinHash
from minhash.shingle import BaseShingle


class BytesMinHash(BaseMinHash):
    """
    Documentation can be found in the inherited class BaseMinHash
    """
    def __init__(self, shingles):
        super(BytesMinHash, self).__init__(BytesShingle, shingles)
        

class BytesShingle(BaseShingle):
    """
    Documentation can be found in the inherited class BaseShingle
    """
    def __init__(self, shingle):
        super(BytesShingle, self).__init__(shingle)
