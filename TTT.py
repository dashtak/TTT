

class TTTGenerator:

    def __init__(self):
        self.ends = [0, 0, 0]

    def GenerateMoves(self, fileName):
        self.f = open(fileName, "w")
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__Gen(1, 0)
        self.f.close()

    def __boardToFile(self, status):
        tmp = str(self.board).strip('[]')
        self.f.write(f'{tmp}, {status}\n')
        self.ends[status] += 1
        # print(status)
        return

    def __Gen(self, side, nmoves):

        if nmoves == 9:
            self.__boardToFile(0)
            return

        for i in range(0, 9):
            if self.board[i] != 0:
                continue

            self.board[i] = side

            win = False

            for k in range(0, 3):
                if self.board[k] == self.board[k+3] == self.board[k+6] == side:
                    win = True
                    break

            for k in range(0, 9, 3):
                if self.board[k] == self.board[k+1] == self.board[k+2] == side:
                    win = True
                    break

            if self.board[2] == self.board[4] == self.board[6] == side:
                win = True

            if self.board[0] == self.board[4] == self.board[8] == side:
                win = True

            if win:
                self.__boardToFile(side)
                self.board[i] = 0
                continue

            self.__Gen(3 - side, nmoves + 1)
            self.board[i] = 0


gam = TTTGenerator()
gam.GenerateMoves("E:\\temp\\output.txt")

print(gam.ends)
print(gam.ends[0] + gam.ends[1] + gam.ends[2])
