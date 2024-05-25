import tkinter
import main_


WALL_COLOR = 'white'
EMPTY_COLOR = 'gray'
BG_COLOR = 'black'
EXIT_COLOR = 'green'
PLAYER_START_POS = [1, 1]


'''
TODO: выход по ESC, поставить по центру
'''


class App:
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.attributes('-fullscreen', True)
        self.cols = main_.COLS
        self.rows = main_.ROWS
        self.maze = main_.make_maze()
        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        self.cell_size = min(self.width // self.cols, self.height // self.rows) - 7
        self.window['bg'] = BG_COLOR
        self.canvas_width = self.cell_size * self.cols
        self.canvas_height = self.cell_size * self.rows
        self.window_padding = (self.width - (self.cell_size * self.cols)) // 2
        self.canvas = tkinter.Canvas(
            self.window,
            width=self.width // self.cell_size * self.cell_size,
            height=self.height // self.cell_size * self.cell_size,
            bg=BG_COLOR,
            highlightthickness=0,
        )
        self.player = Player(
            PLAYER_START_POS[0],
            PLAYER_START_POS[1],
            self.canvas,
            self.maze,

        )
        self.canvas.pack()
        self.canvas.update()
        self.draw_maze()
        self.window.mainloop()

    def draw_maze(self):
        for row_idx, row in enumerate(self.maze):
            print(row_idx, *row)
            for col_idx, col in enumerate(row):
                if col == main_.WALL:
                    self.canvas.create_rectangle(
                        col_idx * self.cell_size + self.window_padding,
                        row_idx * self.cell_size,
                        col_idx * self.cell_size + self.cell_size + self.window_padding,
                        row_idx * self.cell_size + self.cell_size,
                        fill=WALL_COLOR,
                    )
                elif col == main_.EXIT:
                    self.canvas.create_rectangle(
                        col_idx * self.cell_size + self.window_padding,
                        row_idx * self.cell_size,
                        col_idx * self.cell_size + self.cell_size + self.window_padding,
                        row_idx * self.cell_size + self.cell_size,
                        fill=EXIT_COLOR,
                    )
                elif col == main_.EMPTY:
                    self.canvas.create_rectangle(
                        col_idx * self.cell_size + self.window_padding,
                        row_idx * self.cell_size,
                        col_idx * self.cell_size + self.cell_size + self.window_padding,
                        row_idx * self.cell_size + self.cell_size,
                        fill=EMPTY_COLOR,
                    )


class Game:
    def __init__(self) -> None:
        pass


class Player:
    def __init__(
            self,
            col: int,
            row: int,
            canvas: tkinter.Canvas,
            maze: list,
    ) -> None:
        self.col = col
        self.row = row
        self.canvas = canvas
        self.maze = maze


App()
