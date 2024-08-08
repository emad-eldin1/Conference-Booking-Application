import tkinter as tk
from tkinter import messagebox
from classes import *

class ConferenceBookingApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Conference Booking Application")
        
        # Set background color for the window
        self.window.configure(bg='brown')
        
        # Configure grid weights
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_rowconfigure(2, weight=1)
        self.window.grid_rowconfigure(3, weight=1)
        self.window.grid_rowconfigure(4, weight=1)
        self.window.grid_rowconfigure(5, weight=1)
        self.window.grid_rowconfigure(6, weight=3)  # More space for the output area

        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=2)  # Column 1 will be wider
        
        self.create_widgets()
        self.bind_events()
        
    def create_widgets(self):
        # Define label colors
        label_bg = 'lightgreen'
        
        tk.Label(self.window, text="Name", bg=label_bg).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
        
        tk.Label(self.window, text="Age", bg=label_bg).grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.age_entry = tk.Entry(self.window)
        self.age_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=5)
        
        tk.Label(self.window, text="Email", bg=label_bg).grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.email_entry = tk.Entry(self.window)
        self.email_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=5)
        
        tk.Label(self.window, text="Country", bg=label_bg).grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.country_entry = tk.Entry(self.window)
        self.country_entry.grid(row=3, column=1, sticky="ew", padx=10, pady=5)
        
        tk.Label(self.window, text="Number of Tickets", bg=label_bg).grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.tickets_entry = tk.Entry(self.window)
        self.tickets_entry.grid(row=4, column=1, sticky="ew", padx=10, pady=5)
        
        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit)
        self.submit_button.grid(row=5, column=0, columnspan=2, pady=10)
        
        self.output_text = tk.Text(self.window, height=10, width=50)
        self.output_text.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)
        
        self.update_output()
        
    def bind_events(self):
        # Bind Enter key to the submit method
        self.window.bind('<Return>', lambda event: self.submit())
        
    def submit(self):
        newUser = {
            "name": self.name_entry.get(),
            "age": int(self.age_entry.get()),
            "email": self.email_entry.get(),
            "country": self.country_entry.get().lower(),
            "numberOfTickets": int(self.tickets_entry.get())
        }
        
        error_message = validateUserInput(newUser)
        if error_message:
            messagebox.showerror("Error", error_message)
        else:
            cost = checkOut(newUser)
            messagebox.showinfo("Success", f'Congratulations! You have successfully purchased {newUser["numberOfTickets"]} tickets for {newUser["country"]}\'s conference! You will pay {cost}')    
            self.clear_inputs()
            self.update_output()
    
    def clear_inputs(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.country_entry.delete(0, tk.END)
        self.tickets_entry.delete(0, tk.END)
        
    def update_output(self):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "List of Users:\n")
        for user in listOfUsers:
            self.output_text.insert(tk.END, f'{user["name"]}\t{user["numberOfTickets"]}\t{user["country"]}\n')
        
        self.output_text.insert(tk.END, "\nAvailable Tickets:\n")
        for country, tickets in conferenceTickets.items():
            self.output_text.insert(tk.END, f'{country}: {tickets}\n')

# Initialize the window and application
window = tk.Tk()
app = ConferenceBookingApp(window)
window.mainloop()

# Conference data

