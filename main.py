def health_check(request):

	from urllib.request import Request, urlopen
	from urllib.error import URLError, HTTPError
	from google.cloud import storage

	# get url from environment    
	try:  
		os.environ["URL"]
	except KeyError: 
		return "Environment Variable URL not set"

	url = os.environ['URL']
	req = Request(url)
	response_code=-1

	try:
		response = urlopen(req)
		response_code =  response.code
	except HTTPError as e:
		response_code = e.code

	print (f'GET on {url} returned {response_code}')
	return f'{response_code}'