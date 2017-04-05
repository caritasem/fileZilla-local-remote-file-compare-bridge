# fileZilla-local-remote-file-compare-bridge
An Python3 script to do local-remote-file-comparation-job in filezilla for mac os

FileZilla is a great tool for me to do remote server synchronization, but I found it missing the feature to do local/remote file comparation. So i write this convenient script with the help of kdiff3.

The logic behind is very simple. First, download remote file to local tmp file, then read configuration from filezilla xml to identify the corresponding local file. Then invoke kdiff3 as the swiss army knife to compare files.

## How to use ?

1. pull this git
2. set filezilla's settings, set file custom editor
	![custom editor](https://raw.githubusercontent.com/caritasem/fileZilla-local-remote-file-compare-bridge/master/assets/always_use_custom_editor.png) 

	Like :

	```
	/usr/local/bin/python3 #path-to-diffbatch.py#
	```
3.  modify config.py variables, and make sure wirte filezilla log to local file


connect to sever, right click on file you want to compare, then chose view/edit.

## Related
- [kdiff3](http://kdiff3.sourceforge.net/)