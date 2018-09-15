
import numpy as np
import math

class Clashes:
    
    ## constructor does not do anything
    def __init__(self):
#         self.chromosome=[2,4,7,4,8,5,5,2];
#         self.chromosome=[3,2,7,5,2,4,1,1];
#         self.chromosome=[2,4,4,1,5,1,2,4];
#         self.chromosome=[3,2,5,4,3,2,1,3];
##        GA Crossover Quiz
#         self.chromosome=[3,2,7,4,8,5,5,2];
#         self.chromosome=[3,2,7,5,2,1,2,4];        
        self.chromosome=[2,4,7,5,2,4,1,1];                

    def final_value(self, grid):        
        row_clashes = self.calculate_row_clashes(grid);
        column_clashes = self.calculate_column_clashes(grid)
        forward_diag_clashes = self.calculate_forward_diag_clashes(grid)
        backward_diag_clashes = self.calculate_backward_diag_clashes(grid)
        return 28 - (row_clashes + column_clashes + forward_diag_clashes + backward_diag_clashes);


    def nCr(self, n,r):
        f = math.factorial
        return f(n) // f(r) // f(n-r)

    def calculate_column_clashes(self, grid):
        ncols = 8
        column_clashes = 0
        for i in range(ncols):
            column_array = self.get_column_array(grid, i)
            if(column_array[i].count('Q') > 1):
                n_c_r = self.nCr(column_array[i].count('Q'), 2)
                column_clashes +=  n_c_r
                print(column_array[i], n_c_r)                        
        return column_clashes


    def calculate_row_clashes(self, grid):
        row_clashes = 0
        row_array = self.get_rows(grid)
        for i in range(len(row_array)):
            if(row_array[i].count('Q') > 1):
                n_c_r = self.nCr(row_array[i].count('Q'), 2)
                row_clashes +=  n_c_r
                print(row_array[i], n_c_r)
        return row_clashes


    def calculate_forward_diag_clashes(self, grid):
        forward_clashes = 0
        forward_diag = self.get_forward_diagonals(grid)
        print(forward_diag)
        for i in range(len(forward_diag)):
            print(forward_diag[i], forward_diag[i].count('Q'))
            if(forward_diag[i].count('Q') > 1):
                n_c_r = self.nCr(forward_diag[i].count('Q'), 2)
                print(n_c_r)
                forward_clashes += n_c_r
        return forward_clashes

    def calculate_backward_diag_clashes(self, grid):
        backward_clashes = 0
        reverse_diag = self.get_backward_diagonals(grid)        
        print(reverse_diag)
        for j in range(len(reverse_diag)):
            print(reverse_diag[j], reverse_diag[j].count('Q'))
            if (reverse_diag[j].count('Q') > 1):
                n_c_r = self.nCr(reverse_diag[j].count('Q'), 2)
                print(n_c_r)
                backward_clashes += n_c_r
        return backward_clashes;

    def get_rows(self, grid):
        return [[c for c in r] for r in grid]


    def get_cols(self, grid):
        return zip(*grid)


    def get_column_array(self, grid, i):
        return [row[i] for row in grid]

    def get_backward_diagonals(self, grid):
        b = [None] * (len(grid) - 1)
        grid = [b[i:] + r + b[:i] for i, r in enumerate(self.get_rows(grid))]
        return [[c for c in r if not c is None] for r in self.get_cols(grid)]
    
    def get_forward_diagonals(self, grid):
        b = [None] * (len(grid) - 1)
        grid = [b[:i] + r + b[i:] for i, r in enumerate(self.get_rows(grid))]
        return [[c for c in r if not c is None] for r in self.get_cols(grid)]    


        
##client call
##array = ['2','4','7','5','8','5','5','2']
matrix = np.array([
            ['0','0','0','0','0','0','0','0'],
            ['Q','0','0','0','0','0','0','Q'],
            ['0','0','0','0','0','0','0','0'],
            ['0','Q','0','0','0','0','0','0'],
            ['0','0','0','Q','0','Q','Q','0'],
            ['0','0','0','0','0','0','0','0'],
            ['0','0','Q','0','0','0','0','0'],
            ['0','0','0','0','Q','0','0','0']
            ])
clash = Clashes()
total_clash = clash.final_value(matrix)
print('final value : ', total_clash)
