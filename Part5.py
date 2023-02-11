# 5.1.1 The longest string
def longest(strings : list):
    length = 0
    word = ""
    for item in strings:
        if len(item) > length:
            length = len(item)
            word = item
    return word

# 5.1.2 Number of matching elements
def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for row in my_matrix:
        count += row.count(element) 
    return count

# 5.1.3 Go
def who_won(game_board: list):
    count1 = 0
    count2 = 0
    for row in game_board:
        count1 += row.count(1)
        count2 += row.count(2)
    
    if count1 > count2:
        return 1
    elif count1 < count2:
        return 2
    else:
        return 0

# 5.1.4 Sudoku: check row
def row_correct(sudoku: list, row_no:int):
    for i in range(len(sudoku[row_no])):
        number = sudoku[row_no][i]
        if number == 0:
            continue

        
        if sudoku[row_no].count(number) == 1:
            continue
        else:
            return False
    
    return True

# 5.1.5 Sudoku: check column
def column_correct(sudoku: list, column_no: int):
    temp = []
    for row in sudoku:
        number = row[column_no]
        if number == 0:
            continue

        if number in temp:
            return False
        else:
            temp.append(row[column_no])
            
    return True
        
# 5.1.6 Sudoku: check block
def block_correct(sudoku: list, row_no: int, column_no: int):
    temp = []
    for i in range(row_no, row_no+3):
        for j in range(column_no, column_no+3):
            number = sudoku[i][j]
            if number == 0:
                continue

            if number in temp:
                return False
            else:
                temp.append(number)

    return True

# 5.1.7 Sudoku: check grid
def sudoku_grid_correct(sudoku: list):
    # Check rows
    for i in range(9):
        if row_correct(sudoku, i):
            continue
        else:
            return False

    # Check columns
    for i in range(9):
        if column_correct(sudoku, i):
            continue
        else:
            return False

    # Check block
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            if block_correct(sudoku, i, j):
                continue
            else:
                return False

    return True

# 5.2.1 Items multiplied by two
def double_items(numbers: list):
    new_numbers = []
    for item in numbers:
        new_numbers.append(item * 2)
    return new_numbers

# 5.2.2 Remove the smallest
def remove_smallest(number: list):
    number.remove(min(number))

# 5.2.3 Sudoku: print out the grid and add a number
def print_sudoku(sudoku: list):
    height = 0
    for row in sudoku:
        height += 1
        if height == 4 or height == 7:
            print()

        for i in range(len(row)):
            if i == 3 or i == 6:
                print(" ", end="")

            if i == 0 and row[i] > 0:
                print(row[i], end="")
                continue
            elif i == 0 and row[i] == 0:
                print("_", end="")
                continue 
            
            if row[i] > 0:
                print(f" {row[i]}", end="") 
            else:
                print(" _", end="")
        print()

# Sudoku: add number to a copy of the grid