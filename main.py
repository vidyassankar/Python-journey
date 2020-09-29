import webbrowser as wb

While True:
		print("Welcome ! , What are you looking for today? : ", end='')
		p = input()
		if ("date" in p):
		 wb.open("http://172.27.173.58/cgi-bin/local.py?x=date")
		elif("calendar" in p):
		 wb.open("http://172.27.173.58/cgi-bin/local.py?x=cal")
		elif ("disk space" in p):
		 wb.open("http://172.27.173.58/cgi-bin/local.py?x=df%20-k")
		elif (("install" in p) and ("httpd")):
		 wb.open("http://172.27.173.58/cgi-bin/local.py?x=yum%20install%20httpd")
		elif (("exit" in p) or ("quit" in p)):
		 break
		else:
		print("Unable to understand your requirement")