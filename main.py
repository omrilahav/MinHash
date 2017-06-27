from configurations import SIGNATURE_SIZE
from feature_extractors.document import MinHashDocument, extract_shingles
from minhash.hashing_tools import HashingManager


hashing_manager = HashingManager()
document = open('data_examples/document.txt', 'r').read()
shingles = extract_shingles(document, shingle_size=4)
min_hash = MinHashDocument(shingles)
signature = min_hash.get_signature(SIGNATURE_SIZE, hashing_manager)
print signature
