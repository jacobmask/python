"""Breadth First Search(no tree) or Deepening(stack), Monday 9/7 shows pseudocode."""
import math

def main():
    """Creates pond: Could use BFS or Iterative Deepening"""
    lillyPad = input("Enter the values for each lillypad, make sure its a square rooted number: ")
    lillyPadPond = list(lillyPad)
    findRowLength = int(math.sqrt(len(lillyPad)))
    if int(findRowLength * findRowLength) == len(lillyPad) and len(lillyPad) != 1:
        print(lillyPadPond)
        search(findRowLength, lillyPadPond, lillyPad)
    else:
        print("Please insert an amount of values for the lillypad that makes a perfect square")
        main()
def search(findRowLength, lillyPadPond, lillyPad):
    """Returns a string value of 25 with fastest route"""
    start = lillyPadPond[0]
    frontier = {}
    visited = {}
    currentNode = lillyPadPond[0]
    while frontier != {frontier}:
        if currentNode == "G":
            print("Your first node was the end point")


    print(start)
main()
