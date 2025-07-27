#project  through command line arguments three string separated by space are given to you. each string is a series ofno separated by hypen(-). you like all the no in string 1 and dislike all the no in string 2. third string contains the no given to you . your initial happiness is 0. when you encounter a no which is present in string 1, add 1 to your happiness, if it is present in string2, add -1 to your hapinness. otherwisw your happiness does not chnage . output oyur final happiness at the end.

import sys

def calculate_happiness(like_str, dislike_str, given_str):
    like_set = set(like_str.split('-'))
    dislike_set = set(dislike_str.split('-'))
    given_list = given_str.split('-')
    
    happiness = 0
    for num in given_list:
        if num in like_set:
            happiness += 1
        elif num in dislike_set:
            happiness -= 1
    return happiness

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python happiness_calc.py <like> <dislike> <given>")
    else:
        like_str = sys.argv[1]
        dislike_str = sys.argv[2]
        given_str = sys.argv[3]

        result = calculate_happiness(like_str, dislike_str, given_str)
        print("Final Happiness:", result)
