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

    print(f"New colum  :{colum,} to {new_colum} with {number}")
    return new_colum



def subtract_columns(colum0, colum1):
    new_colum = []
    for i in range(len(colum0)):
        new_colum.append(colum0[i] - colum1[i])

    print(f"Subtraction: {colum0} - {colum1} = {new_colum}")
    return new_colum



def matrix_zeros(matrix):
    changed_matrix = []

    #find the max colum number
    max_colum_number = 0
    for colum in matrix:
        max_colum_number += 1

    # find the max row number
    max_row_number = 0
    for row in matrix[0]:
        max_row_number += 1

    for row in range(max_row_number-2): #eins weniger wegen der informatik schreibweise und eines weils weniger sein soll
        print(f"changing ROW to {row}")

        for colum in range(1, max_colum_number): #first colum always stays the same
            print(f"changing COLUM to {colum}")

            if row == 0: #then we have the first row always calculated with the zero colum
                first_colum = calculate_new_column(matrix[0], matrix[colum][row])
                #print(f"First:{first_colum} number was {matrix[colum][row]}")
                new_colum = calculate_new_column(matrix[colum], matrix[0][row])
                # print(f"New:{new_colum}")
                co = subtract_columns(first_colum, new_colum)
                # print(co)
                matrix[colum] = co

            elif colum == max_colum_number-1: #if it is the last column we break
                #print(max_colum_number, colum)
                break

            else:  # for the other columns we need the colum from one above but for the right zero colum we can go one up
                colum = row+1 #the colum we want to change with the zeros is one more below
                print(f"actuall colum {colum}")
                column_above = calculate_new_column(matrix[colum-1], matrix[colum][row])
                colum_here = calculate_new_column(matrix[colum], matrix[colum-1][row])
                co = subtract_columns(column_above,colum_here)
                matrix[colum] = co

            print(matrix)
    return matrix





def get_equations(): #ask the user for equations
    pass




eqs = ["2x + 3y + 1z = 1","4x-1y+3z =11", "3x+1y-1z = 0"]
Matrix =equations_to_matrix(eqs)
print(Matrix)
changed = matrix_zeros(Matrix)
print(changed)


