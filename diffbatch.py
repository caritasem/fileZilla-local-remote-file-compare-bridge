__author__ = 'Caritasem'


import os, re, subprocess, sys
import xml.etree.ElementTree as etree

from config import work_dir, filezilla_sites, filezilla_config, exam
from function import diff, run_cmd, notify

filezilla_log = ""

configxml = etree.parse( filezilla_config )

configroot = configxml.getroot()

configlog = configroot.find(".//*[@name='Logging file']")

if (configlog is None):
    notify("Filezilla", "Logging file location not set")
    sys.exit()

filezilla_log = configlog.text

remote_str = ""

exam_server = run_cmd("grep Connected %s | tail -1 | awk '{ print $8}'" % ( filezilla_log ))

lastlog = run_cmd("grep local:%s %s | tail -1" % (exam, filezilla_log))

m = re.search( "remote\:(.*?)=", lastlog )

remote_file = m.group(1) 


tree = etree.parse( filezilla_sites )

root = tree.getroot()

for server in root.iter('Server'):
	host = server.find("Host").text
	
	if host != exam_server:
		continue

	diff(server, remote_file)


print( "done" )







