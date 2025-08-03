import json
import tkinter as tk
import json as js
from threading import active_count
from tkinter.messagebox import showinfo

# defining function to write/append details while creating account
def write_to_db(data,labs,vars):
    try:
        for i in range(len(labs)):
            data[labs[i]] = vars[i].get()
        file_data = None
        try:
            with open('database.json', 'r') as f:
                file_data = json.load(f)
        except (FileNotFoundError,json.JSONDecodeError):
            file_data = []
        file_data.append(data)
        with open('database.json', 'w') as f:
            json.dump(file_data, f, indent=4)
    except Exception as e:
        print(f'An error occurred: {e}')

# defining function for create account page
def create_signup(d_frame):
    d_frame.pack_forget()
    signup_frame = tk.Frame(root)
    signup_frame.pack(anchor='center',expand=1)
    frame_label = tk.Label(signup_frame, text='Create Account', font=('sans-serif', 14, 'bold'), pady=15)
    frame_label.grid(row=0, column=0, columnspan=2)
                # var1  var2     var3              var4
    labels = ('Name','Email','Create Username','Create Password')
    var1 = tk.StringVar()
    var2= tk.StringVar()
    var3 = tk.StringVar()
    var4 = tk.StringVar()
    variables = [var1,var2,var3,var4]

    # creating labels and entries for taking user details
    for index,item in enumerate(labels,start=1):
        tk.Label(signup_frame, text=f'{item} : ').grid(row=index, column=0, pady=8,sticky='news')
        user_n_entry = tk.Entry(signup_frame, textvariable=variables[index-1], width=40, font=('sans-serif', 10))
        user_n_entry.grid(row=index, column=1, pady=4, ipady=5, padx=4)

    data = {}
    # signup_btn
    tk.Button(signup_frame, text='Create Account', padx=10, pady=3, relief='groove', overrelief='ridge', bd=3,width=48, command=lambda : write_to_db(data,labels,variables)).grid(row=5, column=0, sticky='e', columnspan=2, pady=15)

    # login_btn
    tk.Button(signup_frame, text='Login', padx=10, pady=3, relief='groove', overrelief='ridge', bd=3, width=48, command=lambda : create_login(1,signup_frame)).grid(row=6, column=0, sticky='e', columnspan=2, pady=5)

# defining functionfor read data from database.json
def read_from_db(u_name,psd,login_frame):
    try:
        with open('database.json','r') as f:
            file_data = json.load(f)
            temp = 0
            for dict_d in file_data:
                for widget in login_frame.winfo_children():
                    info = widget.grid_info()
                    if info["row"] == 5:
                        widget.grid_forget()
                if dict_d['Create Username'] == u_name and dict_d['Create Password'] == psd:
                    showinfo(title='Login message',message='Login Successfully.')
                    break
            else:
                temp = 1
            if temp:
                tk.Label(login_frame, text='No Credentials exist.', fg='red',font=('sans-serif', 8)).grid(row=5, column=0,columnspan=2,sticky='w')
    except:
        print('error')

# defining function for login page
def create_login(init = 0,s_frame=None):
        if init : s_frame.pack_forget()
        login_frame = tk.Frame(root, width=200, height=200)
        login_frame.pack(anchor='center', expand=1)

        tk.Label(login_frame,text='Login',font=('sans-serif',14,'bold'),pady=15).grid(row=0,column=0,columnspan=2)
        labels = ('Username','Password')

        for i,items in enumerate(labels,start=1):
            tk.Label(login_frame,text=f'{items} : ').grid(row=i,column=0,pady=4)

        user_n = tk.StringVar()
        pass_wd = tk.StringVar()

        user_n_entry = tk.Entry(login_frame, textvariable=user_n,width=40,font=('sans-serif',10))
        user_n_entry.grid(row=1, column=1,pady=4,ipady=5,padx=4)
        pass_wd_entry = tk.Entry(login_frame, textvariable=pass_wd,show='•',width=40,font=('sans-serif',10))
        pass_wd_entry.grid(row=2, column=1,pady=4,ipady=5,padx=4)

        login_btn = tk.Button(login_frame,text='Login',padx=10,pady=3,relief='groove',overrelief='ridge',bd=3,width=48,command=lambda : read_from_db(user_n.get(),pass_wd.get(),login_frame))
        login_btn.grid(row=3,column=0,sticky='e',columnspan=2,pady=15)

        sign_up_btn = tk.Button(login_frame, text='Create account', padx=10, pady=3, relief='groove', overrelief='ridge', bd=3,width=48,command=lambda : create_signup(login_frame))
        sign_up_btn.grid(row=4, column=0, sticky='e', columnspan=2, pady=2)

root = tk.Tk()
root.geometry('700x550')
root.iconbitmap('./login.ico')
create_login()
root.mainloop()