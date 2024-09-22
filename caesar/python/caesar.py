#!/usr/bin/python3

import sys

ALPHABET: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rotateChr(char: str, rot: int) -> str:
    plainIndex = ALPHABET.find(char)
    if (plainIndex < 0):
        return char
    rotIndex = (plainIndex+rot)%len(ALPHABET)
    return ALPHABET[rotIndex]

def rotateStr(text: str, rot: int) -> str:
    result = ""
    for char in text:
        result += rotateChr(char, rot)
    return result

def main() -> None:
    rot = int(sys.argv[1])
    for line in sys.stdin:
        print(rotateStr(line, rot).strip())

if __name__ == "__main__":
    main()