# Description: Chatbot application
from nltk.chat.util import Chat, reflections

#list of patterns and responses
pairs = [
    ["my name is (.*)", ["Hi %1!"]],
    ["(hi|hello|hey|holla|hola)", ["Hey there!", "Hi there!", "Hi!", "Hey!"]],
    ["(.*) in (.*) is fun", ["%1 in %2 is indeed fun"]],
    ["(.*)(location|city) ?", ["London, United Kingdom"]],
    ["(.*) created you?", ["Ryan did using NLTK!"]],
    # Catch-all pattern
    ["(.*)", ["Tell me more.", "Interesting...", "Why do you say that?", "I'm listening.", "Let's talk more about that."]]
]
#reflections is a dictionary that maps input values to output values (has common responses)
chat = Chat(pairs, reflections)
chat.converse()
