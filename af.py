###########################################
#WAHYU ARIF P - IDSYSTEM404
#UPDATE : 18 DESEMBER 2017 - 3:07 PM
###########################################
#CARA PENGGUNAAN
#INSTALL PYTHON
#RUN CLI : python IDSYSTEM404adminpanel.py
###########################################

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("admin.txt","r"); #LIST DORK ADMIN
	link = raw_input("Masukkan URL Website : ") #MASUKKAN ALAMAT URL WEBSITE
	print "\n\nAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_link

def Credit():
	Space(9); print "##################################"
	Space(9); print "#   +++ Admin Panel Finder +++   #"
	Space(9); print "#     		IDSYSTEM404 	      #"
	Space(9); print "##################################"

Credit()
findAdmin()
