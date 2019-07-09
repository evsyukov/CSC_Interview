from random import randint

prime = 1000000007
x_rand = randint(1, prime-1)


def calculate_hash(string, x_pows):
    """ calculate hash function """
    result = 0
    for index, char in enumerate(string):
        result = (result + ord(char) * x_pows[index]) % prime
    return result


def find_occurrences(text, pattern):
    """ finds the pattern occurrence in the text and
    returns the index of the first character of each occurrence
    from left to right """
    result = []
    n, m = len(text), len(pattern)
    x_pows = [1]
    for i in range(1, m):
        x_pows.append(x_pows[-1] * x_rand % prime)
    hash_pattern = calculate_hash(pattern, x_pows)
    hash_selected = calculate_hash(text[n - m:], x_pows)
    x_pow = x_pows[-1]
    for i in reversed(range(n - m + 1)):
        if hash_selected == hash_pattern and pattern == text[i:i + m]:
            result.append(i)
        hash_selected = ((hash_selected - ord(text[i + m - 1]) * x_pow) * x_rand + ord(text[i - 1])) % prime
    return result


def main():
    pattern = input()
    text = input()
    result = find_occurrences(text, pattern)
    print(" ".join(map(str, reversed(result))))


if __name__ == "__main__":
    main()