# splunkHEC
This module was developed to simplify the process of sending events to Splunk Cloud

## User mode 

Save the file splunkHEC.py in the same directory as your script and then add import splunkHEC at the beginning of your script.

Example code:

```python
import splunkHEC


token="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
url = "https://<endpoint>.splunkcloud.com/services/collector/event"
index = "main"
sourcetype = "Hello"
event = "Hello, Splunk Cloud!"

splunkHEC.HEC(token, url, index, sourcetype, event)

```
