import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
username='a058b551-a067-48ad-9c08-3d57cb331a12',
password='nW4Q8XpczFc4',
version='2017-02-27')

path = "text.txt"

file = open(path, 'r')

texts = ["Afghan militants get injured during heavy explosion",
        "Future stocks are looking good"]

textx = file.read()
texts = textx.splitlines()

# texts = file.readLines()

sum = 0.0
count = 0

i = 0


for i in range(0, len(texts)):
    response = natural_language_understanding.analyze(

    text= texts[i][0:len(texts[i])-1],

    features=Features(
      keywords=KeywordsOptions(
        emotion=True,
        sentiment=True,
        limit=1)))

    # print(json.dumps(response, indent=2))
    
    try:
        data = json.loads(json.dumps(response, indent=2))

        # print(texts[i])

        print(texts[i]) 
        print(data['keywords'][0]['sentiment']['score'])

        sum += data['keywords'][0]['sentiment']['score']
        if (data['keywords'][0]['sentiment']['score'] != 0):
            count += 1
    except IndexError:
        print("")

    i +=1 
    #print(i)

print("Average: " , (sum/count))
