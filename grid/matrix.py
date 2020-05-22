class Matrix:
    def __init__(self, rows, cols):
        self.__cols: int = cols
        self.__rows: int = rows
        self.__blocs = [[x for x in range(self.__cols)] for y in range(self.__rows)]

    def set_bloc_at_position(self, x: int, y: int, value):
        if (0 <= y < self.__cols) and (0 <= x < self.__rows):
            self.__blocs[x][y] = value

    def get_bloc_at_position(self, x, y):
        if (0 <= y < self.__cols) and (0 <= x < self.__rows):
            return self.__blocs[x][y]

    def delete_bloc_at_position(self, x, y):
        if (0 <= y < self.__cols) and (0 <= x < self.__rows):
            # TODO: We shouldn't delete but replace with an empty bloc
            del self.__blocs[x][y]

    def get_row_at_position(self, y):
        if 0 <= y < self.__rows:
            return self.__blocs[y]

    def get_col_at_position(self, x):
        if 0 <= x < self.__cols:
            ret = []
            for bloc in self.__blocs:
                ret.append(bloc[x])
            return ret

    def set_row_at_position(self, row, value):
        if 0 <= row < self.__rows:
            for x in range(len(self.__blocs[row])):
                self.__blocs[row][x] = value

    def set_col_at_position(self, col, value):
        if 0 <= col < self.__cols:
            for bloc in self.__blocs:
                bloc[col] = value

    def insert_row_at_position(self, row, value):
        if 0 <= row < self.__rows:
            new_row = []
            for i in range(self.__cols):
                new_row.append(value)
            self.__blocs.insert(row, new_row)
            self.__rows += 1

    def insert_col_at_position(self, col, value):
        if 0 <= col < self.__cols:
            for row in self.__blocs:
                row.insert(col, value)
            self.__cols += 1

    def delete_row(self, row):
        if 0 <= row < self.__rows:
            del self.__blocs[row]
            self.__rows -= 1

    def delete_col(self, col):
        if 0 <= col < self.__cols:
            for r in self.__blocs:
                del r[col]
            self.__cols -= 1

    def fill_with_value(self, value):
        for row in range(len(self.__blocs)):
            for col in range(len(self.__blocs[row])):
                self.__blocs[row][col] = value

    def get_row_number(self):
        return self.__rows

    def get_col_number(self):
        return self.__cols

    def print(self):
        print(self.__blocs)
