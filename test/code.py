
# frame = [1699348572.49173, 2, '0x23A', 'Rx', 'd', 8, [0, 0, 4, 0, 0, 0, 0, 0]]
from Decoder import *
from datetime import datetime
# import decoder_gui

car_variables = {
	'ID': '0x000',
	'txrx': None,
	'frame': [0,0,0,0,0,0,0],
	'time' : '00:00',
	'car_status': 'Unlocked',
	'key_position': 'Inside',
	'key_button':'Lock button',

	'drd_status_cont': 'Closed', 
	'psd_status_cont':'Closed', 
	'drdr_status_cont':'Closed', 
	'psdr_status_cont':'Closed',

	'unlock_button_status':'Not pressed',
	'lock_button_status':'Not pressed',
	'_3d_button_status': 'Not pressed'
}

get_time = datetime.fromtimestamp

Ids = {'car_status': '0x2FC', 'key_button_status': '0x23A', 'contact_status':'0x2CA', 'key_info': '0x723'}

def trace_construct(file):
	updated_frames = []
	frames_in_file = []
	all_frames = []
	trace = get_trace(file)
	for frame in trace:
		time = get_time(frame[0]).strftime("%I%p %M:%S")
		if frame[2] == Ids['car_status']:
			car_status = get_car_status(frame)
			car_variables.update({'car_status':car_status,'time':time,'ID':frame[2],'frame':frame[6],'txrx':frame[3]})

		elif frame[2] == Ids['key_button_status']:
			key_button_status = get_key_button_status(frame)
			car_variables.update({'unlock_button_status':key_button_status['unlock_button_status'],'lock_button_status':key_button_status['lock_button_status'],'_3d_button_status':key_button_status['_3d_button_status'],'time':time,'ID':frame[2],'frame':frame[6],'txrx':frame[3]})

		elif frame[2] == Ids['contact_status']:
			contact_status = get_contact_status(frame)
			for status in contact_status:
				car_variables.update({status:contact_status.get(status),'time':time,'ID':frame[2],'frame':frame[6],'txrx':frame[3]})

		elif frame[2] == Ids['key_info']:
			key_info = get_key_info(frame)
			car_variables.update({'key_position':key_info[0],'key_button':key_info[1],'time':time,'ID':frame[2],'frame':frame[6],'txrx':frame[3]})
			# print(frame[6], key_info,'\n')
		elif frame[2] == '0x2AF':
			car_variables.update({'ID':frame[2],'frame':[0,0,0,0,0,0,0,0]})

		# all_frames.append(car_variables.copy())
		all_frames.append(car_variables.copy())
		frames_in_file.append(frame)

	return all_frames










