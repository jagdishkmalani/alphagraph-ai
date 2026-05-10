"""
⭐ First: What is this code?
This code defines two LLM chains:

generate_chain → creates a tweet
reflect_chain → critiques the tweet

These two chains are the building blocks of a reflection agent.

A reflection agent works like this:
    User request → Generate tweet → Reflect on tweet → Improve tweet → Final answer

"""

"""
1️⃣ Reflection Prompt
reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral twitter influencer grading a tweet. Generate critique and recommendations..."
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
What this does:Defines a system role: “You are a viral Twitter influencer.”
Tells the LLM: your job is to critique the tweet.
MessagesPlaceholder means: “Insert the conversation history here.”
Why this matters:This chain is the critic in the reflection loop.
It receives:
    the user’s request
    the generated tweet
and produces:
    feedback, critique, suggestions, improvements
This is the “reflection” part of a reflection agent.
"""

"""
2️⃣ Generation Prompt
generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a twitter techie influencer assistant tasked with writing excellent twitter posts..."
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
What this does:Defines a system role: “You write excellent tweets.”
Tells the LLM: generate a tweet  OR revise a tweet if critique is provided
Why this matters:This chain is the writer in the reflection loop.
It produces:
    the first draft
    the improved draft after critique
"""