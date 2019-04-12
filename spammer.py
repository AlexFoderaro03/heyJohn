from tkinter import *
from selenium import webdriver

root = Tk()
label = Label(root, text="Enter the name")
entry = Entry(root)
label.grid(row=0, column=0,sticky=N)
entry.grid(row=0,column=1,sticky=S)
label1 = Label(root, text="Counter")
label1.grid(row=1, column=0,sticky=S)
entry2 = Entry(root)
entry2.grid(row=1, column=1,sticky=N)
label3 = Label(root, text="Message")
entry3= Entry(root)
label3.grid(row=3,column=0)
entry3.grid(row=3,column=1)

def send():
    b = webdriver.Chrome()
    b.get('http://web.whatsapp.com')
    input()
    path = '//span[contains(text(),"' + entry.get() + '")]'
    elem = b.find_element_by_xpath(path)
    elem.click()
    elem1 = b.find_elements_by_class_name('input')
    count = int(entry2.get())
    for i in range(count):
        elem1[1].send_keys(entry3.get())
        b.find_element_by_class_name('send-container').click()


button = Button(root, text="SEND", bg = "green", fg="black", command=send)
button.grid(row=4, columnspan=2)
root.mainloop()