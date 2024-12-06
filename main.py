import string

def count_words(text: str) -> int:
    return len(text.split())

def times_appeared(text: str) -> dict[str]:
    alphabet = set(string.ascii_lowercase)
    alpha_appeared = {}
    for ch in text.lower():
        if ch in alphabet:
            if ch not in alpha_appeared:
                alpha_appeared[ch] = 1
            else:
                alpha_appeared[ch] +=1
    return alpha_appeared

def main():
    with open("books/frankenstain.txt") as f:
        file_contents = f.read()
    print(f"{count_words(file_contents)} words found in document")
    num_of_apperance = times_appeared(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    for ch in set(string.ascii_lowercase):
        print(f"The '{ch}' character was found {num_of_apperance[ch]} times")
    print("--- End report ---")
if __name__ == "__main__":
    main()