from tkinter import *
import random

GRID_SIZE = 9
root = Tk()
p1 = PhotoImage(file = 'sudoku.png')
root.iconphoto(False, p1)
 
class MainWindow():
    

    def __init__(self, gui, width, height):
 
        self.SOLVED, self.NOT_SOLVED, self.INCORRECT = "Solved", "Not Solved", "Incorrect!"

        self.solution_status = StringVar(gui)
        self.gui = gui
        gui.title("IITU Sudoku")

        self.width, self.height = width, height
   
        gui.geometry(f'{width}x{420}')  


        font = ('Arial', 18)

        color = 'white'


        Label(root, text = "Generate New Grid",font = ('Helvetica 11 bold')).place( x = 60, y = 290)
        Button(root, text = 'Easy', command  = self.generate_new_grid, bg = 'black', fg = 'white' ).place( x = 20, y = 320)
        Button(root, text = 'Medium', command  = self.generate_new_gridm, bg = 'black', fg = 'white').place( x = 103, y = 320)
        Button(root, text = 'Hard', command  = self.generate_new_gridh, bg = 'black', fg = 'white').place( x = 210, y = 320)
        Button(root, text = 'Check Solution', command  = self.check_solution, bg = 'black', fg = 'white').place( x = 85, y = 360)
        Label(root, textvariable = self.solution_status, fg='grey',font = ('Helvetica 9 bold')).place( x = self.width/4-5, y = self.height+50)

        self.gui_grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

 
        self.correct_solution_grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]


        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):

                if (row < 3 or row > 5) and (column < 3 or column > 5):
                    color = 'light sky blue'
                elif row in [3,4,5] and column in [3,4,5]:
                    color = 'light sky blue'
                else:
                    color = 'white'
                
                self.gui_grid[row][column] = Entry(gui, width = 2, font = font, bg = color, cursor = 'arrow', borderwidth = 0,
                                                 highlightcolor = 'red', highlightthickness = 1, highlightbackground = 'black',
                                                 textvar = main_sudoku_grid[row][column])
                self.gui_grid[row][column].bind('<Motion>', self.ammend_grid)
                self.gui_grid[row][column].bind('<FocusIn>', self.ammend_grid)
                self.gui_grid[row][column].bind('<Button-1>', self.ammend_grid)
                self.gui_grid[row][column].grid(row=row, column=column)



        # generate new grid function
        self.generate_new_grid()
        



    # ammend the cells in the grid if values are incorrect. 
    def ammend_grid(self, event):
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                if main_sudoku_grid[row][column].get() == '':
                    continue
                if len(main_sudoku_grid[row][column].get()) > 1 or main_sudoku_grid[row][column].get() not in ['1','2','3','4','5','6','7','8','9']:
                    main_sudoku_grid[row][column].set('')



    def clear_grid(self):
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                main_sudoku_grid[row][column].set('')


    def generate_new_grid(self):
        self.clear_grid()
        self.randomize_top_row()
        self.solve_grid()
        self.save_grid()
        self.hide_solutione()
        self.solution_status.set(f"Game State: {self.NOT_SOLVED}")
    def generate_new_gridm(self):
        self.clear_grid()
        self.randomize_top_row()
        self.solve_grid()
        self.save_grid()
        self.hide_solutionm()
        self.solution_status.set(f"Game State: {self.NOT_SOLVED}")
    def generate_new_gridh(self):
        self.clear_grid()
        self.randomize_top_row()
        self.solve_grid()
        self.save_grid()
        self.hide_solutionh()
        self.solution_status.set(f"Game State: {self.NOT_SOLVED}")        

    def solve_grid(self):
        solution = SolveSudoku()  
    
    def randomize_top_row(self):
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        number_choice = random.sample(number_list, len(number_list))

        for n in range(GRID_SIZE):
            main_sudoku_grid[0][n].set(number_choice[n])
    
    def hide_solutione(self):
        CHANCE_TO_HIDE = 63 
        for column in range(GRID_SIZE):
            for row in range(GRID_SIZE):
                random_roll = random.randint(0, 100)
                if random_roll < CHANCE_TO_HIDE:
                    main_sudoku_grid[row][column].set('')
    def hide_solutionm(self):
        CHANCE_TO_HIDE = 77 
        for column in range(GRID_SIZE):
            for row in range(GRID_SIZE):
                random_roll = random.randint(0, 100)
                if random_roll < CHANCE_TO_HIDE:
                    main_sudoku_grid[row][column].set('')
    def hide_solutionh(self):
        CHANCE_TO_HIDE = 87 
        for column in range(GRID_SIZE):
            for row in range(GRID_SIZE):
                random_roll = random.randint(0, 100)
                if random_roll < CHANCE_TO_HIDE:
                    main_sudoku_grid[row][column].set('')

    def save_grid(self):
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                self.correct_solution_grid[row][column] = main_sudoku_grid[row][column].get()

    def is_correct_grid(self):
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                if main_sudoku_grid[row][column].get() != self.correct_solution_grid[row][column]:
                    return False
        return True
    
    def check_solution(self):
        if self.is_correct_grid():
            self.solution_status.set(f"Game State: {self.SOLVED}")
        else:
            self.solution_status.set(f"Game State: {self.INCORRECT}")
            

    


class SolveSudoku():
    
    def __init__(self):
        self.set_all_zero()
        self.sudoku_solve()


    def set_all_zero(self):
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                if main_sudoku_grid[row][column].get() not in ['1','2','3','4','5','6','7','8','9']:
                    main_sudoku_grid[row][column].set(0)

    
    
    def sudoku_solve(self, i=0, j=0):
        i,j = self.fill_next_cell(i, j)

        if i == -1:
            return True
        for e in range(1,10):
            if self.is_valid_cell(i,j,e):
                main_sudoku_grid[i][j].set(e)
                if self.sudoku_solve(i, j):
                    return True
                # set back to 0 for backtracking. 
                main_sudoku_grid[i][j].set(0)
        return False


    def fill_next_cell(self, i, j):
        for row in range(i, GRID_SIZE):
            for column in range(j, GRID_SIZE):
                if main_sudoku_grid[row][column].get() == '0':
                    return row,column

        for row in range(0, GRID_SIZE):
            for column in range(0, GRID_SIZE):
                if main_sudoku_grid[row][column].get() == '0':
                    return row,column

        return -1,-1



    def is_valid_cell(self, row, column, e):
        for x in range(GRID_SIZE):
            if main_sudoku_grid[row][x].get() == str(e):
                return False
        for x in range(GRID_SIZE):
            if main_sudoku_grid[x][column].get() == str(e):
                return False

        secTopX, secTopY = 3 *int((row/3)), 3 *int((column/3))
        for row in range(secTopX, secTopX+3):
            for column in range(secTopY, secTopY+3):
                if main_sudoku_grid[row][column].get() == str(e):
                    return False
        
        return True

# our main 9x9 sudoku grid
main_sudoku_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

for row in range(GRID_SIZE):
    for column in range(GRID_SIZE):
        main_sudoku_grid[row][column] = StringVar(root)

# passing the main root window into the MainWindow class for actual GUI construction. 
sudoku_application = MainWindow(root, 540, 670)
# running tkinter mainloop to display GUI
root.mainloop()
