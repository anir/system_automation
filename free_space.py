import subprocess
partition_threshold = 5
df_cmd = subprocess.check_output(['df','-k'])
lines = df_cmd.splitlines()
for line in lines[1:]:
	col = line.split()
	used = col[4]
	used = used.replace('%', '')
	if int(used) >= partition_threshold:
		print "partition %s usage is beyond threshold of %s" % (col[0], col[4])


