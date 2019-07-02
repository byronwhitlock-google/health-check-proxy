def health_check(request):

	from urllib.request import Request, urlopen
	from urllib.error import URLError, HTTPError
	from google.cloud import storage

	# load list of urls to check from this bucket
	#bucket_name = 'my-new-bucket'
	bucket_name = "bigbuvket-bb"

	# single url
	file_name = 'health-check-proxy.txt' 

	storage_client = storage.Client()

	bucket = storage_client.get_bucket(bucket_name)
	blob = bucket.get_blob(file_name)
	url = blob.download_as_string().decode("utf8").strip()

	req = Request(url)
	response_code=-1

	try:
		response = urlopen(req)
		response_code =  response.code
	except HTTPError as e:
		response_code = e.code

	print (f'GET on {url} returned {response_code}')
	return f'{response_code}'



