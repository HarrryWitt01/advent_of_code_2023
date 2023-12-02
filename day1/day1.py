

"""
Day 1:

Given an input of lines, find the calibration values
(first and last numeric value concatenated) of every
line. Then, compute the sum of each calibration value.

"""

calibration_sum = 0


input_file = open('day1_input.txt', 'r')





curr_line = input_file.readline()



while curr_line:

    # iterate through the line character by character
    # when you find the first numeric value, store it in a var
    # on each iteration, store the numeric value in last_num var
    # after iteration, append the two numbers and add that value to
    # calibration_sum

    first_num = ''
    last_num = ''

    for c in curr_line:

        ascii_val = ord(c)

        if ascii_val >= 48 and ascii_val <= 57:
            # this is a numeric value

            if len(first_num) == 0:
                first_num = c
            
            last_num = c

    cal_val = first_num + last_num

    calibration_sum += int(cal_val)

    curr_line = input_file.readline()



input_file.close()

print('final calibration sum = ', calibration_sum)