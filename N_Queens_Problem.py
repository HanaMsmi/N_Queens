import tkinter as tk


def getn():
    def submit():
        global n
        n = int(n_var.get())
        n_var.set("")
        root.destroy()

    root = tk.Tk()
    n_var = tk.StringVar(root)
    name_label = tk.Label(root, text="N:", font=("calibre", 10, "bold"))
    name_entry = tk.Entry(root, textvariable=n_var, font=("calibre", 10, "normal"))
    sub_btn = tk.Button(root, text="Submit", command=submit)
    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1)
    sub_btn.grid(row=1, column=1)
    root.mainloop()


def gui(n, board):
    def nextboard():
        root.destroy()

    root = tk.Tk()

    convas = tk.Canvas(root, bg="white", height=100 * n, width=100 * n)
    color = "black"
    for i in range(n):

        color = "white" if i % 2 == 0 else "black"

        for j in range(n):
            convas.create_rectangle(100 * i, 100 * j, 100 * (i + 1), 100 * (j + 1), fill=color)
            if board[j][i] == 1:
                convas.create_rectangle(
                    100 * i + 30, 100 * j + 30, 100 * (i + 1) - 30, 100 * (j + 1) - 30, fill="red"
                )
            color = "white" if color == "black" else "black"

    convas.pack()
    sub_btn = tk.Button(root, text="next", command=nextboard)
    sub_btn.pack()
    root.mainloop()


def Show_list_of_answers(board):
    global iter
    print("Solution:", iter)
    iter += 1
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print("")

    print("\n")


def promising(board, row, col):

    for i in range(col):
        if board[row][i]:
            return False
    for i in range(1, col + 1):
        if row - i >= 0:
            if board[row - i][col - i]:
                return False
        if row + i < n:
            if board[row + i][col - i]:
                return False

    return True


def N_Queen(board, col):
    if col >= n:
        Show_list_of_answers(board)
        gui(n, board)
    for row in range(n):
        if promising(board, row, col):
            board[row][col] = 1
            if N_Queen(board, col + 1):
                return True
            board[row][col] = 0
    return False


def call_func():
    if n == 1 or n > 3:
        board = [[0] * n for _ in range(n)]
        N_Queen(board, 0)
    else:
        print("!!! Error: N must be equal to 1 or greater than 3")


n = 0
iter = 1

getn()
call_func()
