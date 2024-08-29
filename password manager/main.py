from tkinter import*
from tkinter import messagebox
import random
import json
window=Tk()
window.title('Password Manager')
window.config(padx=20,pady=20)
def save():
    u=website_entry.get()
    v=email_entry.get()
    w=password_entry.get()
    my_dict={
        u :{'email':v,
            'password':w
        }
    }
    if len(u)==0 or len(w)==0:
        messagebox.showinfo(title='Warning',message='Please check if you have filled all the blanks')

    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(my_dict, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(my_dict)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


canvas=Canvas(width=200,height=200)
lock_image=PhotoImage(file='logo.png')
canvas.create_image(100,100,image=lock_image)
canvas.grid(row=0,column=1)

label=Label(text='Website:')
label.grid(row=1,column=0)
label2=Label(text='Email/Username:')
label2.grid(row=2,column=0)
label3=Label(text='Password:')
label3.grid(row=3,column=0)

website_entry=Entry(width=35)
website_entry.grid(row=1,column=1)
website_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1)
email_entry.insert(0,'vedantmahajan004@gmail.com')
password_entry=Entry(width=28)
password_entry.grid(row=3,column=1)

def find_password():
    search_website = website_entry.get()
    try:
        with open('data.json','r') as file:
            data=json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title='Invalid',
                            message=f'sorry the file doesnt exist')
    except KeyError:
        messagebox.showinfo(title='Invalid Search',
                            message=f'sorry you have not saved the password for {search_website}'.title())
    else:
        if search_website in data:
            email=data[search_website]['email']
            password = data[search_website]['password']
            messagebox.showinfo(title='Your credentials',message=f'Your password is: {password}\nYour email is: {email}')


def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    my_lst=[]

    for i in range(random.randint(4,5)):
        number_letters = random.choice(letters)
        my_lst.append(number_letters)

    for i in range(random.randint(4,5)):
        number_numbers = random.choice(numbers)
        my_lst.append(number_numbers)

    for i in range(random.randint(4,5)):
        number_symbols = random.choice(symbols)
        my_lst.append(number_symbols)

    password=''
    for i in my_lst:
        password=password+i
    password_entry.insert(0,password)


generate_button=Button(text='generate password',command=generate_password)
generate_button.grid(row=3,column=2)
add_button=Button(text='Add',width=10,command=save)
add_button.grid(row=4,column=1)
search_button=Button(text='Search',command=find_password)
search_button.grid(row=1,column=2)


window.mainloop()



