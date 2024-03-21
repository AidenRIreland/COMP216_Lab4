import tkinter as tk
from tkinter import Canvas, messagebox
from Lab7 import DataGenerator
from math import pi, cos, sin, radians
#Group 11
#I had to see how to design it so much, hard gui I designed tbh xd, I only put effort into the guage, not the buttons
class GaugeDisplay(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.width = 300
        self.height = 300  # Make a square for a circular gauge
        self.radius = 100
        self.center = (150, 150)  # Center of the page
        self.pack()
        self.create_widgets()
        self.datagenerator = DataGenerator(num_points=4)# get the first value
        initial_value = self.datagenerator.generate_data()[0]  # Get the first data point
        self.entry.insert(0, str(initial_value))
        self.update_gauge()

    def create_widgets(self):
        self.canvas = Canvas(self, width=self.width, height=self.height)
        self.canvas.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.update_button = tk.Button(self)
        self.update_button["text"] = "Update Gauge"
        self.update_button["command"] = self.update_gauge
        self.update_button.pack()

        self.value_label = tk.Label(self, text="Enter student score (0-100)")
        self.value_label.pack()

        self.draw_gauge()
    def draw_gauge(self):
        segments = [
        (180, -90, "red", "F"),          # F (0-59.4)
        (90, -18, "dark orange", "D"),   # D (59.5-69.4)
        (72, -18, "orange", "C"),        # C (69.5-79.4)
        (54, -18, "yellow", "B"),        # B (79.5-89.4)
        (36, -18, "light green", "A"),   # A (79.5-89.5)
        (18, -18, "light blue", "A+"),   # A+ (89.5-100)
    ]
        for start_angle, extent, color, label in segments:
            self.draw_gauge_segment(start_angle, extent, color)
            self.draw_label(start_angle, extent, label)  # This will draw the label for the segment
    def draw_gauge_segment(self, start_angle, extent, color):
        # pie segments
        return self.canvas.create_arc(
            self.center[0] - self.radius, self.center[1] - self.radius,
            self.center[0] + self.radius, self.center[1] + self.radius, 
            start=start_angle, extent=extent,
            fill=color, style="pieslice", outline="black"
        )
    
    def draw_label(self, start_angle, extent, label):
        mid_angle = start_angle + (extent / 2.0)
        label_radius_offset = 45  
        label_radius = self.radius - label_radius_offset
        mid_angle_rad = radians(mid_angle)
        label_x = self.center[0] + label_radius * cos(mid_angle_rad)
        label_y = self.center[1] - label_radius * sin(mid_angle_rad)
        # Draw the label text
        self.canvas.create_text(label_x, label_y, text=label, font=('Arial', 10), tags="label")

    def get_color_for_value(self, value):
        # Determine the color based on the grade
        if value >= 89.5:
            color = "light blue"
        elif value >= 79.5:
            color = "light green"
        elif value >= 69.5:
            color = "yellow"
        elif value >= 59.5:
            color = "orange"
        else:
            color = "dark orange" if value >= 59.5 else "red"
        return color

    def update_gauge(self):
        try:
            value = round(float(self.entry.get()))
            if 0 <= value <= 100:
                # Delete previous needle and value text to it dosnt stack
                self.canvas.delete("needle")
                self.canvas.delete("value_text")
                # Calculate the angle for the needle
                angle = (value * 180 / 100) - 90
                angle_in_radians = radians(angle)  # Convert angle to radians because I tried brute forcing it
                # Colors
                Needle_color = "black"
                color = self.get_color_for_value(value)
                # Calculate needle coordinates
                x2 = self.center[0] + self.radius * sin(angle_in_radians)
                y2 = self.center[1] - self.radius * cos(angle_in_radians)
                # Draw the needle and circle at the base
                self.canvas.create_oval(self.center[0] - 5, self.center[1] - 5, self.center[0] + 5, self.center[1] + 5, fill=Needle_color, outline=Needle_color)
                self.canvas.create_line(self.center[0], self.center[1], x2, y2, fill=Needle_color, width=2, tags="needle")
                # Draw the value text
                text_x = self.center[0]
                text_y = self.center[1] + 20  # NOTE: Increase this value to move the text further down
                self.canvas.create_text(text_x, text_y, text=f"{value:.0f}", fill=color, font=('Arial', 14), tags="value_text")
            else:
                messagebox.showerror("Error", "Please enter a valid number between 0 - 100")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid input")

root = tk.Tk()
root.title("Success Schema - Gauge")
app = GaugeDisplay(master=root)
root.mainloop()