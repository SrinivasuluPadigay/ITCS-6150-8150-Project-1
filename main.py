"""
main.py
This program is the main program for solving 8 puzzle problem using A* algorithm
It takes the inputs from the user validates it and send to processing to the respective heuristic function
"""
import traceback
import misplacedTiles
import manhattanDistance
def check_for_err(list_input):
    """Checks for errors in the input"""
    # input should be 9 digits/tiles
    if len(list_input) != 9:
        return True
    # numbers should not be repeated
    if any(list_input.count(x) > 1 for x in list_input):
        return True
    # number cannot be less than 0 or greater than 8
    for i in list_input:
        if i < 0 or i > 8:
            return True
    return False

def start():
    """Main function"""
    print("Welcome to 8 puzzle problem")
    print("Please select a heuristic function:")
    print("Input 1 for using Misplaced Tiles heuristic function.")
    print("Input 2 for using Manhattan Distance heuristic function.")
    hrt_fuc_sel = input("Input =").strip()

    if(hrt_fuc_sel == "1" or hrt_fuc_sel == "2"):
        if (hrt_fuc_sel == "1"):
            print("Selected heuristic function is Misplaced Tiles.")
        else:
            print("Selected heuristic function is Manhattan Distance.")

        print("Please input the (1-8) numbers of 8-puzzle problem from left to right, top to bottom, each separated by a whitespace and the empty tile represented by a 0")
        case_input = input("Input =").strip()

        print("Please input the GOAL numbers (or) press enter to consider [1, 2, 3, 4, 5, 6, 7, 8, 0] as your goal")
        case_goal = input("Input =").strip()

        if not case_goal:
            case_goal = "1 2 3 4 5 6 7 8 0"

        try:
            case_input = list(map(int, case_input.split()))
            case_goal = list(map(int, case_goal.split()))

            if check_for_err(case_input) or check_for_err(case_goal):
                raise ValueError("Invalid input format")

            if hrt_fuc_sel == "1":
                misplacedTiles.process(case_input, case_goal)
            else:
                manhattanDistance.process(case_input, case_goal)
        except ValueError:
            print("Error: Invalid input entered!\t Please try again.\n\n")
        except Exception as e:
            traceback.print_exc()
    else:
        print("Error: Invalid input entered!\t Please try again.\n\n")

if __name__ == '__main__':
    while 1:
        start()