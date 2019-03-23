import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    iam_apikey='XYmAr74oduDmMQ-XsnfCgBTT4aAHvv2x2Q5R187I8jmB',
    url='https://gateway.watsonplatform.net/tone-analyzer/api'
)

text = "In Chicago, which has the toughest gun laws in the United States, probably you could say by far, they have more gun violence than any other city. Firearms are cheaper in Indiana. There's less detection, there are less requirements in Indiana and that's why we are seeing this steady flow and large volume of crime originating better. Chicago police superintendent Gary McArthur says its's a big reason he says he's confiscated more than 3000 guns in Chicago that have come from Indiana. 16,500-plus ICE last week, endorsed me. First time they've ever endorsed a candidate. ICE spokeswoman Sarah Rodriguez stated Federal agencies are prohibited from engaging in partison political activity including the endorsement of any candidate for office."
tone_analysis = tone_analyzer.tone(
    {'text': text},
    'application/json'
).get_result()
x=  eval(json.dumps(tone_analysis, indent=2))
emotions = []
for i in range(len(x["sentences_tone"])):
	for j in range(len(x["sentences_tone"][i]["tones"])):
		if x["sentences_tone"][i]["tones"]:
			emotions.append("Neutral")
		emotions.append((x["sentences_tone"][i]["tones"][j]["tone_name"]))
print(emotions)

mydict = {"Neutral": 0, "Analytical": 1, "Confident": 2, "Sadness": 3, "Tentative": 4}

k = []
for item in emotions:
	k.append(mydict[item])
print(k)