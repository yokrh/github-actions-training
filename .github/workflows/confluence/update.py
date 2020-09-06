import requests
import json

# Config
domain = "yokrh.atlassian.net"
basicauth = "Basic eS5va2EuZ21sQGdtYWlsLmNvbTp2TUtSWHFyVEwwalNZSTlZdnhzVUZBRTc="
content_page_id = "262306"

# Constant
get_path = "/wiki/rest/api/content"
get_by_id_path = "/wiki/rest/api/content/"
update_by_id_path = get_by_id_path
get_method = "GET"
update_method = "PUT"

# Main

### get current content
id = content_page_id
path = get_by_id_path + id
query = "?expand=body.storage,version.number"
url = "https://" + domain + path + query
method = get_method
print(method + " " + url)
headers = {
   "Accept": "application/json",
   "Authorization": basicauth
}
response = requests.request(
   method,
   url,
   headers=headers
)
res = json.loads(response.text)
# print(json.dumps(json.loads(res), sort_keys=True, indent=4, separators=(",", ": ")))
crr_title = res['title']
crr_version = res['version']['number']
crr_storage = res['body']['storage']['value']
# print(crr_version)

### update content
version = int(crr_version) + 1
title = crr_title
storage = crr_storage + "<p>" + str(version) + "</p>"
payload = json.dumps({
  "version": {
    "number": version
  },
  "title": title,
  "type": "page",
  "body": {
    "storage": {
      "value": storage,
      "representation": "storage"
    }
  }
})
id = content_page_id
path = update_by_id_path + id
url = "https://" + domain + path
method = update_method
print(method + " " + url)
headers = {
   "Accept": "application/json",
   "Content-Type": "application/json",
   "Authorization": basicauth
}
response = requests.request(
   method,
   url,
   headers=headers,
   data=payload
)
# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
