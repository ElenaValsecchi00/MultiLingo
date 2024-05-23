from nltk.corpus import wordnet
import language_tool_python
tool = language_tool_python.LanguageTool('en')

synt = "My friends has come too late."
#grammar check
matches = tool.check(synt)
print(len(matches),matches)
words = synt.split(' ')
#meaning check
for word in words:
    result = wordnet.synsets(word)
    if not result:
        print('No found: ', word)
        continue

    for item in result:
        print("Synset name: ", item.name())
        print("Synset meaning: ", item.definition())
        print("Synset example: ", item.examples())
