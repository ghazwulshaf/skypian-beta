from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot0(frame):
    fig = Figure(figsize=(3,2), dpi=100)

    y = []

    plot1 = fig.add_subplot(111)
    plot1.plot(y)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)

def plot1(frame):
    # the figure that will contain the plot
    fig = Figure(figsize=(3,2), dpi=100)

    # list of squares
    y = [i**2 for i in range(101)]

    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    plot1.plot(y)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()

    # placing the canvas on the Tkinter master frame
    canvas.get_tk_widget().pack(fill='both', expand=True)

def plot2(frame):
    # the figure that will contain the plot
    fig = Figure(figsize=(3,2), dpi=100)

    # list of squares
    y = [i**2 for i in range(51)]

    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    plot1.plot(y)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()

    # placing the canvas on the Tkinter master frame
    canvas.get_tk_widget().pack(fill='both', expand=True)