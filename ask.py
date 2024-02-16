#!/usr/bin/env python3

def display_invite():
    # Each letter represented by arrays of strings in a bubble style.
    p = [" _ _ _ ", "| _ _ |", "| | | |", "| _ _ |", "| |    ", "| |   ", "  "]
    r = [" _ _ _ ", "| _ _ |", "| | | |", "| _ _ |", "| \\ \\  ", " |  \\ \\ ", "    "]
    o = [" _ _ _ ", "| _ _ |", "| | | |", "| | | |", "| | | |", "| _ _ |", " "]
    m = [" _   _ ", "| \\ / |", "| | | |", "| | | |", "| | | |", "| | | |      ?", "  "]

    # Printing each line of the letters to form the word "PROM"
    for i in range(7):
        print(p[i] + "  " + r[i] + "  " + o[i] + "  " + m[i])

    while True:
      print("Yes or no:")
      reply = input().lower()
      if reply == "yes" or reply == "y":
        break

if __name__ == "__main__":
    display_invite()
