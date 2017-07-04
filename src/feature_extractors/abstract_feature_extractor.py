from minhash.feature import MinHashFeature
from minhash.minhash_metric import MinHashMetric
from minhash.signature import MinHashSignature


class AbstractFeature(MinHashFeature):
    def __init__(self, shingle):
        super(AbstractFeature, self).__init__()
        self.value = shingle

    def hash(self, hashing):
        hashed = abs(int(hash(self.value)))

        feature_signature = []

        for prime_tuple in hashing.prime_tuples:
            feature_signature.append(int((hashed * prime_tuple[0] ^ 2 + hashed * prime_tuple[1]) % hashing.base_prime))

        return feature_signature


class MinHashAbstract(MinHashMetric):
    def __init__(self, shingles):
        super(MinHashAbstract, self).__init__()
        self.shingles = shingles
        self.features = None
        self.signature = None

    def get_signature(self, signature_size, hashing):
        if self.signature is None:
            self.signature = MinHashSignature(signature_size)
            self.signature.generate(self.get_features(), hashing)

        return self.signature

    def get_features(self):
        if self.features is None:
            self.init_features()

        return self.features

    def init_features(self):
        self.features = []
        for shingle in self.shingles:
            self.features.append(AbstractFeature(shingle))
