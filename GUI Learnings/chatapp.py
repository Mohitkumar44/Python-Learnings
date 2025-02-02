import tkinter as tk
from datetime import datetime
import json

def load_responses():
    try:
        with open('responses.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_responses():
    with open('responses.json', 'w') as file:
        json.dump(responses, file, indent=4)

def send_message(event=None):
    message = entry.get()
    if message.strip():
        formatted_message = "You: " + message + " " + get_timestamp() + "\n"
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, formatted_message, 'user')
        chat_log.config(state=tk.DISABLED)
        chat_log.see(tk.END)
        entry.delete(0, tk.END)
        bot_response(message)

def bot_response(message):
    response = "Bot: " + generate_response(message) + " " + get_timestamp() + "\n"
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, response, 'bot')
    chat_log.config(state=tk.DISABLED)
    chat_log.see(tk.END)

def generate_response(message):
    return responses.get(message.lower(), "I didn't understand that. 😕")

def get_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def welcome_message():
    welcome = "Bot: Welcome to the Simple Chat App by Mohit Kumar! " + get_timestamp() + "\n"
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, welcome, 'bot')
    chat_log.config(state=tk.DISABLED)
    chat_log.see(tk.END)

def add_custom_response():
    trigger = entry_trigger.get().lower()
    response = entry_response.get()
    if trigger and response:
        responses[trigger] = response
        save_responses()
        entry_trigger.delete(0, tk.END)
        entry_response.delete(0, tk.END)
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, "Custom response added! " + get_timestamp() + "\n", 'bot')
        chat_log.config(state=tk.DISABLED)
        chat_log.see(tk.END)

# Load initial responses from file
responses = load_responses()

root = tk.Tk()
root.title("Chatting App")

chat_frame = tk.Frame(root)
chat_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

chat_log = tk.Text(chat_frame, state=tk.DISABLED, width=50, height=20, wrap=tk.WORD)
chat_log.tag_config('user', foreground='blue')
chat_log.tag_config('bot', foreground='green')
chat_log.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(chat_frame, command=chat_log.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_log.config(yscrollcommand=scrollbar.set)

entry = tk.Entry(root, width=40)
entry.grid(row=1, column=0, padx=10, pady=10)
entry.bind("<Return>", send_message)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

entry_trigger = tk.Entry(root, width=20)
entry_trigger.grid(row=2, column=0, padx=10, pady=5)
entry_trigger.insert(0, "Enter chat trigger")

entry_response = tk.Entry(root, width=20)
entry_response.grid(row=2, column=1, padx=10, pady=5)
entry_response.insert(0, "Enter response")

add_response_button = tk.Button(root, text="Add Response", command=add_custom_response)
add_response_button.grid(row=3, column=0, columnspan=2, pady=10)

welcome_message()

root.mainloop()
