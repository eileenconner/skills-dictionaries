# To work on the advanced problems, set to True
ADVANCED = False


def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """
    unique_words = {}

    input_string = input_string.strip().split()

    # use .get to check if word in unique_words
    # increment value if so, add new pair if not
    for word in input_string:
        unique_words[word] = unique_words.get(word, 0) + 1

    return unique_words


def find_common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in at least one list and is present
    in both lists, return it each time:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(find_common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """

    # non-dictionary solution that works:

    # common_items = []
    # for item_1 in list1:
    #     for other_item in list2:
    #         if item_1 == other_item:
    #             common_items.append(item_1)
    # return common_items

    ############

    # set version that returns 1 extra of each item in final list
    # AND uses forbidden for x in y
    # such that I'm not going to continue trying to fix it right now:

    # items_in_common = set(list1) & set(list2)
    # master_list = list1 + list2
    # repeated_items = []

    # for item in master_list:
    #     if item in items_in_common:
    #         repeated_items.append(item)

    # return repeated_items

    ############

    # RE-SOLVE WITH DICTIONARY
    # make word key and increment value with get, then build list from that
    # if value >= 2:
    # append to list (value * key) i.e. ("and" * 3)
    # make sure to treat keys as str
    # then transform them back afterward?

    # this was very difficult to brain in terms of dictionaries!

    common_items = {}
    master_list = list1 + list2
    common_items_list = []

    # populate dictionary w pairs of format (list item: number of times seen)
    for word in master_list:
        common_items[word] = common_items.get(word, 0) + 1

    for item, number in common_items.items():
        if number >= 2:
            # first I tried this but it doesn't work, creates ["111", "222"] etc.:
            # common_items_list.append(str(item) * (number - 1))
            # so instead:
            for i in range(number - 1):
                common_items_list.append(item)

    return common_items_list


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `find_common_items`, this should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """

    return list(set(list1) & set(list2))

    # first solution:

    # unique_common_items = set([])

    # for item_1 in list1:
    #     for other_item in list2:
    #         if item_1 == other_item:
    #             unique_common_items.add(item_1)

    # return list(unique_common_items)


def get_sum_zero_pairs(input_list):
    """Given a list of numbers, return list of x,y number pair lists where x + y == 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """
    sum_zero_pairs = {}
    list_copy = input_list[:]

    for num in input_list:
        for num2 in list_copy:
            if num + num2 == 0:
                new_pair = sorted([num, num2])
                sum_zero_pairs[new_pair[0]] = new_pair[1]

    pair_list = list(sum_zero_pairs.iteritems())

    return pair_list


    # here is my thought process before writing the above:

    # check if each number plus another number = 0
    # if so, append those two numbers to sum_zero_pairs as a list.
    # if zero is in the list, add [0, 0]
    # ensure all items in list are unique (use sets)
    # return that list.

    # brainstorming:
    # - create copy of input list and iterate through both with nested for loops

    # for set version:
    # if 0 in input_list:
    #     sum_zero_pairs.add([0, 0])
    # additional loops to build rest of pairs
    # return list(sum_zero_pairs)

    # rethink problem with dictionaries?
    # add pairs to dict and then use dict.items or similar to get them out


def remove_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    Do this without using a Python set.

    For example:

        >>> sorted(remove_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(remove_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    non_duplicates = {}

    for word in words:
        non_duplicates[word] = non_duplicates.get(word, 1)

    #feed keys in dictionary into a list with keys method; sort
    non_dup_list = sorted(non_duplicates.keys())

    return non_dup_list


def encode(phrase):
    """Given a phrase, return the encoded string.

    Replace all "e" characters with "p",
    replace "a" characters with "d", replace "t" characters with "o",
    and "i" characters with "u".

    For example:

        >>> encode("You are a beautiful, talented, brilliant, powerful musk ox.")
        'You drp d bpduouful, odlpnopd, brulludno, powprful musk ox.'
    """
    replaceable_letters = {"e": "p",
                           "a": "d",
                           "t": "o",
                           "i": "u"}

    new_phrase = []

    # iterate over list and check against dict for replaceable letters
    # replace those replaceable with their key values
    for char in list(phrase):
        if char in replaceable_letters.keys():
            new_phrase.append(replaceable_letters[char])
        else:
            new_phrase.append(char)

    # transform new_phrase into a string
    transformed_string = "".join(new_phrase)

    return transformed_string

    # this was hard, required 45 min+ work
    # possibly because trying to do it on the train while feeling sick/burnt
    # immediately after a full week of hackbright
    # I more or less understood concept of how to solve it, but had syntax/actual code issues.
    # being on the train also meant inability to look much up except help/dir
    # but I did solve it before getting home.
    # then the next day fresh I could easily use this to build the pirate translator.


def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """
    # ref to markov chains assignment/building that dictionary
    # use get to add as default value to numbered key or append to value list for existing key

    words_by_length = {}

    # iterate over list of words
    # check if key (length) is in dict
    # if so, add word to list of values assoc with that key
    # if not, add new key-value pair of (len(word): [word]) form

    # I have a feeling we can do this more efficiently with .get
    # but I don't know how yet

    for word in words:
        key = len(word)
        value = []
        value.append(word)

        if key in words_by_length.keys():
            # append new word to existing value list
            words_by_length[key] = words_by_length.get(key, 0) + value
        else:
            # create new key-value pair
            words_by_length[key] = value

    # use .items to translate dict into list of sorted tuples
    words_by_length = sorted(words_by_length.items())

    return words_by_length


def get_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> get_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> get_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    eng_to_pirate = {"sir": "matey",
                     "hotel": "fleabag inn",
                     "student": "swabbie",
                     "boy": "matey",
                     "madam": "proud beauty",
                     "professor": "foul blaggart",
                     "restaurant": "galley",
                     "your": "yer",
                     "excuse": "arr",
                     "students": "swabbies",
                     "are": "be",
                     "lawyer": "foul blaggart",
                     "the": "th'",
                     "restroom": "head",
                     "my": "me",
                     "hello": "avast",
                     "is": "be",
                     "man": "matey"
                     }

    # difference between this and encode fn is word vs char
    pirate_sentence = []

    # iterate over list and check against dict for replaceable words
    # replace those replaceable with their key values
    for word in phrase.split():
        if word in eng_to_pirate.keys():
            pirate_sentence.append(eng_to_pirate[word])
        else:
            pirate_sentence.append(word)

    # transform pirate_sentence into a string joined with spaces
    pirate_translation = " ".join(pirate_sentence)

    return pirate_translation


# End of skills. See below for advanced problems.
# To work on them, set ADVANCED=True at the top of this file.
############################################################################


def adv_get_top_letter(input_string):
    """Given an input string, return a list of letter(s) which appear(s) the most the input string.

    If there is a tie, the order of the letters in the returned
    list should be alphabetical.

    For example:
        >>> adv_get_top_letter("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:
        >>> adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Spaces do not count as letters.

    """

    return ''


def adv_alpha_sort_by_word_length(words):
    """Given a list of words, return a list of tuples, ordered by word-length.

    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.
    Now try doing it with only one call to .sort() or sorted(). What does the
    optional "key" argument for .sort() and sorted() do?

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    return []


##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
