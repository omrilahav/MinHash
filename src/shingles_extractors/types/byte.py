from shingles_extractors.base_shingles_extractor import ShinglesExtractor


class ByteShinglesExtractor(ShinglesExtractor):

    @staticmethod
    def extract_shingles(input_file, shingle_size):
        """
        Documentation can be found in the inherited function
        ShinglesExtractor.extract_shingles(input_element, shingle_size=None)
        """
        shingles = []

        # Read the first [shingle_size] bytes from the file
        bytes_shingle = input_file.read(shingle_size)

        # If the Shingle is not empty push it the the shingles list
        if len(bytes_shingle):
            shingles.append(bytes_shingle)

        # Iterate over the input_file. Extract [shingle_size] bytes as a Shingle
        # and step 1 byte forward every iteration (every two consecutive byte Shingles
        # are overlapping in [shingle_size]-1 bytes.
        i = 1
        while bytes_shingle != "":
            input_file.seek(i)
            i += 1
            bytes_shingle = input_file.read(shingle_size)

            if len(bytes_shingle):
                shingles.append(bytes_shingle)

        return shingles
