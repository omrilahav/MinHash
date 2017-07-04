from configurations import SIGNATURE_SIZE
from feature_extractors.document import MinHashDocument, extract_shingles as extract_shingles_from_document
from minhash.hashing_tools import HashingManager
from feature_extractors.byte import extract_shingles as extract_byte_shingles_from_raw_document, MinHashBytes

HASHING_MANAGER = HashingManager()
SHINGLE_SIZE = 4


def raw_document_to_signature(filename):
    shingles = extract_byte_shingles_from_raw_document(filename, shingle_size=SHINGLE_SIZE)
    min_hash = MinHashBytes(shingles)
    signature = min_hash.get_signature(SIGNATURE_SIZE, HASHING_MANAGER)
    return signature


def document_to_signature(document_path):
    document = open(document_path, 'r').read()
    shingles = extract_shingles_from_document(document, shingle_size=SHINGLE_SIZE)
    min_hash = MinHashDocument(shingles)
    signature = min_hash.get_signature(SIGNATURE_SIZE, HASHING_MANAGER)
    return signature


def calculate_similarity(signature1_title, signature1, signature2_title, signature2):
    similarity = signature1.calculate_similarity(signature2)
    similarity *= 100

    print signature1_title + ' is similar to ' + signature2_title + ' in: ' + str(similarity) + '%'


def main():
    documents_example()
    print '\n'
    bytes_example()


def bytes_example():
    original_document = raw_document_to_signature('data_examples/document1.txt')
    original_copy = raw_document_to_signature('data_examples/document1_copy.txt')
    similar_document2 = raw_document_to_signature('data_examples/document2.txt')
    similar_document3 = raw_document_to_signature('data_examples/document3.txt')
    reversed_sentences_document = raw_document_to_signature('data_examples/document_reversed_sentences.txt')

    calculate_similarity('Original RAW Document', original_document, "Original RAW Document's Copy", original_copy)
    calculate_similarity('Original RAW Document', original_document, "Similar RAW Document 2", similar_document2)
    calculate_similarity('Original RAW Document', original_document, "Similar RAW Document 3", similar_document3)
    calculate_similarity('Original RAW Document', original_document, "Reversed Sentences RAW Document",
                         reversed_sentences_document)


def documents_example():
    original_document = document_to_signature('data_examples/document1.txt')
    original_copy = document_to_signature('data_examples/document1_copy.txt')
    similar_document2 = document_to_signature('data_examples/document2.txt')
    similar_document3 = document_to_signature('data_examples/document3.txt')
    reversed_sentences_document = document_to_signature('data_examples/document_reversed_sentences.txt')

    calculate_similarity('Original Document', original_document, "Original Document's Copy", original_copy)
    calculate_similarity('Original Document', original_document, "Similar Document 2", similar_document2)
    calculate_similarity('Original Document', original_document, "Similar Document 3", similar_document3)
    calculate_similarity('Original Document', original_document, "Reversed Sentences Document",
                         reversed_sentences_document)


if __name__ == '__main__':
    main()