import time
import urllib

def elapsed_time(function_to_time):
	def wrapper():
		t0 = time.time()
		function_to_time
		t1 = time.time()
		print "Elapsed time : %s\n" % (t1-t0)
	return wrapper

@elapsed_time
def download_page():
	url="http://linuxacademy-static-blogspot.s3-website-us-east-1.amazonaws.com/"
	response = urllib.urlopen(url)
	return response.read()

webpage = download_page()
