import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Levels with passwords and hints
levels = [
    {"password": "secure123", "hint": "It means safe and protected."},
    {"password": "keyboard!", "hint": "You're probably using it right now."},
    {"password": "cyber$ecure", "hint": "Relates to technology and computers."},
    {"password": "s4f3ty#1", "hint": "It’s what passwords provide."},
    {"password": "p@ssw0rds", "hint": "You're trying to crack this!"}
]

class PasswordGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Scramble Game")
        self.root.geometry("1200x900")  # Enlarged window size

        # Load and set background image
        self.canvas = tk.Canvas(root, width=1200, height=900)  # Updated canvas size
        self.canvas.pack(fill="both", expand=True)
        #self.set_background("/Users/cyber-max/Documents/AmaraTech IT/AmaraTech IT Solutions Wallpaper HD/AmaraTech IT Solutions Wallpaper HD/AmaraTech IT Solutions Wallpaper V1.png")
        self.set_background("C:/Users/moham/Pictures/AmaraTech IT Solutions Wallpaper V1.png")
        self.player_name = ""
        self.current_level = 0
        self.attempts = 3
        self.time_remaining = 300

        self.logo_image = None
        self.welcome_screen()

    def set_background(self, image_path):
        """Set the PNG background image."""
        try:
            self.background_image = Image.open(image_path)
            self.background_image = self.background_image.resize((1200, 900), Image.Resampling.LANCZOS)  # Resize for larger window
            self.background_photo = ImageTk.PhotoImage(self.background_image)
            self.canvas.create_image(0, 0, anchor="nw", image=self.background_photo)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load background image: {e}")

    def welcome_screen(self):
        """Display the welcome screen with logo and name entry."""
        try:
            #self.logo_image = Image.open("/Users/cyber-max/Documents/AmaraTech IT/Logos/White_logo_transparent.png")
            self.logo_image = Image.open("C:/Users/moham/Pictures/White_logo_transparent.png")
            self.logo_image = self.logo_image.resize((400, 300), Image.Resampling.LANCZOS)  # Larger logo for larger window
            self.logo = ImageTk.PhotoImage(self.logo_image)
            self.canvas.create_image(600, 150, image=self.logo)  # Centered for larger window
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load logo: {e}")

        self.label_name = tk.Label(self.root, text="Enter your name:", font=("Arial", 18), fg="white", bg="black")
        self.canvas.create_window(600, 450, window=self.label_name)

        self.entry_name = tk.Entry(self.root, font=("Arial", 18), width=40)
        self.canvas.create_window(600, 500, window=self.entry_name)

        self.button_start = tk.Button(self.root, text="Start Game", font=("Arial", 16), command=self.start_game)
        self.canvas.create_window(600, 550, window=self.button_start)

    def start_game(self):
        """Initialize the game after getting the player's name."""
        self.player_name = self.entry_name.get().strip()
        if not self.player_name:
            messagebox.showwarning("Error", "Enter your name to start!")
            return

        self.canvas.delete("all")
        #self.set_background("/Users/cyber-max/Documents/AmaraTech IT/AmaraTech IT Solutions Wallpaper HD/AmaraTech IT Solutions Wallpaper HD/AmaraTech IT Solutions Wallpaper V1.png")  # Reset the background
        self.set_background("C:/Users/moham/Pictures/AmaraTech IT Solutions Wallpaper V1.png") 
        self.setup_game_ui()
        self.start_timer()
        self.load_level()

    def setup_game_ui(self):
        """Set up the game UI."""
        self.canvas.create_image(600, 150, image=self.logo)

        self.label_timer = tk.Label(self.root, text="Time Left: 02:00", font=("Arial", 18), fg="red", bg="black")
        self.canvas.create_window(600, 250, window=self.label_timer)

        self.label_welcome = tk.Label(self.root, text=f"Welcome, {self.player_name}!", font=("Arial", 20, "bold"), fg="white", bg="black")
        self.canvas.create_window(600, 300, window=self.label_welcome)

        self.label_level = tk.Label(self.root, text="Level: 1", font=("Arial", 18), fg="white", bg="black")
        self.canvas.create_window(600, 350, window=self.label_level)

        self.label_hint = tk.Label(self.root, text="Hint: ", font=("Arial", 18), fg="white", bg="black")
        self.canvas.create_window(600, 400, window=self.label_hint)

        self.label_scrambled = tk.Label(self.root, text="Scrambled Password: ", font=("Arial", 18), fg="white", bg="black")
        self.canvas.create_window(600, 450, window=self.label_scrambled)

        self.entry_guess = tk.Entry(self.root, font=("Arial", 18), width=40)
        self.canvas.create_window(600, 500, window=self.entry_guess)

        self.button_submit = tk.Button(self.root, text="Submit", font=("Arial", 16), command=self.check_guess)
        self.canvas.create_window(600, 550, window=self.button_submit)

        self.message_area = tk.Label(self.root, text="", font=("Arial", 16), fg="white", bg="black")
        self.canvas.create_window(600, 600, window=self.message_area)

        self.button_next = tk.Button(self.root, text="Next Question", font=("Arial", 16), command=self.next_level, state=tk.DISABLED)
        self.canvas.create_window(600, 650, window=self.button_next)

    def start_timer(self):
        """Start the countdown timer."""
        if self.time_remaining > 0:
            minutes, seconds = divmod(self.time_remaining, 60)
            self.label_timer.config(text=f"Time Left: {minutes:02}:{seconds:02}")
            self.time_remaining -= 1
            self.root.after(1000, self.start_timer)
        else:
            self.display_time_up_message()

    def display_time_up_message(self):
        """Display the time-up message."""
        self.canvas.delete("all")  # Clear everything
        #self.set_background("/Users/cyber-max/Documents/AmaraTech IT/AmaraTech IT Solutions Wallpaper HD/AmaraTech IT Solutions Wallpaper HD/AmaraTech IT Solutions Wallpaper V1.png")  # Reset the background
        self.set_background("C:/Users/moham/Pictures/AmaraTech IT Solutions Wallpaper V1.png") 
        self.canvas.create_image(600, 150, image=self.logo)  # Add logo at the top
        self.canvas.create_text(
            600,
            450,
            text="Sorry, you ran out of time.\nSee you next time :)",
            fill="white",
            font=("Arial", 20, "bold"),
        )
        self.root.after(5000, self.root.quit)  # Quit the game after 5 seconds

    def load_level(self):
        """Load the current level."""
        self.current_password = levels[self.current_level]["password"]
        self.hint = levels[self.current_level]["hint"]
        self.scrambled_password = ''.join(random.sample(self.current_password, len(self.current_password)))

        self.label_level.config(text=f"Level: {self.current_level + 1}")
        self.label_hint.config(text=f"Hint: {self.hint}")
        self.label_scrambled.config(text=f"Scrambled Password: {self.scrambled_password}")
        self.message_area.config(text="")
        self.button_next.config(state=tk.DISABLED)

    def check_guess(self):
        """Check the user's guess."""
        guess = self.entry_guess.get().strip()
        if not guess:
            self.message_area.config(text="Enter a guess!")
            return

        if guess == self.current_password:
            self.message_area.config(text="Well done! Click 'Next Question' to continue.")
            self.button_next.config(state=tk.NORMAL)
        else:
            self.attempts -= 1
            if self.attempts == 0:
                self.display_time_up_message()
            else:
                self.message_area.config(text=f"Incorrect! Attempts left: {self.attempts}")

    def next_level(self):
        """Load the next level."""
        self.current_level += 1
        if self.current_level < len(levels):
            self.load_level()
        else:
            self.display_congratulations_banner()

    def display_congratulations_banner(self):
        """Display the congratulations banner."""
        self.canvas.delete("all")  # Clear everything
        #self.set_background("/Users/cyber-max/Documents/AmaraTech IT/AmaraTech IT Solutions Wallpaper HD/AmaraTech IT Solutions Wallpaper HD/AmaraTech IT Solutions Wallpaper V1.png")  # Reset the background
        self.set_background("C:/Users/moham/Pictures/AmaraTech IT Solutions Wallpaper V1.png") 
        self.canvas.create_image(600, 150, image=self.logo)  # Add logo at the top
        self.canvas.create_text(
            600,
            450,
            text=f"Congratulations {self.player_name}!\n"
                 "You have successfully completed the game.\n"
                 "Please collect your reward.\nGO AMARATECH!! GO CYBER!!!",
            fill="white",
            font=("Arial", 24, "bold")
        )
        self.root.after(10000, self.root.quit)  # Quit the game after 10 seconds


# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    game = PasswordGame(root)
    root.mainloop()
