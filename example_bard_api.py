# Libraries
import bardapi
import os

# set your __Secure-1PSID value to key (don't put the key in the repository)
os.environ['_BARD_API_KEY']="xxxxx"

# set your input text
input_text = "I want to talk about travels"

# Send an API request and get a response.
response = bardapi.core.Bard().get_answer(input_text)
print(response)
