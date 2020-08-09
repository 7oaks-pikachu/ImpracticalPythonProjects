import load_dictionary

word_list = load_dictionary.load("../3of6all.txt")

anagram_list = []
name = "Foster"
print(f"Input Name = {name}")
name = name.lower()
print(f"Unsing name = {name}")

name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name and sorted(word) == name_sorted:
        anagram_list.append(word)

if len(anagram_list) == 0:
    print("\nYou need a longer dictionary or a longer name!")
else:
    print("\nAnagrams =", *anagram_list, sep='\n')