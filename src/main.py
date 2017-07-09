from minhash.hashing_manager import HashingManager
from configurations import SIGNATURE_SIZE
from shingles_extractors.types.text import TextShinglesExtractor
from minhash.types.text_file import TextMinHash

from os import listdir
from os.path import isfile, join

"""
This example demonstrates how to use min-Hash for multiple purposes in multiple domains.
The important stuff is to know which ShingleExtractor and which MinHashObject one should
use for specific domain implementation.
"""

# Initiating HashingManager to be used in this example
# (additional details on can be found in HashingManager module)
HASHING_MANAGER = HashingManager()

# The default Shingle size to use in this example
# (additional details on Shingle size can be found in MinHashShingle module)
SHINGLE_SIZE = 4


def document_to_signature(document_path):
    """
    Convert a given document (text) into a min-Hash signature
    :param document_path: The path to the document
    :return: The min-Hash signature of the document
    """
    # Open the file
    document = open(document_path, 'r').read()
    # Extract Shingles from the document using TextShinglesExtractor
    shingles = TextShinglesExtractor.extract_shingles(document, SHINGLE_SIZE)
    # Generate and return a min-Hash signature
    return TextMinHash(shingles).get_signature(SIGNATURE_SIZE, HASHING_MANAGER)


def example(path, function_to_exec):
    """
    In this example we are calculating how similar each file in the given path to the first file in that path.
    The results are printed to the console.
    :param path: The path for the input files
    :param function_to_exec: Which of the example functions from the above to execute
    :return: None
    """
    signatures = {}
    # Get all the files from the path
    input_files = [f for f in listdir(path) if isfile(join(path, f))]
    # Generate a min-Hash signature for each file
    for input_file in input_files:
        signatures[input_file] = function_to_exec(path + input_file)

    first_filename = signatures.keys()[0]
    first_file_signature = signatures.values()[0]

    # Calculate how similar each file in the path to first_filename
    for filename, signature in signatures.iteritems():
        similarity = signature.calculate_jaccard_coefficient(first_file_signature)

        print '{} is similar to {} in: {}%'.format(
            filename,
            first_filename,
            str(similarity * 100))


def main():
    data_example_path = 'data_examples/'

    print '\nText Documents Comparison:'
    example(data_example_path, document_to_signature)

if __name__ == '__main__':
    main()
