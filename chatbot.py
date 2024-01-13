# GUI
from tkinter import END, Button, Entry, Label, Scrollbar, Text, Tk


def send():
    send_msg = "You -> " + e.get()
    txt.insert(END, "\n" + send_msg)

    user = e.get()

    responses = {
        "hello": "Hi there, how can I help?",
        "hi": "Hi there, what can I do for you?",
        "how are you": "Fine! And you?",
        "Fine":"Nice to know, hope you have a great day",
        "Awesome!":"I'm here and ready to assist",
        "who is Arshad khan": "Arshad khan is a very good student.",
        "fine": "Great! How can I help you?",
        "thanks": "My pleasure!",
        "Wonderful": "Your questions or concerns are always welcome.",
        "tell me a joke": "What did the buffalo say when his son left for college? Bison!",
        "goodbye": "Have a nice day!",
        
    }

    if user in responses:
        txt.insert(END, "\n" + f"Bot -> {responses[user]}")
    else:
        txt.insert(END, "\n" + "Bot -> Sorry, I didn't understand that.")

    e.delete(0, END)


root = Tk()
root.title("Chatbot")

BG_COLOR_LEFT = "#3498DB"  # Light blue for the left side
BG_COLOR_RIGHT = "#17202A"  # Dark background for the right side
TEXT_COLOR = "#EAECEE"
FONT_LEFT = "Arial 12 bold"  # Updated font for the left side
FONT_RIGHT = "Helvetica 14"  # Updated font for the right side

label1 = Label(root, bg=BG_COLOR_LEFT, fg=TEXT_COLOR, text="ChatBot", font=FONT_LEFT, pady=15, width=60, height=1)
label1.grid(row=0, column=0, sticky='nsew')

txt = Text(root, bg=BG_COLOR_RIGHT, fg=TEXT_COLOR, font=FONT_RIGHT, width=60)
txt.grid(row=1, column=0, columnspan=2, sticky='nsew')

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT_RIGHT, width=55)
e.grid(row=2, column=0, sticky='nsew')

send_button = Button(root, text="Send", font=FONT_RIGHT, bg=BG_COLOR_LEFT, command=send)
send_button.grid(row=2, column=1, sticky='nsew')

# Configure row and column weights to make the widgets resizable
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
