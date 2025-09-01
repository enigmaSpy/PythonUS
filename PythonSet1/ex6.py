# Napisz program, który wyznacza odległość Levenshteina dla dwóch zadanych łańcuchów znaków.

def levenshtine(str1: str, str2: str):
    rows, cols = len(str2) + 1, len(str1) + 1
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(cols):
        matrix[0][i] = i
    for j in range(rows):
        matrix[j][0] = j

    for i in range(1, rows):
        for j in range(1, cols):
            if str1[j - 1] == str2[i - 1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,      
                matrix[i][j - 1] + 1,      
                matrix[i - 1][j - 1] + cost 
            )

    print(matrix[rows - 1][cols - 1])

levenshtine("ala", "aaal")