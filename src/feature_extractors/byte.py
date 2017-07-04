from feature_extractors.abstract_feature_extractor import AbstractFeature
from feature_extractors.abstract_feature_extractor import MinHashAbstract


class BytesFeature(AbstractFeature):
    def __init__(self, shingles):
        super(BytesFeature, self).__init__(shingles)


class MinHashBytes(MinHashAbstract):
    def __init__(self, shingles):
        super(MinHashBytes, self).__init__(shingles)


def extract_shingles(filename, shingle_size):
    shingles = []

    with open(filename, "rb") as f:
        bytes_shingle = f.read(shingle_size)

        if len(bytes_shingle):
            shingles.append(bytes_shingle)
        i = 1
        while bytes_shingle != "":
            f.seek(i)
            i += 1
            bytes_shingle = f.read(shingle_size)

            if len(bytes_shingle):
                shingles.append(bytes_shingle)

    return shingles
