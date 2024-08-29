from tkinter import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer=None

window=Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50,bg=YELLOW)
reps=0

def count_down(count):
    global timer
    count_min=count//60
    count_sec=count%60
    if count_sec<10:
        count_sec=f'0{count_sec}'
    canvas.itemconfig(timer_text,text=f'{count_min}:{count_sec}')
    if count>0:
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=''
        for _ in range(reps//2):
            mark=mark+'✓'
        check_mark = Label(text=mark, font=(10), bg=YELLOW, fg=GREEN)
        check_mark.grid(row=2, column=1)
# entered time of 1000 bcoz the time is to be entered in milli seconds

def start_timer():
    global reps
    reps=reps+1
    work_min=WORK_MIN*60
    short_break=SHORT_BREAK_MIN*60
    long_break=LONG_BREAK_MIN*60
    if reps%8==0:
        count_down(long_break)
        label1.config(text='LONG BREAK')
    elif reps%2==0:
        count_down(short_break)
        label1.config(text='SHORT BREAK')
    elif reps%2!=0:
        count_down(work_min)
        label1.config(text='WORK TIME')
def reset_button():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f'00:00')
    label1.config(text='TIMER')
    check_mark.config(text='')
    global reps
    reps=0



#using the highlightthickness=0 to remove the edges of the tomato pic
canvas=Canvas(width=200,height=223,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file='tomato.png')
canvas.create_image(100,109,image=tomato_img)
timer_text=canvas.create_text(100,125,text='00:00',fill='yellow',font=('courier',20,'bold'))
canvas.grid(row=1,column=1)


label1=Label(text='TIMER',font=('courier',25),fg='green',bg=YELLOW)
label1.grid(row=0,column=1)

start_button=Button(text='Start',bg=YELLOW,command=start_timer)
reset_button=Button(text='Reset',bg=YELLOW,command=reset_button)
start_button.grid(row=2,column=0)
reset_button.grid(row=2,column=2)

check_mark = Label( font=(10), bg=YELLOW, fg=GREEN)
check_mark.grid(row=2, column=1)


window.mainloop()
