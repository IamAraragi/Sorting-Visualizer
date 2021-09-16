from tkinter import *
from tkinter import ttk
import random
from colors import *

from algorithms.merge_sort import merge_sort
from algorithms.insertion_sort import insertion_sort

def drawData(data, colorArray):
	canvas.delete('all')
	canvas_width = 1000
	canvas_height = 420
	x_width = canvas_width / (len(data) + 1)
	offset = 4
	spacing = 2
	normalized_data = [i / max(data) for i in data]

	for i, height in enumerate(normalized_data):
		x0 = i*x_width + offset + spacing
		y0 = canvas_height - height *400
		x1 = (i + 1) * x_width + offset
		y1 = canvas_height
		canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

	window.update_idletasks()

def generate():
	global data

	data = []
	for i in range(50):
		random_value = random.randint(20, 200)
		data.append(random_value)

	drawData(data, [BLUE]*len(data))

def speed():
	if speed_menu.get() == 'fast':
		return 0.001
	elif speed_menu.get() == 'medium':
		return 0.1
	else:
		return 0.3

def sort():
	wait_time = speed()

	if algo_menu.get() == 'insertion_sort':
		insertion_sort(data, drawData, wait_time)
	else:
		merge_sort(data, 0, len(data)-1, drawData, wait_time)

#tkinter window
window = Tk()
window.minsize(1080, 720)
window.title('Sorting Visulaizer')
window.config(bg=LIGHT_GRAY)

algo_name = StringVar()
algo_list = ['merge_sort', 'insertion_sort']

speed_name = StringVar()
speed_list = ['fast', 'medium', 'slow']


frame = Frame(window, width=1080, height=300, bg=LIGHT_GRAY)
frame.grid(row=0, column=0, padx=10, pady=5)

name_label = Label(frame, text='Algorithm: ', bg=LIGHT_GRAY)
name_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
algo_menu = ttk.Combobox(frame, textvariable=algo_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=10, pady=5)
algo_menu.current(0)

speed_label = Label(frame, text='Speed: ', bg=LIGHT_GRAY)
speed_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
speed_menu = ttk.Combobox(frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=10, pady=5)
speed_menu.current(0)

sort_button = Button(frame, text='Sort', command=sort, bg=DARK_GRAY)
sort_button.grid(row=2, column=1, padx=5, pady=5)

generate_button = Button(frame, text='Generate', command=generate, bg=DARK_GRAY)
generate_button.grid(row=2, column=0, padx=5, pady=5)

canvas = Canvas(window, width=1000, height=420, bg=LIGHT_GRAY)
canvas.grid(row=1, column=0, padx=10, pady=5)

window.mainloop()