from tkinter import *
import tkinter as tk
import requests

root = tk.Tk()
root.title("Instagram User Details")
root.geometry('1000x750')

def search():
        u_name = user.get()
        url = f"https://www.instagram.com/{u_name}/?__a=1"
        
        data = requests.get(url).json()
        # print(data)
        def pic():
                import webbrowser
                d = data['graphql']['user']['profile_pic_url']
                webbrowser.open(d)
        if details.get(1.0,END) != "":
                details.delete(1.0,END)
                details.insert(END,f"\t  \n  username : {data['graphql']['user']['username']} \n\t  followers : {data['graphql']['user']['edge_followed_by']['count']} \n\t  following : {data['graphql']['user']['edge_follow']['count']} \n\t  full name : {data['graphql']['user']['full_name']} \n\t  Total post : {data['graphql']['user']['edge_owner_to_timeline_media']['count']} \n\t  category : {data['graphql']['user']['category_enum']} \n\t  Email : {data['graphql']['user']['business_email']} \n\t  bio-link:{data['graphql']['user']['external_url']}\n\t  private account:{data['graphql']['user']['is_private']} \n\t  verified account:{data['graphql']['user']['is_verified']} \n\t  bussiness account:{data['graphql']['user']['is_business_account']}  \n \n   see profile picture" )



                Button(innerframe1,text="click to see",relief=RAISED,borderwidth=2,font=('verdana',18,'bold'),bg='#248aa2',fg="white",command=pic).place(x=680,y=445)



frame = Frame(root,width=1000,height=750,relief=RIDGE,borderwidth=5,bg='#248aa2')
frame.place(x=0,y=0)
Label(root,text ="Developed By Rohan", font = 'arial 30 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')

innerframe = LabelFrame(frame,width=980,height=60,relief=RIDGE,borderwidth=3,bg='#248aa2',highlightbackground="white", highlightcolor="white", highlightthickness=2)
innerframe.place(x=5,y=5)


user = Entry(frame,width=60,font=('verdana',11,'bold'),relief=RIDGE,borderwidth=3)
user.place(x=70,y=15, height=42)

search = Button(frame,text="Search",relief=RAISED,borderwidth=3,font=('verdana',14,'bold'),bg='#248aa2',fg="white",command=search)
search.place(x=745,y=15)


innerframe = LabelFrame(frame,width=980,height=620,relief=RIDGE,borderwidth=3,bg='#248aa2',highlightbackground="white", highlightcolor="white", highlightthickness=2)
innerframe.place(x=5,y=65)


innerframe1 = LabelFrame(innerframe,text="Users Details",width=970,height=605,highlightbackground="white", highlightcolor="white", highlightthickness=5,font=('verdana',10,'bold'))
innerframe1.place(x=0,y=0)


details = Text(innerframe1,height=36,width=133,relief=RIDGE,borderwidth=5,highlightbackground="white", highlightcolor="white",font=('courier',22,''))
details.place(x=5,y=5)

root.mainloop()
