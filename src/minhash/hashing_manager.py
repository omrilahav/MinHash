import pickle
import random

from configurations import BASE_PRIME, MAX_PRIME, MIN_PRIME, SIGNATURE_SIZE, HASH_FUNCTIONS_PATH


class HashingManager(object):
    """
    This class is responsible for the hash functions used by the Min-Hash module.
    Each hash function is represented by a tuple of prime numbers (used in the function itself)
    """
    def __init__(self,
                 signature_size=SIGNATURE_SIZE,
                 path_of_hash_functions=HASH_FUNCTIONS_PATH,
                 base_prime=BASE_PRIME,
                 min_prime=MIN_PRIME,
                 max_prime=MAX_PRIME):
        """
        Initiating new HashingManager instance
        :param signature_size: Min-Hash signature number
        :param path_of_hash_functions: The path to the file that consists previously generated hash functions
        :param base_prime: Base prime number to use in the hash functions - Should be configurable
        :param min_prime: Lower bound for the generated prime numbers
        :param max_prime: Upper bound for the generated prime numbers
        """
        self.signature_size = signature_size
        self.base_prime = base_prime
        self.min_prime = min_prime
        self.max_prime = max_prime
        self.path_of_hash_function = path_of_hash_functions

        # Check if required hash functions were generation already before. If not, generate
        # new [signature_size] hash functions (each hash function is represented by two prime
        # numbers) and save it to a file, to be used later.
        # It is important to use the same hash functions in the entire task.
        if not self.load_prime_tuples():
            # Generate a list of all the prime numbers between self.minPrime to self.max_prime
            self.cached_primes = HashingManager.create_prime_numbers(self.min_prime, self.max_prime)
            # Randomly create [signature_size] hash functions (tuples of prime numbers) using self.cached_primes
            self.prime_tuples = self.generate_prime_tuples(signature_size)
            # Save the hash functions into a file
            self.save_prime_tuples()

    @staticmethod
    def create_prime_numbers(min_prime, max_prime):
        """
        Generate a list of all the prime numbers between self.minPrime to self.max_prime
        :param min_prime: Lower bound for the generated prime numbers
        :param max_prime: Upper bound for the generated prime numbers
        :return: List oa all the prime numbers between the given lower to the given upper bound
        """
        return [i for i in range(min_prime, max_prime) if HashingManager.is_prime(i)]

    @staticmethod
    def is_prime(number):
        """
        Checks if a given number is a prime number or not
        :param number: A number to check
        :return: True if number is a prime number, False otherwise
        """
        return all(number % i for i in xrange(2, number))

    def generate_primes(self):
        """
        Create a hash function by randomly choosing two prime numbers to construct the hash function with
        :return: A tuple of two prime numbers
        """
        prime_number_1 = random.choice([i for i in self.cached_primes])
        prime_number_2 = random.choice([i for i in self.cached_primes])

        return [prime_number_1, prime_number_2]

    def generate_prime_tuples(self, amount):
        """
        Generate a list in the length of [amount] of tuples of prime numbers
        :param amount: The length of the list to generate
        :return: A list of tuples of prime numbers
        """
        tuples = []
        for i in range(0, amount):
            tuples.append(self.generate_primes())

        return tuples

    def save_prime_tuples(self):
        """
        Saves the generated hash functions (represented as tuples of prime numbers) into a .pkl file
        called 'hash_primes_[self.signature_size].pkl'. Every different signature size will has its own
        file contains different hash functions. It is recommended to use the same file (the same hash
        functions) in the entire task for successful results.
        :return: None
        """
        with open(self.path_of_hash_function + 'hash_primes_' + str(self.signature_size) + '.pkl', 'w') as output:
            pickle.dump(self.prime_tuples, output, pickle.HIGHEST_PROTOCOL)

    def load_prime_tuples(self):
        """
        Loads previously generated hash functions (represented by tuples of prime numbers) if possible
        and overwrite self.prime_tuples with the loaded tuples.
        :return: True if loaded successfully, False otherwise (if file doesn't exists for example)
        """
        try:
            with open(self.path_of_hash_function + 'hash_primes_' + str(self.signature_size) + '.pkl', 'r') as input:
                self.prime_tuples = pickle.load(input)
                return True
        except IOError:
            return False
