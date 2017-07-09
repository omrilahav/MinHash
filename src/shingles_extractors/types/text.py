from shingles_extractors.base_shingles_extractor import ShinglesExtractor


class TextShinglesExtractor(ShinglesExtractor):

    @staticmethod
    def extract_shingles(document, shingle_size):
        """
        Documentation can be found in the inherited function
        ShinglesExtractor.extract_shingles(input_element, shingle_size=None)
        """
        shingles = []

        # Generate a list of all the words in the document
        words = document.split(' ')
        # Every iteration step one word forward and take the next [shingle_size] words as a new Shingle
        # (Between every to consecutive words there is an overlap of [shingle_size]-1 words)
        for i in range(0, len(words) - (shingle_size - 1)):
            # Extract a sequence of [shingle_size] words and save them as a shingle Shingle
            shingles.append(' '.join(words[i:i + shingle_size]))

        return shingles
