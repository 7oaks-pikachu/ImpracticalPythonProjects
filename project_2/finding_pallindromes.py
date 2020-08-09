"""Find palindromes in a dictionary file."""
import load_dictionary


def main():
    word_list = load_dictionary.load('../deutsche_woerter.txt')
    pali_list = []

    for word in word_list:
        if len(word) > 1 and word == word[::-1]:
            pali_list.append(word)

    print(f"\nThe nunmber of palindromes found is {len(pali_list)}.")
    print(*pali_list, sep="\n")


if __name__ == "__main__":
    main()
