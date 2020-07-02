from tkinter import *
from tkinter import messagebox,scrolledtext
import random
import datetime
import hashlib
import sqlite3
font="arial 20 bold"
font1="arial 15 bold"
transd=[]
#import mysql.connector
withdrawal_self=""
new_self=""
statement_self=""
account_self=""

#con=mysql.connector.connect(user="root",password="08782",host="localhost",database="Banking",autocommit=True)
con=sqlite3.connect("banking.db")
cur=con.cursor()
columns1=("Account No","Name","Email","Mobile")
columns2=("Transaction Id","Amount","Date","Time","Type")
def acc():
        c=random.randrange(10000,100000)
        cur.execute(f"select * from customers where account='{str(c)}'")
        l=cur.fetchone()
        
        if l:
                acc()
        return(str(c))
def transaction_id(dt):
        cur.execute("select * from transaction_id")
        l=cur.fetchone()
        if l:
                if dt==l[0]:
                        cur.execute(f"update transaction_id set number=number+1")
                        con.commit()
                        return(dt+str(int(l[1])+1))
                else:
                        cur.execute(f"update transaction_id set date='{dt}' and number=0")
                        con.commit()
                        return(dt+"0")
        else:
                cur.execute(f"insert into transaction_id values('{dt}',0)")
                con.commit()
                return(dt+"0")
        
def reset(cont,page):
        mob.set("")
        cname.set("")
        acco.set("")
        fname.set("")
        dob.set("")
        email.set("")
        new_self.txt.delete("1.0",END)
        aadhar.set("")
        amount.set("")
        statement_self.from_date.set((datetime.date.today()-datetime.timedelta(30)).strftime("%Y/%m/%d"))
        statement_self.to_date.set(datetime.date.today().strftime("%Y/%m/%d"))
        cont.show_frame(page)


class banking():
        def __init__(self,root):
                uf=Frame(root)
                uf.place(relwidth=1,relheight=.15)
                lf=Frame(root)
                self.login_label=Label(uf,text="",font=font1)
                self.login_label.place(relx=.7,rely=.5)
                lf.place(rely=.15,relwidth=1,relheight=.85)
                lab=Label(uf,text="JRT BANKING LTD",fg="red",font="arial 40 bold")
                lab.place(relx=.35,rely=.05)
                self.frames={}
                for F in (LoginPage,New,Deposit,Withdraw,Statement,Close_Account,Balance_Check,Accounts):
                        
                        frame=F(lf,self)
                        self.frames[F]=frame
                        frame.place(rely=0,relwidth=1,relheight=1)
                self.show_frame(LoginPage)
        def show_frame(self,page):
                frame=self.frames[page]
                if page==Accounts:
                        account_self.search()
                frame.tkraise()

class LoginPage(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)
                self.frame=LabelFrame(self,text="Login")
                self.frame.place(relx=.1,rely=0.1,relwidth=.8,relheight=.8)
                self.user=StringVar()
                self.pwd=StringVar()
                self.user.set("Jrtyagi")
                self.pwd.set("Jt123456@")
                
                self.Controller=controller
                Label(self.frame,text="Username",fg="red",font=font).place(relx=.1,rely=.1)
                Entry(self.frame,textvariable=self.user,width=20,font=font,border=10,insertwidth=4).place(relx=.5,rely=.1)
                Label(self.frame,text="Password",fg="red",font=font).place(relx=.1,rely=.4)
                Entry(self.frame,textvariable=self.pwd,width=20,font=font,border=10,insertwidth=4).place(relx=.5,rely=.4)
                Button(self.frame,text="Login",bg="blue",command=self.check).place(relx=.6,rely=.6)
        def check(self):
                password=hashlib.sha256(str(self.pwd.get()).encode()).hexdigest()
                script=f"select * from admin where username='{self.user.get().title()}' and password='{password}'"
               
                cur.execute(script)
                l=cur.fetchone()
               
                if l:
                       
                        self.Controller.login_label.config(text="Welcome ,"+l[1],fg="skyblue")
                        self.Controller.show_frame(New)
                else:
                        messagebox.showerror("Error","Authentication failed")

class New(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)
                self.container=Frame(self)
                self.container.place(relwidth=1,relheight=1)
                Button(self.container,text="New Account",font=font1,relief=SUNKEN,command=lambda:reset(controller,New)).place(relx=0.05,rely=0.0,relwidth=w)
                Button(self.container,text="Deposit",font=font1,relief=GROOVE,command=lambda:reset(controller,Deposit)).place(relx=0.05+w1,rely=0.0,relwidth=w)
                Button(self.container,text="Withdraw",font=font1,relief=GROOVE,command=lambda:reset(controller,Withdraw)).place(relx=0.05+2*w1,rely=0.0,relwidth=w)
                Button(self.container,text="Check Balance",font=font1,relief=GROOVE,command=lambda:reset(controller,Balance_Check)).place(relx=0.05+3*w1,rely=0,relwidth=w)
                Button(self.container,text="Statement",font=font1,relief=GROOVE,command=lambda:reset(controller,Statement)).place(relx=0.05+4*w1,rely=0,relwidth=w)
                Button(self.container,text="Accounts",font=font1,relief=GROOVE,command=lambda:reset(controller,Accounts)).place(relx=0.05+5*w1,rely=0,relwidth=w)
                Button(self.container,text="Close Account",font=font1,relief=GROOVE,command=lambda:reset(controller,Close_Account)).place(relx=0.05+6*w1,rely=0,relwidth=w)
                self.frame=LabelFrame(self.container,text="New Account")
                self.frame.place(relx=.05,rely=.1,relheight=.8,relwidth=.9)
                self.c=controller
                global new_self
                new_self=self
                
                Label(self.frame,text="Customer Name",fg="red",font=font1).place(relx=.02,rely=.02)
                Entry(self.frame,textvariable=cname,width=30,font=font1,border=10,insertwidth=4).place(relx=.2,rely=.02)
                
                Label(self.frame,text="Fathers's Name",fg="red",font=font1).place(relx=.55,rely=.02)
                Entry(self.frame,textvariable=fname,width=30,font=font1,border=10,insertwidth=4).place(relx=.7,rely=.02)
                
                Label(self.frame,text="Date Of Birth",fg="red",font=font1).place(relx=.02,rely=.2)
                Entry(self.frame,textvariable=dob,width=30,font=font1,border=10,insertwidth=4).place(relx=.2,rely=.2)
                
                Label(self.frame,text="Email",fg="red",font=font1).place(relx=.55,rely=.2)
                Entry(self.frame,textvariable=email,width=30,font=font1,border=10,insertwidth=4).place(relx=.7,rely=.2)
                
                Label(self.frame,text="Contact Number",fg="red",font=font1).place(relx=.02,rely=.4)
                Entry(self.frame,textvariable=mob,width=30,font=font1,border=10,insertwidth=4).place(relx=.2,rely=.4)
                
                Label(self.frame,text="Aadhar Number",fg="red",font=font1).place(relx=.55,rely=.4)
                Entry(self.frame,textvariable=aadhar,width=30,font=font1,border=10,insertwidth=4).place(relx=.7,rely=.4)

                Label(self.frame,text="Permanent Address",fg="red",font=font1).place(relx=.02,rely=.6)

                self.txt=Text(self.frame,font=font1)
                self.txt.place(relx=.3,rely=.6,relwidth=.6,relheight=.2)
                Button(self.frame,text="Submit",bg="skyblue",width=10,command=self.submit).place(relx=.6,rely=.82)

        def submit(self):
                
                try:
                        acc_no=acc()
                        s=f"""insert into customers values('{acc_no}','{cname.get()}','{fname.get()}','{dob.get()}','{aadhar.get()}',
                        '{email.get()}','{mob.get()}','{self.txt.get('1.0',END)}',0,'Open')"""
                        cur.execute(s)
                        con.commit()
                        acco.set(str(acc_no))
                        
                        self.c.show_frame(Deposit)
                        messagebox.showinfo("Hurray","Congratulations! Account created successfully.\n Your account number is "+acc_no)
                except Exception as e:
                        for i in ("account","aadhar","email","mobile"):
                                if i in str(e):
                                        break
                        messagebox.showerror("Error!",i+" Already Registered")

class Deposit(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)
                self.container=Frame(self)
                self.container.place(relwidth=1,relheight=1)
                Button(self.container,text="New Account",font=font1,relief=GROOVE,command=lambda:reset(controller,New)).place(relx=0.05,rely=0.0,relwidth=w)
                Button(self.container,text="Deposit",font=font1,relief=SUNKEN,command=lambda:reset(controller,Deposit)).place(relx=0.05+w1,rely=0.0,relwidth=w)
                Button(self.container,text="Withdraw",font=font1,relief=GROOVE,command=lambda:reset(controller,Withdraw)).place(relx=0.05+2*w1,rely=0.0,relwidth=w)
                Button(self.container,text="Check Balance",font=font1,relief=GROOVE,command=lambda:reset(controller,Balance_Check)).place(relx=0.05+3*w1,rely=0,relwidth=w)
                Button(self.container,text="Statement",font=font1,relief=GROOVE,command=lambda:reset(controller,Statement)).place(relx=0.05+4*w1,rely=0,relwidth=w)
                Button(self.container,text="Accounts",font=font1,relief=GROOVE,command=lambda:reset(controller,Accounts)).place(relx=0.05+5*w1,rely=0,relwidth=w)
                Button(self.container,text="Close Account",font=font1,relief=GROOVE,command=lambda:reset(controller,Close_Account)).place(relx=0.05+6*w1,rely=0,relwidth=w)
                self.frame=LabelFrame(self.container,text="Deposit")
                self.frame.place(relx=.05,rely=.1,relheight=.8,relwidth=.9)
                Label(self.frame,text="Account Number",font=font,fg="red").place(relx=.1,rely=.1)
                Entry(self.frame,textvariable=acco,width=30,font=font).place(relx=.4,rely=.1)
                Label(self.frame,text="Customer Name",font=font,fg="red").place(relx=.1,rely=.3)
                Entry(self.frame,textvariable=cname,width=30,font=font).place(relx=.4,rely=.3)
                Label(self.frame,text="Mobile Number",font=font,fg="red").place(relx=.1,rely=.5)
                Entry(self.frame,textvariable=mob,width=30,font=font).place(relx=.4,rely=.5)
                Label(self.frame,text="Amount",font=font,fg="red").place(relx=.1,rely=.7)
                Entry(self.frame,textvariable=amount,width=30,font=font).place(relx=.4,rely=.7)
                Button(self.frame,text="Deposit",bg="skyblue",width=20,command=self.deposit).place(relx=.6,rely=.8)
        def deposit(self):
                dt=datetime.date.today().strftime("%Y/%m/%d")
                t=datetime.datetime.now().strftime("%H:%M:%S")
                cur.execute(f"select * from customers where account='{acco.get()}'")
                l=cur.fetchone()
                if l:
                        if l[1].upper()==cname.get().upper():
                                tran_id=transaction_id(dt.replace("/",""))
                                cur.execute(f"update customers set balance=balance+{float(amount.get())} where account={acco.get()}")
                                con.commit()
                                cur.execute(f"insert into transactions values('{tran_id}','{acco.get()}','{amount.get()}','{dt}','{t}','Credit')")
                                con.commit()
                                
                                messagebox.showinfo("info",f"Transcation Id :{tran_id}\n Deposited Amount :{amount.get()}\n Status : Success ")
                        else:
                                messagebox.showerror("error","wrong name")
                else:
                        messagebox.showerror("error","wrong account number")

class Withdraw(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)
                self.container=Frame(self)
                self.container.place(relwidth=1,relheight=1)
                Button(self.container,text="New Account",font=font1,relief=GROOVE,command=lambda:reset(controller,New)).place(relx=0.05,rely=0.0,relwidth=w)
                Button(self.container,text="Deposit",font=font1,relief=GROOVE,command=lambda:reset(controller,Deposit)).place(relx=0.05+w1,rely=0.0,relwidth=w)
                Button(self.container,text="Withdraw",font=font1,relief=SUNKEN,command=lambda:reset(controller,Withdraw)).place(relx=0.05+2*w1,rely=0.0,relwidth=w)
                Button(self.container,text="Check Balance",font=font1,relief=GROOVE,command=lambda:reset(controller,Balance_Check)).place(relx=0.05+3*w1,rely=0,relwidth=w)
                Button(self.container,text="Statement",font=font1,relief=GROOVE,command=lambda:reset(controller,Statement)).place(relx=0.05+4*w1,rely=0,relwidth=w)
                Button(self.container,text="Accounts",font=font1,relief=GROOVE,command=lambda:reset(controller,Accounts)).place(relx=0.05+5*w1,rely=0,relwidth=w)
                Button(self.container,text="Close Account",font=font1,relief=GROOVE,command=lambda:reset(controller,Close_Account)).place(relx=0.05+6*w1,rely=0,relwidth=w)
                self.frame=LabelFrame(self.container,text="Withdraw")
                self.frame.place(relx=.05,rely=.1,relheight=.8,relwidth=.9)
                global withdrawal_self
                withdrawal_self=self

                Label(self.frame,text="Account Number",font=font,fg="red").place(relx=.1,rely=.1)
                Entry(self.frame,textvariable=acco,width=30,font=font).place(relx=.4,rely=.1)
                Label(self.frame,text="Customer Name",font=font,fg="red").place(relx=.1,rely=.3)
                Entry(self.frame,textvariable=cname,width=30,font=font).place(relx=.4,rely=.3)
                Label(self.frame,text="Mobile Number",font=font,fg="red").place(relx=.1,rely=.5)
                Entry(self.frame,textvariable=mob,width=30,font=font).place(relx=.4,rely=.5)
                Label(self.frame,text="Amount",font=font,fg="red").place(relx=.1,rely=.7)
                Entry(self.frame,textvariable=amount,width=30,font=font).place(relx=.4,rely=.7)
                Button(self.frame,text="Withdraw",bg="skyblue",width=20,command=self.withdraw).place(relx=.6,rely=.8)

        def withdraw(self):
                dt=datetime.date.today().strftime("%Y/%m/%d")
                
                t=datetime.datetime.now().strftime("%H:%M:%S")
                cur.execute(f"select * from customers where account='{acco.get()}'")
                l=cur.fetchone()
                if l:
                        if l[1].upper()==cname.get().upper():
                                if float(l[8])>=float(amount.get()):
                                        tran_id=transaction_id(dt.replace("/",""))
                                        cur.execute(f"update customers set balance=balance-{float(amount.get())} where account='{acco.get()}''")
                                        con.commit()
                                        cur.execute(f"insert into transactions values('{tran_id}','{acco.get()}','{amount.get()}','{dt}','{t}','Debit')")
                                        con.commit()
                                       
                                        messagebox.showinfo("info",f"Transcation Id :{tran_id}\n Withdrawal Amount :{amount.get()}\n Status : Success ")
                                else:
                                        messagebox.showerror("Error!","Not Enough Balance\n Avilable balance is "+str(l[8]))

                        else:
                                messagebox.showerror("error","wrong name")
                else:
                        messagebox.showerror("error","wrong account number")
                

class Close_Account(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)
                self.container=Frame(self)
                self.container.place(relwidth=1,relheight=1)
                Button(self.container,text="New Account",font=font1,relief=GROOVE,command=lambda:reset(controller,New)).place(relx=0.05,rely=0.0,relwidth=w)
                Button(self.container,text="Deposit",font=font1,relief=GROOVE,command=lambda:reset(controller,Deposit)).place(relx=0.05+w1,rely=0.0,relwidth=w)
                Button(self.container,text="Withdraw",font=font1,relief=GROOVE,command=lambda:reset(controller,Withdraw)).place(relx=0.05+2*w1,rely=0.0,relwidth=w)
                Button(self.container,text="Check Balance",font=font1,relief=GROOVE,command=lambda:reset(controller,Balance_Check)).place(relx=0.05+3*w1,rely=0,relwidth=w)
                Button(self.container,text="Statement",font=font1,relief=GROOVE,command=lambda:reset(controller,Statement)).place(relx=0.05+4*w1,rely=0,relwidth=w)
                Button(self.container,text="Accounts",font=font1,relief=GROOVE,command=lambda:reset(controller,Accounts)).place(relx=0.05+5*w1,rely=0,relwidth=w)
                Button(self.container,text="Close Account",font=font1,relief=SUNKEN,command=lambda:reset(controller,Close_Account)).place(relx=0.05+6*w1,rely=0,relwidth=w)
                self.frame=LabelFrame(self.container,text="Close Account")
                self.frame.place(relx=.05,rely=.1,relheight=.8,relwidth=.9)
                
                Label(self.frame,text="Account Number",font=font,fg="red").place(relx=.1,rely=.1)
                Entry(self.frame,textvariable=acco,width=30,font=font).place(relx=.4,rely=.1)
                Label(self.frame,text="Customer Name",font=font,fg="red").place(relx=.1,rely=.3)
                Entry(self.frame,textvariable=cname,width=30,font=font).place(relx=.4,rely=.3)
                Label(self.frame,text="Mobile Number",font=font,fg="red").place(relx=.1,rely=.5)
                Entry(self.frame,textvariable=mob,width=30,font=font).place(relx=.4,rely=.5)
                Label(self.frame,text="Amount",font=font,fg="red").place(relx=.1,rely=.7)
                Entry(self.frame,textvariable=amount,width=30,font=font).place(relx=.4,rely=.7)
                self.b1=Button(self.frame,text="Close Account",bg="skyblue",width=20,command=withdrawal_self.withdraw)
                self.b1.place(relx=.6,rely=.8)

class Balance_Check(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)
                self.container=Frame(self)
                self.container.place(relwidth=1,relheight=1)
                Button(self.container,text="New Account",font=font1,relief=GROOVE,command=lambda:reset(controller,New)).place(relx=0.05,rely=0.0,relwidth=w)
                Button(self.container,text="Deposit",font=font1,relief=GROOVE,command=lambda:reset(controller,Deposit)).place(relx=0.05+w1,rely=0.0,relwidth=w)
                Button(self.container,text="Withdraw",font=font1,relief=GROOVE,command=lambda:reset(controller,Withdraw)).place(relx=0.05+2*w1,rely=0.0,relwidth=w)
                Button(self.container,text="Check Balance",font=font1,relief=SUNKEN,command=lambda:reset(controller,Balance_Check)).place(relx=0.05+3*w1,rely=0,relwidth=w)
                Button(self.container,text="Statement",font=font1,relief=GROOVE,command=lambda:reset(controller,Statement)).place(relx=0.05+4*w1,rely=0,relwidth=w)
                Button(self.container,text="Accounts",font=font1,relief=GROOVE,command=lambda:reset(controller,Accounts)).place(relx=0.05+5*w1,rely=0,relwidth=w)
                Button(self.container,text="Close Account",font=font1,relief=GROOVE,command=lambda:reset(controller,Close_Account)).place(relx=0.05+6*w1,rely=0,relwidth=w)
                self.frame=LabelFrame(self.container,text="Balance Check")
                self.frame.place(relx=.05,rely=.1,relheight=.8,relwidth=.9)

                Label(self.frame,text="Account Number",font=font,fg="red").place(relx=.1,rely=.1)
                Entry(self.frame,textvariable=acco,width=30,font=font).place(relx=.4,rely=.1)
                Label(self.frame,text="Customer Name",font=font,fg="red").place(relx=.1,rely=.3)
                Entry(self.frame,textvariable=cname,width=30,font=font).place(relx=.4,rely=.3)
                Label(self.frame,text="Mobile Number",font=font,fg="red").place(relx=.1,rely=.5)
                Entry(self.frame,textvariable=mob,width=30,font=font).place(relx=.4,rely=.5)
                Label(self.frame,text="Amount",font=font,fg="red").place(relx=.1,rely=.7)
                self.e1=Entry(self.frame,textvariable=amount,width=30,font=font,state="disabled")
                self.e1.place(relx=.4,rely=.7)
                self.b1=Button(self.frame,text="Check Balance",bg="skyblue",width=20,command=self.show_balance)
                self.b1.place(relx=.6,rely=.8)
        def show_balance(self):
                script=f"select balance from customers where account='{acco.get()}'"
                cur.execute(script)
                l=cur.fetchone()
                if l:
                        amount.set(l[0])
                else:
                        messagebox.showerror("error","Wrong Account Number")

class Statement(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)
                self.container=Frame(self)
                self.container.place(relwidth=1,relheight=1)
                Button(self.container,text="New Account",font=font1,relief=GROOVE,command=lambda:reset(controller,New)).place(relx=0.05,rely=0.0,relwidth=w)
                Button(self.container,text="Deposit",font=font1,relief=GROOVE,command=lambda:reset(controller,Deposit)).place(relx=0.05+w1,rely=0.0,relwidth=w)
                Button(self.container,text="Withdraw",font=font1,relief=GROOVE,command=lambda:reset(controller,Withdraw)).place(relx=0.05+2*w1,rely=0.0,relwidth=w)
                Button(self.container,text="Check Balance",font=font1,relief=GROOVE,command=lambda:reset(controller,Balance_Check)).place(relx=0.05+3*w1,rely=0,relwidth=w)
                Button(self.container,text="Statement",font=font1,relief=SUNKEN,command=lambda:reset(controller,Statement)).place(relx=0.05+4*w1,rely=0,relwidth=w)
                Button(self.container,text="Accounts",font=font1,relief=GROOVE,command=lambda:reset(controller,Accounts)).place(relx=0.05+5*w1,rely=0,relwidth=w)
                Button(self.container,text="Close Account",font=font1,relief=GROOVE,command=lambda:reset(controller,Close_Account)).place(relx=0.05+6*w1,rely=0,relwidth=w)
                self.frame=LabelFrame(self.container,text="Account Statement")
                self.frame.place(relx=.05,rely=.1,relheight=.8,relwidth=.9)

                self.from_date=StringVar()
                self.to_date=StringVar()
                self.type=StringVar()
                global statement_self
                statement_self=self
                self.lists=[""]*5
                self.type.set("All")
                self.from_date.set((datetime.date.today()-datetime.timedelta(30)).strftime("%Y/%m/%d"))
                self.to_date.set(datetime.date.today().strftime("%Y/%m/%d"))
                options=("All","Credit","Debit")
                Label(self.frame,text="Account",width=10,font=font).place(relx=0,rely=0)
                Entry(self.frame,textvariable=acco,width=20,font=font1,border=10,insertwidth=4).place(relx=.1,rely=0)

                Label(self.frame,text="From",font=font).place(relx=.3,rely=0)
                Entry(self.frame,textvariable=self.from_date,width=10,font=font1,border=10,insertwidth=4).place(relx=.4,rely=0)

                Label(self.frame,text="To",font=font).place(relx=.55,rely=0)
                Entry(self.frame,textvariable=self.to_date,width=10,font=font1,border=10,insertwidth=4).place(relx=.65,rely=0)

                Label(self.frame,text="Type",width=10,font=font).place(relx=.75,rely=0)
                opm=OptionMenu(self.frame,self.type,*options)
                opm.place(relx=.85,rely=0)
                for i in range(len(columns2)):
                        Label(self.frame,text=columns2[i],font=font1).place(relx=.005+.194*i,rely=.2,relwidth=.19)
                        self.lists[i]=Listbox(self.frame,font=font1)
                        self.lists[i].place(relx=0.005+.194*i,rely=.25,relheight=.5,relwidth=.19)
                Button(self.frame,text="Search",width=20,command=self.search).place(relx=.9,rely=0)
                
        def search(self):
                if self.type.get()=="All":
                        script=f"select * from transactions where account='{acco.get()}' and date between '{self.from_date.get()}' and '{self.to_date.get()}'"
                else:
                        script=f"select * from transactions where account='{acco.get()}' and type='{self.type.get()}'"
                cur.execute(script)
                l=cur.fetchall()

                for i in range(len(columns2)):
                                self.lists[i].delete(0,END)     
                
                for i in l:
                        self.lists[0].insert(END,str(i[0]))
                        self.lists[1].insert(END,str(i[2]))
                        self.lists[2].insert(END,str(i[3]))
                        self.lists[3].insert(END,i[4])
                        self.lists[4].insert(END,str(i[5]))
        def reset(self):
                acco.set("")
                self.type.set("All")
                self.from_date.set("")
                self.to_date.set("")
                for i in range(len(columns2)):
                        self.lists[i].delete(0,END)

class Accounts(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)
                self.container=Frame(self)
                self.columns3=("Account No","Name","Father's Name","DOB","Aadhar","Email","Mobile","Address","Balance")

                self.container.place(relwidth=1,relheight=1)
                Button(self.container,text="New Account",font=font1,relief=GROOVE,command=lambda:reset(controller,New)).place(relx=0.05,rely=0.0,relwidth=w)
                Button(self.container,text="Deposit",font=font1,relief=GROOVE,command=lambda:reset(controller,Deposit)).place(relx=0.05+w1,rely=0.0,relwidth=w)
                Button(self.container,text="Withdraw",font=font1,relief=GROOVE,command=lambda:reset(controller,Withdraw)).place(relx=0.05+2*w1,rely=0.0,relwidth=w)
                Button(self.container,text="Check Balance",font=font1,relief=GROOVE,command=lambda:reset(controller,Balance_Check)).place(relx=0.05+3*w1,rely=0,relwidth=w)
                Button(self.container,text="Statement",font=font1,relief=GROOVE,command=lambda:reset(controller,Statement)).place(relx=0.05+4*w1,rely=0,relwidth=w)
                Button(self.container,text="Accounts",font=font1,relief=SUNKEN,command=lambda:reset(controller,Accounts)).place(relx=0.05+5*w1,rely=0,relwidth=w)
                Button(self.container,text="Close Account",font=font1,relief=GROOVE,command=lambda:reset(controller,Close_Account)).place(relx=0.05+6*w1,rely=0,relwidth=w)
                self.frame=LabelFrame(self.container,text="Account Holders")
                self.frame.place(relx=.05,rely=.1,relheight=.8,relwidth=.9)

                
                global account_self
                account_self=self
                self.lists=[""]*9
                scrollbar=Scrollbar(self.frame,orient=VERTICAL,command=self.onvsb)
                
                for i in range(len(self.columns3)):
                        Label(self.frame,text=self.columns3[i],font=font1).place(relx=.005+0.11*i,rely=.01,relwidth=.11)
                        self.lists[i]=Listbox(self.frame,font=font1,yscrollcommand=scrollbar.set)
                        scrollbar.pack(side=RIGHT,fill=Y)
                        self.lists[i].place(relx=0.005+0.11*i,rely=.1,relheight=.89,relwidth=.11)

        def onvsb(self,*args):
                for i in range(len(self.columns3)):
                        self.lists[i].yview(*args)

        def search(self):
                script=f"select * from customers where status='Open'"

                cur.execute(script)
                l=cur.fetchall()
                for i in range(len(self.columns3)):
                                self.lists[i].delete(0,END)     
                
                for i in l:
                        
                        self.lists[0].insert(END,str(i[0]))
                        self.lists[1].insert(END,str(i[1]))
                        self.lists[2].insert(END,str(i[2]))
                        self.lists[3].insert(END,i[3])
                        self.lists[4].insert(END,str(i[4]))
                        self.lists[5].insert(END,str(i[5]))
                        self.lists[6].insert(END,str(i[6]))
                        self.lists[7].insert(END,str(i[7]))
                        self.lists[8].insert(END,i[8])
                

root=Tk()
cname=StringVar()
mob=StringVar()
acco=StringVar()
amount=DoubleVar()
fname=StringVar()
dob=StringVar()
email=StringVar()
aadhar=StringVar()
root.title("JRT BANKING LTD")
root.geometry("1920x1080")
w=0.9/7
w1=w-0.002
a=banking(root)
root.mainloop()
