import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
LONG_BREAK_SEC = LONG_BREAK_MIN * 60
SHORT_BREAK_SEC = SHORT_BREAK_MIN * 60
WORK_SEC = WORK_MIN * 60
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def resettimer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer,text="00:00")
    label.config(text="TIMER", fg=GREEN)
    check.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def starttimer():
    global reps
    reps += 1
    if reps == 8:
        label.config(text="Break", fg=GREEN)
        countdown(LONG_BREAK_SEC)
    elif reps % 2 == 0:
        label.config(text="Break", fg=PINK)
        countdown(SHORT_BREAK_SEC)
    else:
        label.config(text="Work", fg=RED)
        countdown(WORK_SEC)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")
    if count > 0:
        global TIMER
        TIMER = window.after(1080, countdown, count - 1)
    else:
        starttimer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✓"
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
#Window
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#Labels
label = tkinter.Label(text="TIMER", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

check = tkinter.Label(font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)

#Buttons
start = tkinter.Button(text="Start", highlightthickness=0, command=starttimer)
reset = tkinter.Button(text="Reset", highlightthickness=0, command=resettimer)

start.grid(column=0, row=2)
reset.grid(column=2, row=2)


#Canvas
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=img)
timer = canvas.create_text(100,130,text="00:00",fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



window.mainloop()