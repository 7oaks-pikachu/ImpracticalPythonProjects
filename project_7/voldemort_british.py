import sys
from itertools import permutations
from collections import Counter
import load_dictionary


def main():
    """Load files, run filters, allow users to view anagrams by 1st letter."""
    name = 'tmvoordle'
    name = name.lower()

    word_list_ini = load_dictionary.load('..\\3of6all.txt')
    trigrams_filtered = load_dictionary.load('..\\least-likely_trigrams.txt')

    word_list = prep_words(name, word_list_ini)
    filtered_cv_map = cv_map_words(word_list)
    filter_1 = cv_map_filter(name, filtered_cv_map)
    filter_2 = trigram_filter(filter_1, trigrams_filtered)
    filter_3 = letter_pair_filter(filter_2)
    view_by_letter(name, filter_3)

def prep_words(name, word_list_ini):
    """Prep word list for finding anagrams."""
    print(f"length initial word_list = {len(word_list_ini)}")
    len_name = len(name)
    word_list = [word.lower() for word in word_list_ini if len(word) == len_name]
    print(f"length of new word list = {len(word_list)}")
    return word_list


def cv_map_words(word_list):
    """Map letters into word to consonants and vowles."""
    vowels = 'aeiouy'
    cv_mapped_words = []
    for word in word_list:
        temp = ''
        for letter in word:
            if letter in vowels:
                temp += 'v'
            else:
                temp += 'c'
        cv_mapped_words.append(temp)

    # determine the number of unique c-v patters
    total = len(set(cv_mapped_words))
    # target fraction to eliminate
    target = 0.05
    n = int(total * target)
    count_pruned = Counter(cv_mapped_words).most_common(total - n)
    filtered_cv_map = set()
    for pattern, count in count_pruned:
        filtered_cv_map.add(pattern)
    print(f"length filtered cv map = {len(filtered_cv_map)}")
    return filtered_cv_map


def cv_map_filter(name, filtered_cv_map):
    """Remove pernumtations of words based on unlikely consonant vowel combination."""
    perms = {"".join(i) for i in permutations(name)}
    print(f"Total number of permutations = {len(perms)}")
    vowels = "aeiouy"
    filter_1 = set()
    for candidate in perms:
        temp = ''
        for letter in candidate:
            if letter in vowels:
                temp += 'v'
            else:
                temp += 'c'
        if temp in filtered_cv_map:
            filter_1.add(candidate)
    print(f'Number of choices after filter 1 = {len(filter_1)}')
    return filter_1


def trigram_filter(filter_1, trigrams_filtered):
    """Remove unlikely trigrams from permutations"""
    filtered = set()
    for candidate in filter_1:
        for triplet in trigrams_filtered:
            triplet = triplet.lower()
            if triplet in candidate:
                filtered.add(candidate)
    filter_2 = filter_1 - filtered
    print(f'Number of choices after filter 2 = {len(filter_2)}')
    return filter_2


def letter_pair_filter(filter_2):
    """Filter to anagrams starting with imput letter."""
    filtered = set()
    rejects = ['dt', 'lr', 'md', 'ml', 'mr', 'mt', 'mv', 'td', 'tv', 'vd', 'vl', 'vm', 'vr', 'vt']
    first_pair_rejects = ['ld', 'lm', 'lt', 'lv', 'rd', 'rl', 'rm', 'rt', 'rv', 'tl', 'tm']
    for candidate in filter_2:
        for r in rejects:
            if r in candidate:
                filtered.add(candidate)
        for fp in first_pair_rejects:
            if candidate.startswith(fp):
                filtered.add(candidate)
    filter_3 = filter_2 - filtered
    print(f"Number of choices after filter 3 = {len(filter_3)}")
    return filter_3

def view_by_letter(name, filter_3):
    """Filter to anagrams starting with input letter."""
    print(f"remaining letters = {name}")
    first = input('Select a starting letter or press Enter to see all:')
    subset = []
    for candidate in filter_3:
        if candidate.startswith(first):
            subset.append(candidate)
    print(*sorted(subset), sep='\n')



if __name__ == '__main__':
    main()
