from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk


root = Tk()
root.title("Home Page")

width = 500
height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
# root.config(bg="#b2bec3")

# ========================================VARIABLES========================================
Stextinpid = StringVar()
Stextinpname = StringVar()
Stextinpprice = StringVar()
Stextinpcategory = StringVar()
Stextinpstock = StringVar()
Stextinprating = StringVar()
Stextinaid = StringVar()
CSEARCH = StringVar()

Stextinaid = StringVar()
Stextinausername = StringVar()
Stextinapassword = StringVar()
Stextinaname = StringVar()
Stextinadob = StringVar()
Stextinaemailid = StringVar()

Stextincid = StringVar()
Stextincusername = StringVar()
Stextincpassword = StringVar()
Stextincname = StringVar()
Stextincaddress = StringVar()
Stextincphoneno = StringVar()
Stextincshoppingexp = StringVar()
Stextincpincode = StringVar()
Stextinaid = StringVar()
 
inpid=StringVar()
inquantity=IntVar()
inamount=IntVar()
total=IntVar()    
total=0
SEARCH = StringVar()
QSEARCH = StringVar()
a="#B0BEC5"


def Database():
    global conn, cursor
    conn = sqlite3.connect("ukiyorobstop.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS admin(AID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,AUSERNAME VARCHAR(20) UNIQUE,APASSWORD VARCHAR(50),ANAME VARCHAR(30),ADOB DATE,AEMAILID VARCHAR(50))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS customer(CID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,CUSERNAME VARCHAR(20) UNIQUE,CPASSWORD VARCHAR(50),CNAME VARCHAR(30),CADDRESS VARCHAR(30),CPHONENO INTEGER,CPINCODE INTEGER,AID INTEGER,FOREIGN KEY (AID) REFERENCES admin(AID))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS product(PID VARCHAR(10) PRIMARY KEY NOT NULL,PNAME VARCHAR(30),PPRICE VARCHAR(30),PCATEGORY VARCHAR(30),PSTOCK BOOLEAN,AID INTEGER,FOREIGN KEY (AID) REFERENCES admin(AID))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS purchases(CID INTEGER,PID VARCHAR(20),FOREIGN KEY (CID) REFERENCES product(CID)FOREIGN KEY (PID) REFERENCES customer(PID))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS invoice(IID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,PID VARCHAR(10),IQUANTITY INTEGER,IAMOUNT VARCHAR(30),CID INTEGER,FOREIGN KEY (CID) REFERENCES customer(CID),FOREIGN KEY (PID) REFERENCES product(PID))")
    
def ShowLoginForm():                  #for the admin login for geometry
    global ShowLoginForm
    global loginform

    loginform = Toplevel()
    loginform.title("Ukiyo Robstop")
    width = 500
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()


def LoginForm():                     #for admin logon for widgets
    global lbl_result
#    a="#B0BEC5"
    loginform.config(bg=a)


    label1 = Label(loginform, text='ADMIN LOGIN', fg='black',bg=a, font=('Bahnschrift SemiBold SemiConden', 20,))
    label1.place(x=175, y=95)

    label2 = Label(loginform, text="Username:", fg='black',bg=a, font=('Bahnschrift SemiBold SemiConden', 13))
    label2.place(x=130, y=210)

    entry_1 = Entry(loginform, textvar=Stextinausername, font=('Bahnschrift SemiBold SemiConden', 13), width=15)
    entry_1.place(x=215, y=210)

    label3 = Label(loginform, text="Password:", fg='black',bg=a, font=('Bahnschrift SemiBold SemiConden', 13))
    label3.place(x=130, y=280)

    label4 = Label(loginform, text="forgot account ?", fg='grey',bg=a, font=('Bahnschrift SemiBold SemiConden', 10))
    label4.place(x=240, y=300)

    entry_2 = Entry(loginform, textvar=Stextinapassword, font=('Bahnschrift SemiBold SemiConden', 13), width=15,show='*')
    entry_2.place(x=210, y=280)

    button1 = Button(loginform, height="1", width="10", text="Login", fg='black', relief=RAISED, font=('Bahnschrift SemiBold SemiConden', 12,),
                     command=Login)
    button1.place(x=150, y=335)

    button2 = Button(loginform, height="1", width="10", text="Sign Up", fg='black', relief=RAISED, font=('Bahnschrift SemiBold SemiConden', 12,),
                     command=ShowSignUpForm)
    button2.place(x=250, y=335)

    lbl_result = Label(loginform, text="",bg=a, fg='grey', font=('Bahnschrift SemiBold SemiConden', 13))
    lbl_result.place(x=130, y=370)


def Login(event=None):                          #functions to check the condition for login
    global AID
    Database()
    if Stextinausername.get == "" or Stextinapassword.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `AUSERNAME` = ? AND `APASSWORD` = ?",
                       (Stextinausername.get(), Stextinapassword.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `AUSERNAME` = ? AND `APASSWORD` = ?",
                           (Stextinausername.get(), Stextinapassword.get()))
            data = cursor.fetchone()
            Stextinaid = data[0]
            Stextinausername.set("")
            Stextinapassword.set("")
            lbl_result.config(text="")
            ProcusGeo()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            Stextinausername.set("")
            Stextinapassword.set("")
    cursor.close()
    conn.close()


def ShowSignUpForm():                     #funtion for the geometry for admin sign up form
    global signupform
    signupform = Toplevel()
    signupform.title("Ukiyo Robstop")
    width = 600
    height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    signupform.resizable(0, 0)
    signupform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    SignupForm()


def SignupForm():                        #funtions for the widgets for admin login for
    global lbl_result1
 #   a = "#B0BEC5"
    signupform.config(bg=a)
    TopSignupForm = Frame(signupform, width=600, height=100, bd=1, relief=SOLID)
    TopSignupForm.pack(side=TOP, pady=20)

    lbl_text1 = Label(TopSignupForm, text="ADMIN - SIGN UP",bg=a, font=('Bahnschrift SemiBold SemiConden', 18), width=600)
    lbl_text1.pack(fill=X)

    MidSignupForm = Frame(signupform, width=600)
    MidSignupForm.pack(side=TOP, pady=50)

    MidSignupForm.config(bg=a)

    lbl_aid = Label(MidSignupForm, text="ID:",bg=a, font=('Bahnschrift SemiBold SemiConden', 13), bd=15)
    lbl_aid.grid(row=0, sticky=W)

    lbl_name = Label(MidSignupForm, text="Name:",bg=a ,font=('Bahnschrift SemiBold SemiConden', 13), bd=15)
    lbl_name.grid(row=1, sticky=W)

    lbl_username = Label(MidSignupForm, text="Username:",bg=a,font=('Bahnschrift SemiBold SemiConden', 13), bd=15)
    lbl_username.grid(row=2, sticky=W)

    lbl_password = Label(MidSignupForm, text="Password:",bg=a, font=('Bahnschrift SemiBold SemiConden', 13), bd=15)
    lbl_password.grid(row=3, sticky=W)

    lbl_dob = Label(MidSignupForm, text="DOB:",bg=a, font=('Bahnschrift SemiBold SemiConden', 13), bd=15)
    lbl_dob.grid(row=4, sticky=W)

    lbl_emailid = Label(MidSignupForm,bg=a, text="Email ID:", font=('Bahnschrift SemiBold SemiConden', 13), bd=15)
    lbl_emailid.grid(row=5, sticky=W)

    lbl_result1 = Label(MidSignupForm,bg=a, text="", font=('Bahnschrift SemiBold SemiConden', 5))
    lbl_result1.grid(row=6, columnspan=2)

    aid = Entry(MidSignupForm, textvariable=Stextinaid, font=('Bahnschrift SemiBold SemiConden', 13), width=15)
    aid.grid(row=0, column=1)

    aname = Entry(MidSignupForm, textvariable=Stextinaname,font=('Bahnschrift SemiBold SemiConden', 13), width=15)
    aname.grid(row=1, column=1)

    ausername = Entry(MidSignupForm, textvariable=Stextinausername, font=('Bahnschrift SemiBold SemiConden', 13), width=15)
    ausername.grid(row=2, column=1)

    apassword = Entry(MidSignupForm, textvariable=Stextinapassword, font=('Bahnschrift SemiBold SemiConden', 13), width=15)
    apassword.grid(row=3, column=1)

    adob = Entry(MidSignupForm, textvariable=Stextinadob, font=('Bahnschrift SemiBold SemiConden', 13), width=15)
    adob.grid(row=4, column=1)

    aemailid = Entry(MidSignupForm, textvariable=Stextinaemailid, font=('Bahnschrift SemiBold SemiConden', 13), width=15)
    aemailid.grid(row=5, column=1)

    btn_submit = Button(MidSignupForm, text="Submit", font=('Bahnschrift SemiBold SemiConden', 13), width=10, command=SubmitAdmin)
    btn_submit.grid(row=7, column=0)

    btn_submit = Button(MidSignupForm, text="Back", font=('Bahnschrift SemiBold SemiConden', 13), width=10, command=backadminsignup)
    btn_submit.grid(row=7, column=1)

    btn_submit.bind('<Return>', SubmitAdmin)


def backadminsignup():                     #funtion for the back button in the admin signup form
    signupform.destroy()


def CusShowLoginForm():                        # funtion for geometry of customer login form
    global cusloginform
    cusloginform = Toplevel()
    cusloginform.title("Ukiyo Robstop")
    width = 500
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    cusloginform.resizable(0, 0)
    cusloginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    CusLoginForm()


def CusLoginForm():          #funtion for the widgets of customer login form
    global lbl_result1
    a = "#B0BEC5"
    cusloginform.config(bg=a)
#    imge2 = Image.open("C:/Users/chandhana menon/Desktop/cuspic.png")
#    photo2 = ImageTk.PhotoImage(imge2)

#    lab2 = Label(cusloginform, image=photo2)
#    lab2.place(x=205, y=10)

    label1 = Label(cusloginform, text='CUSTOMER LOGIN',bg=a, fg='black', font=('Bahnschrift SemiBold SemiConden', 20,))
    label1.place(x=145, y=95)

    label2 = Label(cusloginform, text="Username:",bg=a, fg='black', font=('Bahnschrift SemiBold SemiConden', 13))
    label2.place(x=130, y=210)

    entry_1 = Entry(cusloginform, textvar=Stextincusername, font=('Bahnschrift SemiBold SemiConden', 13), width=15)
    entry_1.place(x=215, y=210)

    label3 = Label(cusloginform, text="Password:", fg='black',bg=a, font=('Bahnschrift SemiBold SemiConden', 13))
    label3.place(x=130, y=280)

    label4 = Label(cusloginform, text="forgot account ?", fg='grey',bg=a, font=('Bahnschrift SemiBold SemiConden', 10))
    label4.place(x=240, y=300)

    entry_2 = Entry(cusloginform, textvar=Stextincpassword, font=('Bahnschrift SemiBold SemiConden', 13), width=15,show='*')
    entry_2.place(x=210, y=280)

    button1 = Button(cusloginform, height="1", width="10", text="Login", fg='black', relief=RAISED, font=('Bahnschrift SemiBold SemiConden', 12,),
                     command=CusLogin)
    button1.place(x=150, y=335)

    button2 = Button(cusloginform, height="1", width="10", text="Sign Up", fg='black', relief=RAISED,
                     font=('Bahnschrift SemiBold SemiConden', 12,), command=CusShowSignUpForm)
    button2.place(x=250, y=335)

    lbl_result1 = Label(cusloginform, text="", fg='grey',bg=a, font=('Bahnschrift SemiBold SemiConden', 13))
    lbl_result1.place(x=130, y=370)


def CusLogin(event=None):               #funtion to verify the cutomer login information
    global CID
    Database()
    if Stextincusername.get == "" or Stextincpassword.get() == "":
        lbl_result1.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `customer` WHERE `CUSERNAME` = ? AND `CPASSWORD` = ?",
                       (Stextincusername.get(), Stextincpassword.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `customer` WHERE `CUSERNAME` = ? AND `CPASSWORD` = ?",
                           (Stextincusername.get(), Stextincpassword.get()))
            data = cursor.fetchone()
            Stextincid = data[0]
            Stextincusername.set("")
            Stextincpassword.set("")
            lbl_result1.config(text="")
            CShowView()
        else:
            lbl_result1.config(text="Invalid username or password", fg="red")
            Stextincusername.set("")
            Stextincpassword.set("")
    #    cursor.close()
    conn.close()


def CusShowSignUpForm():                    #funtion for the geometry of customer sign up form
    global CusShowLoginForm
    global cussignupform
    cussignupform = Toplevel()
    cussignupform.title("Ukiyo Robstop")
    width = 600
    height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    cussignupform.resizable(0, 0)
    cussignupform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    CusSignupForm()


def CusSignupForm():             #function for the widgets of customer sign up form
    global lbl_result2
#    a="#B0BEC5"
    cussignupform.config(bg=a)
    TopCusSignupForm = Frame(cussignupform, width=800, height=100, bd=1, relief=SOLID)
    TopCusSignupForm.pack(side=TOP, pady=20)

    lbl_text = Label(TopCusSignupForm, text="CUSTOMER - SIGN UP",bg=a, font=('Bahnschrift SemiBold SemiConden', 18), width=600)
    lbl_text.pack(fill=X)

    MidCusSignupForm = Frame(cussignupform, width=600,bg=a)
    MidCusSignupForm.pack(side=TOP, pady=50)

    lbl_cid = Label(MidCusSignupForm, text="ID:",bg=a, font=('Bahnschrift SemiBold SemiConden', 13), bd=18)
    lbl_cid.grid(row=0, sticky=W)

    lbl_name = Label(MidCusSignupForm, text="Name:",bg=a, font=('Bahnschrift SemiBold SemiConden', 13), bd=18)
    lbl_name.grid(row=1, sticky=W)

    lbl_username = Label(MidCusSignupForm, text="Username:",bg=a, font=('Bahnschrift SemiBold SemiConden', 13), bd=18)
    lbl_username.grid(row=2, sticky=W)

    lbl_password = Label(MidCusSignupForm, text="Password:",bg=a, font=('Bahnschrift SemiBold SemiConden', 13), bd=18)
    lbl_password.grid(row=3, sticky=W)

    lbl_address = Label(MidCusSignupForm, text="Address:",bg=a, font=('Bahnschrift SemiBold SemiConden', 13), bd=18)
    lbl_address.grid(row=4, sticky=W)

    lbl_phone = Label(MidCusSignupForm, text="Phone no.:",bg=a, font=('Bahnschrift SemiBold SemiConden', 13), bd=18)
    lbl_phone.grid(row=5, sticky=W)

    lbl_pincode = Label(MidCusSignupForm, text="Pincode:",bg=a, font=('Bahnschrift SemiBold SemiConden', 13), bd=18)
    lbl_pincode.grid(row=6, sticky=W)

    lbl_result2 = Label(MidCusSignupForm, text="",bg=a, font=('Bahnschrift SemiBold SemiConden', 5))
    lbl_result2.grid(row=7, columnspan=2)

    cid = Entry(MidCusSignupForm, textvariable=Stextincid, font=('Bahnschrift SemiBold SemiConden', 13), width=15)
    cid.grid(row=0, column=1)

    cname = Entry(MidCusSignupForm, textvariable=Stextincname, font=('Bahnschrift SemiBold SemiConden', 13), width=15)
    cname.grid(row=1, column=1)

    cusername = Entry(MidCusSignupForm, textvariable=Stextincusername, font=('Bahnschrift SemiBold SemiConden', 13), width=15)
    cusername.grid(row=2, column=1)

    cpassword = Entry(MidCusSignupForm, textvariable=Stextincpassword, font=('Bahnschrift SemiBold SemiConden', 13), width=15)
    cpassword.grid(row=3, column=1)

    caddress = Entry(MidCusSignupForm, textvariable=Stextincaddress, font=('Bahnschrift SemiBold SemiConden', 13), width=15)
    caddress.grid(row=4, column=1)

    cphoneno = Entry(MidCusSignupForm, textvariable=Stextincphoneno, font=('Bahnschrift SemiBold SemiConden', 13), width=15)
    cphoneno.grid(row=5, column=1)

    pincode = Entry(MidCusSignupForm, textvariable=Stextincpincode, font=('Bahnschrift SemiBold SemiConden', 13), width=15)
    pincode.grid(row=6, column=1)

    btn_submit = Button(MidCusSignupForm, text="Submit", font=('Bahnschrift SemiBold SemiConden', 13), width=10, command=SubmitCus)
    btn_submit.grid(row=7, column=0, pady=20)

    btn_submit = Button(MidCusSignupForm, text="Back", font=('Bahnschrift SemiBold SemiConden', 13), width=10, command=cussignupback)
    btn_submit.grid(row=7, column=1, pady=20)


def cussignupback():               #funtion for the back button in cutomer sign up form
    cussignupform.destroy()

def SubmitAdmin():                 #funtion to insert the admin details to the table through the signup page
    db = sqlite3.connect("ukiyo.db")
    cursor = db.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS admin(AID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,AUSERNAME VARCHAR(20) UNIQUE,APASSWORD VARCHAR(50),ANAME VARCHAR(30),ADOB DATE,AEMAILID VARCHAR(50))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS customer(CID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,CUSERNAME VARCHAR(20) UNIQUE,CPASSWORD VARCHAR(50),CNAME VARCHAR(30),CADDRESS VARCHAR(30),CPHONENO INTEGER,CPINCODE INTEGER,AID INTEGER,FOREIGN KEY (AID) REFERENCES admin(AID))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS product(PID VARCHAR(10) PRIMARY KEY NOT NULL,PNAME VARCHAR(30),PPRICE VARCHAR(30),PCATEGORY VARCHAR(30),PSTOCK BOOLEAN,AID INTEGER,FOREIGN KEY (AID) REFERENCES admin(AID))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS purchases(CID INTEGER,PID VARCHAR(20),FOREIGN KEY (CID) REFERENCES product(CID)FOREIGN KEY (PID) REFERENCES customer(PID))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS invoice(IID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,PID VARCHAR(10),IQUANTITY INTEGER,IAMOUNT VARCHAR(30),CID INTEGER,FOREIGN KEY (CID) REFERENCES customer(CID),FOREIGN KEY (PID) REFERENCES product(PID))")

    db.commit()
    Said = Stextinaid.get()
    Sausername = Stextinausername.get()
    Sapassword = Stextinapassword.get()
    Saname = Stextinaname.get()
    Sadob = Stextinadob.get()
    Saemailid = Stextinaemailid.get()
    connect1 = sqlite3.connect("ukiyo.db")
    with connect1:
        cursor = connect1.cursor()
        cursor.execute("INSERT INTO admin (AID,AUSERNAME,APASSWORD,ANAME,ADOB,AEMAILID) VALUES(?,?,?,?,?,?)",
                       (Said, Sausername, Sapassword, Saname, Sadob, Saemailid))
        db.close()


def SubmitCus():                       #funtion to insert the customer details to the table through the signup page
    db = sqlite3.connect("ukiyo.db")
    cursor = db.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS admin(AID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,AUSERNAME VARCHAR(20) UNIQUE,APASSWORD VARCHAR(50),ANAME VARCHAR(30),ADOB DATE,AEMAILID VARCHAR(50))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS customer(CID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,CUSERNAME VARCHAR(20) UNIQUE,CPASSWORD VARCHAR(50),CNAME VARCHAR(30),CADDRESS VARCHAR(30),CPHONENO INTEGER,CPINCODE INTEGER,AID INTEGER,FOREIGN KEY (AID) REFERENCES admin(AID))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS product(PID VARCHAR(10) PRIMARY KEY NOT NULL,PNAME VARCHAR(30),PPRICE VARCHAR(30),PCATEGORY VARCHAR(30),PSTOCK BOOLEAN,AID INTEGER,FOREIGN KEY (AID) REFERENCES admin(AID))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS purchases(CID INTEGER,PID VARCHAR(20),FOREIGN KEY (CID) REFERENCES product(CID)FOREIGN KEY (PID) REFERENCES customer(PID))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS invoice(IID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,PID VARCHAR(10),IQUANTITY INTEGER,IAMOUNT VARCHAR(30),CID INTEGER,FOREIGN KEY (CID) REFERENCES customer(CID),FOREIGN KEY (PID) REFERENCES product(PID))")

    db.commit()

    Scid = Stextincid.get()
    Scusername = Stextincusername.get()
    Scpassword = Stextincpassword.get()
    Scname = Stextincname.get()
    Scaddress = Stextincaddress.get()
    Scphoneno = Stextincphoneno.get()

    Scpincode = Stextincpincode.get()
    Said = Stextinaid.get()

    connect2 = sqlite3.connect("ukiyo.db")
    with connect2:
        cursor = connect2.cursor()
        cursor.execute(
            "INSERT INTO `customer` (CID,CUSERNAME,CPASSWORD,CNAME,CADDRESS,CPHONENO,CPINCODE) VALUES(?,?,?,?,?,?,?)",
            (Scid, Scusername, Scpassword, Scname, Scaddress, Scphoneno, Scpincode,))
        db.close()


def ShowProductForm():         #funtion for the geometry of the product form
    global productform
    productform = Toplevel()
    productform.title("Ukiyo Robstop")
    width = 600
    height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    productform.resizable(0, 0)
    productform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    ProductForm()


def ProductForm():               #funtion to for the widgets in the product form
    global lbl_result3
#    a = "#B0BEC5"
    productform.config(bg=a)
    TopProductForm = Frame(productform, width=600, height=100, bd=1, relief=SOLID)
    TopProductForm.pack(side=TOP, pady=20)

    lbl_text1 = Label(TopProductForm, text="ADD PRODUCT",bg=a, font=('Bahnschrift SemiBold SemiConden', 18), width=600)
    lbl_text1.pack(fill=X)

    MidProductForm = Frame(productform, width=600,bg=a)
    MidProductForm.pack(side=TOP, pady=50)

    lbl_pid = Label(MidProductForm, text="PID:",bg=a, font=('Bahnschrift SemiBold SemiConden', 13), bd=13)
    lbl_pid.grid(row=0, sticky=W)

    lbl_pname = Label(MidProductForm, text="Product Name:",bg=a, font=('Bahnschrift SemiBold SemiConden', 13), bd=13)
    lbl_pname.grid(row=1, sticky=W)

    lbl_pprice = Label(MidProductForm, text="Price",bg=a, font=('Bahnschrift SemiBold SemiConden', 13), bd=13)
    lbl_pprice.grid(row=2, sticky=W)

    lbl_pcategory = Label(MidProductForm, text="Category",bg=a, font=('Bahnschrift SemiBold SemiConden', 13), bd=13)
    lbl_pcategory.grid(row=3, sticky=W)

    lbl_pstock = Label(MidProductForm, text="In Stock",bg=a, font=('Bahnschrift SemiBold SemiConden', 13), bd=13)
    lbl_pstock.grid(row=4, sticky=W)



    lbl_result3 = Label(MidProductForm, text="",bg=a, font=('Bahnschrift SemiBold SemiConden', 10))
    lbl_result3.grid(row=6, columnspan=2)

    pid = Entry(MidProductForm, textvariable=Stextinpid, font=('Bahnschrift SemiBold SemiConden', 13), width=13)
    pid.grid(row=0, column=1)

    pname = Entry(MidProductForm, textvariable=Stextinpname, font=('Bahnschrift SemiBold SemiConden', 13), width=13)
    pname.grid(row=1, column=1)

    pprice = Entry(MidProductForm, textvariable=Stextinpprice, font=('Bahnschrift SemiBold SemiConden', 13), width=13)
    pprice.grid(row=2, column=1)

    pcategory = Entry(MidProductForm, textvariable=Stextinpcategory, font=('Bahnschrift SemiBold SemiConden', 13), width=13)
    pcategory.grid(row=3, column=1)

    pstock = Entry(MidProductForm, textvariable=Stextinpstock, font=('Bahnschrift SemiBold SemiConden', 13), width=13)
    pstock.grid(row=4, column=1)



    btn_submit = Button(MidProductForm, text="Submit", font=('Bahnschrift SemiBold SemiConden', 12), width=10, command=InsertProduct)
    btn_submit.grid(row=7, column=1)

    btn_submit = Button(MidProductForm, text="Back", font=('Bahnschrift SemiBold SemiConden', 12), width=10, command=addproductback)
    btn_submit.grid(row=7, column=2)
        



def addproductback():              #function for the backbutton in the product form for the admin
    productform.destroy()


def InsertProduct():              #funtion to insert product into the product table 
    db = sqlite3.connect("ukiyo.db")
    cursor = db.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS admin(AID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,AUSERNAME VARCHAR(20) UNIQUE,APASSWORD VARCHAR(50),ANAME VARCHAR(30),ADOB DATE,AEMAILID VARCHAR(50))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS customer(CID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,CUSERNAME VARCHAR(20) UNIQUE,CPASSWORD VARCHAR(50),CNAME VARCHAR(30),CADDRESS VARCHAR(30),CPHONENO INTEGER,CPINCODE INTEGER,AID INTEGER,FOREIGN KEY (AID) REFERENCES admin(AID))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS product(PID VARCHAR(10) PRIMARY KEY NOT NULL,PNAME VARCHAR(30),PPRICE VARCHAR(30),PCATEGORY VARCHAR(30),PSTOCK BOOLEAN,AID INTEGER,FOREIGN KEY (AID) REFERENCES admin(AID))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS purchases(CID INTEGER,PID VARCHAR(20),FOREIGN KEY (CID) REFERENCES product(CID)FOREIGN KEY (PID) REFERENCES customer(PID))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS invoice(IID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,PID VARCHAR(10),IQUANTITY INTEGER,IAMOUNT VARCHAR(30),CID INTEGER,FOREIGN KEY (CID) REFERENCES customer(CID),FOREIGN KEY (PID) REFERENCES product(PID))")

    db.commit()
    Spid = Stextinpid.get()
    Spname = Stextinpname.get()
    Spprice = Stextinpprice.get()
    Spcategory = Stextinpcategory.get()
    Spstock = Stextinpstock.get()


    connect4 = sqlite3.connect("ukiyo.db")
    with connect4:
        cursor = connect4.cursor()
        cursor.execute("INSERT INTO product (PID,PNAME,PPRICE,PCATEGORY,PSTOCK) VALUES(?,?,?,?,?)",
                       (Spid, Spname, Spprice, Spcategory, Spstock))
        db.close()


def ProcusGeo():                   #funtion for the option table after logging in as a admin
    global procusform
    procusform = Toplevel()
    procusform.title("Ukiyo Robstop")
    width = 500
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    procusform.resizable(0, 0)
    procusform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    ProcusForm()


def ProcusForm():         #
    global home

    label2 = Label(procusform, text="WELCOME TO ADMIN PORTAL", fg='black', font=("Bahnschrift SemiBold SemiConden", 16))
    label2.place(x=140, y=160)
    button2 = Button(procusform, height="2", width="30", text="CUSTOMER", fg='black', relief=GROOVE, font=("arial", 12),
                     command=CusShowView)
    button2.place(x=110, y=250)
    button3 = Button(procusform, height="2", width="30", text="PRODUCT", fg='black', relief=GROOVE, font=("arial", 12),
                     command=ShowView)
    button3.place(x=110, y=320)
    button3 = Button(procusform, height="2", width="30", text="LOGOUT", fg='black', relief=GROOVE, font=("arial", 12),
                     command=Logout)
    button3.place(x=110, y=390)


def ShowView():  # for admin -product
    global viewform
    viewform = Toplevel(root)
    viewform.title("Ukiyo Robstop")
    width = 1024
    height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm()


def ViewForm(): #for admin -product
    global tree
 #   a="#B0BEC5"
    viewform.config(bg=a)
    
#    cusloginform.destroy()
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID,bg=a)
    TopViewForm.pack(side=TOP, fill=X)

    LeftViewForm = Frame(viewform, width=200,bg=a)
    LeftViewForm.pack(side=LEFT, fill=Y)

    MidViewForm = Frame(viewform, width=800)
    MidViewForm.pack(side=RIGHT)

    lbl_text = Label(TopViewForm, text="PRODUCT INFORMATION",bg=a, font=('Bahnschrift SemiBold SemiConden', 18), width=600)
    lbl_text.pack(fill=X)

    lbl_txtsearch = Label(LeftViewForm, text="Search",bg=a, font=('Bahnschrift SemiBold SemiConden', 10))
    lbl_txtsearch.pack(side=TOP, anchor=W)

    search = Entry(LeftViewForm, textvariable=SEARCH, font=('Bahnschrift SemiBold SemiConden', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)

    btn_delete = Button(LeftViewForm, text="Add", command=ShowProductForm)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_search = Button(LeftViewForm, text="Search", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_delete = Button(LeftViewForm, text="Back", command=AdminProductBack)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)

    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)

    tree = ttk.Treeview(MidViewForm, columns=("PID", "NAME", "PRICE", "CATEGORY", "STOCK"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)

    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)

    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('PID', text="PID", anchor=W)
    tree.heading('NAME', text="NAME", anchor=W)
    tree.heading('PRICE', text="PRICE", anchor=W)
    tree.heading('CATEGORY', text="CATEGORY", anchor=W)
    tree.heading('STOCK', text="STOCK", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#5', stretch=NO, minwidth=0, width=200)


    tree.pack()
    DisplayData()


def DisplayData():  #display the data product view -admin
    db = sqlite3.connect("ukiyo.db")
    cursor = db.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS admin(AID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,AUSERNAME VARCHAR(20) UNIQUE,APASSWORD VARCHAR(50),ANAME VARCHAR(30),ADOB DATE,AEMAILID VARCHAR(50))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS customer(CID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,CUSERNAME VARCHAR(20) UNIQUE,CPASSWORD VARCHAR(50),CNAME VARCHAR(30),CADDRESS VARCHAR(30),CPHONENO INTEGER,CPINCODE INTEGER,AID INTEGER,FOREIGN KEY (AID) REFERENCES admin(AID))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS product(PID VARCHAR(10) PRIMARY KEY NOT NULL,PNAME VARCHAR(30),PPRICE VARCHAR(30),PCATEGORY VARCHAR(30),PSTOCK BOOLEAN,AID INTEGER,FOREIGN KEY (AID) REFERENCES admin(AID))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS purchases(CID INTEGER,PID VARCHAR(20),FOREIGN KEY (CID) REFERENCES product(CID)FOREIGN KEY (PID) REFERENCES customer(PID))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS invoice(IID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,PID VARCHAR(10),IQUANTITY INTEGER,IAMOUNT VARCHAR(30),CID INTEGER,FOREIGN KEY (CID) REFERENCES customer(CID),FOREIGN KEY (PID) REFERENCES product(PID))")

    db.commit()
    cursor.execute("SELECT * FROM `product`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def Search():  #used to search the product list
    tree.delete(*tree.get_children())
    Database()
    print(str(SEARCH.get()))
    cursor.execute("SELECT * FROM product WHERE PID = '%s'" % (str(SEARCH.get())))
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def Reset(): #resetthe view of the product list
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")


def Delete(): #  delets the view of
    if not tree.selection():
        print("ERROR")
    else:
        result = tkMessageBox.askquestion('Ukiyo Robstop', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            Database()
            cursor.execute("DELETE FROM product WHERE PID = '%s'" % selecteditem[0])
            conn.commit()
            cursor.close()
            viewform.deiconify()
        if result == 'no':
            viewform.deiconify()

def CusShowView():
    global cusviewform
    cusviewform = Toplevel(root)
    cusviewform.title("Ukiyo Robstop")
    width = 1024
    height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    cusviewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    cusviewform.resizable(0, 0)
    CusViewForm()


def CusViewForm():
    global tree
    global cusviewform
 #   a="#B0BEC5"
    cusviewform.config(bg=a)
    TopCusViewForm = Frame(cusviewform, width=600, bd=1, relief=SOLID,bg=a)
    TopCusViewForm.pack(side=TOP, fill=X)

    LeftCusViewForm = Frame(cusviewform, width=600,bg=a)
    LeftCusViewForm.pack(side=LEFT, fill=Y)

    MidCusViewForm = Frame(cusviewform, width=800,bg=a)
    MidCusViewForm.pack(side=RIGHT)

    lbl_text = Label(TopCusViewForm, text="CUSTOMER INFORMATION", font=('Bahnschrift SemiBold SemiConden', 18), width=600,bg=a)
    lbl_text.pack(fill=X)

    lbl_txtsearch = Label(LeftCusViewForm, text="Search",bg=a, font=('Bahnschrift SemiBold SemiConden', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)

    search = Entry(LeftCusViewForm, textvariable=CSEARCH, font=('Bahnschrift SemiBold SemiConden', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)

    btn_search = Button(LeftCusViewForm, text="Search", command=CusSearch)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_reset = Button(LeftCusViewForm, text="Reset", command=CusReset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_delete = Button(LeftCusViewForm, text="Back", command=AdminCusBack)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)

    scrollbarx = Scrollbar(MidCusViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidCusViewForm, orient=VERTICAL)

    tree = ttk.Treeview(MidCusViewForm,
                        columns=("CID", "NAME", "PHONE NO.", "ADDRESS", "PINCODE"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)

    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)

    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('CID', text="CID", anchor=W)
    tree.heading('NAME', text="NAME", anchor=W)
    tree.heading('PHONE NO.', text="PHONE NO.", anchor=W)
    tree.heading('ADDRESS', text="ADDRESS", anchor=W)
    tree.heading('PINCODE', text="PINCODE", anchor=W)


    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#5', stretch=NO, minwidth=0, width=200)

    tree.pack()
    CusDisplayData()


def CusDisplayData():
    Database()
    cursor.execute("SELECT CID,CNAME,CPHONENO,CADDRESS,CPINCODE FROM `customer`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def CusSearch():
    tree.delete(*tree.get_children())
    Database()
    print(str(CSEARCH.get()))
    cursor.execute("SELECT * FROM customer WHERE CID = '%s'" % (str(CSEARCH.get())))
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def CusReset():
    tree.delete(*tree.get_children())
    CusDisplayData()
    CSEARCH.set("")


def CShowView():  # from cutomer's view product

    global cviewform
    cviewform = Toplevel(root)
    cviewform.title("Ukiyo Robstop")
    width = 1024
    height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    cviewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    cviewform.resizable(0, 0)
    CViewForm()
    
def insertin(): #add into invoice form
    global total
    db = sqlite3.connect("ukiyo.db")
    cursor = db.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS admin(AID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,AUSERNAME VARCHAR(20) UNIQUE,APASSWORD VARCHAR(50),ANAME VARCHAR(30),ADOB DATE,AEMAILID VARCHAR(50))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS customer(CID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,CUSERNAME VARCHAR(20) UNIQUE,CPASSWORD VARCHAR(50),CNAME VARCHAR(30),CADDRESS VARCHAR(30),CPHONENO INTEGER,CPINCODE INTEGER,AID INTEGER,FOREIGN KEY (AID) REFERENCES admin(AID))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS product(PID VARCHAR(10) PRIMARY KEY NOT NULL,PNAME VARCHAR(30),PPRICE VARCHAR(30),PCATEGORY VARCHAR(30),PSTOCK BOOLEAN,AID INTEGER,FOREIGN KEY (AID) REFERENCES admin(AID))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS purchases(CID INTEGER,PID VARCHAR(20),FOREIGN KEY (CID) REFERENCES product(CID)FOREIGN KEY (PID) REFERENCES customer(PID))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS invoice(IID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,PID VARCHAR(10),IQUANTITY INTEGER,IAMOUNT VARCHAR(30),CID INTEGER,FOREIGN KEY (CID) REFERENCES customer(CID),FOREIGN KEY (PID) REFERENCES product(PID))")

    data=cursor.execute("SELECT PPRICE FROM product WHERE PID = '%s'" %(Stextinpid.get()),)
#    total=IntVar()
#    total=0
    for i in data:
        inamount=int(i[0])
    sump=IntVar()
    sump= int(inamount) * int(inquantity.get())
    
    
    cursor.execute("INSERT INTO invoice(PID,IQUANTITY,IAMOUNT) values('%s','%d','%d')"%(Stextinpid.get(),int(inquantity.get()),int(sump)))
    Stextinpid.set("")
    inquantity.set("1")
    db.commit()

def InDisplayData():  # for INVOICE ONLY
    Database()
    cursor.execute("SELECT * FROM `invoice`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    
def InViewForm():
    global tree
#    a = "#B0BEC5"
    db = sqlite3.connect("ukiyo.db")
    cursor = db.cursor()

    inviewform.config(bg=a)
    TopInViewForm = Frame(inviewform, width=600, bd=1, relief=SOLID,bg=a)
    TopInViewForm.pack(side=TOP, fill=X)

    LeftInViewForm = Frame(inviewform, width=300,bg=a)
    LeftInViewForm.pack(side=LEFT, fill=Y)

    MidInViewForm = Frame(inviewform, width=800,bg=a)
    MidInViewForm.pack(side=RIGHT)

    lbl_text = Label(TopInViewForm, text="CART", font=('Bahnschrift SemiBold SemiConden', 18), width=600,bg=a)
    lbl_text.pack(fill=X)
    
    btn_delete = Button(LeftInViewForm,height="1", text="PLACE YOUR ORDER",font=('Bahnschrift SemiBold SemiConden', 12), command=CODform)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    
    btn_delete = Button(LeftInViewForm, text="Back",font=('Bahnschrift SemiBold SemiConden', 12), command=InBack)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    
    btn_delete = Button(LeftInViewForm, text="Exit",font=('Bahnschrift SemiBold SemiConden', 12), command=Exit)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    
    lbl_text = Label(LeftInViewForm, text="", font=('Bahnschrift SemiBold SemiConden', 18),bg=a)
    lbl_text.pack(fill=X)
    
    lbl_text = Label(LeftInViewForm, text="", font=('Bahnschrift SemiBold SemiConden', 18),bg=a)
    lbl_text.pack(fill=X)
    
    lbl_text = Label(LeftInViewForm, text="", font=('Bahnschrift SemiBold SemiConden', 18),bg=a)
    lbl_text.pack(fill=X)
    
    lbl_text = Label(LeftInViewForm, text="Total Amount : ", font=('Bahnschrift SemiBold SemiConden', 18),bg=a)
    lbl_text.pack(fill=X)
    
    tdata=cursor.execute("select sum(IAMOUNT) from `invoice`")
    for i in tdata:
        tot=i[0]
    
    lbl_tot = Label(LeftInViewForm, text= tot, font=('Bahnschrift SemiBold SemiConden', 18),bg=a)
    lbl_tot.pack(fill=X)
    
    
    scrollbarx = Scrollbar(MidInViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidInViewForm, orient=VERTICAL)

    tree = ttk.Treeview(MidInViewForm, columns=( "IID","PID", "IQUANTITY", "AMOUNT"), selectmode="extended",
                        height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)

    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)

    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('IID', text="IID", anchor=W)
    tree.heading('PID', text="PID", anchor=W)
    tree.heading('IQUANTITY', text="QUANTITY", anchor=W)
    tree.heading('AMOUNT', text="AMOUNT", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=200)
    db.commit()
    tree.pack()

    InDisplayData()
    

def InShowView():  # for invoice
    global inviewform

    inviewform = Toplevel(root)
    inviewform.title("Ukiyo Robstop")
    width = 1024
    height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    inviewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    inviewform.resizable(0, 0)
    InViewForm()

def CViewForm(): # from cutomer's view product

    global tree
    global QSEARCH
#    a="#B0BEC5"
    cusloginform.destroy()
    cviewform.config(bg=a)
    TopCViewForm = Frame(cviewform, width=600, bd=1, relief=SOLID,bg=a)
    TopCViewForm.pack(side=TOP, fill=X)

    LeftCViewForm = Frame(cviewform, width=600,bg=a)
    LeftCViewForm.pack(side=LEFT, fill=Y)

    MidCViewForm = Frame(cviewform, width=800,bg=a)
    MidCViewForm.pack(side=RIGHT)

    lbl_text = Label(TopCViewForm, text="PRODUCT", font=('Bahnschrift SemiBold SemiConden', 18), width=600,bg=a)
    lbl_text.pack(fill=X)

    lbl_txtsearch = Label(LeftCViewForm, text="Search", font=('Bahnschrift SemiBold SemiConden', 13),bg=a)
    lbl_txtsearch.pack(side=TOP, anchor=W)

    search = Entry(LeftCViewForm, textvariable=QSEARCH, font=('Bahnschrift SemiBold SemiConden', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)

    btn_search = Button(LeftCViewForm, text="Search", command=CSearch)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)



    btn_reset = Button(LeftCViewForm, text="Reset", command=CReset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_reset = Button(LeftCViewForm, text="Logout", command=CLogout)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    
    lbl_1 = Label(LeftCViewForm, text=" ", font=('Bahnschrift SemiBold SemiConden', 15),bg=a)
    lbl_1.pack(side=TOP, anchor=W)
    
    lbl_insertinto = Label(LeftCViewForm, text="  Enter PID of  ", font=('Calibri', 12),bg=a)
    lbl_insertinto.pack(side=TOP, anchor=W)
    
    lbl_insertinto = Label(LeftCViewForm, text="  the product to", font=('Calibri', 12),bg=a)
    lbl_insertinto.pack(side=TOP, anchor=W)
    
    lbl_insertinto = Label(LeftCViewForm, text="  add to cart.", font=('Calibri', 12),bg=a)
    lbl_insertinto.pack(side=TOP, anchor=W)
    
    insertinto = Entry(LeftCViewForm, font=('Bahnschrift SemiBold SemiConden', 15),textvariable=Stextinpid, width=10)
    insertinto.pack(side=TOP, padx=10, fill=X)
    
    lbl_insertinto = Label(LeftCViewForm, text="Quantity", font=('Calibri', 12),bg=a)
    lbl_insertinto.pack(side=TOP, anchor=W)
    
#    insertinto = Entry(LeftCViewForm, font=('Bahnschrift SemiBold SemiConden', 15), width=10)
#    insertinto.pack(side=TOP, padx=10, fill=X)
 
    

    spin = Spinbox(LeftCViewForm, from_=1, to=100,font=('Bahnschrift SemiBold SemiConden', 15),textvariable=inquantity, width=10) 
    spin.pack(side=TOP, padx=10, fill=X)
    
    btn_delete = Button(LeftCViewForm, text="Add to cart", command=insertin)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    
    btn_delete = Button(LeftCViewForm, text="View cart", command=InShowView)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    
    

    scrollbarx = Scrollbar(MidCViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidCViewForm, orient=VERTICAL)

    tree = ttk.Treeview(MidCViewForm, columns=("PID", "NAME", "PRICE", "CATEGORY", "STOCK"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)

    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)

    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('PID', text="PID", anchor=W)
    tree.heading('NAME', text="NAME", anchor=W)
    tree.heading('PRICE', text="PRICE", anchor=W)
    tree.heading('CATEGORY', text="CATEGORY", anchor=W)
    tree.heading('STOCK', text="STOCK", anchor=W)


    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#5', stretch=NO, minwidth=0, width=200)


    tree.pack()
    CDisplayData()


def CDisplayData():  # for CUSTOMER ONLY
    Database()
    cursor.execute("SELECT * FROM `product`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def CSearch():  # search for procus-customer-producttable
    tree.delete(*tree.get_children())
    Database()
    print(str(QSEARCH.get()))
    cursor.execute("SELECT * FROM product WHERE PCATEGORY ='%s'" % (str(QSEARCH.get())))
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    QSEARCH.set("")
    cursor.close()
    conn.close()


def CReset():  # reset for procus-customer-product table
    tree.delete(*tree.get_children())
    DisplayData()
    QSEARCH.set("")


def CLogout():  # for customer
    result = tkMessageBox.askquestion('Ukiyo Robstop', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':
        CID = ""
        cusloginform.destroy()
        cviewform.destroy()
        root.deiconify()
    if result == 'no':
        cviewform.deiconify()    


def CODform():
    global codform
    codform = Tk()
    codform.geometry("500x300") 
    codform.config(bg=a)
    codform.title("Ukiyo Robstop - INVOICE")
    inviewform.destroy()
    db = sqlite3.connect("ukiyo.db")
    cursor = db.cursor()
    tdata=cursor.execute("select sum(IAMOUNT) from `invoice`")
    for i in tdata:
        tot=i[0]

    l1=Label(codform,bg=a, text="By placing your order, you agree to Ukiyo Robstop.co.india Privacy Notice",fg=("white"),font=('Bahnschrift SemiBold',10))
    l1.place(x=0,y=0)
    l1=Label(codform,bg=a, text="of Use & Sale and Cookies & Internet Advertising.",fg=("white"),font=('Bahnschrift SemiBold',10))
    l1.place(x=0,y=19)
    l1=Label(codform,bg=a, text="Thank you, your order has been ",font=('Bahnschrift SemiBold',25))
    l1.place(x=0,y=50)
    l1=Label(codform,bg=a, text="placed.",font=('Bahnschrift SemiBold',25))
    l1.place(x=0,y=90)
    l2=Label(codform,bg=a, text="We have sent you an email for confirmation.",font=('Bahnschrift SemiBold',15))
    l2.place(x=0,y=140)
    l2=Label(codform,bg=a, text="Estimated delivery :",font=('Bahnschrift SemiBold',19))
    l2.place(x=20,y=200)
    l2=Label(codform,bg=a, text="Total Amount : Rs. ",font=('Bahnschrift SemiBold',19))
    l2.place(x=20,y=250)
    l2=Label(codform,bg=a, text="/-",font=('Bahnschrift SemiBold',19))
    l2.place(x=320,y=250)
    l2=Label(codform,bg=a, text="01 Jan. 2020",fg="green",font=('Bahnschrift SemiBold',19))
    l2.place(x=245,y=200)
    lbl_tot = Label(codform, text= tot, font=('Bahnschrift SemiBold SemiConden', 18),bg=a)
    lbl_tot.place(x=230,y=250)
  #  e1=Entry(codform,font=('Bahnschrift SemiBold', 19),textvariable=tot, width=6,bg=a)
  #  e1.place(x=230,y=250)
    cursor.execute("delete from `invoice`")
    db.commit()
    
def Logout():  # foradmin
    result = tkMessageBox.askquestion('Ukiyo Robstop', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':
        AID = ""
        loginform.destroy()
        procusform.destroy()
        root.deiconify()
    if result == 'no':
        procusform.deiconify()


def InBack():  ##for CUSTOMER - product- invoice - back

    cviewform.deiconify()
    cusloginform.destroy()
    inviewform.destroy()


def AdminProductBack():  # admin- #procus- #product- back

    procusform.deiconify()
    loginform.destroy()
    viewform.destroy()


def AdminCusBack():  # admin- #procus- #customer- back

    procusform.deiconify()
    loginform.destroy()
    cusviewform.destroy()


    

def Exit():
    result = tkMessageBox.askquestion('Ukiyo Robstop', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def Exit2():
    result = tkMessageBox.askquestion('Ukiyo Robstop', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()


def ShowHome():
    
    Home()




# ========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)


label1 = Label(root, text="WELCOME  TO  UKIYO  ROBSTOP", font=("Bahnschrift SemiBold SemiConden", 16))
label1.place(x=120, y=160)
button1 = Button(root, height="2", width="30", text="ADMIN", fg='black', relief=GROOVE, font=("arial", 12,),
                 command=ShowLoginForm)
button1.place(x=110, y=250)
button2 = Button(root, height="2", width="30", text="CUSTOMER", fg='black', relief=GROOVE, font=("arial", 12),
                 command=CusShowLoginForm)
button2.place(x=110, y=320)

# ========================================FRAME============================================
Title = Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)


if __name__ == '__main__':
    root.mainloop()
