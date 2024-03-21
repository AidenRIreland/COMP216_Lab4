import tkinter as tk
from tkinter import Canvas, messagebox
from Lab7 import DataGenerator
#Idk how you want me to design a bar for the grade calculatior
class BarChart(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.datagenerator = DataGenerator(num_points=4)# get the first value
        initial_value = self.datagenerator.generate_data()[0]  # Get the first data point
        self.entry.insert(0, str(initial_value))
        self.update_bar()
        

    def create_widgets(self):
        self.canvas = Canvas(self, width=200, height=200)
        self.canvas.pack()
        
        self.entry = tk.Entry(self)
        self.entry.pack()
        
        self.update_button = tk.Button(self)
        self.update_button["text"] = "Update Bar"
        self.update_button["command"] = self.update_bar
        self.update_button.pack()

        self.value_label = tk.Label(self, text="Enter student score (0-100)")
        self.value_label.pack()

    def update_bar(self):
        try:
            value = round(float(self.entry.get()))
            if 0 <= value <= 100:
                self.canvas.delete("bar")
                self.canvas.delete("text")
                bar_height = 150 * (value / 100)
                #the color based on the specific grading scale.
                if value >= 89.5:
                    color = "light blue"
                elif value >= 79.5:
                    color = "light green"
                elif value >= 79.4:
                    color = "yellow"
                elif value >= 69.5:
                    color = "orange"
                elif value >= 59.5:
                    color = "dark orange"
                else:
                    color = "red"
                self.canvas.create_rectangle(75, 150, 125, 150 - bar_height, tags="bar", fill=color)
                self.canvas.create_text(100, 150 - bar_height / 2, tags="text", text=f"{value:.2f}")
            else:
                messagebox.showerror("Error", "Please enter a valid number between 0 - 100")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

root = tk.Tk()
root.title("Success Schema - Bar Chart")
app = BarChart(master=root)
root.mainloop()