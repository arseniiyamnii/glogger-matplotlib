# Google offline logger
## Create graph with matplotlob, from google logger json
  
### Requirements:
Create enviroment  
```bash
source env/bin/activate || python3 -m venv env && source env/bin/activate
```
Install requirements:  
```bash
pip install -r requirements.txt
```
### Usage:
Download logs with command(example query):
```bash
timestamp="2022-08-09 02:30:00"
gcloud logging read \
  'resource.type=k8s_container AND 
	timestamp>"'$(date +'%Y-%m-%dT%H:%M:%S%z' -d $timestamp'+5 -3 hour')'" AND 
	timestamp<"'$(date +'%Y-%m-%dT%H:%M:%S%z' -d $timestamp'+5 +7 hour')'" AND
	textPayload=~"POST /.*/register"' \
--format json > /tmp/longlog.json
```
  
Then run   
```bash
./main.py /tmp/longlog.json
```
  
Output, its something like this:
![Graph](img/test.png?raw=true "Title")
