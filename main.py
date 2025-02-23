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

    #print(f"New colum  :{colum,} to {new_colum} with {number}")
    return new_colum



def subtract_columns(colum0, colum1):
    new_colum = []
    for i in range(len(colum0)):
        new_colum.append(colum0[i] - colum1[i])

    #print(f"Subtraction: {colum0} - {colum1} = {new_colum}")
    return new_colum



def matrix_zeros(matrix):


    #find the max colum number
    max_colum_number = 0
    for colum in matrix:
        max_colum_number += 1

    # find the max row number
    max_row_number = 0
    for row in matrix[0]:
        max_row_number += 1

    for row in range(max_row_number-2):  #One less cause ones of the IT counting from 0 and one because the solution elements don´t need to be changed
        #print(f"changing ROW to {row}")

        for colum in range(1, max_colum_number): #first colum always stays the same so we start at index 1
            #print(f"changing COLUM to {colum}")

            if row == 0: #then we have the first row always calculated with the zero colum
                #first_colum = calculate_new_column(matrix[0], matrix[colum][row])
                #print(f"First:{first_colum} number was {matrix[colum][row]}")
                #new_colum = calculate_new_column(matrix[colum], matrix[0][row])
                # print(f"New:{new_colum}")
                matrix[colum]= subtract_columns(calculate_new_column(matrix[0], matrix[colum][row]),  calculate_new_column(matrix[colum], matrix[0][row]) )
                # print(co)
                #matrix[colum] = co

            elif colum == max_colum_number-1: #if it is the last column we break because we already changed it. See further comments
                #print(max_colum_number, colum)
                break

            else:
                colum = row+1 #the colum where the number needs to be changed to 0, is the row index+1.
                #print(f"actual colum {colum}")
                #column_above = calculate_new_column(matrix[colum-1], matrix[colum][row])
                #colum_here = calculate_new_column(matrix[colum], matrix[colum-1][row])
                matrix[colum]= subtract_columns(calculate_new_column(matrix[colum-1], matrix[colum][row]), calculate_new_column(matrix[colum], matrix[colum-1][row]))
                #matrix[colum] = co

            #print(matrix)
    return matrix





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
Matrix =equations_to_matrix(eqs)
print(Matrix)
changed = matrix_zeros(Matrix)
print(changed)