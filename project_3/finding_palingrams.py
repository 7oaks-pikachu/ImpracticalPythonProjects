"""Find all word-pair palingrams in a dictionary file."""
import load_dictionary

word_list = load_dictionary.load("../3of6all.txt")
word_list = set(word_list)

def find_palingrams():
    """Find dictonary palingrams."""
    pali_list = []
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end - i] and rev_word[end - i:] in word_list and len(rev_word[end - i:]) > 1:
                    pali_list.append((word, rev_word[end - i:]))
                if word[:i] == rev_word[end - i:] and rev_word[:end - i] in word_list and len(rev_word[:end - i]) > 1:
                    pali_list.append((rev_word[:end - i], word))
    return pali_list


palingrams = find_palingrams()
palingrams_sorted = sorted(palingrams)
print(f"\nNumber of Palingrams = {len(palingrams_sorted)}\n")
for first, second in palingrams_sorted:
    print(f"{first}, {second}")
