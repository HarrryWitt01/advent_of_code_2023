import re

"""
For this approach, I used a mapping from integer values -> lexemes.
At each line I do a regex search of each lexeme to find all starting indices.
Otherwise, this is exactly the same as part one.

"""

term_map = {
    0: ['zero', '0'],
    1: ['one', '1'],
    2: ['two', '2'],
    3: ['three', '3'],
    4: ['four', '4'],
    5: ['five', '5'],
    6: ['six', '6'],
    7: ['seven', '7'],
    8: ['eight', '8'],
    9: ['nine', '9'],
    
}

calibration_value = 0


input_file = open('/Users/Harry/advent-of-code-2023/advent_of_code_2023/day1/day1_pt2_input.txt')



curr_line = input_file.readline()

line_num = 1

# this while loop is to iterate over all lines
while (curr_line):

    idx = 0

    first_num = 0
    first_idx = float('inf')

    last_num = 0
    last_idx = -1
   
    
    for key in term_map.keys():

        # print('SEARCHING FOR', key)

        key_str_lst = term_map[key]

        for sub_str in key_str_lst:


            # new idea... use regular expressions!

            sub_occ = [m.start() for m in re.finditer(sub_str, curr_line)]


            for occ_start in sub_occ:
                
                if occ_start < first_idx:
                    first_num = key
                    first_idx = occ_start

                if occ_start > last_idx:
                    last_num = key
                    last_idx = occ_start

       

    
    line_cal = int(str(first_num) + str(last_num))

    calibration_value += line_cal

   

    curr_line = input_file.readline()
    line_num += 1


print('part 2 total calibration: ', calibration_value)
