import pickle
import random

from configurations import BASE_PRIME, MAX_PRIME, MIN_PRIME, SIGNATURE_SIZE, HASH_FUNCTIONS_PATH


class HashingManager(object):
    """
    This class is responsible for the hash functions used by the Min-Hash module.
    Each hash function is represented by a tuple of prime numbers (used in the function itself)
    """
    def __init__(self, signature_size=SIGNATURE_SIZE, path_of_hash_function=HASH_FUNCTIONS_PATH, base_prime=BASE_PRIME, min_prime=MIN_PRIME, max_prime=MAX_PRIME):
        """
        :param signature_size: The size of the min-Hash signature
        :param from_load: Load previously generated prime numbers from a file if from_load = True,
        or generate new on-memory orime numbers of from_load = False
        """
        self.signature_size = signature_size                    # Min-Hash signature number
        self.base_prime = base_prime                            # Base prime number to use in the hash functions - Should be configurable
        self.minPrime = min_prime                               # Lower bound for the generated hash numbers
        self.maxPrime = max_prime                               # Upper bound for the generated hash numbers
        self.path_of_hash_function = path_of_hash_function

        if not self.load_prime_tuples():
            self.cached_primes = HashingManager.create_prime_numbers(self.minPrime, self.maxPrime)
            self.prime_tuples = self.generate_prime_tuples(signature_size)
            self.save_prime_tuples()

    @staticmethod
    def create_prime_numbers(min, max):
        return [i for i in range(min, max) if HashingManager.is_prime(i)]

    @staticmethod
    def is_prime(a):
        return all(a % i for i in xrange(2, a))

    def generate_primes(self):
        a = random.choice([i for i in self.cached_primes])
        b = random.choice([i for i in self.cached_primes])

        return [a, b]

    def generate_prime_tuples(self, amount):
        tuples = []
        for i in range(0, amount):
            tuples.append(self.generate_primes())

        return tuples

    def get_prime_tuples(self):
        return self.prime_tuples

    def get_base_prime(self):
        return self.base_prime

    def save_prime_tuples(self):
        with open(self.path_of_hash_function + 'hash_primes_' + str(self.signature_size) + '.pkl', 'w') as output:
            pickle.dump(self.prime_tuples, output, pickle.HIGHEST_PROTOCOL)

    def load_prime_tuples(self):
        try:
            with open(self.path_of_hash_function + 'hash_primes_' + str(self.signature_size) + '.pkl', 'r') as input:
                self.prime_tuples = pickle.load(input)
                return True
        except IOError:
            return False


