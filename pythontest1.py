#print("press 1 for chrome: ")
#print("press 2 for mediaplayer: ")
#print("press 3 for notepad: ")

import os

while True:
	print("Welcome ! , What are you looking for today? : ", end='')
	p = input()



	if (('run' in p) or ('open' in p)) and (('browser' in p) or ('chrome' in p)):
		os.system("start chrome")
 
	elif (('run' in p) or ('open' in p)) and (('acrobat' in p) or ('pdf' in p) or ('reader' in p)):
		os.system("start AcroRd32")

	elif (('run' in p) or ('open' in p)) and (('notepad' in p) or ('text' in p) or ('text editor' in p)):
		os.system("notepad")

	elif (('run' in p) or ('open' in p) or ('play' in p)) and (('media' in p) or ('music' in p) or ('audio player' in p)):
		os.system("start wmplayer")


	elif (('run' in p) or ('open' in p) or ('play' in p)) and (('calculator' in p) or ('calc' in p) or ('calculation' in p)):
		os.system("start calc")


	elif (('run' in p) or ('open' in p) or ('play' in p)) and (('paint' in p) or ('mspaint' in p) or ('draw' in p)):
		os.system("start mspaint")


	elif (('run' in p) or ('open' in p) or ('play' in p)) and (('excel' in p) or ('spreadsheet' in p) or ('office excel' in p)):
		os.system("start excel")


	elif (('run' in p) or ('open' in p) or ('play' in p)) and (('word' in p) or ('document editor' in p) or ('doc editor' in p)):
		os.system("start winword")


	elif (('run' in p) or ('open' in p) or ('play' in p)) and (('snipping' in p) or ('cutting tool' in p)):
		os.system("start SnippingTool")
 
	elif ('exit' in p) or ('quit' in p) or ('come out' in p ) or ('escape' in p):
		break

	

	else:
		print(" Unable to support your request ")