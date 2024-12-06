from collections import Counter

def count_words(text: str) -> int:
    return len(text.split())

def times_appeared(text: str) -> dict[str]:
    return Counter(text.lower())

def main():
    with open("books/frankenstain.txt") as f:
        file_contents = f.read()
        print(file_contents)
    print(count_words(file_contents))
    print(times_appeared(file_contents))

if __name__ == "__main__":
    main()