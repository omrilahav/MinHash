from __future__ import division


class MinHashSignature(object):
    def __init__(self, signature_size, machine_name=None):
        self.signature_size = signature_size
        self.signature = [float("inf") for i in range(0, signature_size)]
        self.machine_name = machine_name

    def generate(self, features, hashing):
        for feature in features:
            feature_signature = feature.hash(hashing)
            self.update_signature(feature_signature)

    def update_signature(self, feature_signature):
        for i in range(0, self.signature_size):
            if feature_signature[i] < self.signature[i]:
                self.signature[i] = feature_signature[i]

    def calculate_similarity(self, other_signature):
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
