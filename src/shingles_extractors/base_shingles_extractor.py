class ShinglesExtractor(object):
    """
    This class handles Shingles extraction from an input object, to be used for the generation
    of a min-Hash signature for that object.

    This is one of the "trickiest" parts since every different type of object (text, photo, etc.)
    requires specific domain implementation, and the success of the entire method depends on the
    quality of the shingles the were extracted from the object.

    Every Shingles extractor should implement the static method extract_shingles. For every different
    input type there should be implemented dedicated extractor.
    """

    @staticmethod
    def extract_shingles(input_element, shingle_size=None):
        """
        Given an input object, this function will extract Shingles from it and return it as a list
        :param input_element: An input object to extract Shingles from in order to generate a min-Hash signature for it
        :param shingle_size: The size of the extracted Shingle (if required)
        :return: A list of Shingles
        """
        return NotImplementedError
