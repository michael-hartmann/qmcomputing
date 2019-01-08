from math import log2

def alphabet(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    return d

def entropy(s):
    elems = len(s)
    d = alphabet(s)
    H = 0
    for key in d:
        p = d[key] / elems
        H -= p*log2(p)

    return H

def block_encode(text, coding):
    output = ""
    for c in text:
        output += coding[c]
    return output


text = "ABADDCCAABABEDAECBDDDAAAABAAAABBCAECEEC"
text = "mississippi"
print(len(text))

print(alphabet(text))
