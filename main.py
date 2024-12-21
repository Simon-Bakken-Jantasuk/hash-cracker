import hashlib
import itertools
import string
import argparse

def hash(text, algorithm):
    hash_function = getattr(hashlib, algorithm)
    return hash_function(text.encode()).hexdigest()

def brute_force(algorithm, target_hash, max_length, charset):
    for length in range(1, max_length + 1):
        combinations = itertools.product(charset, repeat=length)
        for combination in combinations:
            combination = ''.join(combination)
            if hash(combination, algorithm) == target_hash:
                return combination
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--hashing-algorithm",
        type=str,
        required=True,
        choices=hashlib.algorithms_available,
    )
    parser.add_argument(
        "--target-hash",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--max-length",
        type=int,
        required=True,
    )
    parser.add_argument(
        "-u", "--use-uppercase",
        action="store_true",
    )
    parser.add_argument(
        "-l", "--use-lowercase",
        action="store_true",
    )
    parser.add_argument(
        "-d", "--use-digits",
        action="store_true",
    )
    args = parser.parse_args()

    charset = ""
    if args.use_uppercase:
        charset += string.ascii_uppercase
    if args.use_lowercase:
        charset += string.ascii_lowercase
    if args.use_digits:
        charset += string.digits

    found_password = brute_force(args.hashing_algorithm, args.target_hash, args.max_length, charset)

    if found_password:
        print(f"Password found: {found_password}")
    else:
        print("Password not found.")
