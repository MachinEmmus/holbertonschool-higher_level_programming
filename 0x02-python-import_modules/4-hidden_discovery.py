#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4
    for i in range(0, len(dir(hidden_4))):
        if dir(hidden_4)[i][0] != "_":
            print(dir(hidden_4)[i])
