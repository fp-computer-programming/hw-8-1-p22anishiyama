# Author: ATN 12/1/21

def anagram(a, b):
    '''This program allows you to check if your input is an anagram of
    itself'''

    ana_sorted = list(a)
    ana_sorted.sort()
    ana_sorted_2nd = list(b)
    ana_sorted_2nd.sort()

    if(ana_sorted == ana_sorted_2nd):
        return(
            "true"
            )
    else:
        return(
            "false"
            )


print(anagram("listen", "silent") == "true")
print(anagram("the", "bats") == "false")
print(anagram("the morse code", "here come dots") == "true")
