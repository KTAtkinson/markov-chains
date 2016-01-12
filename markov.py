from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    text_file = open(file_path)
    text = text_file.read().replace('\n', ' ').rstrip()
    text_file.close()
    return text


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('mary', 'hi'): ['there'], ('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi']}

    """

    chains = {}
    first_word =  None
    second_word = None
    for word in text_string.split(" "):
        if not first_word:
            first_word = word
            continue
        if not second_word:
            second_word = word
            continue

        if chains.has_key((first_word, second_word)):
            chains[(first_word, second_word)].append(word)
        else:
            chains[(first_word, second_word)] = [word]

        first_word = second_word
        second_word = word

    return chains

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    first_pair = choice(chains.keys())
    text = ' '.join(first_pair)

    while chains.has_key((first_pair)):
        next_word = choice(chains[first_pair])
        text += ' {}'.format(next_word)
        first_pair = (first_pair[1], next_word)
    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
