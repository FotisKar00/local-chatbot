import ollama
import time


messages = []

system_prompt={
   "role":"system","content":"You are helpful assistant."
}

with open("conversation.txt","w",encoding="utf-8") as f:
       f.write(f"System:{system_prompt['content']}\n\n")

while True:
    user_input = input("You: ")
    if user_input=="/help":
      print("""
Available commands:
/help->Show commands
/clear->Clear conversation history
/exit->Exit app""")
      continue

    if user_input=="/clear":
       messages=[system_prompt]
       print("History Cleared")
       continue

    if user_input=="/exit":
       print("Exiting")
       break

    blocked_words=['violence','drugs','hate']

    if any(word in user_input.lower() for word in blocked_words):
       print ("Content not allowed")
       continue
    
    messages.append({"role": "user", "content": user_input})

    start_time=time.time()
    response = ollama.chat(
        model="tinyllama",
        messages=messages
    )
    end_time=time.time()

    assistant_reply = response["message"]["content"]
    print("AI:", assistant_reply)
    messages.append({"role": "assistant", "content": assistant_reply})

    with open("conversation.txt","a",encoding="utf-8") as f:
      f.write(f"User:{user_input}\n\n")
      f.write(f"Assistant:{assistant_reply}\n\n")

    if len(messages)>11:
      summary_prompt=messages+[{"role":"assistant","content":"Summarize this conversation in 5 lines"}]
      summary_response=ollama.chat(
         model="tinyllama",
         messages=summary_prompt
      )
      summary_text=summary_response["message"]["content"]
      messages=[system_prompt,{"role":"assistant","content":f"Summary so far:{summary_text}"}]
      
    print(f"Response time :{end_time-start_time:.2f}seconds")
