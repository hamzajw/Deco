import tkinter as tk
# from tkinter import Tk     # from tkinter import Tk for Python 3.x
# import code, Decoder
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk



# frame = [1699348572.49173, 2, '0x23A', 'Rx', 'd', 8, [0, 0, 4, 0, 0, 0, 0, 0]]



status_colors = {
	'Secured': '#33FF55',
	'Unlocked': 'red',
	'Locked' : '#9FE2BF',
	None : '#808080'
}



root = tk.Tk() # create a window
root.geometry("950x400")
root.title('Can Decoder by Hamza')


index = -1
my_list = []
def choose_file():
	global my_list
	from code import trace_construct   # I import it here to avoid circular import (when two modules import each other)
	filename = askopenfilename()
	my_list = trace_construct(filename)
	frame_up()

	
def frame_up():
	if not(my_list):
		return
	global index
	if index >= len(my_list)-1:
		index =-1
	index +=1
	frame_text.set(my_list[index]['frame'])
	id_value.set(my_list[index]['ID'])
	TxRx_value.set(my_list[index]['txrx'])
	time_value.set(my_list[index]['time'])
	car_status_value.set(my_list[index].get('car_status'))
	key_pos_value.set(my_list[index]['key_position'])
	unlock_btn_value.set(my_list[index]['unlock_button_status'])
	lock_btn_value.set(my_list[index]['lock_button_status'])
	drd_cont_value.set(my_list[index]['drd_status_cont'])
	_3d_btn_value.set(my_list[index]['_3d_button_status'])
	drdr_cont_value.set(my_list[index]['drdr_status_cont'])
	psd_cont_value.set(my_list[index]['psd_status_cont'])
	psdr_cont_value.set(my_list[index]['psdr_status_cont'])
	index_value.set(f'{index+1} :')
	status_color_btn.configure(bg=status_colors[my_list[index].get('car_status')])
	if my_list[index]['drd_status_cont'] == 'Opened':
		lock_drd_label.place_forget()
		unlock_drd_label.place(x=610,y=160)
	elif my_list[index]['drd_status_cont'] == 'Closed':
		lock_drd_label.place(x=610,y=160)
		unlock_drd_label.place_forget()

	if my_list[index]['drdr_status_cont'] == 'Opened':
		lock_drdr_label.place_forget()
		unlock_drdr_label.place(x=610,y=250)
	else:
		lock_drdr_label.place(x=610,y=250)
		unlock_drdr_label.place_forget()

	if my_list[index]['psd_status_cont'] == 'Opened':
		lock_psd_label.place_forget()
		unlock_psd_label.place(x=830,y=160)
	else:
		lock_psd_label.place(x=830,y=160)
		unlock_psd_label.place_forget()

	if my_list[index]['psdr_status_cont'] == 'Opened':
		lock_psdr_label.place_forget()
		unlock_psdr_label.place(x=830,y=250)
	else:
		lock_psdr_label.place(x=830,y=250)
		unlock_psdr_label.place_forget()



def frame_down():
	if not(my_list):
		return
	global index
	if index <=0:
		index = len(my_list)
	index -= 1
	frame_text.set(my_list[index]['frame'])
	id_value.set(my_list[index]['ID'])
	TxRx_value.set(my_list[index]['txrx'])
	time_value.set(my_list[index]['time'])
	car_status_value.set(my_list[index].get('car_status'))
	key_pos_value.set(my_list[index]['key_position'])
	unlock_btn_value.set(my_list[index]['unlock_button_status'])
	lock_btn_value.set(my_list[index]['lock_button_status'])
	_3d_btn_value.set(my_list[index]['_3d_button_status'])
	drd_cont_value.set(my_list[index]['drd_status_cont'])
	drdr_cont_value.set(my_list[index]['drdr_status_cont'])
	psd_cont_value.set(my_list[index]['psd_status_cont'])
	psdr_cont_value.set(my_list[index]['psdr_status_cont'])
	index_value.set(f'{index +1} :')
	status_color_btn.configure(bg=status_colors[my_list[index].get('car_status')])

	if my_list[index]['drd_status_cont'] == 'Opened':
		lock_drd_label.place_forget()
		unlock_drd_label.place(x=610,y=160)
	else:
		lock_drd_label.place(x=610,y=160)
		unlock_drd_label.place_forget()

	if my_list[index]['drdr_status_cont'] == 'Opened':
		lock_drdr_label.place_forget()
		unlock_drdr_label.place(x=610,y=250)
	else:
		lock_drdr_label.place(x=610,y=250)
		unlock_drdr_label.place_forget()

	if my_list[index]['psd_status_cont'] == 'Opened':
		lock_psd_label.place_forget()
		unlock_psd_label.place(x=830,y=160)
	else:
		lock_psd_label.place(x=830,y=160)
		unlock_psd_label.place_forget()

	if my_list[index]['psdr_status_cont'] == 'Opened':
		lock_psdr_label.place_forget()
		unlock_psdr_label.place(x=830,y=250)
	else:
		lock_psdr_label.place(x=830,y=250)
		unlock_psdr_label.place_forget()

		




previous_frame_button = tk.Button(root,text ="<<",command=frame_down)
previous_frame_button.place(x=10,y=10,width=42)

next_frame_button = tk.Button(root,text =">>",command=frame_up)
next_frame_button.place(x=55,y=10,width=42)

index_value = tk.StringVar()
# index_value.set(f'#{index+1} :')
index_label = tk.Label(root,textvariable=index_value,width=2,bg='white')
index_label.place(x=110,y=10)

frame_text = tk.StringVar()
# frame_text.set(my_list[0]['frame'])
frame_label = tk.Label(root,textvariable=frame_text,width=15,bg='white')
frame_label.place(x=140,y=10)



id_btn = tk.Button(root,text='ID:',width=4)
id_btn.place(x=265,y=10)
id_value = tk.StringVar()
# id_value.set(my_list[0]['ID'])
id_label = tk.Label(root,textvariable=id_value,width=10,bg='white')
id_label.place(x=310,y=10)

TxRx_value = tk.StringVar()
# TxRx_value.set(my_list[0]['txrx'])
TxRx_label = tk.Label(root,textvariable=TxRx_value,width=2,bg='white')
TxRx_label.place(x=390,y=10)


time_btn = tk.Button(root,text='Time : ')
time_btn.place(x=10,y=40,width=90)
time_value = tk.StringVar()
# time_value.set(my_list[0]['time'])
time_label = tk.Label(root,textvariable=time_value,width=15,bg='white')
time_label.place(x=110,y=40)


car_status_btn = tk.Button(root,text='Car Status: ')
car_status_btn.place(x=10,y=70,width=90)
car_status_value = tk.StringVar()
# car_status_value.set(my_list[0]['car_status'])
car_status_label = tk.Label(root,textvariable=car_status_value,width=15,bg='white')
car_status_label.place(x=110,y=70)

status_color_btn = tk.Button(root,text='  ')
status_color_btn.place(x=200,y=70,height=20)



key_pos_btn = tk.Button(root,text='Key Position : ')
key_pos_btn.place(x=10,y=100,width=90)
key_pos_value = tk.StringVar()
# key_pos_value.set(my_list[0]['key_position'])
key_pos_label = tk.Label(root,textvariable=key_pos_value,width=15,bg='white')
key_pos_label.place(x=110,y=100)

unlock_btn_btn = tk.Button(root,text='Unlock button : ')
unlock_btn_btn.place(x=10,y=130,width=90)
unlock_btn_value = tk.StringVar()
# unlock_btn_value.set(my_list[0]['unlock_button_status'])
unlock_btn_label = tk.Label(root,textvariable=unlock_btn_value,width=15,bg='white')
unlock_btn_label.place(x=110,y=130)

lock_btn_btn = tk.Button(root,text='Lock button : ')
lock_btn_btn.place(x=10,y=160,width=90)
lock_btn_value = tk.StringVar()
# lock_btn_value.set(my_list[0]['lock_button_status'])
lock_btn_label = tk.Label(root,textvariable=lock_btn_value,width=15,bg='white')
lock_btn_label.place(x=110,y=160)

_3d_btn_btn = tk.Button(root,text='3d button : ')
_3d_btn_btn.place(x=10,y=190,width=90)
_3d_btn_value = tk.StringVar()
# _3d_btn_value.set(my_list[0]['_3d_button_status'])
_3d_btn_label = tk.Label(root,textvariable=_3d_btn_value,width=15,bg='white')
_3d_btn_label.place(x=110,y=190)

drd_cont_btn = tk.Button(root,text='DRD status: ')
drd_cont_btn.place(x=260,y=70,width=100)
drd_cont_value = tk.StringVar()
# drd_cont_value.set(my_list[0]['drd_status_cont'])
drd_cont_label = tk.Label(root,textvariable=drd_cont_value,width=15,bg='white')
drd_cont_label.place(x=370,y=70)


drdr_cont_btn = tk.Button(root,text='DRDR status: ')
drdr_cont_btn.place(x=260,y=100,width=100)
drdr_cont_value = tk.StringVar()
# drdr_cont_value.set(my_list[0]['drdr_status_cont'])
drdr_cont_label = tk.Label(root,textvariable=drdr_cont_value,width=15,bg='white')
drdr_cont_label.place(x=370,y=100)


psd_cont_btn = tk.Button(root,text='PSD status: ')
psd_cont_btn.place(x=260,y=130,width=100)
psd_cont_value = tk.StringVar()
# psd_cont_value.set(my_list[0]['psd_status_cont'])
psd_cont_label = tk.Label(root,textvariable=psd_cont_value,width=15,bg='white')
psd_cont_label.place(x=370,y=130)


psdr_cont_btn = tk.Button(root,text='PSDR status: ')
psdr_cont_btn.place(x=260,y=160,width=100)
psdr_cont_value = tk.StringVar()
# psdr_cont_value.set(my_list[0]['psdr_status_cont'])
psdr_cont_label = tk.Label(root,textvariable=psdr_cont_value,width=15,bg='white')
psdr_cont_label.place(x=370,y=160)


choose_file_btn = tk.Button(root,text='Choose trace file',command=choose_file)
choose_file_btn.place(x=100,y=220,width=300)


car_img = Image.open('car_top_view.png')  # using pillow Image method to open an image
resized_car_img = car_img.resize((380,380), Image.LANCZOS)  #
converted_car_img = ImageTk.PhotoImage(resized_car_img)  # convert the image to a fomart compatible with tkinter/ or normal image
car_label = tk.Label(root,image=converted_car_img,bg='#808080')
car_label.place(x=550,y=10)


#unlock images
unlock_img = ImageTk.PhotoImage(Image.open('unlock.png').resize((40,40),Image.LANCZOS))  # same as for the car image but in one line
unlock_drd_label = tk.Label(root,image=unlock_img)
unlock_drdr_label = tk.Label(root,image=unlock_img)
unlock_psd_label = tk.Label(root,image=unlock_img)
unlock_psdr_label = tk.Label(root,image=unlock_img)

unlock_drd_label.place(x=610,y=160)
unlock_drdr_label.place(x=610,y=250)
unlock_psd_label.place(x=830,y=160)
unlock_psdr_label.place(x=830,y=250)

#lock images
lock_img = ImageTk.PhotoImage(Image.open('lock.png').resize((40,40),Image.LANCZOS))  # same as for the car image but in one line
lock_drd_label = tk.Label(root,image=lock_img)
lock_drdr_label = tk.Label(root,image=lock_img)
lock_psd_label = tk.Label(root,image=lock_img)
lock_psdr_label = tk.Label(root,image=lock_img)

lock_drd_label.place(x=610,y=160)
lock_drdr_label.place(x=610,y=250)
lock_psd_label.place(x=830,y=160)
lock_psdr_label.place(x=830,y=250)



root.mainloop()