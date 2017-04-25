from fabric.api import sudo

def update_server():
	sudo ("yum -y upgrade", pty=True)
 
