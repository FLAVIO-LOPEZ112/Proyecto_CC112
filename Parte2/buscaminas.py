import random

class Board:
    def __init__(self, n, num_bombas):
        self.n=n
        self.num_bombas=num_bombas

        self.board=self.crear_board()
        self.colocar_valores()
        self.cavado=set()

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

    def asignar_valores_a_la_matriz(self):
        for f in range(self.n):
            for c in range(self.n):
                if self.board[f][c] == "*":
                    continue
                self.board[f][c] = self.asignar_numero_de_bombas_cercanas(f,c)
    
    
    def asignar_numero_de_bombas_cercanas(self, fila, columna):
        numero_de_bombas_cercanas = 0
        for f in range(max(0,fila-1),min(self.n,(fila+1)+1)):
            for c in range(max(0,columna-1),min(self.n,(columna+1)+1)):
                if f == fila and c== columna:
                    continue
                elif self.boar[f][c] == "*":
                    numero_de_bombas_cercanas += 1

        return numero_de_bombas_cercanas
    
    def cavar(self, fila, columna):
        self.cavado.add(fila,columna)
        if self.board[fila][columna] == "*":
            return False
        if self.board[fila][columna] > 0:
            return True 
        for f in range(max(0,fila-1),min(self.n,(fila+1)+1)):
            for c in range(max(0,columna-1),min(self.n,(columna+1)+1)):
                if (f,c) in self.dug:
                    continue 
                return self.cavar(f,c)
    
    def __str__(self, fila, columna):
        tablero_visible = [[None for _ in range(self.n)] for _ in range(self.n)]
        for f in range(self.n):
            for c in range(self.n):
                if (f, c) in self.cavado:
                    tablero_visible[f][c] = str(self.board[f][c])
                else:
                    tablero_visible[f][c] = " "
        
def play(n=10, num_bombas=10):
    pass
