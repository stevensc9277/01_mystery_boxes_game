from tkinter import *
import random
from functools import partial
import re
# from pandas import to_datetime
import datetime as dt

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

    #     # instructions / help button
    #     self.help_button = Button(self.start_frame, text="How to Play", bg="#808080", fg="white", font=button_font, command=self.to_help)
    #     self.help_button.grid(row=5, pady=10)

    # def to_help(self):
    #     get_help = Help(self)
    #     root.withdraw()

    def check_funds(self):
        starting_balance = IntVar()
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

class Help:
    def __init__(self, partner):

        # disable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window (ie: help box)
        self.help_box = Toplevel()

        # if user presses cross at top, closes help and releases help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # set up GUI frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        # set up help heading
        self.how_heading = Label(self.help_frame, text="Help / Instructions", font="arial 14 bold")
        self.how_heading.grid(row=0)

        help_text = "Choose an amount to play with and then choose the stakes. Higher stakes cost more per round but you can win more as well.\n\nWhen you enter the play area, you will see three mystery boxes. To reveal the contents of the boxes, click the 'Open Boxes' button. If you don't have enough money to play, the button will turn red and you will need to quite the game.\n\nThe contents of the boxes will be added to your balance. The boxes could contain...\n\nLow: Lead ($0) | Copper ($1) | Silver ($2) | Gold ($10)\nMedium: Lead ($0) | Copper ($2) | Silver ($4) | Gold ($25)\nHigh: Lead ($0) | Copper ($5) | Silver ($10) | Gold ($25)\n\nIf each box contains gold, you earn $30 (low stakes). If they contained copper, silver and gold, you would receive $13 ($1 + $2 + $10) and so on."
        
        self.help_text = Label(self.help_frame, text=help_text, justify=LEFT, wrap=400, padx=10, pady=10)
        self.help_text.grid(row=1)

        # dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="#660000", fg="white", font="arial 15 bold", command = partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        self.help_box.destroy()
        partner.help_button.config(state=NORMAL)
        

class Game:
    def __init__(self, partner, stakes, starting_balance):
        # convert from string to integer
        starting_balance = int(starting_balance)
        # list for holding stats
        self.game_stats_list = [starting_balance, starting_balance]
        self.round_stats_list = []
            
      
        # initialise variables
        self.balance = IntVar()
        # set starting balance to amount entered by user at start of game
        self.balance.set(starting_balance)

        # get value of stakes (use it as a multiplier when calculating winnings)
        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # list for holding statistics
        self.round_stats_list = []

        # GUI setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # if users press cross at top, game quits
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)
        # heading row (row 0)
        self.heading_label = Label(self.game_frame, text="Play...", font="Arial 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)

        # Mystery heading (row 1)
        self.instructions_label = Label(self.game_frame, text="Press <enter> or click the 'Open Boxes' button to reveal the contents of the mystery boxes.", font="Arial 10", justify=LEFT, padx=10, pady=10, wrap=300)
        self.instructions_label.grid(row=1)

        # boxes go here (row 2)
        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2, pady=10)

        photo = PhotoImage(file="question.gif")

        self.prize1_label = Label(self.box_frame, padx=10, pady=10, image=photo)
        self.prize1_label.photo = photo
        self.prize1_label.grid(row=0, column=0)

        self.prize2_label = Label(self.box_frame, padx=10, pady=10, image=photo)
        self.prize2_label.photo = photo
        self.prize2_label.grid(row=0, column=1, padx=10)

        self.prize3_label = Label(self.box_frame, padx=10, pady=10, image=photo)
        self.prize3_label.photo = photo
        self.prize3_label.grid(row=0, column=2)

        # Play button goes here (row 3)
        self.play_button = Button(self.game_frame, text="Open Boxes", bg="#FFFF33", font="Arial 15 bold", width=20, padx=10, pady=10, command=self.reveal_boxes)
        self.play_button.grid(row=3)

        # bind button to <enter> (users can push enter to reveal the boxes)
        self.play_button.focus()
        self.play_button.bind('<Return>', lambda e: self.reveal_boxes())
        self.play_button.grid(row=3)

        # Balance label (row 4)

        start_text = "Game Cost: ${} \n\nHow much will you win?".format(stakes*5)

        self.balance_label = Label(self.game_frame, font="Arial 12 bold", fg="green", text=start_text, wrap=300, justify=LEFT)
        self.balance_label.grid(row=4, pady=10)

        # help and game stats button (row 5)
        self.help_export_frame = Frame(self.game_frame)
        self.help_export_frame.grid(row=5, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help / Rules", font="Arial 15 bold", bg="#808080", fg="white", command=self.to_help)
        self.help_button.grid(row=0, column=0, padx=2)

        self.stats_button = Button(self.help_export_frame, text="Game Stats...", font="Arial 15 bold", bg="#003366", fg="white", command=lambda: self.to_stats(self.round_stats_list, self.game_stats_list))
        self.stats_button.grid(row=0, column=1, padx=2)

        # Quit button
        self.quit_button = Button(self.game_frame, text="Quit", fg="white", bg="#660000", font="arial 15 bold", width=20, command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=6, pady=10)
    
    def to_help(self):
        get_help = Help(self)

    def reveal_boxes(self):
        # retrieve the balance from the initial function
        copper = ["copper_low.gif", "copper_med.gif", "copper_high.gif"]
        silver = ["silver_low.gif", "silver_med.gif", "silver_high.gif"]
        gold = ["gold_low.gif", "gold_med.gif", "gold_high.gif"]
        current_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()

        round_winnings = 0
        prizes = []
        stats_prizes = []

        for thing in range(0, 3):

        # random finds numbers between given endpoints, including both endpoints
            prize_num = random.randint(1, 100)

            if 0 < prize_num <= 5:
                prize = PhotoImage(file=gold[stakes_multiplier-1])
                prize_list = "gold(${})".format(5*stakes_multiplier)
                round_winnings += 5 * stakes_multiplier
            
            elif 5 < prize_num <= 25:
                prize = PhotoImage(file=silver[stakes_multiplier-1])
                prize_list = "silver(${})".format(2*stakes_multiplier)
                back_colour = "#B7B7B5"     # silver colour
                round_winnings += 2 * stakes_multiplier

            elif 25 < prize_num <= 65:
                prize = PhotoImage(file=copper[stakes_multiplier-1])  
                prize_list = "copper(${})".format(1*stakes_multiplier)
                back_colour = "#BC7F61"
                round_winnings += 1 * stakes_multiplier
            
            else:
                prize = PhotoImage(file="lead.gif")
                prize_list = "lead($0)"
                back_colour = "#595E71"     # lead colour

            prizes.append(prize)
            stats_prizes.append(prize_list)

        photo1 = prizes[0]
        photo2 = prizes[1]
        photo3 = prizes[2]

        # display prizes...
        self.prize1_label.config(image=photo1)
        self.prize1_label.photo = photo1
        self.prize2_label.config(image=photo2)
        self.prize2_label.photo = photo2
        self.prize3_label.config(image=photo3)
        self.prize3_label.photo = photo3

        # adjust the balance (subtract game cost and add pay out)
        current_balance -= 5 * stakes_multiplier

        # add winnings
        current_balance += round_winnings

        # set balance to adjusted balance
        self.balance.set(current_balance)
        self.game_stats_list[1] = current_balance
        # update game_stats_list with current balance (replace item in position 1 with current balance
        self.game_stats_list[1] = current_balance

        balance_statement = "Game Cost: ${}\nPayback: ${}\nCurrent Balance: ${}".format(5 * stakes_multiplier, round_winnings, current_balance)

        # add round results to statistics list
        round_summary = "{} | {} | {} - Cost: ${} | Payback: ${} | Current Balance: ${}".format(stats_prizes[0], stats_prizes[1], stats_prizes[2], 5 * stakes_multiplier, round_winnings, current_balance)

        self.round_stats_list.append(round_summary)
        # edit label so user can their balance
        self.balance_label.configure(text=balance_statement)

        if current_balance < 5 * stakes_multiplier:
            self.play_button.config(state=DISABLED)
            self.game_box.focus()
            self.play_button.config(text="Game Over")

            balance_statement = "Current Balance: ${}\nYour balance is too low. You can only quit or view your stats. Sorry about that.".format(current_balance)
            self.balance_label.config(fg="#660000", font="Arial 10 bold", text=balance_statement)
         
        else:
            balance_statement = "Game Cost: ${}\nPayback: ${} \nCurrent Balance: ${}".format(5 * stakes_multiplier, round_winnings, current_balance)

        # edit label so user can see their balance
        self.balance_label.configure(text=balance_statement)

    def to_quit(self):
        root.destroy()

    def to_stats(self, game_history, game_stats):
        GameStats(self, game_history, game_stats)
        self.game_box.withdraw()

class GameStats:
    def __init__(self, partner, game_history, game_stats):

        # disable stats button
        partner.stats_button.config(state=DISABLED)

        heading = "arial 12 bold"
        content = "arial 12"

        # sets up child window (ie: stats box)
        self.stats_box = Toplevel()

        # if user presses cross at top, close stats and releases stats button
        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

        # set up GUI frame
        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid()

        # set up stats heading (row 0)
        self.stats_heading_label = Label(self.stats_frame, text="Game Statistics", font="arial 19 bold")
        self.stats_heading_label.grid(row=0)

        # to export <instructions> (row 1)
        self.export_instructions = Label(self.stats_frame, text="Here are your game statistics. Please use the export button to access the results of each round that you played", wrap=250, font="arial 10 italic", justify=LEFT, fg="green", padx=10, pady=10)
        self.export_instructions.grid(row=1)

        # starting balance (row 2)
        self.details_frame = Frame(self.stats_frame)
        self.details_frame.grid(row=2)

        self.start_balance_label = Label(self.details_frame, text="Starting Balance:", font=heading, anchor="e")
        self.start_balance_label.grid(row=0, column=0, padx=0)

        self.start_balance_value_label1 = Label(self.details_frame, font=content, text="${}".format(game_stats[0]), anchor="w")
        self.start_balance_value_label1.grid(row=0, column=1, padx=0)

        self.current_balance_label = Label(self.details_frame, text="Current Balance:", font=heading, anchor="e")
        self.current_balance_label.grid(row=1, column=0, padx=0)
        
        self.current_balance_value_label1 = Label(self.details_frame, font=content, text="${}".format(game_stats[1]), anchor="w")
        self.current_balance_value_label1.grid(row=1, column=1, padx=0)

        if game_stats[1] > game_stats[0]:
            win_loss = "Amount Won:"
            amount = game_stats[1] - game_stats[0]
            win_loss_fg = "green"
        else:
            win_loss = "Amount Lost:"
            amount = game_stats[0] - game_stats[1]
            win_loss_fg = "#660000"

        # amount won / lost (row 2)
        self.win_loss_label = Label(self.details_frame, text=win_loss, font=heading, anchor="e")
        self.win_loss_label.grid(row=2, column=0, padx=0)

        self.win_loss_value_label1 = Label(self.details_frame, font=content, text="${}".format(amount), fg=win_loss_fg, anchor="w")
        self.win_loss_value_label1.grid(row=2, column=1, padx=0)

        # rounds played (row 4)
        self.games_played_label = Label(self.details_frame, font=heading, text="Rounds Played:", anchor="e")
        self.games_played_label.grid(row=4, column=0, padx=0)

        self.games_played_value_label = Label(self.details_frame, font=content, text=len(game_history), anchor="w")
        self.games_played_value_label.grid(row=4, column=1, padx=0)

        # export and dismiss buttons (row 5)
        self.export_dismiss_frame = Frame(self.stats_box)
        self.export_dismiss_frame.grid(row=5, pady=10)

        # export button
        self.export_button = Button(self.export_dismiss_frame, width=10, text="Export...", font=heading, bg="#003366", fg="white", command=lambda: self.export(game_history, game_stats))
        self.export_button.grid(row=0, column=0, padx=10)

        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss", width=10, bg="#660000", font=heading, fg="white", command=partial(self.close_stats, partner))
        self.dismiss_button.grid(row=0, column=1)

    def export(self, game_history, game_stats):
        get_export = Export(self, game_history, game_stats)
        self.stats_box.withdraw()

    def close_stats(self, partner):
        self.stats_box.destroy()
        partner.game_box.deiconify()
        partner.stats_button.config(state=NORMAL)

class Export:
    
    def __init__(self, partner, game_history, all_game_stats):

        # disable export button
        partner.export_button.config(state=DISABLED)

        # sets up child window (ie: export box)
        self.export_box = Toplevel()

        # If users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))
        

        # set up GUI frame
        self.export_frame = Frame(self.export_box, width=300)
        self.export_frame.grid()

        # set up export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions", font=("Arial", "14", "bold"))
        self.how_heading.grid(row=0)

        # export instructions (label, row 1)
        self.export_text = Label(self.export_frame, width=40, text="Enter a filename in the box below and press the Save button to save your calculation history to a text file", justify=LEFT, wrap=250)
        self.export_text.grid(row=1)

        # warning text.. (label, row 2)
        self.export_text = Label(self.export_frame, text="If the filename you enter below already exists, its contents will be replaced with your game history", justify=LEFT, bg="#ffafaf", fg="maroon", font="Arial 10 italic", wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)
       
        # filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20, font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error message labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon")
        self.save_error_label.grid(row=4)

        # save / cancel frame
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # save and cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, fg="white", bg="#660000", text="Save", font="arial 12 bold", command=partial(lambda: self.save_history(partner, game_history, all_game_stats)))
        self.save_button.grid(row=0, column=0)

        # cancel button
        self.cancel_button = Button(self.save_cancel_frame, text="Cancel", font="arial 12 bold", bg="#003366", fg="white", command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1, padx=10)

    
    def save_history(self, parent,game_history, game_stats):
        
        # regular expression to check filename is valid
        valid_char = "[A-Za-z0-9]"
        has_error = "no"

        filename = self.filename_entry.get()
        
        # iterate through name to check for errors (spaces and blank names)
        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"
                has_error = "yes"

            else:
                problem = ("(no {}'s allowed)".format(letter))
                has_error = "yes"
                break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))

            # change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()
        
        else:
            # If there are no errrors, generate text file and then close dialogue box
            
            # change entry box color back to normal if no errors after previous error
            self.save_error_label.configure(text="", fg="blue")
            self.filename_entry.configure(bg="white")

            # add .txt suffix!
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # find and return current date for testing purposes
            now = dt.datetime.now()

            # add new line at end of each item
            f.write("Mystery Box Game Statistics \n\n")
            f.write("Made on: " + now.strftime('%A, %B %d, %Y') + "\n\n")

            for round in game_stats:
                if game_stats.index(round) == 0:
                    f.write("Starting balance: ${}\n".format(round))
                else:
                    f.write("Current balance: ${}\n".format(round))

            # heading for rounds
            f.write("\nRound Details\n\n")

            # add new line at end of each item
            for item in game_history:
                f.write(item + "\n")
            # close file
            f.close()
            self.close_export(parent)
            self.export_box.destroy()
            

    def close_export(self, partner):
        # put export button back to normal...
        partner.stats_box.deiconify()

        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()
   

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()
