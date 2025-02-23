c = [2,3,1,1]
z = [4,-1,3,11]


def calculate_new_column(colum, number):
    new_colum = []
    for element in colum:
        new_colum.append(element * number)
    print(new_colum)
    return new_colum



def subtract_columns(colum0, colum):
    new_colum = []
    for i in range(len(colum0)):
        new_colum.append(colum0[i] - colum[i])

    return new_colum

sol = subtract_columns(calculate_new_column(c,4), calculate_new_column(z, 2))
print(sol)