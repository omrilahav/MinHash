from configurations import SIGNATURE_SIZE
from feature_extractors.document import MinHashDocument, extract_shingles
from minhash.hashing_tools import HashingManager

HASHING_MANAGER = HashingManager()
SHINGLE_SIZE = 4


def document_to_signature(document_path):
    document = open(document_path, 'r').read()
    shingles = extract_shingles(document, shingle_size=SHINGLE_SIZE)
    min_hash = MinHashDocument(shingles)
    signature = min_hash.get_signature(SIGNATURE_SIZE, HASHING_MANAGER)
    return signature


def calculate_similarity(signature1_title, signature1, signature2_title, signature2):
    similarity = signature1.calculate_similarity(signature2)
    similarity *= 100

    print signature1_title + ' is similar to ' + signature2_title + ' in: ' + str(similarity) + '%'


def main():
    original_document = document_to_signature('data_examples/document1.txt')
    original_copy = document_to_signature('data_examples/document1_copy.txt')
    similar_document2 = document_to_signature('data_examples/document2.txt')
    similar_document3 = document_to_signature('data_examples/document3.txt')
    reversed_sentences_document = document_to_signature('data_examples/document_reversed_sentences.txt')

    calculate_similarity('Original Document', original_document, "Original Document's Copy", original_copy)
    calculate_similarity('Original Document', original_document, "Similar Document 2", similar_document2)
    calculate_similarity('Original Document', original_document, "Similar Document 3", similar_document3)
    calculate_similarity('Original Document', original_document, "Reversed Sentences Document", reversed_sentences_document)

if __name__ == '__main__':
    main()