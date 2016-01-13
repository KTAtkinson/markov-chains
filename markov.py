from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    text_file = open(file_path)
    text = text_file.read().replace('\n', ' ').rstrip()
    text_file.close()
    return text


def make_chains(text_string, gram_len):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('mary', 'hi'): ['there'], ('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi']}

    """

    chains = {}

    text_list = text_string.split(" ")
    gram = tuple(text_list[:gram_len])
    
    # for index in range(len(text_list) - gram_len):
    #     if chains.has_key(gram):
    #         chains[gram].append(text_list[index+gram_len])
    #     else:
    #         chains[gram] = [text_list[index+gram_len]]

    #     gram = tuple(text_list[index+1:index+gram_len+1])


    for word in text_list[gram_len:]:
        if chains.has_key(gram):
            chains[gram].append(word)
        else:
            chains[gram] = [word]

        gram = gram[1:] + tuple([word])

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

# print make_text(make_chains(open_and_read_file('gettysburg.txt')))
input_path = sys.argv[1]
n = int(sys.argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text , n)

# Produce random text
random_text = make_text(chains)

print random_text
