import json
# frame = [1699348497.111499, 2, '0x2FC', 'Rx', 'd', 8, [1, 0, 0, 0, 0, 0, 0, 0]]

def maskIt(string_byte, mask):
	maskedByte = ''
	for i in range(8):
		if mask[i] == '1':
			maskedByte += string_byte[i]
	return(maskedByte)

def get_car_status(frame):
	if frame[2] != '0x2FC':
		return
	mask = 'xxxx1111'
	status = {'0001': 'Unlocked', '0010': 'Locked', '0011': 'Selective_unlock', '0100': 'Secured', '0110': 'Unsecured'}
	data = frame[6]
	byte0 = format(data[0], '08b')
	maskedByte = maskIt(byte0, mask)
	car_status = status.get(maskedByte)
	return car_status

def get_doors_status(frame):
	if frame[2] != '0x2FC':
		return
	data = frame[6]
	byte1 = format(data[1], '08b')

	drd_mask = 'xxxxxx11'
	psd_mask = 'xxxx11xx'
	drdr_mask = 'xx11xxxx'
	psdr_mask = '11xxxxxx'

	door_status = {'00': 'Closed', '01': 'Opened'}
	drd_status = door_status.get(maskIt(byte1, drd_mask))
	psd_status = door_status.get(maskIt(byte1, psd_mask))
	drdr_status = door_status.get(maskIt(byte1, drdr_mask))
	psdr_status = door_status.get(maskIt(byte1, psdr_mask))

	return (f'Drd is {drd_status}, Psd is {psd_status}, Drdr is {drdr_status}, Psdr is {psdr_status}.')


# frame = [1699348540.976008, 1, '0x2CA', 'Tx', 'd', 8, [4, 0, 0, 0, 0, 0, 0, 0]]
def get_contact_status(frame):
	if frame[2] != '0x2CA':
		return
	data = frame[6]
	byte0 = format(data[0], '08b')

	drd_cont_mask = 'xxxxxx11'
	psd_cont_mask = 'xxxx11xx'
	drdr_cont_mask = 'xx11xxxx'
	psdr_cont_mask = '11xxxxxx'

	status_cont = {'00': 'Closed', '01': 'Opened'}
	drd_status_cont = status_cont.get(maskIt(byte0, drd_cont_mask))
	psd_status_cont = status_cont.get(maskIt(byte0, psd_cont_mask))
	drdr_status_cont = status_cont.get(maskIt(byte0, drdr_cont_mask))
	psdr_status_cont = status_cont.get(maskIt(byte0, psdr_cont_mask))

	return {'drd_status_cont':drd_status_cont, 'psd_status_cont':psd_status_cont, 'drdr_status_cont':drdr_status_cont, 'psdr_status_cont':psdr_status_cont}

# get_contact_status(frame)


# frame = [1699348572.49173, 2, '0x23A', 'Rx', 'd', 8, [0, 0, 4, 0, 0, 0, 0, 0]]
def get_key_button_status(frame):
	if frame[2] != '0x23A':
		return
	data = frame[6]
	byte2 = format(data[2], '08b')

	unlock_button_status_mask = 'xxxxxx11'
	lock_button_status_mask = 'xxxx11xx'
	_3d_button_status_mask = 'xx11xxxx'

	key_button_status = {'00': 'Not pressed', '01': 'Pressed', '11':'Invalid'}
	unlock_button_status = key_button_status.get(maskIt(byte2, unlock_button_status_mask))
	lock_button_status = key_button_status.get(maskIt(byte2, lock_button_status_mask))
	_3d_button_status = key_button_status.get(maskIt(byte2, _3d_button_status_mask))

	return {'unlock_button_status': unlock_button_status, 'lock_button_status': lock_button_status, '_3d_button_status': _3d_button_status}

# get_key_button_status(frame)


# frame = [1699348565.156761, 2, '0x723', 'Tx', 'd', 8, [0, 67, 232, 3, 0, 0, 0, 0]]
def get_key_info(frame):
	if frame[2] != '0x723':
		return
	data = frame[6]
	byte1 = format(data[1], '08b')
	key_pos_mask = '11xxxxxx'
	key_button_mask = 'xxxxxx11'

	key_positions = {'01': 'Inside', '10': 'Outside', '11':'Unkown'}
	key_buttons = {'10': 'Lock button', '01': 'Unlock button', '11': '3rd button'}
	key_pos = key_positions.get(maskIt(byte1, key_pos_mask))
	key_button = key_buttons.get(maskIt(byte1, key_button_mask))

	return [key_pos,key_button]


def get_trace(file_path):
	with open(file_path, 'r') as f:
		file_content = f.readlines()
		frames = []
		for frame in file_content:
			frames.append(frame)

	# remove the first 3 lines
	frames = frames[3:]
	trace = []
	for frame in frames:
		
		# split the frame into two parts, first contains frame info, and second contains data bytes
		frame_splitted = frame.split('[')
		
		# frame_info contains timestamp, can(2 for car, 1 for key), id, rx/tx, decimal, length
		frame_info = frame_splitted[0]

		# data_bytes contains data bytes, we add back the opening bracket that was removed when splitting the frame,
		# to get a valid json format so we can then convert it into a list because it is still a string representation of a list (of type string)
		data_bytes =  '[' + frame_splitted[1]

		# know we convert it into a list
		data_bytes = json.loads(data_bytes)
		# print(data_bytes)
		

		# convert frame_info into a list, and converting digital items into numeric types
		frame_info = frame_info.split()
		# print(frame_info)
		frame_info_list = []
		for index, info in enumerate(frame_info):
			if index == 0:
				frame_info_list.append(float(info))
			elif index == 1 or index == 5:
				frame_info_list.append(int(info))
			else:
				frame_info_list.append(info)
		# print(frame_info_list)


		# reconstruct the whole frame
		frame_info_list.append(data_bytes)
		frame = frame_info_list
		trace.append(frame)
	return(trace)

# def update():




