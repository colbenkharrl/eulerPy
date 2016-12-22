# Colben Kharrl | December 2016 | Project Euler Problem 15

##
##    Description:
##    Starting in the top left corner of a 2×2 grid, and only being
##    able to move to the right and down, there are exactly 6 routes
##    to the bottom right corner.
##    How many such routes are there through a 20×20 grid?
##

#   class to hold grid
class direct_grid:
    #   init; set grid states
    def __init__(self, size):
        self.size = size
        self.grid = []
        for i in range(size + 1):
            self.grid.append([])
            for j in range(size+1):
                #    state definition: 3 = open, 2 = bottom, 1 = right edge, 0 = goal
                next_states = 3
                if i == size: next_states -= 1
                if j == size: next_states -= 2
                self.grid[i].append([next_states])

    #   recursive function to find number of paths from grid point
    def find_paths_from_point(self, row, col):
        solutions = 0
        if len(self.grid[row][col]) > 1:
            solutions = self.grid[row][col][1]
        else:
            if self.grid[row][col][0] == 0:
                solutions += 1
            elif self.grid[row][col][0] == 1:
                solutions += self.find_paths_from_point(row + 1, col)
            elif self.grid[row][col][0] == 2:
                solutions += self.find_paths_from_point(row, col + 1)
            else:
                solutions += self.find_paths_from_point(row + 1, col)
                solutions += self.find_paths_from_point(row, col + 1)
            self.grid[row][col].append(solutions)
        return solutions

#   beginning of code execution
width = 20
grid = direct_grid(width)
answer = grid.find_paths_from_point(0,0)
print("Number of paths in a 20x20 grid:", answer)
