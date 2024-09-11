

def create_multiplication_table(columns: int, column_start: int, rows: int, rows_start: int):

    # Headers
    print("{0:^5}|".format(''), end=" ")
    for column_number in range(column_start, column_start + columns):
        print('{0:^5}'.format(column_number), end=' ')
    print()
    for column_number in range(column_start, column_start + columns + 1):
        print('{:{fill}^5}'.format("", fill="—"), end=" ")
    print()


    for row_number in range(rows_start, rows_start + rows):
        print('{0:^5}|'.format(row_number), end=' ')
        for column_number in range(column_start, column_start + columns):
            print('{0:^5}'.format(column_number * row_number), end=' ')
        print()

if __name__ == "__main__":
    create_multiplication_table(5, 27, 8, 10)