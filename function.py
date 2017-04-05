import os, subprocess
import config

def run_cmd(cmd):
	output = ""
	try:
		output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
	except	subprocess.CalledProcessError as e:
		pass
	return output.strip()

def diff(server, remote_file):
    remote_cfg = server.find("RemoteDir").text
    local_path = server.find("LocalDir").text
    
    #print(server.find("Name").text)

    remote_cfg_ary = remote_cfg.split(" ")
    remote_cfg_path = ""
    for idx, val in enumerate(remote_cfg_ary):
        if idx < 2:
            continue

        _tmp = ""
        if idx % 2 == 1:
            _tmp = val
        else:
            _tmp = "/"
        remote_cfg_path = remote_cfg_path + _tmp

    if remote_cfg_path in remote_file:
        file_name = remote_file[len(remote_cfg_path):]
        localfile = (local_path + file_name).strip()

        if (os.path.exists(localfile)):
            
            #subprocess.call("%s %s %s" % (config.kdiff3_path, localfile, config.exam), shell=True)
            subprocess.Popen([config.kdiff3_path, localfile, config.exam])

        else:
            
            notify("Filezilla", "%s does not exist! " % (localfile))
    else:
        #print("not same site")
        pass



def notify(title, content):
	subprocess.Popen("osascript -e 'display notification \"" + content + "\" with title \"" + title + "\"'", shell=True,
                             stdin=None, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, close_fds=True)

