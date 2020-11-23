import pandas as pd
import numpy as np
import xlsxwriter as writer

from tkinter import *
from tkinter import filedialog 
import tkinter.ttk as ttk

def file_selection():
	file_name = filedialog.askopenfilename(title = "Select the excel file")
	file_path.config(text = file_name)

def loc_selection():
	loc_name = filedialog.askdirectory(title = "Select the location")
	loc_path.config(text = loc_name)

def get_data(path):
	data_copy = pd.read_excel(f"{path}")
	return data_copy

def brand_names_list(data):
	#lower casing the brand names
	brand_names_lower_list = []
	brand_names = data['merchant brand name'].unique()
	
	for name in brand_names:
	    name_lower = name.lower()
	    brand_names_lower_list.append(name_lower)

	brand_names_lower = np.array(brand_names_lower_list)

	return brand_names, brand_names_lower

def replace_dup_value(data,old_value,new_value):
	my_dict = {}
	for key,val in zip(old_value,new_value):
	    my_dict[key] = val

	clean_data = data.replace({'merchant brand name': my_dict})

	return clean_data



def main_fun():
	path = file_path.cget('text')
	# check for empty path
	if len(path) == 0:
		msg = (f'\nPlease choose a file first.')
		t1.insert('1.0',msg)
	
	# check for file extension
	elif path.endswith('.xlsx') == False:
		msg = (f'\nPlease choose a excel file.')
		t1.insert('1.0',msg)

	else:
		data = get_data(path)
		brand_old_val, brand_new_val = brand_names_list(data)
		result_data = replace_dup_value(data,brand_old_val,brand_new_val)

		#brand selection
		selected_brand = brand_value.get()
		final_data = result_data.loc[result_data['merchant brand name']==selected_brand.lower()]
		
		#excel file creation and data insertion
		file_name = newfile_value.get()
		new_file_loc = loc_path.cget('text')

		if len(new_file_loc) == 0:
			msg = (f'\nPlease select the new file location')
			t1.insert('1.0',msg)

		else:
			final_data.to_excel(f'{new_file_loc}/{file_name}.xlsx', sheet_name='Sheet_name_1', index = False)
			msg = (f'\nYour file has been created, named as : {file_name}.xlsx at {new_file_loc}.')
			t1.insert('1.0',msg) 

# Gui coding
root = Tk(className = "File mover")
root.geometry("900x600")
root.configure(bg="#488AA9")

f1= Frame(root, width=900, height=100, bg="#488AA9")
f1.grid(row=0, column=0, columnspan=8)

f2= Frame(root, width=40, height=500, bg="#488AA9")
f2.grid(row=1, column=0, rowspan=35 ,sticky=NSEW)

app_title= Label(f1, text="Excel data filter", bg="#488AA9")
app_title.configure(font=("Courier", 50))
app_title.place(x=440,y=75, anchor="s")

filepath_label= Label(root, text="Filepath : ", bg="#488AA9")
filepath_label.configure(font=("Courier", 20))
filepath_label.grid(row=4, column=1, sticky=NSEW)

file_path = Label(root)
file_path.grid(row=4, column=2, columnspan=4, sticky=NSEW)

choose_button = Button(root, text='Choose file...', command=file_selection)
choose_button.configure(font=("Courier", 20))
choose_button.grid(row=6, column=2)

locpath_label= Label(root, text="Location : ", bg="#488AA9")
locpath_label.configure(font=("Courier", 20))
locpath_label.grid(row=8, column=1, sticky=NSEW)

loc_path = Label(root)
loc_path.grid(row=8, column=2, columnspan=4, sticky=NSEW)

loc_button = Button(root, text='Choose location', command=loc_selection)
loc_button.configure(font=("Courier", 20))
loc_button.grid(row=10, column=2)

brand_filter= Label(root, text="Brand name : ", bg="#488AA9")
brand_filter.configure(font=("Courier", 20))
brand_filter.grid(row=14, column=1, sticky=NSEW)

brand_value= StringVar()
brand= Entry(root, textvariable=brand_value )
brand.configure(font=("Courier", 16))
brand.grid(row=14,column=2, columnspan=3, sticky=NSEW)

newfile_name= Label(root, text="New file name : ", bg="#488AA9")
newfile_name.configure(font=("Courier", 20))
newfile_name.grid(row=16, column=1, sticky=NSEW)

newfile_value= StringVar()
newfile= Entry(root, textvariable=newfile_value )
newfile.configure(font=("Courier", 16))
newfile.grid(row=16,column=2, columnspan=3, sticky=NSEW)

create_button = Button(root, text='Create new file', command=main_fun)
create_button.configure(font=("Courier", 20))
create_button.grid(row=19, column=2)

f3= Frame(root, width= 850, height=150, bg="#488AA9")
f3.grid(row=30, column=1,columnspan=5, sticky=NSEW)

t1= Text(f3, width=60, height=6, bd=10, bg="#D2D9DD")
t1.configure(font=("helvetica", 18))
t1.grid(row=0, column=0, sticky=NSEW)

root.mainloop()