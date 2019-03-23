import audio_transcribe
import sentimentAnalysis
import pprint

vidName='mark_zuckerbergs_testimony_before_congress.mp4'
# text=audio_transcribe.getTextMain(vidName)
# print(text)
with open('captions.txt') as f:
    captions=f.read()
sentimentJson= sentimentAnalysis.getSentimentJson(captions)

pprint.pprint(sentimentJson)

