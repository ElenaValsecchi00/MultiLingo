import nltk
from nltk.corpus import wordnet
import language_tool_python

tool = language_tool_python.LanguageTool('en')

synt = "My friends has come too late."
'''
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
for word in answer.split(' '):
    if word != meaning_to_search and word not in question.split(' '):
        print(word)
        result = wordnet.synsets(word)
        if not result:
            print('No found: ', word)
            continue
        for item in result:
            defin = item.definition('eng')
            if meaning_to_search in defin:
                print(True, defin)
'''


def check_answer(question, answer):
    question_words = set(question.split())
    answer_words = set(answer.split())
    
    question_synsets = [wordnet.synsets(word) for word in question_words]
    answer_synsets = [wordnet.synsets(word) for word in answer_words]
    
    question_synonyms = set([synset for word_synsets in question_synsets for synset in word_synsets])
    answer_synonyms = set([synset for word_synsets in answer_synsets for synset in word_synsets])
    print(question_synonyms, answer_synonyms)
    similarity_score = len(question_synonyms.intersection(answer_synonyms)) / len(question_synonyms.union(answer_synonyms))
    
    return similarity_score

question = "What's your favourite color ?"
print("scrivi")
answer = input()
matches = tool.check(answer)
print(len(matches),matches)

similarity = check_answer(question, answer)
print(f"Similarity score between question and answer: {similarity}")

