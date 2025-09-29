def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False
        # Check diagonals
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens_recursive(n):
    # recursiva
    solutions = []
    def solve(row, board):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                solve(row + 1, board)
    solve(0, [-1]*n)
    return solutions

def solve_n_queens_iterative(n):
    # iterativa
    solutions = []
    stack = [([], 0)]
    while stack:
        board, row = stack.pop()
        if row == n:
            solutions.append(board)
            continue
        for col in range(n):
            safe = True
            for r in range(row):
                if board[r] == col or abs(board[r] - col) == abs(r - row):
                    safe = False
                    break
            if safe:
                stack.append((board + [col], row + 1))
    return solutions

def print_solutions(solutions, n):
    for sol in solutions:
        for i in range(n):
            row = ['.']*n
            row[sol[i]] = 'Q'
            print(' '.join(row))
        print()

if __name__ == "__main__":
    for n in range(4, 9):
        print(f"=== {n} REINAS (Recursivo) ===")
        rec_solutions = solve_n_queens_recursive(n)


#dependiendo en numero de la muestra es mas eficiente una u otra
#pocas recursivo
#muuchas iterativa
