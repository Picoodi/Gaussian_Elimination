def equations_to_matrix(equations): #we pass a list of equations and iterate over all of them to create a matrix of all components
    matrix = []

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
                    term = term.replace(char, "")
                    new_term.append(float(term))

        new_term.append(right)
        matrix.append(new_term)


    return matrix



def calculate_new_column(colum, number):
    new_colum = []
    for element in colum:
        new_colum.append(element * number)

    return new_colum



def subtract_columns(colum0, colum):
    new_colum = []
    for i in range(len(colum0)):
        new_colum.append(colum0[i] + colum[i])

    return new_colum



def matrix_zeros(matrix):
    changed_matrix = [matrix[0]]

    #find the max colum number
    max_colum_number = 0
    for colum in matrix:
        max_colum_number += 1




    for colum in range(1,max_colum_number):
        for row in range(colum):
            new_colum = calculate_new_column(matrix[colum], matrix[0][row])

            new_colum0 = calculate_new_column(matrix[0], matrix[colum][row])

            changed_matrix.append(subtract_columns(new_colum0, new_colum))

    return changed_matrix





def get_equations(): #ask the user for equations
    pass




eqs = ["2x + 3y + 1z = 1","4x-1y+3z =11", "3x+1y-1z = 0"]
Matrix =equations_to_matrix(eqs)
print(Matrix)
changed = matrix_zeros(Matrix)
print(changed)


