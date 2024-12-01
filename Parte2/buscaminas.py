import random

class Board:
    def __init__(self, n, num_bombas):
        self.n=n
        self.num_bombas=num_bombas

        self.board=self.crear_board()
        self.colocar_valores()
        self.dug=set()

    def crear_board(self):

        board=[[None for _ in range (self.dim_size)] for _ in range(self.n)]

        bombas_colocadas=0
        while bombas_colocadas < self.num_bombas:
            ubicacion = random. randint(0, self.dim_size**2 - 1)
            fila=ubicacion//self.n
            columna=ubicacion% self.n

            if board[fila][columna]=='*':
                continue

            board[fila][columna]= '*'
            bombas_colocadas+=1

        return board





    # Separación -----
    


def play(n=10, num_bombas=10):
    pass