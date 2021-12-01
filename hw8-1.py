# Author: ATN 12/1/21

def anagram(a, b):
    '''This program allows you to check if your input ()'''

    ana_sorted = list(a)
    ana_sorted.sort()
    ana_sorted_2nd = list(b)
    ana_sorted_2nd.sort()

    if(ana_sorted == ana_sorted_2nd):
        return(
            "The word {0} is an anagram of {1}."
            .format(a, b)
            )
    else:
        return(
            "The word {0} is not an anagram of {1}."
            .format(a, b)
            )


print(anagram("a", 'a'))
