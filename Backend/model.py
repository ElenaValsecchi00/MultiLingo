import openai

openai.api_key = "pk-RDJcFFYXBQkLLrnNkYALCvsjbUewgRkbNFkQcxaIecjuTBbP"
openai.api_base = "https://api.pawan.krd/v1"

history = []
while True: 
    
    message = input(">")
    if message == quit:
        break
    chat_completion = openai.ChatCompletion.create(
        model = "pai-001",
        messages=[{"role": "user", "content": message}]
    )
    response = chat_completion.choices[0].message.content
    print(chat_completion)
    
    
    history.append({"role": "user", "content": message})
    history.append({"role": "system", "content": response})
    #print(f"User : {message}")
    #print(f"Bot : {response}")


