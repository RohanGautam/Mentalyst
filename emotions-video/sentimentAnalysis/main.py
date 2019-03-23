import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    iam_apikey='XYmAr74oduDmMQ-XsnfCgBTT4aAHvv2x2Q5R187I8jmB',
    url='https://gateway.watsonplatform.net/tone-analyzer/api'
)

text = 'Team, I know that times are tough! Product '\
    'sales have been disappointing for the past three '\
    'quarters. We have a competitive product, but we '\
    'need to do a better job of selling it!'

tone_analysis = tone_analyzer.tone(
    {'text': text},
    'application/json'
).get_result()
print(json.dumps(tone_analysis, indent=2))
