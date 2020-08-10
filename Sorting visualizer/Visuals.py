from tkinter import *           # for gui
from tkinter import ttk         #for the combo box
import random                   # for generating random data
from bubbleSort import bubble_sort
from selectionSort import selection_sort
from insertionSort import insertion_sort

#creating the window
root = Tk()                         # creating object of the Tk class
root.title('Sorting visualizer')    # title of the window
root.maxsize(900, 800)     # size of the window
root.config(bg = 'black')    #setting the background of the window

#variables
selected_alg = StringVar()     # string variable to contain list of algo names
data = []       # declaring data as global variable because we need to access this in our sorting algos

#function for drawing the data generated
def drawData(data, colorArray):          #colorArray required to colour the currently sorting elements
    canvas.delete(('all'))   #for clearing the canvas after each time data is regenerated
    c_height =680     #canvas height
    c_width = 800     #canvas width
    x_width = c_width // (len(data)+1)   #width of each bar
    offset = 30       # so that we dont start from the border
    spacing = 10      # spacing between each bar

    #normalizing the data so that even if the data is small bar height is big enough to view
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):        # enumerate adds a counter to an iterable

        #data required by create rectangle function
        x0 = i * x_width + offset + spacing       #top left
        y0 = c_height - (height * 660)              # 380 = bottom of the canvas
        x1 =  (i+1)*x_width + offset              #bottom right
        y1 = c_height

        #creating the bars
        canvas.create_rectangle(x0, y0, x1, y1, fill = colorArray[i-1])
        canvas.create_text(x0+2, y0,anchor = SW,  text = str(data[i]))

    root.update_idletasks()    #for showing each step, i.e. updating the canvas at each step

#creating the function for generating data while generate button is clicked
def Generate():
    global data                # accessing the gobal data array
    min = int(minEntry.get())
    max = int(maxEntry.get())
    size = int(sizeEntry.get())
    # generating the data array
    data = []
    for i in range(size):        #resetting the global data array
        data.append(random.randrange(min, max+1))
    drawData(data, ['red' for x in range(len(data))])   #drawing red colored bars

#function to start the algo
def startAlgo():
    global data
    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get())
    elif algo_menu.get == 'Selection Sort':
        selection_sort(data, drawData, speedScale.get())
    else:
         insertion_sort(data, drawData, speedScale.get())



#Place where user will give the inputs
UI_frame = Frame(root, width = 800, height = 200, bg = 'grey')    #Frame creates a container which can hold other widgets
UI_frame.grid(row = 0, column = 0, padx = 10, pady = 5)

#place where the sorting visuals will be shown
canvas = Canvas(root, width = 800, height = 680, bg = 'white')    #Canvas creates rectangular area for any type of graphical layouts
canvas.grid(row = 1, column = 0, padx = 10, pady = 5 )

#creating the sort selection menu
Label(UI_frame, text = 'Algorithms', bg = 'grey').grid(row = 0, column = 0, padx = 5, pady = 5 , sticky = W)
algo_menu = ttk.Combobox(UI_frame, text = selected_alg , values = ['Bubble Sort', 'Selection Sort', 'Insertion Sort'])
algo_menu.grid(row = 0 , column = 1, padx = 5, pady = 5)
algo_menu.current(0)         #making bubble sort as default choice

#creating the speed scale
speedScale = Scale(UI_frame, from_=0.01, to=0.5, length=200, digits=2, resolution=0.01, orient=HORIZONTAL, label='select speed[sec]')
speedScale.grid(row = 0, column = 2, padx = 5, pady = 5)

#creating the button to generate random data
Btn = Button(UI_frame, text = 'Generate' , command = Generate, bg = 'light green')
Btn.grid(row = 0, column = 3, padx = 5, pady = 5)

#creating the button to start the algo
Btn = Button(UI_frame, text = 'Start' , command = startAlgo, bg = 'red')
Btn.grid(row = 0, column = 4, padx = 5, pady = 5)


#creating the size of data selection menu
sizeEntry = Scale(UI_frame, from_=3, to=50, resolution=1, orient=HORIZONTAL, label='Data Size')
sizeEntry.grid(row = 1, column = 1, padx = 2, pady = 2 )

#creating the min value setting menu
minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label='Min value')
minEntry.grid(row = 1, column = 3, padx = 2, pady = 2)

#creating the max value setting menu
maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label='Max value')
maxEntry.grid(row = 1, column = 5, padx = 2, pady = 2)




root.mainloop()