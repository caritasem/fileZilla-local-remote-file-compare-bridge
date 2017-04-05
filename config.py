__author__ = 'Caritasem'

import os, re, subprocess, sys
import function

work_dir = os.path.dirname(os.path.realpath(__file__))

current_user = function.run_cmd("whoami")

fz_path = "/Users/%s/.config/filezilla/" % (current_user)

filezilla_sites = fz_path + "sitemanager.xml"

filezilla_config = fz_path + "filezilla.xml"

#kdiff3_path = "/usr/local/bin/kdiff3"
kdiff3_path = "/Applications/kdiff3.app/Contents/MacOS/kdiff3"

#file needed to be differed from remote server
#exam = "/var/folders/1g/vcz6g0n95gv36g6qgtttsm4w0000gn/T/fz3temp-2/readme.txt"

exam = sys.argv [1]
