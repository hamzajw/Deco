
# frame = [1699348572.49173, 2, '0x23A', 'Rx', 'd', 8, [0, 0, 4, 0, 0, 0, 0, 0]]
from Decoder import *
from datetime import datetime
# import decoder_gui

car_variables = {
	'ID': '0x000',
	'txrx': None,
	'frame': '0,0,0,0,0,0,0',
	'time' : '00:00',
	'car_status': 'Unlocked',
	'key_position': 'Inside',

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
	all_frames = []
	trace = get_trace(file)
	for frame in trace:
		if frame[2] == Ids.get('car_status'):
			car_status = get_car_status(frame)
			if car_status != car_variables.get('car_status'):
				time = get_time(frame[0]).strftime("%I%p %M:%S")
				car_variables.update({'car_status':car_status,'time':time,'ID':frame[2],'frame':frame[6],'txrx':frame[3]})
				updated_frames.append(car_variables.copy())

		elif frame[2] == Ids.get('key_button_status'):
			key_button_status = get_key_button_status(frame)
			for kb_status in key_button_status:
				if key_button_status.get(kb_status) != car_variables.get(kb_status):
					time = time = get_time(frame[0]).strftime("%I%p %M:%S")
					car_variables.update({kb_status:key_button_status.get(kb_status),'time':time,'ID':frame[2],'frame':frame[6],'txrx':frame[3]})
					updated_frames.append(car_variables.copy())

		elif frame[2] == Ids.get('contact_status'):
			contact_status = get_contact_status(frame)
			for status in contact_status:
				if contact_status.get(status) != car_variables.get(status):
					time = time = get_time(frame[0]).strftime("%I%p %M:%S")
					car_variables.update({status:contact_status.get(status),'time':time,'ID':frame[2],'frame':frame[6],'txrx':frame[3]})
					updated_frames.append(car_variables.copy())

		elif frame[2] == Ids.get('key_info'):
			key_position = get_key_info(frame)[0]
			if key_position != car_variables.get('key_position'):
				time = time = get_time(frame[0]).strftime("%I%p %M:%S")
				car_variables.update({'key_position': key_position,'time':time,'ID':frame[2],'frame':frame[6],'txrx':frame[3]})
				updated_frames.append(car_variables.copy())
		all_frames.append(car_variables.copy())
	# return updated_frames
	print(len(all_frames))
	return all_frames













