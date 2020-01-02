from functools import partial
from time import strftime
from tkinter import *
from datetime import datetime, time
import csv


def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.now().time()
    if begin_time < end_time:
        return begin_time <= check_time <= end_time
    else:  # crosses midnight
        return check_time >= begin_time or check_time <= end_time


def open_datetimepicker(window):
    window.destroy()
    datetimemenu = Tk()

    selectdateinputtext = StringVar()
    selecttimeinputtext = StringVar()

    selectdatelabel = Label(datetimemenu, text="Select A Date: (DD/MM/YYYY", font=('time', 10, 'bold'))
    selecttimelabel = Label(datetimemenu, text="Select A Time: (23:59)", font=('time', 10, 'bold'))

    backbutton = Button(datetimemenu, font=('time', 10, 'bold'), text="Back", fg="white", bg="red",
                        command=lambda: listofstorewindows(datetimemenu))
    selectdatelabel.grid(row=0, column=0, sticky=E)
    selectdateinput = Entry(datetimemenu, textvariable=selectdateinputtext)

    confirmbutton = Button(datetimemenu, font=('time', 10, 'bold'), text="Confirm", fg="white", bg="blue",
                           command= partial(test(selectdateinputtext,22)))
    selectdateinput.grid(row=0, column=1, sticky=E)
    selecttimelabel.grid(row=1, column=0, sticky=E)
    selecttimeinput = Entry(datetimemenu, textvariable=selecttimeinputtext)
    selecttimeinput.grid(row=1, column=1, sticky=E)
    backbutton.grid(row=2, columnspan=4)
    confirmbutton.config(test(selectdateinputtext, 123))
    confirmbutton.grid(row=2, column=1, columnspan=4, sticky=W)

    datetimemenu.mainloop()

def test(date, time):
    date1 = datetime.strptime(date, '%d/%m/%Y')
    print(date1)

def open_menu(window, label):
    window.destroy()
    menu = Tk()
    menuTiming = ""
    clocks = Label(menu, font=('time', 10, 'bold'))
    buttonExit = Button(menu, font=('time', 10, 'bold'), text="Back", fg="red", bg="pink",
                        command=lambda: listofstorewindows(menu))

    result = {}
    if label == "Beverage":
        with open('CSV/menu.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if is_time_between(time(8, 00), time(11, 59)):
                    if row['store'] == 'beverage':
                        if row['type'] == 'breakfast':
                            menuTiming = 'Breakfast'
                            result.update({row['item']: row['price']})
                elif is_time_between(time(12, 00), time(17, 59)):
                    if row['store'] == 'beverage':
                        if row['type'] == 'lunch':
                            menuTiming = 'Lunch'
                            result.update({row['item']: row['price']})
    elif label == "Chicken Rice":
        with open('CSV/menu.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if is_time_between(time(8, 00), time(11, 59)):
                    if row['store'] == 'chicken rice':
                        if row['type'] == 'breakfast':
                            menuTiming = 'Breakfast'
                            result.update({row['item']: row['price']})
                elif is_time_between(time(12, 00), time(17, 59)):
                    if row['store'] == 'chicken rice':
                        if row['type'] == 'lunch':
                            menuTiming = 'Lunch'
                            result.update({row['item']: row['price']})
    elif label == "Vegetarian":
        with open('CSV/menu.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if is_time_between(time(8, 00), time(11, 59)):
                    if row['store'] == 'vegetarian':
                        if row['type'] == 'breakfast':
                            menuTiming = 'Breakfast'
                            result.update({row['item']: row['price']})
                elif is_time_between(time(12, 00), time(17, 59)):
                    if row['store'] == 'vegetarian':
                        if row['type'] == 'lunch':
                            menuTiming = 'Lunch'
                            result.update({row['item']: row['price']})
    elif label == "Indian":
        with open('CSV/menu.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if is_time_between(time(8, 00), time(11, 59)):
                    if row['store'] == 'indian':
                        if row['type'] == 'breakfast':
                            menuTiming = 'Breakfast'
                            result.update({row['item']: row['price']})
                elif is_time_between(time(12, 00), time(17, 59)):
                    if row['store'] == 'indian':
                        if row['type'] == 'lunch':
                            menuTiming = 'Lunch'
                            result.update({row['item']: row['price']})
    elif label == "Muslim":
        with open('CSV/menu.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if is_time_between(time(8, 00), time(11, 59)):
                    if row['store'] == 'muslim':
                        if row['type'] == 'breakfast':
                            menuTiming = 'Breakfast'
                            result.update({row['item']: row['price']})
                elif is_time_between(time(12, 00), time(17, 59)):
                    if row['store'] == 'muslim':
                        if row['type'] == 'lunch':
                            menuTiming = 'Lunch'
                            result.update({row['item']: row['price']})
    rowForLabel = 5
    between = ' ' * 60
    for items in result:
        print(items)
        temp_text = '{0}{1}{2}'.format(items, between, result[items])
        Label(menu, text=temp_text).grid(row=rowForLabel, sticky=E)
        rowForLabel = rowForLabel + 1

    def tick():
        time1 = ''
        # get the current local time from the PC
        time2 = strftime('%H:%M:%S')

        # if time string has changed, update it
        if time2 != time1:
            time1 = time2
        clocks.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
        clocks.after(200, tick)

    tick()
    date_iso = Label(menu, font=('time', 10, 'bold'), fg='black')
    date_iso.grid(row=0, column=0, sticky=E)

    date_etc = Label(menu, font=('time', 10, 'bold'), fg='black')
    date_etc.grid(row=0, column=0, sticky=W)

    def tick1():
        date_iso_txt = strftime('%d-%m-%Y')
        date_etc_txt = "%s" % (strftime('%A'))

        date_iso.config(text=date_iso_txt)
        date_etc.config(text=date_etc_txt)

    tick1()
    labelstore = Label(menu,
                       font=('time', 10, 'bold'),
                       text="Store: " + label)
    currentMenuLabel = Label(menu,
                             font=('time', 10, 'bold'),
                             text="Current Menu: " + menuTiming)
    clocks.grid(row=2, columnspan=6)
    labelstore.grid(row=3, columnspan=6)
    currentMenuLabel.grid(row=4, columnspan=6)

    buttonExit.grid(row=100, sticky=E)

    menu.mainloop()


def listofstorewindows(window):
    storewindow = Tk()
    window.destroy()
    label_1 = Label(storewindow, font=('time', 10, 'bold'), text="North Spine Foodcourt")
    label_2 = Label(storewindow, font=('time', 10, 'bold'), text="Date and Time:")
    button1 = Button(storewindow, font=('time', 10, 'bold'), text="Beverage", fg="red", bg="pink",
                     command=lambda: open_menu(storewindow, 'Beverage'))
    button2 = Button(storewindow, font=('time', 10, 'bold'), text="Chicken Rice", fg="blue", bg="cyan",
                     command=lambda: open_menu(storewindow, 'Chicken Rice'))
    button3 = Button(storewindow, font=('time', 10, 'bold'), text="Vegetarian ", fg="green",
                     command=lambda: open_menu(storewindow, 'Vegetarian'))
    button4 = Button(storewindow, font=('time', 10, 'bold'), text="Indian", fg="purple",
                     command=lambda: open_menu(storewindow, 'Indian'))
    button5 = Button(storewindow, font=('time', 10, 'bold'), text="Muslim", fg="yellow", bg="grey",
                     command=lambda: open_menu(storewindow, 'Muslim'))

    clock = Label(storewindow, font=('time', 10, 'bold'))

    def tick():
        time1 = ''
        # get the current local time from the PC
        time2 = strftime('%H:%M:%S')

        # if time string has changed, update it
        if time2 != time1:
            time1 = time2
        clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
        clock.after(200, tick)

    tick()
    date_iso = Label(storewindow, font=('time', 10, 'bold'), fg='black')
    date_iso.grid(row=1, column=3)

    date_etc = Label(storewindow, font=('time', 10, 'bold'), fg='black')
    date_etc.grid(row=1, column=2)

    def tick1():
        date_iso_txt = strftime('%d-%m-%Y')
        date_etc_txt = "%s" % (strftime('%A'))

        date_iso.config(text=date_iso_txt)
        date_etc.config(text=date_etc_txt)

    tick1()
    with open('CSV/operatingtime.csv') as f:
        reader = csv.DictReader(f)
        count = 3
        for row in reader:
            if is_time_between(time(int(row['starttime']), 00), time(int(row['endtime'])), 00):
                new_btn = Button(storewindow, font=('time', 10, 'bold'), text=row['store'], fg="black", bg="white",
                                 command=lambda: open_menu(storewindow, row['store']))
                new_btn.grid(row=count, sticky=E)
                new_btn.config(height=2, width=10)
                count = count + 1

    label_1.grid(row=0, sticky=E)
    label_2.grid(row=1, sticky=E)
    clock.grid(row=1, column=4)
    storewindow.mainloop()


root = Tk()
HEIGHT = 1000
WIDTH = 1000
canvas = Canvas(root, height=HEIGHT, width=WIDTH)

labelMainTitle = Label(root, text="Nanyang Technological University")
labelMainTitle2 = Label(root, text="Welcome to North Spine Menu System!")
buttonViewStores = Button(root, text="View Today's Stores", command=lambda: listofstorewindows(root))
buttonViewStoresByOtherDates = Button(root, text="View Stores by other dates",
                                      command=lambda: open_datetimepicker(root))
buttonExit = Button(root, bg="red", text="Exit")
labelMainTitle.grid(row=0)
labelMainTitle2.grid(row=1)
buttonViewStores.grid(row=2)
buttonViewStoresByOtherDates.grid(row=3)
buttonExit.grid(row=4, columnspan=4)

root.mainloop()
