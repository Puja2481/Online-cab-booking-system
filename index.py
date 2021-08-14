from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox as ms
import sqlite3


#Item4 = 0


# make database and users (if not exists already) table at programme start up
with sqlite3.connect('database.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEXT NOT NULL)')
db.commit()
db.close()

#main Class
class user:
    '''def __init__(self,master):
    	# Window 
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()'''

    #Login Function
    '''def login(self):
    	#Establish Connection
        with sqlite3.connect('database.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM login WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = "Welcome " + self.username.get()
            self.head.configure(fg="black")
            self.head.pack(fill=X)
            demo = travel(root)
            
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
    	#Establish Connection
        with sqlite3.connect('database.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM login WHERE username = ?')
        c.execute(find_user,[(self.username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Already Taken!')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account 
        insert = 'INSERT INTO login(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()'''

        #Frame Packing Methords
    '''def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'Login'
        self.logf.pack()'''
    '''def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()'''
        
    #Draw Widgets
    def widgets(self):
        '''self.head = Label(self.master,text = 'Login Panel',font = ('',30),pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10)
        Label(self.logf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login).grid()
        Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logf.pack()'''
        
        '''self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.new_user).grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.log).grid(row=2,column=1)'''
    

class travel:

    def __init__(self,root):
        self.root = root
        self.root.title("Cab Booking System")
        self.root.geometry(geometry) 
        self.root.configure(background='black')

        DateofOrder=StringVar()
        DateofOrder.set(time.strftime(" %d / %m / %Y "))
        Receipt_Ref=StringVar()
        PaidTax=StringVar()
        SubTotal=StringVar()
        TotalCost=StringVar()

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        journeyType=IntVar()
        carType=IntVar()
        
        varl1=StringVar()
        varl2=StringVar()
        varl3=StringVar()
        reset_counter=0


        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        Postcode=StringVar()
        Mobile=StringVar()
        Telephone=StringVar()
        Email=StringVar()

        CabTax=StringVar()
        Km=StringVar()
        Travel_Ins=StringVar()
        Luggage=StringVar()
        Receipt=StringVar()


        Mini=StringVar()
        Swift=StringVar()
        Dzire=StringVar()


        CabTax.set("0")
        Km.set("0")
        Travel_Ins.set("0")
        Luggage.set("0")


        Mini.set("0")
        Swift.set("0")
        Dzire.set("0")

       
        

    
    #==========================================Define Functiom==================================================

        def iExit():
            iExit= ms.askyesno("Prompt!","Do you want to exit?")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            CabTax.set("0")
            Km.set("0")
            Travel_Ins.set("0")
            Luggage.set("0")

            Mini.set("0")
            Swift.set("0")
            Dzire.set("0")

            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Mobile.set("")
            Telephone.set("")
            Email.set("")

            PaidTax.set("")
            SubTotal.set("")
            TotalCost.set("")
            self.txtReceipt1.delete("1.0",END)
            self.txtReceipt2.delete("1.0",END)
            
            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            journeyType.set(0)
            carType.set(0)
            varl1.set("0")
            varl2.set("0")
            varl3.set("0")

            self.cboPickup.current(0)
            self.cboDrop.current(0)
            self.cboPooling.current(0)

            self.txtCabTax.configure(state=DISABLED)
            self.txtKm.configure(state=DISABLED)
            self.txtTravel_Ins.configure(state=DISABLED)
            self.txtLuggage.configure(state=DISABLED)
        
            self.txtMini.configure(state=DISABLED)
            self.txtSwift.configure(state=DISABLED)
            self.txtDzire.configure(state=DISABLED)
            self.reset_counter=1

        def Receiptt():
            try:
                if reset_counter == 0 and Firstname.get()!="" and Surname.get()!="" and Address.get()!="" and Postcode.get()!="" and Mobile.get()!="" and Telephone.get()!="" and Email.get()!="":
                    self.txtReceipt1.delete("1.0",END)
                    self.txtReceipt2.delete("1.0",END)
                    x=random.randint(10853,500831)
                    randomRef = str(x)
                    Receipt_Ref.set(randomRef)

                    self.txtReceipt1.insert(END,"Receipt Ref:\n")
                    self.txtReceipt2.insert(END, Receipt_Ref.get() + "\n")
                    self.txtReceipt1.insert(END,'Date:\n')
                    self.txtReceipt2.insert(END, DateofOrder.get() + "\n")
                    self.txtReceipt1.insert(END,'Cab No:\n')
                    self.txtReceipt2.insert(END, 'CH ' + Receipt_Ref.get() + " BW\n")
                    self.txtReceipt1.insert(END,'Firstname:\n')
                    self.txtReceipt2.insert(END, Firstname.get() + "\n")
                    self.txtReceipt1.insert(END,'Surname:\n')
                    self.txtReceipt2.insert(END, Surname.get() + "\n")
                    self.txtReceipt1.insert(END,'Address:\n')
                    self.txtReceipt2.insert(END, Address.get() + "\n")
                    self.txtReceipt1.insert(END,'Postal Code:\n')
                    self.txtReceipt2.insert(END, Postcode.get() + "\n")
                    self.txtReceipt1.insert(END,'Telephone:\n')
                    self.txtReceipt2.insert(END, Telephone.get() + "\n")
                    self.txtReceipt1.insert(END,'Mobile:\n')
                    self.txtReceipt2.insert(END, Mobile.get() + "\n")
                    self.txtReceipt1.insert(END,'Email:\n')
                    self.txtReceipt2.insert(END, Email.get() + "\n")
                    self.txtReceipt1.insert(END,'From:\n')
                    self.txtReceipt2.insert(END, varl1.get() + "\n")
                    self.txtReceipt1.insert(END,'To:\n')
                    self.txtReceipt2.insert(END, varl2.get() + "\n")
                    self.txtReceipt1.insert(END,'Pooling:\n')
                    self.txtReceipt2.insert(END, varl3.get() + "\n")
                    self.txtReceipt1.insert(END,'Mini:\n')
                    self.txtReceipt2.insert(END, Mini.get() + "\n")
                    self.txtReceipt1.insert(END,'Swift:\n')
                    self.txtReceipt2.insert(END, Swift.get() + "\n")
                    self.txtReceipt1.insert(END,'Dzire:\n')
                    self.txtReceipt2.insert(END, Dzire.get() + "\n")
                    self.txtReceipt1.insert(END,'Paid:\n')
                    self.txtReceipt2.insert(END, PaidTax.get() + "\n")
                    self.txtReceipt1.insert(END,'SubTotal:\n')
                    self.txtReceipt2.insert(END, str(SubTotal.get()) + "\n")
                    self.txtReceipt1.insert(END,'Total Cost:\n')
                    self.txtReceipt2.insert(END, str(TotalCost.get()))
                    
                else:
                    self.txtReceipt1.delete("1.0",END)
                    self.txtReceipt2.delete("1.0",END)
                    self.txtReceipt1.insert(END,"\nNo Input")
            except:
                ms.showerror("Error", "Something went wrong..!")
            pass
                

        def Cab_Tax():
            global Item1
            try:
                if var1.get() == 1:
                    self.txtCabTax.configure(state = NORMAL)
                    Item1=float(50)
                    CabTax.set("Rs " + str(Item1))
                elif var1.get() == 0:
                    self.txtCabTax.configure(state=DISABLED)
                    CabTax.set("0")
                    Item1=0
            except:
                ms.showerror("Error", "Something went wrong..!")
            pass

        
        def Kilo():
            try:
                if var2.get() == 0:
                    self.txtKm.configure(state=DISABLED)
                    Km.set("0")
                elif var2.get() == 1 and varl1.get() != "" and varl2.get() != "":
                    self.txtKm.configure(state=NORMAL)
                    if varl1.get() == "Chandigarh":
                        switch ={"Mohali": 10,"Zirakpur": 8,"Kharar":6,"Chandigarh": 0}
                        Km.set(switch[varl2.get()])
                    elif varl1.get() == "Mohali":
                        switch ={"Mohali": 0,"Zirakpur": 2,"Kharar":5,"Chandigarh": 10}
                        Km.set(switch[varl2.get()])
                    elif varl1.get() == "Zirakpur":
                        switch ={"Mohali": 2,"Zirakpur": 0,"Kharar":3,"Chandigarh": 8}
                        Km.set(switch[varl2.get()])
                    elif varl1.get() == "Kharar":
                        switch ={"Mohali": 5,"Zirakpur": 3,"Kharar":0,"Chandigarh": 6}
                        Km.set(switch[varl2.get()])     
            except:
                ms.showerror("Error", "Something went wrong..!")
            pass   

        
        def Travelling():
            global Item3
            try:
                if var3.get() == 1:
                    self.txtTravel_Ins.configure(state = NORMAL)
                    Item3=float(10)
                    Travel_Ins.set("Rs " + str(Item3))
                elif var3.get() == 0:
                    self.txtTravel_Ins.configure(state = DISABLED)
                    Travel_Ins.set("0")
                    Item3=0
            except:
                ms.showerror("Error", "Something went wrong..!")
            pass

        
        def Lug():
            global Item4
            try:
                if (var4.get()==1):
                    self.txtLuggage.configure(state = NORMAL)
                    Item4=float(30)
                    Luggage.set("Rs "+ str(Item4))
                elif var4.get()== 0:
                    self.txtLuggage.configure(state = DISABLED)
                    Luggage.set("0")
                    Item4=0
            except:
                ms.showerror("Error", "Something went wrong..!")
            pass

        
        def selectCar():
            global Item5
            try:
                if carType.get() == 1:
                    self.txtSwift.configure(state = DISABLED)
                    Swift.set("0") 
                    self.txtDzire.configure(state = DISABLED)
                    Dzire.set("0")
                    self.txtMini.configure(state = NORMAL)
                    Item5 = float(8)
                    Mini.set("Rs "+ str(Item5))
                elif carType.get() == 2:
                    self.txtMini.configure(state =DISABLED)
                    Mini.set("0")
                    self.txtDzire.configure(state = DISABLED)
                    Dzire.set("0")
                    self.txtSwift.configure(state = NORMAL)
                    Item5 = float(15)
                    Swift.set("Rs "+ str(Item5))
                else:
                    self.txtMini.configure(state =DISABLED)
                    Mini.set("0")
                    self.txtSwift.configure(state = DISABLED)
                    Swift.set("0")
                    self.txtDzire.configure(state = NORMAL)
                    Item5 = float(22)
                    Dzire.set("Rs "+ str(Item5))
            except:
                ms.showerror("Error", "Something went wrong..!")
            pass
                
                       
        def Total_Paid():
            try:
                if ((var1.get() == 1 and var2.get() == 1 and var3.get() == 1 or var4.get() == 1) and carType.get() != 0 and journeyType.get() != 0 and (varl1.get() != "" and varl2.get() !="")):
                    if journeyType.get()==1:
                        Item2=Km.get()
                        Cost_of_fare = (Item1+(float(Item2)*Item5)+Item3+Item4)

                        Tax = "Rs " + str('%.2f'%((Cost_of_fare) *0.15))
                        ST = "Rs " + str('%.2f'%((Cost_of_fare)))
                        TT = "Rs " + str('%.2f'%(Cost_of_fare+((Cost_of_fare)*0.15)))
                    elif journeyType.get()==2:
                        Item2=Km.get()
                        Cost_of_fare = (Item1+(float(Item2)*Item5)*1.5+Item3+Item4)

                        Tax = "Rs " + str('%.2f'%((Cost_of_fare) *0.15))
                        ST = "Rs " + str('%.2f'%((Cost_of_fare)))
                        TT = "Rs " + str('%.2f'%(Cost_of_fare+((Cost_of_fare)*0.15)))
                    else:
                        Item2=Km.get()
                        Cost_of_fare = (Item1+(float(Item2)*Item5)*2+Item3+Item4)

                        Tax = "Rs " + str('%.2f'%((Cost_of_fare) *0.15))
                        ST = "Rs " + str('%.2f'%((Cost_of_fare)))
                        TT = "Rs " + str('%.2f'%(Cost_of_fare+((Cost_of_fare)*0.15)))

                    PaidTax.set(Tax)
                    SubTotal.set(ST)
                    TotalCost.set(TT)
                else:
                    w = ms.showwarning("Error !","Invalid Input\nPlease try again !!!")
            except:
                ms.showerror("Error !", "Invalid Input\nPlease try again !!!")
            pass

            

   #================================================mainframe========================================================================

        MainFrame=Frame(self.root)
        MainFrame.pack(fill=BOTH,expand=True)
        
        Tops = Frame(MainFrame, 
        bd=10, 
        width=1350,
        relief=RIDGE, 
        background = "#c4ffc4",
        highlightbackground = "#b9ffb9",
        highlightcolor = "#b9ffb9")

        Tops.pack(side=TOP,fill=BOTH)

        self.lblTitle=Label(Tops,
        font=("{MS Sans Serif} 9",50,'bold'),
        text="\t   Cab Booking System ", 
        background = "#c4ffc4",        
        highlightbackground = "#b9ffb9",
        highlightcolor = "#b9ffb9",
        relief = "flat"  )

        self.lblTitle.grid()

    #================================================customerframedetail=============================================================
        CustomerDetailsFrame=LabelFrame(MainFrame, 
        width=1350,
        height=500,
        bd=20, 
        pady=5, 
        relief=RIDGE,
        background = "#d5d5ea")
        
        CustomerDetailsFrame.pack(side=BOTTOM,fill=BOTH,expand=True)

        FrameDetails=Frame(CustomerDetailsFrame,
        width=880,
        height=400,bd=10, 
        relief=RIDGE,
        background = "#d5d5ea")
        
        FrameDetails.pack(side=LEFT,fill=BOTH,expand=True)

        CustomerName=LabelFrame(FrameDetails,
        width=150,
        height=250,
        bd=10, 
        font=("{MS Sans Serif} 9",12,'bold'),
        text="Customer Info", 
        relief=RIDGE,
        background = "#ffff9d")

        CustomerName.grid(row=0,column=0)

        TravelFrame = LabelFrame(FrameDetails,
        bd=10, 
        width=300,
        height=250, 
        font=("{MS Sans Serif} 9",12,'bold'),
        text="Booking Detail", 
        relief=RIDGE,
        background = "#ffff9d")

        TravelFrame.grid(row=0,column=1)

        Book_Frame=LabelFrame(FrameDetails,
        width=300,
        height=150,
        relief=FLAT)

        Book_Frame.grid(row=1,column=0)

        CostFrame = LabelFrame(FrameDetails,
        width=150,
        height=150,
        bd=5,
        relief=FLAT)
        CostFrame.grid(row=1,column=1)


    #===============================================recipt======================================================================
        Receipt_BottonFrame=LabelFrame(CustomerDetailsFrame,
        bd=10, 
        width=450,
        height=400, 
        relief=RIDGE, 
        background = "#ffff9d")

        Receipt_BottonFrame.pack(side=RIGHT,fill=BOTH,expand=True)

        ReceiptFrame=LabelFrame(Receipt_BottonFrame, 
        width=350,
        height=300, 
        font=("{MS Sans Serif} 9",12,'bold'),
        text="Receipt", 
        relief=RIDGE, 
        background = "#ffff9d")

        ReceiptFrame.grid(row=0,column=0)

        ButtonFrame=LabelFrame(Receipt_BottonFrame, 
        width=350,
        height=100, 
        relief=RIDGE, 
        background = "#ffff9d")

        ButtonFrame.grid(row=1,column=0)
    #=========================================================CustomerName====================================================

        self.lblFirstname=Label(CustomerName,
        font=("{MS Sans Serif} 9",14,'bold'),
        text="Firstname",
        bd=7,
        background = "#ffff9d")

        self.lblFirstname.grid(row=0,column=0,sticky=W)

        self.txtFirstname=Entry(CustomerName,
        font=("{MS Sans Serif} 9",14,'bold'),
        textvariable=Firstname,
        bd=7,
        insertwidth=2,
        justify=RIGHT)

        self.txtFirstname.grid(row=0,column=1)


        self.lblSurname=Label(CustomerName,
        font=("{MS Sans Serif} 9",14,'bold'),
        text="Surname",
        bd=7,
        background = "#ffff9d")

        self.lblSurname.grid(row=1,column=0,sticky=W)

        self.txtSurname=Entry(CustomerName,
        font=("{MS Sans Serif} 9",14,'bold'),
        textvariable=Surname,
        bd=7,
        insertwidth=2,
        justify=RIGHT)

        self.txtSurname.grid(row=1,column=1,sticky=W)


        self.lblAddress=Label(CustomerName,
        font=("{MS Sans Serif} 9",14,'bold'),
        text="Address",
        bd=7,
        background = "#ffff9d")

        self.lblAddress.grid(row=2,column=0,sticky=W)

        self.txtAddress=Entry(CustomerName,
        font=("{MS Sans Serif} 9",14,'bold'),
        textvariable=Address,
        bd=7,
        insertwidth=2,
        justify=RIGHT)

        self.txtAddress.grid(row=2,column=1)


        self.lblPostcode=Label(CustomerName,
        font=("{MS Sans Serif} 9",14,'bold'),
        text="Postcode",
        bd=7,
        background = "#ffff9d")

        self.lblPostcode.grid(row=3,column=0,sticky=W)
        
        self.txtPostcode=Entry(CustomerName,
        font=("{MS Sans Serif} 9",14,'bold'),
        textvariable=Postcode,
        bd=7,
        insertwidth=2,
        justify=RIGHT)

        self.txtPostcode.grid(row=3,column=1)


        self.lblTelephone=Label(CustomerName,
        font=("{MS Sans Serif} 9",14,'bold'),
        text="Telephone",
        bd=7,
        background = "#ffff9d")

        self.lblTelephone.grid(row=4,column=0,sticky=W)

        self.txtTelephone=Entry(CustomerName,
        font=("{MS Sans Serif} 9",14,'bold'),
        textvariable=Telephone,
        bd=7,
        insertwidth=2,
        justify=RIGHT)
        self.txtTelephone.grid(row=4,column=1)

        self.lblMobile=Label(CustomerName,
        font=("{MS Sans Serif} 9",14,'bold'),
        text="Mobile",
        bd=7,
        background = "#ffff9d")

        self.lblMobile.grid(row=5,column=0,sticky=W)

        self.txtMobile=Entry(CustomerName,
        font=("{MS Sans Serif} 9",14,'bold'),
        textvariable=Mobile,
        bd=7,
        insertwidth=2,
        justify=RIGHT)

        self.txtMobile.grid(row=5,column=1)

        self.lblEmail=Label(CustomerName,
        font=("{MS Sans Serif} 9",14,'bold'),
        text="Email",
        bd=7,
        background = "#ffff9d")
        self.lblEmail.grid(row=6,column=0,sticky=W)

        self.txtEmail=Entry(CustomerName,
        font=("{MS Sans Serif} 9",14,'bold'),
        textvariable=Email,
        bd=7,
        insertwidth=2,
        justify=RIGHT)

        self.txtEmail.grid(row=6,column=1)

 
    #===============================================Cab Information==============================================================
        self.lblPickup=Label(TravelFrame,
        font=("{MS Sans Serif} 9",14,'bold'),
        text="Pickup",
        bd=7,
        background = "#ffff9d")

        self.lblPickup.grid(row=0,column=0,sticky=W)

        self.cboPickup =ttk.Combobox(TravelFrame, 
        textvariable = varl1 , 
        state='readonly', 
        font=("{MS Sans Serif} 9",12,'bold'), 
        width=14)

        self.cboPickup['value']=('','Chandigarh','Kharar','Zirakpur','Mohali')
        self.cboPickup.current(0)
        self.cboPickup.grid(row=0,column=1)


        self.lblDrop=Label(TravelFrame,
        font=("{MS Sans Serif} 9",14,'bold'),
        text="Drop",
        bd=7,
        background = "#ffff9d")

        self.lblDrop.grid(row=1,column=0,sticky=W)

        self.cboDrop =ttk.Combobox(TravelFrame, 
        textvariable = varl2 , 
        state='readonly', 
        font=("{MS Sans Serif} 9",12,'bold'), 
        width=14)

        self.cboDrop['value']=('','Mohali','Zirakpur','Chandigarh','Kharar')
        self.cboDrop.current(0)
        self.cboDrop.grid(row=1,column=1)

        self.lblPooling=Label(TravelFrame,
        font=("{MS Sans Serif} 9",14,'bold'),
        text="Pooling",
        bd=7,
        background = "#ffff9d")

        self.lblPooling.grid(row=2,column=0,sticky=W)

        self.cboPooling =ttk.Combobox(TravelFrame, 
        textvariable = varl3 , 
        state='readonly', 
        font=("{MS Sans Serif} 9",12,'bold'), 
        width=14)

        self.cboPooling['value']=('','1','2','3','4')
        self.cboPooling.current(1)
        self.cboPooling.grid(row=2,column=1)

    #===============================================Cab Information==============================================================

        self.chkCabTax=Checkbutton(TravelFrame,
        text="Base Charge *",
        background = "#ffff9d",
        variable = var1, 
        onvalue=1, 
        offvalue=0,
        font=("{MS Sans Serif} 9",16,'bold'),
        command=Cab_Tax).grid(row=3, column=0, sticky=W)

        self.txtCabTax=Label(TravelFrame,
        font=("{MS Sans Serif} 9",14,'bold'),
        textvariable=CabTax,
        bd=6,
        width=18,
        bg="white",
        state= DISABLED,
        justify=RIGHT,
        relief=SUNKEN)

        self.txtCabTax.grid(row=3,column=1)


        self.chkKm=Checkbutton(TravelFrame,text="Distance(KMs) *",
        background = "#ffff9d",
        variable = var2, 
        onvalue=1, 
        offvalue=0,
        font=("{MS Sans Serif} 9",16,'bold'),
        command=Kilo).grid(row=4, column=0, sticky=W)

        self.txtKm=Label(TravelFrame,
        font=("{MS Sans Serif} 9",14,'bold'),
        textvariable=Km,
        bd=6,
        width=18,
        bg="white",
        state= DISABLED,
        justify=RIGHT,
        relief=SUNKEN,
        highlightthickness=0)

        self.txtKm.grid(row=4,column=1)

        self.chkTravel_Ins=Checkbutton(TravelFrame,
        text="Travelling Insurance *",
        background = "#ffff9d",
        variable = var3, 
        onvalue=1, 
        offvalue=0,
        font=("{MS Sans Serif} 9",16,'bold'),
        command=Travelling).grid(row=5, column=0, sticky=W)

        self.txtTravel_Ins=Label(TravelFrame,
        font=("{MS Sans Serif} 9",14,'bold'),
        textvariable=Travel_Ins,
        bd=6,
        width=18,
        bg="white",
        state= DISABLED,
        justify=RIGHT,
        relief=SUNKEN)

        self.txtTravel_Ins.grid(row=5,column=1)

      
        self.chkLuggage=Checkbutton(TravelFrame,
        text="Extra Luggage",
        background = "#ffff9d",
        variable = var4, 
        onvalue=1, 
        offvalue=0,
        font=("{MS Sans Serif} 9",16,'bold'),
        command=Lug).grid(row=6, column=0, sticky=W)

        self.txtLuggage=Label(TravelFrame,
        font=("{MS Sans Serif} 9",14,'bold'),
        textvariable=Luggage,
        bd=6,
        width=18,
        bg="white",
        state= DISABLED,
        justify=RIGHT,
        relief=SUNKEN)

        self.txtLuggage.grid(row=6,column=1)
    
    #=================================payment information ===========================================================================
         
        self.lblPaidTax=Label(CostFrame,
        font=("{MS Sans Serif} 9",14,'bold'),
        text="Paid Tax\t\t",
        bd=7)

        self.lblPaidTax.grid(row=0,column=2,sticky=W)

        self.txtPaidTax = Label(CostFrame,
        font=("{MS Sans Serif} 9",14,'bold'),
        textvariable=PaidTax,
        bd=7, 
        width=10, 
        justify=RIGHT,
        bg="white",
        relief=SUNKEN)

        self.txtPaidTax.grid(row=0,column=3)
            

        
        self.lblSubTotal=Label(CostFrame,
        font=("{MS Sans Serif} 9",14,'bold'),
        text="Sub Total",
        bd=7)

        self.lblSubTotal.grid(row=1,column=2,sticky=W)

        self.txtSubTotal = Label(CostFrame,
        font=("{MS Sans Serif} 9",14,'bold'),
        textvariable=SubTotal,
        bd=7, 
        width=10, 
        justify=RIGHT,
        bg="white",
        relief=SUNKEN)

        self.txtSubTotal.grid(row=1,column=3)



        self.lblTotalCost=Label(CostFrame,
        font=("{MS Sans Serif} 9",14,'bold'),
        text="Total Cost",
        bd=7)

        self.lblTotalCost.grid(row=2,column=2,sticky=W)

        self.txtTotalCost = Label(CostFrame,
        font=("{MS Sans Serif} 9",14,'bold'),
        textvariable=TotalCost,
        bd=7, width=10, 
        justify=RIGHT,
        bg="white",
        relief=SUNKEN)

        self.txtTotalCost.grid(row=2,column=3)

    #==========================================================Cabselect=======================================================================

        self.chkMini=Radiobutton(Book_Frame,
        text="Mini Cab",
        value=1,
        variable = carType,
        font=("{MS Sans Serif} 9",14,'bold'),
        command=selectCar).grid(row=0, column=0, sticky=W)

        self.txtMini = Label(Book_Frame,
        font=("{MS Sans Serif} 9",14,'bold'),
        width =7,
        textvariable=Mini,
        bd=5, 
        state= DISABLED, 
        justify=RIGHT,
        bg="white",
        relief=SUNKEN)

        self.txtMini.grid(row=0,column=1)
        

        self.chkSwiftd=Radiobutton(Book_Frame,
        text="Swift Cab",
        value=2,
        variable = carType,
        font=("{MS Sans Serif} 9",14,'bold'),
        command=selectCar).grid(row=1, column=0, sticky=W)

        self.txtSwift= Label(Book_Frame,
        font=("{MS Sans Serif} 9",14,'bold'),
        width =7,
        textvariable=Swift,
        bd=5, 
        state= DISABLED, 
        justify=RIGHT,
        bg="white",
        relief=SUNKEN)

        self.txtSwift.grid(row=1,column=1)
             
       
        self.chkDzire = Radiobutton(Book_Frame,
        text="Dzire Cab",
        value=3,
        variable = carType,
        font=("{MS Sans Serif} 9",14,'bold'),
        command=selectCar).grid(row=2, column=0)

        self.txtDzire = Label(Book_Frame,
        font=("{MS Sans Serif} 9",14,'bold'),
        width =7,
        textvariable=Dzire,
        bd=5, 
        state= DISABLED, 
        justify=RIGHT,
        bg="white",
        relief=SUNKEN)

        self.txtDzire.grid(row=2,column=1)

        self.chkSingle =Radiobutton(Book_Frame,
        text="Single",
        value=1,
        variable = journeyType,
        font=("{MS Sans Serif} 9",14,'bold')).grid(row=0, column=2, sticky=W)

        self.chkReturn =Radiobutton(Book_Frame,
        text="Return",
        value=2,
        variable = journeyType,
        font=("{MS Sans Serif} 9",14,'bold')).grid(row=1, column=2, sticky=W)

        self.chkSpecialsNeeds =Radiobutton(Book_Frame,
        text="SpecialNeeds",
        value=3,
        variable = journeyType,font=("{MS Sans Serif} 9",14,'bold')).grid(row=2, column=2, sticky=W)
    
    
    #=======================================Receipt====================================================================================

        self.txtReceipt1 = Text(ReceiptFrame,
        width = 22, 
        height = 21,
        font=("{MS Sans Serif} 9",10,'bold'),
        borderwidth=0)

        self.txtReceipt1.grid(row=0,column=0,columnspan=2)

        self.txtReceipt2 = Text(ReceiptFrame,
        width = 22, 
        height = 21,
        font=("{MS Sans Serif} 9",10,'bold'),
        borderwidth=0)

        self.txtReceipt2.grid(row=0,column=2,columnspan=2)


    #======================================Button========================================================================================
        
        self.btnTotal = Button(ButtonFrame,
        padx=18,
        bd=7,
        font=("{MS Sans Serif} 9",11,'bold'),
        width = 2,
        text='Total',
        command=Total_Paid).grid(row=0,column=0)

        self.btnReceipt = Button(ButtonFrame,
        padx=18,
        bd=7,
        font=("{MS Sans Serif} 9",11,'bold'),
        width = 2,
        text='Receipt',
        command=Receiptt).grid(row=0,column=1)

        self.btnReset = Button(ButtonFrame,
        padx=18,
        bd=7,
        font=("{MS Sans Serif} 9",11,'bold'),
        width = 2,
        text='Reset',
        command=Reset).grid(row=0,column=2)

        self.btnExit = Button(ButtonFrame,
        padx=18,bd=7,font=("{MS Sans Serif} 9",11,'bold'),
        width = 2,
        text='Exit', 
        command=iExit).grid(row=0,column=3)
        
    #====================================================================================================================================

        
if __name__=='__main__':
    

    root = Tk()

    #=========================================== Getting Screen Width ==================================================================

    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    geometry="%dx%d+%d+%d"%(w,h,0,0)
    
    root.geometry("500x300+320+200")
    root.title('Main Page')
    #demo = user(root)
    demo = travel(root)
    root.mainloop()
    

