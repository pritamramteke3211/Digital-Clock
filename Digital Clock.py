import time
from tkinter import *
import datetime

clk = Tk()
clk.title("Clock")
clk.geometry("1350x700+0+0")     #width , height , x-axis , y-axis we have kept 0 because we will start from left top corner
clk.config(bg = "#0C1E28")     # you can give any color you want

def clock():

    hr = str(time.strftime("%H"))
    mn = str(time.strftime("%M"))
    sc = str(time.strftime("%S"))
    # print(hr,mn,sc)

    if int(hr) > 12 and int (mn) > 0:     # to convert am to pm
        lb_dn.config(text=hr)
    if int(hr) > 12:
        hr = str(int(int(hr)-12))

    lb_hr.config(text=hr)
    lb_mn.config(text=mn)
    lb_sc.config(text=sc)

    lb_hr.after(200,clock)  ## to make clock update every second

    ### to get date
    now = datetime.datetime.now()
    date = now.strftime('%d %b, %Y')
    # print(date)
    lb_date.config(text=date)

    ## to get wish according to time
    if int(hr) < 12 :
        lb_wish.config(text='Good Morning')
    elif int(hr) >= 12 and int(hr) < 17:
        lb_wish.config(text='Good Afternoon')
    elif int(hr) >= 17 and int(hr) < 22:
        lb_wish.config(text='Good Evening')
    else:
        lb_wish.config(text='Good Night')






lb_hr = Label(clk,text = "12", font = ("Times 20 bold", 75, 'bold'),bg = '#0875B7',fg="white")
lb_hr.place(x=350,y=200,width=150,height=150)

lb_hr_txt = Label(clk,text = "HOUR", font = ("Times 20 bold", 20, 'bold'),bg = '#0875B7',fg="white")
lb_hr_txt.place(x=350,y=360,width=150,height=50)


lb_mn = Label(clk,text = "12", font = ("Times 20 bold", 75, 'bold'),bg = '#008EA4',fg="white")
lb_mn.place(x=520,y=200,width=150,height=150)

lb_mn_txt = Label(clk,text = "MINUTE", font = ("Times 20 bold", 20, 'bold'),bg = '#008EA4',fg="white")
lb_mn_txt.place(x=520,y=360,width=150,height=50)


lb_sc = Label(clk,text = "12", font = ("Times 20 bold", 75, 'bold'),bg = '#06B4B8',fg="white")
lb_sc.place(x=690,y=200,width=150,height=150)

lb_sc_txt = Label(clk,text = "SECOND", font = ("Times 20 bold", 20, 'bold'),bg = '#06B4B8',fg="white")
lb_sc_txt.place(x=690,y=360,width=150,height=50)


lb_dn = Label(clk,text = "AM", font = ("Times 20 bold", 70, 'bold'),bg = '#9F0646',fg="white")
lb_dn.place(x=860,y=200,width=150,height=150)

lb_dn_txt = Label(clk,text = "NOON", font = ("Times 20 bold", 20, 'bold'),bg = '#9F0646',fg="white")
lb_dn_txt.place(x=860,y=360,width=150,height=50)

lb_date = Label(clk,text = "12", font = ("Times 20 bold", 20, 'bold'),bg = 'green',fg="white")
lb_date.place(x=520,y=420,width=490,height=50)

lb_date_txt = Label(clk,text = "DATE", font = ("Times 20 bold", 20, 'bold'),bg = 'blue',fg="white")
lb_date_txt.place(x=350,y=420,width=150,height=50)

lb_wish = Label(clk,text = "12", font = ("Times 20 bold", 20, 'bold'),bg = 'red',fg="white")
lb_wish.place(x=350,y=480,width=660,height=50)



clock()

clk.mainloop()