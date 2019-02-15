import numpy as np


class Snake():
    def __init__(self, board):
        self.input = 8
        self.output = 4
        self.snake = [[int(board[0] / 2), int(board[1] / 2)]]
        self.fruit = []
        self.board = board
        self.score = 0
        self.new_fruit()

    def run_genome(self, g):
        order = g.assemble()
        done = False
        time = 0
        while not done:
            time += 1
            action = max(g.run(self.get_state(), order))
            self.act(action)
            done = self.is_dead()
        score = self.score
        self.reset()
        return score, time

    def act(self, action):
        if action == 0:
            snake = self.snake.append[[self.snake[-1][0], self.snake[-1][1] + 1]]
            # move up
        elif action == 1:
            snake = self.snake.append[[self.snake[-1][0] + 1, self.snake[-1][1]]]
            # move right
        elif action == 2:
            snake = self.snake.append[[self.snake[-1][0], self.snake[-1][1] - 1]]
            # move down
        elif action == 3:
            snake = self.snake.append[[self.snake[-1][0] - 1, self.snake[-1][1]]]
            # move left
        else:
            print("Not an Action")
            return

        if snake[-1] == self.fruit:
            self.score += 1
            self.snake = snake
            self.new_fruit()
            return
            # landed on fruit
        else:
            self.snake = snake[1:]
            return

    def reset(self):
        self.snake = [[int(self.board[0] / 2), int(self.board[1] / 2)]]
        self.score = 0
        self.new_fruit()

    def new_fruit(self):
        grid = np.vstack(np.meshgrid(np.linspace(0, self.board[0], num=self.board[0], endpoint=False),
                                     np.linspace(0, self.board[1], num=self.board[1], endpoint=False))).T
        for p in self.snake:
            grid.remove(p)
        self.fruit = np.random.choice(grid)

    def is_dead(self):
        if self.snake[-1][0] >= self.board[0] or self.snake[-1][1] >= self.board[1] or self.snake[-1][1] < 0 or \
                self.snake[-1][0] < 0:
            # out of bounds
            return True
        if self.snake[-1] in self.snake[:-1]:
            # hit itself
            return True
        return False