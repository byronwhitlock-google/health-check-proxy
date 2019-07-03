# Health Check Proxy

This GCP cloud function allows non standard uptime checks to be performed. The stackdriver uptime check does not allow verification of http error codes. The response must always be 200. This GCP cloud function is should be called by the stackdriver uptime check. It will do a subrequest (HTTP GET) to a url defined in cloud storage, then print out the http status code of the subrequest. This cloud function should always return 200 itself so it can be checked via response output in stackdriver monitoring.

## Getting Started

### Create Cloud Function.
 - Clone this repository
 - Run the following commands change URL to the url you wish to check.
 ```
  gcloud init
  gcloud functions deploy health-check-proxy --runtime python37 --trigger-http --entry-point health_check --set-env-vars=URL=http://google.com
```
 - This will create a cloud function named "health-check-proxy" 
 - Copy the value `httpsTrigger` from the response
 - Alternatively follow the [instructions](https://cloud.google.com/functions/docs/quickstart-python) for creating a cloud function. 

### Create uptime check policy
 - Go to stackdriver alerting
 - Create an uptime check
 - Use the `httpsTrigger` url from step one
 - under "advanced options" add "403" to the 'Response content contains the text' field.
 - This will cause the uptime check to fail if it does not see the 403 response code from the subrequest in the cloud function
 - Add an alerting policy based on this uptime check



## Copyright
Copyright 2019 Google LLC. This software is provided as-is, without warranty or representation for any use or purpose. Your use of it is subject to your agreement with Google.  
