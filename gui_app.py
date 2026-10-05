import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class StreamScapeDesigner:
    def __init__(self, root):
        self.root = root
        self.root.title('StreamScape Designer')
        self.root.geometry('1200x800')
        self.root.configure(bg='#2e2e2e')
        self.create_widgets()

    def create_widgets(self):
        # Left Panel for Nodes
        self.left_panel = tk.Frame(self.root, bg='#1e1e1e', width=200)
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y)

        # Node buttons
        self.node_buttons = {
            'Source': tk.Button(self.left_panel, text='Source', bg='#3e3e3e', fg='white', command=lambda: self.add_node('Source')),
            'Transform': tk.Button(self.left_panel, text='Transform', bg='#3e3e3e', fg='white', command=lambda: self.add_node('Transform')),
            'Visualize': tk.Button(self.left_panel, text='Visualize', bg='#3e3e3e', fg='white', command=lambda: self.add_node('Visualize'))
        }
        for btn in self.node_buttons.values():
            btn.pack(fill=tk.X, pady=5)

        # Main Canvas
        self.canvas = tk.Canvas(self.root, bg='#2e2e2e', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bottom Panel for Controls
        self.bottom_panel = tk.Frame(self.root, bg='#1e1e1e', height=100)
        self.bottom_panel.pack(side=tk.BOTTOM, fill=tk.X)

        # Start/Stop Button
        self.start_button = tk.Button(self.bottom_panel, text='Start', bg='#3e3e3e', fg='white', command=self.start_stream)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.stop_button = tk.Button(self.bottom_panel, text='Stop', bg='#3e3e3e', fg='white', command=self.stop_stream)
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Status Label
        self.status_label = tk.Label(self.bottom_panel, text='Stopped', bg='#1e1e1e', fg='white')
        self.status_label.pack(side=tk.LEFT, padx=10, pady=10)

        # Add a chart
        self.fig, self.ax = plt.subplots()
        self.canvas_chart = FigureCanvasTkAgg(self.fig, master=self.canvas)
        self.canvas_chart.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def add_node(self, node_type):
        print(f'Added {node_type} node')

    def start_stream(self):
        self.status_label.config(text='Running')
        self.update_chart()

    def stop_stream(self):
        self.status_label.config(text='Stopped')

    def update_chart(self):
        if self.status_label['text'] == 'Running':
            self.ax.clear()
            self.ax.plot([random.random() for _ in range(10)])
            self.canvas_chart.draw()
            self.root.after(1000, self.update_chart)

if __name__ == '__main__':
    root = tk.Tk()
    app = StreamScapeDesigner(root)
    root.mainloop()