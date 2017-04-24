import subprocess
users = {}
ps_cmd = subprocess.check_output(['ps','-ef'])
for line in ps_cmd.splitlines()[1:]:
	user = line.split()[0]
	if users.get(user):
		users[user]+=1
	else:
		users[user]=1
print "Active users on the system are" + ','.join(users.keys())
print users.items()

for user, process_count in users.items():
	print "%s in running %s processes" % (user, process_count)

 
