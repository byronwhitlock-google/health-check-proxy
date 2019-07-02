# Health Check Proxy

This GCP cloud function allows non standard uptime checks to be performed. The stackdriver uptime check does not allow verification of http error codes. The response must always be 200. This GCP cloud function is should be called by the stackdriver uptime check. It will do a subrequest to a url defined in cloud storage, then print out the http status code of the subrequest. This cloud function should always return 200 itself so it can be checked via response output in stackdriver monitoring.

## Getting Started

Make sure you have access to a cloud storage bucket, cloud functions and stackdriver alerting and monitoring.


### Installing

Installation involves
  - Create Cloud Function.
  - Grant IAM permission to cloud function bucket.
  - Upload config file to GCS.
  - Create Uptime check & Alerting Policy.

Create cloud function

```
Follow the [instructions] (https://cloud.google.com/functions/docs/quickstart-python) for creating a cloud function. 
 - Copy the code from this repository, or zip and upload to the console.
 - Copy the trigger url from the "trigger" tab once the function is created.
```

Grant IAM permissions
```
 - Copy the "service account" in the cloud function details.
 - Go to Cloud storage > (select your bucket) > Permissions.
 - Add the service account as a Cloud Storage Reader. 
```

Upload Config file To GCS
```
 - Create a file named "health-check-proxy.txt" locally
 - Add the url you want to health check. 
 - for example http://35.193.169.251/403 will return a 403 and I only want to alert if it is NOT 403
```

Create uptime check policy
```
 - Go to stackdriver alerting
 - Create an uptime check
 - Use the trigger url from step one
 - under "advanced options" add "403" to the 'Response content contains the text' field.
 - This will cause the uptime check to fail if it does not see the 403 response code from the subrequest in the cloud function
 - Add an alerting policy based on this uptime check
```


## Copyright
Copyright 2019 Google LLC. This software is provided as-is, without warranty or representation for any use or purpose. Your use of it is subject to your agreement with Google.  
