from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
    # Sorry, the file alice.txt does not exist.
else:
    # Count the approximate number of words in the file:
    words = contents.split() # sep is any whitespace
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
    # The file alice.txt has about 4 words.