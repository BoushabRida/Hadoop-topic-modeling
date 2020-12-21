import sys 
import string
from itertools import chain 
from collections import defaultdict 

#elle permet de donner une liste qui rassemble au couple (cle valeur)
def develop_dict(itemList):
    return list(chain.from_iterable(map(lambda x: map(lambda y: (x[0], y), x[1]), itemList)))

#inverse un dictionnaire
def invert_dict(init_dict):
    my_inverted_dict = defaultdict(list)
    for k, v in develop_dict(init_dict.items()):
        my_inverted_dict[v].append(k)
    return my_inverted_dict

#enlever la ponctuation 
def simplify(s):
    return s.translate(None, string.punctuation)


def main():
    # build base dictionnaire from file and invert it
    lexicon = {
        "education": [
            "teaching",
            "learning",
            "teachers",
            "diplomas",
            "academic",
            "school",
            "college"
        ],
        "economics": [
            "business",
            "management",
            "money",
            "markets"
        ],
        "cars": [
            "vehicle",
            "machine",
            "engine",
            "bus",
            "driver",
            "truck",
            "impounded",
            "road"
        ]
    }

    lexicon = invert_dict(lexicon)

    result = list(chain.from_iterable(map(lambda w: lexicon[w] if w in lexicon.keys(
    ) else [], simplify(sys.stdin.read()).split())))

    for w in result:
        print(w)


if __name__ == '__main__':
    main()
