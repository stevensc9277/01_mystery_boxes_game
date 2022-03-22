from tkinter import *
import random
from functools import partial


class Start:
    def __init__(self, parent):

        # formatting variables
        self.game_stats_list = [50, 6]

        # in actual program this is blank and populated with user calculations
        self.round_stats_list = ['gold\n($10) | lead\n($0) | lead\n($0) - Cost: $10 | Payback: $10 | Current Balance: $50', 'silver\n($4) | lead\n($0) | lead\n($0) - Cost: $10 | Payback: $4 | Current Balance: $44', 'silver\n($4) | silver\n($4) | copper\n($2) - Cost: $10 | Payback: $10 | Current Balance: $44', 'lead\n($0) | lead\n($0) | lead\n($0) - Cost: $10 | Payback: $0 | Current Balance: $34', 'silver\n($4) | silver\n($4) | copper\n($2) - Cost: $10 | Payback: $10 | Current Balance: $34', 'lead\n($0) | silver\n($4) | lead\n($0) - Cost: $10 | Payback: $4 | Current Balance: $28', 'lead\n($0) | copper\n($2) | copper\n($2) - Cost: $10 | Payback: $4 | Current Balance: $22', 'gold\n($10) | copper\n($2) | lead\n($0) - Cost: $10 | Payback: $12 | Current Balance: $24', 'silver\n($4) | lead\n($0) | silver\n($4) - Cost: $10 | Payback: $8 | Current Balance: $22', 'copper\n($2) | copper\n($2) | lead\n($0) - Cost: $10 | Payback: $4 | Current Balance: $16', 'lead\n($0) | lead\n($0) | lead\n($0) - Cost: $10 | Payback: $0 | Current Balance: $6']

        self.game_frame = Frame()
        self.game_frame.grid()

        # Heading row
        self.heading_label = Label(self.game_frame, text="Play...", font="arial 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)

        # history button (row 1)
        self.stats_button = Button(self.game_frame, text="Game Stats", font="arial 14", padx=10, pady=10, command=lambda: self.to_stats(self.round_stats_list, self.game_stats_list))
        self.stats_button.grid(row=1)

    def to_stats(self, game_history, game_stats):
        GameStats(self, game_history, game_stats)
        root.withdraw()

class GameStats:
    def __init__(self, partner, game_history, game_stats):
        print(game_history)

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

    def close_stats(self, partner):
        self.stats_box.destroy()
        root.deiconify()
        partner.stats_button.config(state=NORMAL)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()
