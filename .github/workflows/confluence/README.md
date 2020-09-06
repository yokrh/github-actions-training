# Confluence 

My test confluence

https://yokrh.atlassian.net/wiki/spaces/TESTSPACE/pages/262306/content+1-1-a


## Confluence api

https://developer.atlassian.com/cloud/confluence/rest/intro/


### Auth

* Token

    https://id.atlassian.com/manage-profile/security/api-tokens

* Basic auth

    https://developer.atlassian.com/cloud/confluence/basic-auth-for-rest-apis/


### Request

https://developer.atlassian.com/cloud/confluence/rest/api-group-content/

```sh
CF_USERNAME='y.oka.gml@gmail.com'
CF_PASSWORD='vMKRXqrTL0jSYI9YvxsUFAE7'
echo "Basic $(echo -n $CF_USERNAME:$CF_PASSWORD | base64)"
# Basic eS5va2EuZ21sQGdtYWlsLmNvbTp2TUtSWHFyVEwwalNZSTlZdnhzVUZBRTc=
```

```sh
# Get content
curl --request GET \
  --url 'https://yokrh.atlassian.net/wiki/rest/api/content' \
  --header 'Accept: application/json' \
  --header 'Authorization: Basic eS5va2EuZ21sQGdtYWlsLmNvbTp2TUtSWHFyVEwwalNZSTlZdnhzVUZBRTc='
```

```sh
# Get content by id
curl --request GET \
  --url 'https://yokrh.atlassian.net/wiki/rest/api/content/262306?expand=body.storage' \
  --header 'Accept: application/json' \
  --header 'Authorization: Basic eS5va2EuZ21sQGdtYWlsLmNvbTp2TUtSWHFyVEwwalNZSTlZdnhzVUZBRTc=' | jq . > hoge.json
```

```sh
# Update content by id
curl --request PUT \
  --url 'https://yokrh.atlassian.net/wiki/rest/api/content/262306' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Basic eS5va2EuZ21sQGdtYWlsLmNvbTp2TUtSWHFyVEwwalNZSTlZdnhzVUZBRTc=' \
  --data '{
  "version": {
    "number": 19
  },
  "title": "<string>",
  "type": "page",
  "status": "current",
  "ancestors": [
    {
      "id": "<string>"
    }
  ],
  "body": {
    "view": {
      "value": "<string>",
      "representation": "view"
    },
    "export_view": {
      "value": "<string>",
      "representation": "view"
    },
    "styled_view": {
      "value": "<string>",
      "representation": "view"
    },
    "storage": {
      "value": "<string>",
      "representation": "storage"
    },
    "editor2": {
      "value": "<string>",
      "representation": "view"
    },
    "anonymous_export_view": {
      "value": "<string>",
      "representation": "view"
    }
  }
}'
```

## Thanks
https://qiita.com/KAWAII/items/3a10f17776121c9e7da3
https://asmz.hatenablog.jp/entry/create-confluence-page-via-api
