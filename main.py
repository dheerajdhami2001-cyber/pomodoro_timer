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
reps = -1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="Timer")
    check_label.config(text = "")
    global reps
    reps = -1

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps in (0,2,4,6):
        my_label.config(text="Work", font=("FONT_NAME", 40, "bold"), fg=GREEN)
        count_down(WORK_MIN * 60)
    elif reps in (1,3,5):
        my_label.config(text="Short Break", font=("FONT_NAME", 40, "bold"), fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)

    elif reps == 7:
        my_label.config(text="Long Break", font=("FONT_NAME", 40, "bold"), fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    else:
        reps = -1
        start_timer()
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_session = reps // 2
        for _ in range(work_session):
            marks += "✓"
        check_label.config(text = marks)

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Clock")
window.config(padx = 100 , pady = 50, bg = YELLOW)


canvas = tkinter.Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness=0)
tomato_pic = tkinter.PhotoImage(file = "tomato.png")
canvas.create_image(100,112,image = tomato_pic)
timer_text = canvas.create_text(100,130,text = "00:00",fill = "white",font = ("FONT_NAME", 35,"bold"))
canvas.grid(row = 1, column = 1)


my_label = tkinter.Label(text = "Timer",font = ("FONT_NAME", 40,"bold"),fg = GREEN,bg = YELLOW)
my_label.grid(row =0 , column = 1)

check_label = tkinter.Label(font = ("FONT_NAME", 40,"bold"),bg = YELLOW, fg = GREEN)
check_label.grid(row = 3 , column = 1)

start_button = tkinter.Button(text = "Start" , font = ("FONT_NAME", 15,"bold"),bg = YELLOW,highlightthickness=0,command = start_timer)
start_button.grid(row = 2 , column = 0)

restart_button = tkinter.Button(text = "Restart" , font = ("FONT_NAME", 15,"bold"),bg = YELLOW,highlightthickness=0,command = reset_timer)
restart_button.grid(row = 2,column = 2)




window.mainloop()

