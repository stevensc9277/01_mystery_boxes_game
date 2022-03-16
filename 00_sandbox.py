import tkinter as tk

root = tk.Tk()
LeftFrame = tk.Frame(root)
LeftFrame.grid()

#Define functions
def checker(i,j):
    print("You pressed button {},{}".format(i, j))

#Create a 2-d list containing 3 rows, 3 columns (using list comprehension)
botones = [[None for i in range(3)] for j in range(3) ]

for i in range(2):
    for j in range(2):
        current_button = tk.Button(LeftFrame,
                               text = "{}, {}".format(i, j),
                               font=("tahoma", 25, "bold"),
                               height = 3,
                               width = 20,
                               bg="gainsboro",
                               command=lambda i=i,j=j:checker(i,j)) #lambda is passed parameters i and j
        #Grid occurs on a new line
        current_button.grid(row = i+1, column = j+1, padx=10, pady=10)
        botones[i][j] = current_button

root.mainloop()