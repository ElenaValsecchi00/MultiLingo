import spacy


nlp = spacy.load("en_core_web_sm")
#it_core_news_sm
answers = {
    "tool": ["hammer", "shovel", "scissor"],
    "clothe": ["shirt", "trouser", "dress"],
    "fruit": ["apple", "banana", "passion fruit"]
}

#logic of the conversation
def handle_input(user_input):
    doc = nlp(user_input.lower())
    #for token in doc: print(token.lemma_)
    
    if any(token.lemma_ in ["tool", "clothe", "fruit"] for token in doc):
        return reveal_list(doc)
    elif any(token.lemma_ in answers["tool"] or token.lemma_ in answers["clothe"] for token in doc):
        return "Would you like to have it now or delivered?"
    elif any(token.lemma_ in ["here", "now"] or token.lemma_ in answers["fruit"] for token in doc):
        return "Would you like to pay cash or by card?" 
    elif any(token.lemma_ in ["deliver", "home"] for token in doc):
        return "Can I get your address?" 
    elif any(token.lemma_ in ["address", "street", "avenue", "live"]  for token in doc):
        return "Ok, you can pay once delivered. Thanks for the purchase. Have a nice day!"
    elif any(token.lemma_ in ["cash", "card"] for token in doc):
        return "Ok, thanks for the purchase. Have a nice day!"
    else: 
        return "I didn't understand. Can you repeat?"

#gets the list corresponding to the purchase category
def reveal_list(doc):
    for token in doc:
        if token.lemma_ in answers:
            answers_type = token.lemma_
            answers_list = ", ".join(answers[answers_type])
            return f"Which kind of {answers_type} do you want to buy ? We currently have these available: {answers_list}."
    return "I couldn't understand. Can you repeat?"

#########
print("Welcome to Megastore! Are you looking for fruit, tools or clothes?")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "bye", "end"]:
        print("Bot: Goodbye!")
        break
    response = handle_input(user_input)
    print(f"Bot: {response}")