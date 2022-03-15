import tkinter as tk

root = tk.Tk()
LeftFrame = tk.Frame(root)
LeftFrame.grid()

def checker(i,j):
    print("You pressed button {i},{j}")

#Create a 2-d list containing 3 rows, 3 columns (using list comprehension)
botones = [[None for i in range(3)] for j in range(3) ]

for i in range(3):
    for j in range(3):
        a = 1
        b = 1
        current_button = tk.Button(LeftFrame,
                               text = "{},{}".format(a, b),
                               font=("tahoma", 25, "bold"),
                               height = 3,
                               width = 8,
                               bg="gainsboro",
                               command=lambda i=i,j=j:checker(i,j)) #lambda is passed parameters i and j
        #Grid occurs on a new line
        a += 1
        b += 1
        current_button.grid(row = i+1, column = j+1)
        botones[i][j] = current_button

root.mainloop()