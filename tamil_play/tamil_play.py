import time
import random
import tkinter as tk
from tkinter import font
from tkinter import messagebox

uyir_ezhuthukal = [
    'அ', 'ஆ', 'இ', 'ஈ', 'உ', 'ஊ', 'எ', 'ஏ', 'ஐ', 'ஒ', 'ஓ', 'ஔ',
]
mei_ezhuthukal = [
    'க்', 'ங்', 'ச்', 'ஞ்', 'ட்', 'ண்', 'த்', 'ந்', 'ப்', 'ம்', 'ய்', 'ர்', 'ல்', 'வ்', 'ழ்', 'ள்', 'ற்', 'ன்',
]
uyir_mei_ezhuthukal = [
    'க', 'ங', 'ச', 'ஞ', 'ட', 'ண', 'த', 'ந', 'ப', 'ம', 'ய', 'ர', 'ல', 'வ', 'ழ', 'ள', 'ற', 'ன',
    'கா', 'ஙா', 'சா', 'ஞா', 'டா', 'ணா', 'தா', 'நா', 'பா', 'மா', 'யா', 'ரா', 'லா', 'வா', 'ழா', 'ளா', 'றா', 'னா',
    'கி', 'ஙி', 'சி', 'ஞி', 'டி', 'ணி', 'தி', 'நி', 'பி', 'மி', 'யி', 'ரி', 'லி', 'வி', 'ழி', 'ளி', 'றி', 'னி', 
    'கீ', 'ஙீ', 'சீ', 'ஞீ', 'டீ', 'ணீ', 'தீ', 'நீ', 'பீ', 'மீ', 'யீ', 'ரீ', 'லீ', 'வீ', 'ழீ', 'ளீ', 'றீ', 'னீ', 
    'கு', 'ஙு', 'சு', 'ஞு', 'டு', 'ணு', 'து', 'நு', 'பு', 'மு', 'யு', 'ரு', 'லு', 'வு', 'ழு', 'ளு', 'று', 'னு', 
    'கூ', 'ஙூ', 'சூ', 'ஞூ', 'டூ', 'ணூ', 'தூ', 'நூ', 'பூ', 'மூ', 'யூ', 'ரூ', 'லூ', 'வூ', 'ழூ', 'ளூ', 'றூ', 'னூ', 
    'கெ', 'ஙெ', 'செ', 'ஞெ', 'டெ', 'ணெ', 'தெ', 'நெ', 'பெ', 'மெ', 'யெ', 'ரெ', 'லெ', 'வெ', 'ழெ', 'ளெ', 'றெ', 'னெ', 
    'கே', 'ஙே', 'சே', 'ஞே', 'டே', 'ணே', 'தே', 'நே', 'பே', 'மே', 'யே', 'ரே', 'லே', 'வே', 'ழே', 'ளே', 'றே', 'னே', 
    'கை', 'ஙை', 'சை', 'ஞை', 'டை', 'ணை', 'தை', 'நை', 'பை', 'மை', 'யை', 'ரை', 'லை', 'வை', 'ழை', 'ளை', 'றை', 'னை', 
    'கொ', 'ஙொ', 'சொ', 'ஞொ', 'டொ', 'ணொ', 'தொ', 'நொ', 'பொ', 'மொ', 'யொ', 'ரொ', 'லொ', 'வொ', 'ழொ', 'ளொ', 'றொ', 'னொ', 
    'கோ', 'ஙோ', 'சோ', 'ஞோ', 'டோ', 'ணோ', 'தோ', 'நோ', 'போ', 'மோ', 'யோ', 'ரோ', 'லோ', 'வோ', 'ழோ', 'ளோ', 'றோ', 'னோ', 
    'கௌ', 'ஙௌ', 'சௌ', 'ஞௌ', 'டௌ', 'ணௌ', 'தௌ', 'நௌ', 'பௌ', 'மௌ', 'யௌ', 'ரௌ', 'லௌ', 'வௌ', 'ழௌ', 'ளௌ', 'றௌ', 'னௌ',
]
aaidha_ezhuthu = ['ஃ']

ezhuthukal = []


def get_random_letter():
    return ezhuthukal[random.randrange(247)]


def get_letters():
    global ezhuthukal
    ezhuthukal = []
    if include_uyir.get():
        ezhuthukal.extend(uyir_ezhuthukal)
    if include_mei.get():
        ezhuthukal.extend(mei_ezhuthukal)
    if include_uyirmei.get():
        ezhuthukal.extend(uyir_mei_ezhuthukal)
    if include_aaidham.get():
        ezhuthukal.extend(aaidha_ezhuthu)
    if len(ezhuthukal) == 0:
        messagebox.showerror('Time Limit exception', 'Choose at least one letter type in Configuration')
        ezhuthukal.extend(uyir_ezhuthukal)


def timer():
    try:
        limit = int(time_limit.get())
    except:
        messagebox.showerror('Time Limit exception', 'Enter a valid number in Time Limit Configuration. \nNow defaulting to 5 seconds')
        limit = 5
    
    while limit > 0:
        btn_next.config(text=limit)
        ltr_play.update()
        limit -= 1
        time.sleep(1)
    btn_next.config(state=tk.NORMAL)
    btn_next.config(text="Next")


def change_letter():
    new_ltr = ezhuthukal[random.randrange(len(ezhuthukal))]
    lbl_ltr.config(text=new_ltr)
    if is_timer_needed.get():
        btn_next.config(state=tk.DISABLED)
        timer()


def config():
    def on_timer_toggle():
        if is_timer_needed.get():
            txt_time_limit.config(state=tk.NORMAL)
            lbl1.config(state=tk.NORMAL)
        else:
            txt_time_limit.config(state=tk.DISABLED)
            lbl1.config(state=tk.DISABLED)
    
    config_window = tk.Toplevel(ltr_play)
    config_window.title('Configure the Play')
    fra_timer = tk.Frame(master=config_window, width=350, height=75, relief='groove', borderwidth=5)
    fra_timer.pack(padx=10, pady=10)
    chk_tmr = tk.Checkbutton(
        master=fra_timer,
        text="Timer",
        variable=is_timer_needed,
        onvalue=tk.TRUE,
        offvalue=tk.FALSE,
        font=font_style_btn,
        command=on_timer_toggle,
        # height=5, width=5
    )
    # chk_tmr.pack()
    chk_tmr.place(x=10, y=10)
    txt_time_limit = tk.Entry(
        master=fra_timer,
        font=font_style_btn,
        textvariable=time_limit,
        width=3
    )
    # txt_time_limit.pack()
    txt_time_limit.place(x=150, y=15)

    lbl1 = tk.Label(master=fra_timer, text=" seconds", font=font_style_btn)
    lbl1.place(x=200, y=15)
    on_timer_toggle()

    fra_ltr_types = tk.Frame(master=config_window, width=350, height=250, relief='groove', borderwidth=5)
    fra_ltr_types.pack(pady=(0, 10))
    lbl2 = tk.Label(master=fra_ltr_types, text="Include", font=font_style_btn)
    lbl2.place(x=10, y=15)
    chk_uyir = tk.Checkbutton(
        master=fra_ltr_types, text="உயிர்",
        variable=include_uyir,
        onvalue=tk.TRUE, offvalue=tk.FALSE,
        font=font_style_btn, command=get_letters,
    )
    chk_uyir.place(x=10, y=50)
    chk_mei = tk.Checkbutton(
        master=fra_ltr_types, text="மெய்",
        variable=include_mei,
        onvalue=tk.TRUE, offvalue=tk.FALSE,
        font=font_style_btn, command=get_letters,
    )
    chk_mei.place(x=10, y=90)
    chk_uyirmei = tk.Checkbutton(
        master=fra_ltr_types, text="உயிர்மெய்",
        variable=include_uyirmei,
        onvalue=tk.TRUE, offvalue=tk.FALSE,
        font=font_style_btn, command=get_letters,
    )
    chk_uyirmei.place(x=10, y=130)
    chk_aaidham = tk.Checkbutton(
        master=fra_ltr_types, text="ஆய்தம்",
        variable=include_aaidham,
        onvalue=tk.TRUE, offvalue=tk.FALSE,
        font=font_style_btn, command=get_letters,
    )
    chk_aaidham.place(x=10, y=170)

    ltr_play.update()

def close_app():
    ltr_play.destroy()

ltr_play = tk.Tk()
ltr_play.title('Tamil')
ltr_play.geometry("800x475")

font_style_lbl = font.Font(size=100)
font_style_btn = font.Font(size=20)

is_timer_needed = tk.BooleanVar(value=tk.TRUE)
time_limit = tk.StringVar(value="5")
include_uyir = tk.BooleanVar(value=tk.TRUE)
include_mei = tk.BooleanVar(value=tk.TRUE)
include_uyirmei = tk.BooleanVar(value=tk.TRUE)
include_aaidham = tk.BooleanVar(value=tk.TRUE)

lbl_ltr = tk.Label(
    text='',
    width=8,
    height=2,
    font=font_style_lbl
)
lbl_ltr.pack()

fra_buttons = tk.Frame(master=ltr_play, width=800, height=475)
fra_buttons.pack(pady=10, expand=1, fill="x")
# fra_buttons.grid(row=0, column=0, sticky='news')  

btn_next = tk.Button(
    master=fra_buttons, text="Next", command=change_letter,
    font=font_style_btn,
    width=5
)
# btn_next.pack(pady=10)
btn_next.grid(row=0, column=1, padx=10, sticky='news')
# chat_history.grid(row=0, column=0, padx=10, pady=10)

btn_config = tk.Button(
    master=fra_buttons, text="Config", command=config,
    font=font_style_btn,
    width=5
)
btn_config.grid(row=0, column=0, padx=10, sticky='w')

btn_close = tk.Button(
    master=fra_buttons, text="Close", command=close_app,
    font=font_style_btn,
    width=5
)
btn_close.grid(row=0, column=2, padx=10, sticky='e')

fra_buttons.columnconfigure(0, weight=1)
fra_buttons.columnconfigure(1, weight=1)
fra_buttons.columnconfigure(2, weight=1)

get_letters()
change_letter()


if __name__ == '__main__':
    ltr_play.mainloop()
