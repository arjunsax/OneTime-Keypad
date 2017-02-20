''' define global variables '''

SWITCH = 0
CAPS = 0
PAGES = []
#global AUTO_DICT
#global CAPS_LOCK



keys_poss = ['Numlock', 'Divide', 'Multiply', 'Numpad7',
			 'Numpad8', 'Numpad9', 'Subtract', 'Numpad4',
			 'Numpad5', 'Numpad6', 'Add' , 'Numpad1',
			 'Numpad2', 'Numpad3', 'Numpad0', 'Decimal']

keys_poss2 = ['Numlock', 'Divide', 'Multiply', 'Home',
			 'Up', 'Prior', 'Subtract', 'Left',
			 'Clear', 'Right', 'Add' , 'End',
			 'Down', 'Next', 'Insert', 'Delete']




def init():
	'''
	the upper four function keys, Backspace, enter and whitespace buttons are not mapped.
	the num_lock button is always mapping to switch.
	'''
	global SWITCH
	global PAGES
	#AUTO_DICT = []
	#CAPS_LOCK = False
	char_set = ['a', 'b', 'c', 'd', 'e',
				'f', 'g', 'h', 'i', 'j',
				'k', 'l', 'm', 'n', 'o',
				'p', 'q', 'r', 's', 't',
				'u', 'v', 'w', 'x', 'y',
				'z', '1', '2', '3', '4',
				'5', '6', '7', '8', '9',
				'0', '`', '!', '@', '#',
				'$', '%', '^', '&', '*',
				'(', ')', '-', '_', '=',
				'+', '[', ']', '{', '}',
				'|', ';', ':', '/', '?',
				',', '.', '<', '>', '\'',
				'\"', '\\', '~', 'Tab',
				'A', 'B', 'C', # psi(968), <<(171), not(172)
				'D', 'E', 'F', # omega(969), deg(176), +=(177)
				'G', 'H', 'I', # chi(967), >>(187), phi(966)
				'J', 'K', 'L', # lambda(955), alpha(945), Beta(946)
				'M', 'N', 'O'] # gamma(947), delta(948), epsilon(949)
	tmp = 0
	for t in range(0, 6):
		dict_Temp = {}
		dict_Temp[keys_poss[0]] = 'Switch'
		dict_Temp[keys_poss[1]] = 'CapsLock'
		for x in range(2, 16):
			char = char_set[tmp]
			if tmp < 84 and (t % 2 is 0):
				dict_Temp[keys_poss[x]] = char
				tmp += 1
			elif tmp < 84 and (t % 2 is 1):
				dict_Temp[keys_poss2[x]] = char
				tmp += 1
		PAGES.append(dict_Temp)
	print(PAGES)

