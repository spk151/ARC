#!/usr/bin/python

import os, sys
import json
import numpy as np
import re
import math as mt
import itertools as its

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.



### Required Transform Description:
### The input consists of a square array made up of a nxn grid of 2x2 cubes each 
### separated by a line of uniquely coloured squares. Some of these 2x2 cubes 
### are black, while others are coloured. If any two 2x2 coloured cubes are 
### aligned either horizontally and/or vertically then all other 2x2 cubes 
### between these two aligned cubes must be changed to the same colour as the 
### aligned cubes.

### Solution Transform Description:
### I first iterate through the inputted array and identified the location of 
### each of the 2x2 coloured cubes and created a list containing the colour, row 
### index and column index of the top left-hand square in the coloured cube, which 
### I in turn added to the list named ‘top_left_coord’. From this I create a new 
### list of lists containing all combinations of the elements in the ‘top_left_coord’ 
### list. For each of these combinations I check if the colours were equal. If 
### they are not, I ignored this combination, otherwise I proceed to check if the 
### row or column index match. If either the row or column indexes are equal, I 
### iterate in blocks of 3 squares (2 of the cube length + 1 for the coloured 
### squares separating the cubes) between the matching indexes in the horizontal 
### (for row match) or vertical (for column match) direction. This iteration 
### locates the top left-hand square of each 2x2 cube between the aligned cubes 
### with the same colour, which is in turn updated to match the colour of the 
### aligned cubes. 

### Test Results:
### All test results are returned correctly.

def solve_06df4c85(x):
    # Convert to list
    x = x.tolist()
    # Store coordinates of top left-hand square in cube 
    top_left_coord = [] 
    # Iterate through each element of x (initial array)
    for i in range(len(x) - 1):
        for j in range(len(x[i]) - 1):
            # If a non-black 2x2 cube is located add its colour and the coordinates
            # of top left-hand square of the cube to the 'top_left_coord' list.
            if x[i][j] == x[i][j+1] == x[i+1][j] == x[i+1][j+1] and x[i][j] != 0:
                top_left_coord.append([x[i][j], i, j])
    # Create a list of all combinates of pairs of lists in the 'top_left_coord' list
    compare_align = list(its.combinations(top_left_coord, 2))  
    # For each pair of squares 
    for k in compare_align:
        # If there colours are equal
        if k[0][0] == k[1][0]:
            # If there row indexes are equal
            if k[0][1] == k[1][1]:
                # Identify the colour
                colour = k[0][0]
                # Identify there column indexes 
                left_column = k[0][2]
                right_column = k[1][2]
                row = k[0][1]
                # Identify the top left-hand square of each cube between the two 
                # identiaclly coloured cubes by iteration along the row in s
                # increment of 3.
                for col in range(left_column+3, right_column, 3):
                    # Update the colour or the located cubes
                    x[row][col] = colour 
                    x[row][col+1] = colour 
                    x[row+1][col] = colour
                    x[row+1][col+1] = colour
            # If there coloumn indexes are equal  
            if k[0][2] == k[1][2]:
                # Identify the colour
                colour = k[0][0]
                # Identify there row indexes 
                top_row = k[0][1]
                bottom_row = k[1][1]
                col = k[0][2]
                # Identify the top left-hand square of each cube between the two 
                # identiaclly coloured cubes by iteration along the column in 
                # increments of 3.
                for row in range(top_row+3, bottom_row, 3):
                    # Update the colour or the located cubes
                    x[row][col] = colour 
                    x[row][col+1] = colour 
                    x[row+1][col] = colour
                    x[row+1][col+1] = colour
    # Convert the list x back to an array
    x = np.array(x)
    return x 



### Required Transform Description:
### The input consists of a square array made up of solely black squares with 
### the exception of one 2x2 cube located randomly within the array. This 2x2 
### cube is made up of a minimum of one red square with the remaining of the 
### squares being of a different colour. All squares that are traversed by 
### diagonally extending the cube in the direction of the red square(s) 
### in the cube are updated to the colour of the non-red colour. The red square(s) 
### and also updated to the non-red colour.

### Solution Transform Description:
### I first iterate through the inputted array and identified the location of 
### each of the coloured squares and create a list containing the colour, row 
### index and column index of each square. I add each of these four lists to a 
### list named ‘initial_cube’. Looping through each list in ‘initial_cube’ if 
### the corresponding square is red (identified by the number 2) I update the 
### colours of each square that is traversed by diagonally extending the cube 
### in the direction of each red square. The squares to be updated when diagonally 
### extending the cube are identified by simultaneously iterating through the 
### rows and columns between the initial cube and the border. There are four 
### potential direction; top left (row and column decremented), top right (row 
### decremented, column incremented), bottom left (row incremented, column 
### decremented) and bottom right (row and column incremented).

### Test Results:
### All test results are returned correctly.

def solve_1f0c79e5(x):
    # Convert to list
    x = x.tolist() 
    # Store coordinates of the initial cube
    initial_cube = []
    # Initiate the colour to red. This ensures that is all 4 squares in the cube 
    # are red then the correct colour will be set when the cube is extended.
    colour = 2
    # Iterate through each element of x (initial array)
    for i in range(len(x)):
        for j in range(len(x[i])):
            # Locate the position of the coloured cube
            if x[i][j] != 0:
                # Store the list 'initial_cube' the colour, row index and 
                # column index of each square in the coloured cube.
                initial_cube.append([x[i][j], i, j]) 
                # Update 'colour' to the non-red colour
                if x[i][j] != 2:
                    colour = x[i][j]
    # For each square in the list 'initial_cube' if the colour of the square 
    # is red extend the cube in the direction of that red square as far as the 
    # boundary.
    for m in initial_cube:
        # If square colour is red
        if m[0] == 2:
            # If the top left square of the cube is red
            if initial_cube.index(m) == 0:
                for r, c in zip(range(m[1], -1, -1), range(m[2], -1, -1)):
                    print(r, c)
                    x[r][c] = colour
                    if r > 0:
                        x[r-1][c] = colour
                    if c > 0:
                        x[r][c-1] = colour
            # If the top right square of the cube is red   
            if initial_cube.index(m) == 1:
                for r, c in zip(range(m[1], -1, -1), range(m[2], len(x[0])+1)):
                    print(r, c)
                    x[r][c] = colour
                    if r > 0:
                        x[r-1][c] = colour
                    if c < len(x[0]) - 1:
                        x[r][c+1] = colour
            # If the bottom left square of the cube is red        
            if initial_cube.index(m) == 2:
                for r, c in zip(range(m[1], len(x)), range(m[2], -1, -1)):
                    print(r, c)
                    x[r][c] = colour
                    if r < len(x) - 1:
                        x[r+1][c] = colour
                    if c > 0:
                        x[r][c-1] = colour
            # If the bottom right square of the cube is red   
            if initial_cube.index(m) == 3:
                for r, c in zip(range(m[1], len(x)), range(m[2], len(x[0]))):
                    print(r, c)
                    x[r][c] = colour
                    if r < len(x) - 1:
                        x[r+1][c] = colour
                    if c < len(x[0]) - 1:
                        x[r][c+1] = colour
    # Convert the list x back to an array
    x = np.array(x)
    return x



### Required Transform Description:
### The input consists of a nxm array where n is an uneven number (Note: in all 
### test examples nxm = 13x5 but this function will correctly solve any 2D input 
### as long as the number of rows are uneven). All the squares along the middle 
### row of the array are coloured in yellow creating two equidimensional arrays 
### one above and one below this middle row. The equidimensional arrays have 
### dimensions ((n-1)/2)xm and consist of red and black squares. The objective 
### is to output a single array with dimensions equal to the equidimensional 
### arrays by comparing compare each corresponding square of the two 
### equidimensional arrays. If both squares are black, or if both squares are 
### red then the corresponding output square is set to black. If one square is 
### black and the other is red the corresponding output square is set to green.

### Solution Transform Description:
### I first extract the two equidimensional arrays from the original array. These 
### two lists correspond to the rows of black and red squares above and below 
### the line of yellow squares in the original array respectively. I then 
### simultaneously iterate through each corresponding row in these two arrays 
### comparing each of the corresponding elements. For each row pair if two 
### corresponding elements are equal (either both black or both red) then I add 
### 1 (a black square) to the ‘row’ list otherwise I add a 3 (a green square) 
### to the ‘row’ list. I construct the output array by adding this ‘row’ list 
### to the ‘overlay’ list for each row pair once every element in the row pair 
### had been iterated through.

### Test Results:
### All test results are returned correctly.
    
def solve_3428a4f5(x):
    # Convert to list
    x = x.tolist()  
    # Store the 
    list1 = []
    list2 = []
    # Store the output as a list of lists 
    overlay = []
    # For all the rows above the middle row
    for row in range(mt.floor(len(x)/2)):
        list1.append(x[row])
    # For all the rows below the middle row
    for row in range(mt.ceil(len(x)/2), len(x)):
        list2.append(x[row])
    # For each row in 'list1' and 'list2' respectively
    for i, j in zip (list1, list2):
        row = []
        # For each element in the respective rows
        for n, m in zip(i, j):
            # If the elements are equal (both black or both red)
            if n == m:
                row.append(0)
            # If the elements are not equal (one black and one red)
            else:
                row.append(3)
        # Add the list 'row' to the list 'overlay'
        overlay.append(row)
    # Convert the list x back to an array
    x = np.array(overlay)
    return x 



### Required Transform Description:
### The input consists of a nxm array where n and m can be equal or unequal. 
### Within is two randomly positioned squares are coloured red and green respectively. 
### The objective is to update the colour each square along the row containing 
### the red square in the direction of the green square until inline with the 
### green square to blue. Similarly, each square along the column containing 
### the green square in the direction of the red square until inline with the 
### red square also should be updated to blue. The red and green square remain 
### unchanged.

### Solution Transform Description:
### I first iterate through the inputted array and identified the location of 
### the red and green coloured squares. I store the two row and two column 
### indexes for these locations in four variables. I then change each square to 
### blue along the row containing the red square from the red square up to and 
### including the column index of the green square. Similarly, I change each 
### square to blue along the column containing the green square from the green 
### square up to and including the row index of the red square.

### Test Results:
### All test results are returned correctly.
    
def solve_a2fd1cf0(x):
    # Convert to list
    x = x.tolist()
    # Store the red row and column indexes 
    red_column = 0
    red_row = 0
    # Store the green row and column indexes
    green_column = 0
    green_row = 0
    # Iterate through each element of x (initial array) to locate the 
    # positions of the red and green squares.
    for i in x:
        for j in i:
            if j == 2:
                red_column = i.index(2)
                red_row = x.index(i)
            if j == 3:
                green_column = i.index(3)
                green_row = x.index(i)
    # Update the squares horizontal to the red square and verticle to the 
    # green square to blue as required considering the following layouts.
    # The red is located left of the green (not necessarily on the same row)
    if red_column < green_column:
        for column_index in range(red_column+1, green_column+1):
            x[red_row][column_index] = 8
    # The red is located right of the green (not necessarily on the same row)
    if red_column > green_column:
        for column_index in range(green_column+1, red_column ):
            x[red_row][column_index] = 8
    # The red is located above of the green (not necessarily on the same column)
    if red_row < green_row:
        for row_index in range(red_row, green_row):
            x[row_index][green_column] = 8
    # The red is located below of the green (not necessarily on the same column)
    if red_row > green_row:
        for row_index in range(green_row+1, red_row):
            x[row_index][green_column] = 8
    # Convert the list x back to an array
    x = np.array(x)
    return x



### Required Transform Description:
### The input array consists of a nxn (in this case 3x3) square array. A maximum 
### of one square in each column is coloured however it is possible for columns 
### to be completely uncoloured. For any row that contains a coloured square at 
### index x the objective is to update the index x of each row beneath this to 
### have the same colour.

### Solution Transform Description:
### To solve this, I create n nxn arrays (in this case three 3x3 arrays) each 
### with a unique column partially of fully coloured. I then add these arrays 
### together to get the final output array.

### Test Results:
### All test results are returned correctly.

def solve_d037b0a7(x):
    # Convert to list
    x = x.tolist()
    # List of unique arrays to be added together
    build = []
    # Iterate through each row in x (initial array) 
    for i in range(len(x)):
        # Define 'unique' list 
        unique = []
        # For each element in a row
        for j in range(len(x)):
            # If the elements column index is less then the elements row index 
            # add a list of length 3 containing only 0's to 'unique' list
            if j < i:
                zeros = []
                for k in range(len(x[i])):
                    zeros.append(0)
                unique.append(zeros)
            # Otherwise add a list of the rows original values to the 'unique' list
            else:
                unique.append(x[i])
        # Add an array of the list of lists 'unique' to the list 'build'        
        build.append(np.array(unique))
    # Add together three 3x3 arrays in the list 'build'
    x = sum(build)
    return x



### Summary and Reflection:
### For each of the solutions I use python lists as the patterns that we are 
### attempting to identify can be efficiently located using list indexing. In 
### certain cases, to reduce the number of calculations that would be involved 
### in large ‘for’ loop iterations, ‘itertools.combination’ function can be 
### used to generate n lists of lists of length two that are of relevance for 
### comparing. This reduces the number of comparison calculations to the ones 
### that are most likely to be relevant (an example of this can be seen in the 
### solve_06df4c85 function). For the majority of tasks, I focused on updating 
### values however in some cases where multiple arrays of non-overlapping colours 
### can be created the addition of arrays can be easily utilised. For task such 
### as this I used NumPy arrays as arrays can be easily added using NumPy arrays 
### compared with attempting to add elements of python lists. The adding of 
### arrays was however limited to cases where partial solutions represented by 
### multiple arrays of non-overlapping colours can be created. The reason for 
### this is due to the fact that each possible square colour is represented by 
### a unique integer and by adding these integers the range of possible values 
### will be exceeded or result in an incorrect colour being returned therefore 
### this method could only be used when adding colours to a blank array or when 
### adding multiple arrays with non-overlapping coloured squares. 



def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})" 
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals(): 
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join("..", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)
        
    
def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""
    
    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)

        
def show_result(x, y, yhat):
    print("Input")
    print(x)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    # if yhat has the right shape, then (y == yhat) is a bool array
    # and we test whether it is True everywhere. if yhat has the wrong
    # shape, then y == yhat is just a single bool.
    print(np.all(y == yhat))


if __name__ == "__main__": main()

