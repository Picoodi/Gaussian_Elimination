#necessary library that would have the power to solve the system from the start bt that would not be much fun.
from sympy import symbols, Eq, solve


# we pass a list of equations and iterate over all of them to create a matrix of all components and also create a list with all variables in the system.
# #We return that matrix and the list of variables
def equations_to_matrix(equations):
    matrix = []
    variable_names = []

    for equation in equations:
        equation = equation.replace(" ", "").replace("=", "=")
        sides = equation.split("=")   #we split at the = because the right side of = is always just one number and the left has variables in it
        left, right  = sides[0], float(sides[1])

        terms = left.replace("-", "+-").split("+") #makes it easy to split at +

        abc = "abcdefghijklmnopqrstuvwxyz"  # String with all possible variables
        new_term = []
        for term in terms:
            for char in term:

                if char in abc:
                    if char in variable_names: #we check, so the variable is stored not multiple times
                        pass
                    else:
                        variable_names.append(char)

                    term = term.replace(char, "") #delete the char because it is not a number
                    new_term.append(float(term))

        new_term.append(right)
        matrix.append(new_term)


    return matrix, variable_names #we return 2 things



#This function calculates the new row of a matrix with the given number
def calculate_new_rows(row, number):
    new_row = []
    for element in row:
        new_row.append(element * number)

    return new_row


#This function take two matrix rows and subtracts them from each other and returns one new row
def subtract_rows(row0, row1):
    new_row = []
    for i in range(len(row0)):
        new_row.append(row0[i] - row1[i])

    return new_row


#This function creates the upper triangular matrix and from the given matrix and returns the new one
def matrix_zeros(matrix):

    #find the max row number
    max_row_number = 0
    for row in matrix:
        max_row_number += 1

    # find the max colum number
    max_colum_number = 0
    for colum in matrix[0]:
        max_colum_number += 1

    #going through the matrix with 2 for loops one for columns and one for rows of the matrix
    # -2 because one less of the IT counting from 0 and one because the function changes the numbers in the row one below
    for colum in range(max_colum_number - 2):

        # first row always stays the same so we start at index 1
        for row in range(1, max_row_number):

            # we have the first colum always calculated with the row at index 0
            if colum == 0:
                matrix[row]= subtract_rows(calculate_new_rows(matrix[0], matrix[row][colum]),
                                           calculate_new_rows(matrix[row], matrix[0][colum]))

            # if it is the last row we break because we already changed it.
            elif row == max_row_number-1:
                break

            #for all the other rows we just do the algorithm
            else:
                row = colum + 1 #the row where the number needs to be changed to 0, is the colum index+1.
                matrix[row]= subtract_rows(calculate_new_rows(matrix[row - 1], matrix[row][colum]),
                                           calculate_new_rows(matrix[row], matrix[row - 1][colum]))


    return matrix


#The function solves the matrix with the corresponding variables and uses sympy for that.
def solve_matrix_equations(matrix, var_names):
    variables = symbols(' '.join(var_names))

    equations = [] #a list where all equations are going get stored
    for row in matrix: #each row represents one equation
        left_side = sum(coef * var for coef, var in zip(row[:-1], variables))
        right_side = row[-1]
        equation = Eq(left_side, right_side)
        equations.append(equation)

    return solve(equations) #returning a list in the form of e.g. {x: 0.307692307692308, y: 0.461538461538462}

#tThis equation explains how to use the program and asks repeatedly for new equations until the user leaves a blank and presses Enter
#Then we return a list of all equations
def get_equations(): #ask the user for equations
    print(f"Hello there! \n"
          f"Plz insert yor equations one by one! \n"
          f"When you are finished press ENTER. \n"
          f"The Equations NEED to be typed in the form \n"
          f"3x+2y + z = 1 \n"
          f"4x-1y+3z = 11 \n"
          f"so that every variable has a number in front of it, \n"
          f"the solutions are on the right side of the = \n"
          f"and the variables are in order in each equation!")

    equations_list = []
    equation = None

    while equation != "":
        print("Whats your equation: ")
        equation = str(input())
        if equation == "":
            pass
        else:
            equations_list.append(equation)

    return equations_list




#only if the file is called main then we run it
if __name__ == '__main__':
    #all the print statements create a nice visual output about the process
    #they are not needed if you don´t want.
    #The function calls are necessary on the other hand

    Equations = get_equations()
    print(f"The linear equation system with the equations:")
    for eq in range(len(Equations)):
        print(f"{eq+1}:  {Equations[eq]}")
    print("")

    Matrix, Variable_names =equations_to_matrix(Equations)
    print(f"And the variables: \n {Variable_names}")
    print("")

    print(f"Creates a matrix of the form:")
    for Row in Matrix:
        print(Row)
    print("")

    Changed_Matrix = matrix_zeros(Matrix)
    solution = solve_matrix_equations(Matrix, Variable_names)
    print(f"Creates a new matrix of the form:")
    for Row in Changed_Matrix:
        print(Row)
    print("")

    print("Has the solutions: ")
    for var, value in solution.items():
        print(f"{var} = {value}")