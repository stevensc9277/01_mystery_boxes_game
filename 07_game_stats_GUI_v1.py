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
        self.stats_button = Button(self.game_frame, text="Game Stats", font="arial 14", padx=10, pady=10, command=lambda: self.to_stats(self.round_stats_list))
        self.stats_button.grid(row=1)

    def to_stats(self, game_history, game_stats):
        GameStats(self, game_history, game_stats)

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

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()
