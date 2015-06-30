__author__ = 'Caritasem'


import os, re, subprocess, sys

work_dir = os.path.dirname(os.path.realpath(__file__))

'''
filezilla's default sitemanager.xml
Change this line to your machine's path
'''
filezilla_sites = "/Users/caritasem/.config/filezilla/sitemanager.xml"


'''
Open filezilla's setting->logging
check "Log to file"
'''
filezilla_log = work_dir + "/filezilla.log"

'''
tmp remote file
'''
exam = sys.argv [1] 

remote_str = ""

'''
Get last remote host that filezilla connected to
'''
exam_server = subprocess.check_output("grep Connected " + filezilla_log + " | tail -1 | awk '{ print $8}'", shell=True)

'''
Get the real remote file needed to  differ
'''
lastlog = subprocess.check_output("grep local:" + exam + " " + filezilla_log + " | tail -1", shell=True, universal_newlines=True)

m = re.search( "remote\:(.*?)=", lastlog )

remote_file = m.group(1) 


'''
Get corresponding local directory 
'''
import xml.etree.ElementTree as etree

tree = etree.parse( filezilla_sites )

root = tree.getroot()

for server in root[0]:
	host = server.find("Host").text

	if host != exam_server.decode("utf-8").strip():
		continue

	remote_cfg = server.find("RemoteDir").text
	local_path = server.find("LocalDir").text

	remote_cfg_ary = remote_cfg.split(" ")
	remote_cfg_path = ""
	for idx, val in enumerate(remote_cfg_ary):
		if idx < 2:
			continue

		_tmp = ""
		if idx % 2 == 1  :
			_tmp = val
		else:
			_tmp = "/"
		remote_cfg_path = remote_cfg_path + _tmp
	
	if remote_cfg_path in remote_file:
		file_name = remote_file[ len(remote_cfg_path) : ]
		localfile = (local_path + file_name).strip()

		if ( os.path.exists(localfile) ):

			'''
			differ file
			'''
		
			subprocess.call( "/usr/local/bin/kdiff3 " + localfile + " " + exam, shell=True )
		
		else:

			subprocess.Popen( "osascript -e 'tell app \"System Events\" to display alert \""+localfile+" does not exist\"'" , shell=True,
				stdin=None, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, close_fds=True)



print( "hello" )







