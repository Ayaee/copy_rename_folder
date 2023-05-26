import customtkinter
from customtkinter import filedialog

customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.geometry("400x300")


def button_click_event():
    dossier = filedialog.askopenfilename (initialdir="/", title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    # dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="Test")
    print("Chemin:", dossier)


button = customtkinter.CTkButton(app, text="Open Dialog", command=button_click_event)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()