from feature_extractors.abstract_feature_extractor import AbstractFeature
from feature_extractors.abstract_feature_extractor import MinHashAbstract


class ShingleFeature(AbstractFeature):
    def __init__(self, shingle):
        super(ShingleFeature, self).__init__(shingle)


class MinHashDocument(MinHashAbstract):
    def __init__(self, shingles):
        super(MinHashDocument, self).__init__(shingles)


def extract_shingles(document, shingle_size):
    shingles = []

    words = document.split(' ')
    for i in range(0, len(words) - (shingle_size - 1)):
        shingles.append(' '.join(words[i:i + shingle_size]))

    return shingles
