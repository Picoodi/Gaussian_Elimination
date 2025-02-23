from sympy import symbols, Eq, solve


def equations_to_matrix(equations): #we pass a list of equations and iterate over all of them to create a matrix of all components
    matrix = []
    variable_names = []

    for equation in equations:
        equation = equation.replace(" ", "").replace("=", "=")
        sides = equation.split("=")
        left, right  = sides[0], float(sides[1])

        terms = left.replace("-", "+-").split("+")

        abc = "abcdefghijklmnopqrstuvwxyz"  # String with all possible variables
        new_term = []
        for term in terms:
            for char in term:

                if char in abc:
                    if char in variable_names:
                        pass
                    else:
                        variable_names.append(char)

                    term = term.replace(char, "")
                    new_term.append(float(term))

        new_term.append(right)
        matrix.append(new_term)


    return matrix, variable_names



def calculate_new_rows(row, number):
    new_row = []
    for element in row:
        new_row.append(element * number)

    return new_row



def subtract_rows(row0, row1):
    new_row = []
    for i in range(len(row0)):
        new_row.append(row0[i] - row1[i])

    return new_row



def matrix_zeros(matrix):

    #find the max row number
    max_row_number = 0
    for row in matrix:
        max_row_number += 1

    # find the max colum number
    max_colum_number = 0
    for colum in matrix[0]:
        max_colum_number += 1

    #going through the matrix
    for colum in range(max_colum_number - 2):  #One less cause ones of the IT counting from 0 and one because the solution elements don´t need to be changed

        for row in range(1, max_row_number): #first row always stays the same so we start at index 1

            if colum == 0: #then we have the first colum always calculated with the zero row
                matrix[row]= subtract_rows(calculate_new_rows(matrix[0], matrix[row][colum]),
                                           calculate_new_rows(matrix[row], matrix[0][colum]))

            elif row == max_row_number-1: #if it is the last row we break because we already changed it. See further comments
                break
            else:
                row = colum + 1 #the row where the number needs to be changed to 0, is the colum index+1.
                matrix[row]= subtract_rows(calculate_new_rows(matrix[row - 1], matrix[row][colum]),
                                           calculate_new_rows(matrix[row], matrix[row - 1][colum]))


    return matrix




def build_equation(row, var_names):
    variables = symbols(' '.join(var_names))
    left_side = sum(coef * var for coef, var in zip(row[:-1], variables) if coef != 0)
    right_side = row[-1]
    return Eq(left_side, right_side)





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
    eq = None

    while eq != "":
        print("Whats your equation: ")
        eq = str(input())
        if eq == "":
            pass
        else:
            equations_list.append(eq)

    return equations_list



#eqs = get_equations()
eqs = ["2x + 3y + 1z = 1","4x-1y+3z =11", "3x+1y-1z = 0"]
Matrix, Variable_names =equations_to_matrix(eqs)
print(Matrix)
changed = matrix_zeros(Matrix)
