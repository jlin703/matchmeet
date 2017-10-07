########### Python 3.6 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, json
import sys

###############################################
#### Update or verify the following values. ###
###############################################

tags = json.loads(open('tags.json').read())
tags = set(tags)
# Read images url from stdin
# json_input = sys.stdin.readlines()
json_input = '["https://stillmed.olympic.org/media/Photos/2016/08/14/part-2/14-08-2016-tennis-doubles-mixed-04.jpg"]'
json_input = open('tennis_person.json').read()
urls = json.loads(json_input)

# Replace the subscription_key string value with your valid subscription key.
subscription_key = '35b0725209e04bb187f8b512e935cc3d'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'westcentralus.api.cognitive.microsoft.com'

headers = {
    # Request headers.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = urllib.parse.urlencode({
    # Request parameters. All of them are optional.
    'visualFeatures': 'Categories,Description,Color',
    'language': 'en',
})

def analyzeImage(url):
    # Replace the three dots below with the URL of a JPEG image of a celebrity.
    body = "{'url': '" + url + "'}"

    try:
        # Execute the REST API call and get the response.
        conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()

        # 'data' contains the JSON data. The following formats the JSON data for display.
        parsed = json.loads(data)
        img_tags = set(parsed['description']['tags'])
        # print ("Response:")
        # print (json.dumps(parsed, sort_keys=True, indent=2))
        conn.close()
        return set.intersection(img_tags, tags)

    except Exception as e:
        pass

counts = dict()
for tag in tags:
    counts[tag] = 0
for img in urls:
    common_tags = analyzeImage(img)
    for common_tag in common_tags:
        counts[common_tag] += 1
countsLst = [counts[tag] for tag in tags]
maxCount = max(countsLst)
scores = [c / maxCount * 10 for c in countsLst]
print(counts)
print(scores)
