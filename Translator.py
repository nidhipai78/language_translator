from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Style
from googletrans import Translator, LANGUAGES

translator_object = Translator()


def translate_function():
    src_v = src_entry.get().strip().lower()
    dest_v = dest_entry.get().strip().lower()
    text_v = text_entry.get("1.0", "end-1c").strip()

    if not text_v:
        messagebox.showerror(message="Enter valid text")
        return

    try:
        if not src_v and not dest_v:
            translated_text = translator_object.translate(text_v)
        elif not src_v:
            translated_text = translator_object.translate(text_v, dest=dest_v)
        elif not dest_v:
            translated_text = translator_object.translate(text_v, src=src_v)
        else:
            translated_text = translator_object.translate(text_v, src=src_v, dest=dest_v)

        messagebox.showinfo(message="TRANSLATED TEXT: " + translated_text.text)
    except Exception as e:
        messagebox.showerror(message=f"Translation error: {str(e)}")


def clear():
    dest_entry.delete(0, "end")
    src_entry.delete(0, "end")
    text_entry.delete("1.0", "end")


window = Tk()
window.geometry("500x300")
window.title("Language Translator")

style = Style()
style.configure('TButton', font=('Arial', 10))

title_label = Label(window, text="Language Translator", font=("Helvetica", 14)).pack()

text_label = Label(window, text="Text to translate:").place(x=10, y=40)
text_entry = Text(window, width=40, height=5)
text_entry.place(x=130, y=40)

src_label = Label(window, text="Source language (auto-detect if empty):").place(x=10, y=120)
src_entry = Entry(window, width=20)
src_entry.place(x=270, y=120)

dest_label = Label(window, text="Target language (default: English):").place(x=10, y=150)
dest_entry = Entry(window, width=20)
dest_entry.place(x=270, y=150)

translate_button = Button(window, text='Translate', command=translate_function)
translate_button.place(x=160, y=200)

clear_button = Button(window, text='Clear', command=clear)
clear_button.place(x=270, y=200)

window.mainloop()