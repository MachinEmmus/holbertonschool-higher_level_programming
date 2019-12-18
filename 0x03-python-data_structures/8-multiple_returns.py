#!/usr/bin/python3
def multiple_return(sentence):
    size = len(sentece)
    if size == 0:
        return (0, None)
    return (size, sentence[0])
