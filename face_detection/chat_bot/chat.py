import tkinter as tk
from tkinter import scrolledtext
import requests
from bs4 import BeautifulSoup

class ChatBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic ChatBot")

        # Create a text area to display the conversation
        self.chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
        self.chat_history.pack(padx=10, pady=10)

        # Create an entry widget for user input
        self.user_input = tk.Entry(root, width=50)
        self.user_input.pack(padx=10, pady=10)

        # Create a send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=10)

    def send_message(self):
        user_message = self.user_input.get()
        self.chat_history.insert(tk.END, f"You: {user_message}\n")
        self.user_input.delete(0, tk.END)

        # Fetch response from the internet
        response = self.fetch_response_from_internet(user_message)
        self.chat_history.insert(tk.END, f"Bot: {response}\n")

    def fetch_response_from_internet(self, query):
        # Example: Fetching data from a webpage
        url = f"https://www.example.com/search?q={query}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract relevant information from the webpage
        result = soup.find('div', class_='result').text
        return result

if __name__ == "__main__":
    root = tk.Tk()
    chatbot_gui = ChatBotGUI(root)
    root.mainloop()
