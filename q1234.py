def common_elements(list1, list2):
    return [element for element in list1 if element in list2]

def palindrome_strings(string_list):
    return [string for string in string_list if string == string[::-1]]

def sieve_of_eratosthenes(number_list):
    primes = []
    for num in number_list:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

def anagrams(word, word_list):
    sorted_word = sorted(word.lower())
    anagram_list = []
    for word_candidate in word_list:
        if sorted(word_candidate.lower()) == sorted_word:
            anagram_list.append(word_candidate)
    return anagram_list
