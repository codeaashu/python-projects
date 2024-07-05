import tkinter as tk
import random

class Game2048:
    def __init__(self, master):
        self.master = master
        self.master.title("2048")
        self.master.geometry("400x400")
        self.master.bind("<Key>", self.handle_key)

        self.grid_size = 4
        self.grid = [[0] * self.grid_size for _ in range(self.grid_size)]
        self.score = 0

        self.init_grid()
        self.add_tile()
        self.update_grid()

    def init_grid(self):
        self.tiles = []
        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                tile = tk.Label(self.master, text="", font=("Helvetica", 32), width=4, height=2, relief="raised")
                tile.grid(row=i, column=j, padx=5, pady=5)
                row.append(tile)
            self.tiles.append(row)

    def add_tile(self):
        empty_cells = [(i, j) for i in range(self.grid_size) for j in range(self.grid_size) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4

    def update_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                value = self.grid[i][j]
                if value == 0:
                    self.tiles[i][j].configure(text="", bg="lightgray")
                else:
                    self.tiles[i][j].configure(text=str(value), bg="lightblue")
        self.master.update_idletasks()

    def handle_key(self, event):
        if event.keysym in ['Up', 'Down', 'Left', 'Right']:
            self.move_tiles(event.keysym)
            self.add_tile()
            self.update_grid()
            if self.check_game_over():
                print("Game Over! Score:", self.score)

    def move_tiles(self, direction):
        if direction == 'Up':
            self.grid = self.transpose(self.grid)
            self.grid = self.merge_tiles(self.grid)
            self.grid = self.transpose(self.grid)
        elif direction == 'Down':
            self.grid = self.reverse(self.transpose(self.grid))
            self.grid = self.merge_tiles(self.grid)
            self.grid = self.transpose(self.reverse(self.grid))
        elif direction == 'Left':
            self.grid = self.merge_tiles(self.grid)
        elif direction == 'Right':
            self.grid = self.reverse(self.grid)
            self.grid = self.merge_tiles(self.grid)
            self.grid = self.reverse(self.grid)

    def merge_tiles(self, grid):
        score = 0
        for i in range(self.grid_size):
            j = 0
            while j < self.grid_size - 1:
                if grid[i][j] == grid[i][j+1] and grid[i][j] != 0:
                    grid[i][j] *= 2
                    score += grid[i][j]
                    grid[i][j+1] = 0
                    j += 2
                else:
                    j += 1
        self.score += score
        return grid

    def check_game_over(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j] == 0:
                    return False
                if j < self.grid_size - 1 and self.grid[i][j] == self.grid[i][j+1]:
                    return False
                if i < self.grid_size - 1 and self.grid[i][j] == self.grid[i+1][j]:
                    return False
        return True

    @staticmethod
    def transpose(matrix):
        return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

    @staticmethod
    def reverse(matrix):
        return [row[::-1] for row in matrix]

def main():
    root = tk.Tk()
    game = Game2048(root)
    root.mainloop()

if __name__ == "__main__":
    main()