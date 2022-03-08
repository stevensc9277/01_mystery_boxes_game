from tkinter import *
import random



class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Set initial balance to zero
        self.starting_funds = IntVar()
        self.starting_funds.set(0)

        # Mystery heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game", font="Arial 19 bold")
        self.mystery_box_label.grid(row=0)

        # Mystery heading (row 1)
        self.mystery_instructions = Label(self.start_frame, text="Please enter a dollar amount (between $5 and $50) in the box below. Then choose the stakes. The higher the stakes, the more you can win!", font="Arial 10 italic", justify=LEFT, padx=10, pady=10, wrap=250)
        self.mystery_instructions.grid(row=1)

        # Entry box, Button & Error label (row 2)
        self.entry_error_frame = Frame(self.start_frame, width=200)
        self.entry_error_frame.grid(row=2)

        self.start_amount_entry = Entry(self.entry_error_frame, font="Arial 19 bold", width=10)
        self.start_amount_entry.grid(row=0, column=0)

        self.add_funds_button = Button(self.entry_error_frame, font="Arial 14 bold", text="Add Funds", command=self.check_funds)
        self.add_funds_button.grid(row=0, column=1)

        self.amount_error_label = Label(self.entry_error_frame, fg="maroon", text="", font="Arial 10 bold", wrap=250, justify=LEFT)
        self.amount_error_label.grid(row=1, columnspan=2, pady=5)        

        button_font = "Arial 12 bold"

        # stakes buttons frame (row 3)
        self.stakes_frame = Frame(self.start_frame)
        self.stakes_frame.grid(row=4, pady=10)

        # Orange low stakes button
        self.low_stakes_button = Button(self.stakes_frame, text="Low ($5)", font=button_font, bg="#FF9933", command=lambda: self.to_game(1))
        self.low_stakes_button.grid(row=0, column=0, pady=10)
        
        # Yellow medium stakes button
        self.medium_stakes_button = Button(self.stakes_frame, text="Medium ($10)", font=button_font, bg="#FFFF33", command=lambda: self.to_game(2))
        self.medium_stakes_button.grid(row=0, column=1, pady=10, padx=5)        

        # Pale green high stakes button
        self.high_stakes_button = Button(self.stakes_frame, text="High ($15)", font=button_font, bg="#99FF33", command=lambda: self.to_game(3))
        self.high_stakes_button.grid(row=0, column=2, pady=10)     

        # disable all stakes buttons at start
        self.low_stakes_button.config(state=DISABLED)
        self.medium_stakes_button.config(state=DISABLED)
        self.high_stakes_button.config(state=DISABLED)

        # instructions / help button
        self.help_button = Button(self.start_frame, text="How to Play", bg="#808080", fg="white", font=button_font)
        self.help_button.grid(row=5, pady=10)

    def check_funds(self):
        starting_balance = self.start_amount_entry.get()

        # set error background colours (and assume that there are no errors at the start)
        error_back = "#ffafaf"
        has_errors = "no"

        # change background to white for testing purposes
         # change bg to white (for testing purposes)
        self.start_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")

        # disable all stakes buttons in case user changes mind and decreases amount entered
        self.low_stakes_button.config(state=DISABLED)
        self.medium_stakes_button.config(state=DISABLED)
        self.high_stakes_button.config(state=DISABLED)

        try:
            starting_balance = int(starting_balance)

            if starting_balance < 5:
                has_errors = "yes"
                error_feedback = "Sorry, the least you can play with is $5"

            elif starting_balance > 50:
                has_errors = "yes"
                error_feedback = "Too high! The most you can risk in this game is $50"

            elif starting_balance >= 15:
                # enable all buttons
                self.low_stakes_button.config(state=NORMAL)
                self.medium_stakes_button.config(state=NORMAL)
                self.high_stakes_button.config(state=NORMAL)
            
            elif starting_balance >= 10:
                # enable low and medium stakes buttons
                self.low_stakes_button.config(state=NORMAL)
                self.medium_stakes_button.config(state=NORMAL)
            
            else:
                self.low_stakes_button.config(state=NORMAL)

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a dollar amount (no text / decimals)"

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)

        else:
            # set starting balance to amount entered by user
            self.starting_funds.set(starting_balance)

    def to_game(self, stakes):

        # retrieve starting balance
        starting_balance = self.start_amount_entry.get()
                
        Game(self, stakes, starting_balance)

        # hide start up window
        root.withdraw()
         
class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        # initialise variables
        self.balance = IntVar()

        # set starting balance to amount entered by user at start of game
        self.balance.set(starting_balance)
        
        # GUI setup
        self.game_box = Toplevel()

        # GUI to get starting balance and stakes
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # heading row (row 0)
        self.game_label = Label(self.game_frame, text="Heading", font="Arial 24 bold", padx=10, pady=10)
        self.game_label.grid(row=0)

        # Balance label (row 1)
        self.balance_frame = Frame(self.game_frame)
        self.balance_frame.grid(row=1)

        self.balance_label = Label(self.game_frame, font="Arial 16 bold", text="Balance: {}".format(starting_balance))
        self.balance_label.grid(row=3)

        # play button
        self.play_button = Button(self.game_frame, text="Gain", padx=10, pady=10, command=self.reveal_boxes)
        self.play_button.grid(row=4)

    def reveal_boxes(self):
        # retrieve the balance from the initial function
        current_balance = self.balance.get()

        # adjust the balance (subtract game cost and add pay out)
        # for testing purposes, just add 2
        current_balance += 2

        # set balance to adjusted balance
        self.balance.set(current_balance)

        # edit label so user can see their balance
        self.balance_label.configure(text="Balance: {}".format(current_balance))



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Start(root)
    root.mainloop()
