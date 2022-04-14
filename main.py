



"what is instance "
import os

"the occurence of any thing like it can be object "
"or you can say an element"
"that how many times the element or object is repeated"



"self means it call  all the instances in ca class . by" \
"using self  "



"this is most important thing"

"init reversed method in python "
"which is concept of object oriented programming " \
"and it is constructor"













from tkinter import *


import math,random
from tkinter import messagebox




class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1430x8500+0+0")
        self.root.title("Billing software")
        bgcolor="red"
        title =Label(self.root,text="Billing Software ",bd=12,relief=GROOVE,bg=bgcolor,font=("times new roman ",30,"italic"),fg="white",pady=2).pack(fill=X)
        "#======================variable=====================#"

        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.Gell = IntVar()
        self.loshan = IntVar()

        "#====================cosmetics==========+#"

        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar= IntVar()
        self.tea = IntVar()

        "#====================Cold drinks==========+#"

        self.maza = IntVar()
        self.cock = IntVar()
        self.frooti= IntVar()
        self.thumspup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        "#=============total product price and Tax price===============#"
        self.cosmetics_price=StringVar()
        self.groccery_price = StringVar()
        self.colddrinks_price = StringVar()
        self.cosmetic_tax_price = StringVar()
        self.grocerry_tax = StringVar()
        self.Cold_drinks_tax = StringVar()

        "#=============customers==========++++#"
        self.c_name=StringVar()
        self.c_phone = StringVar()

        self.c_bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.c_bill_no.set(str(x))
        self.search_bill = StringVar()




        "++++++++++++++++++==========Customer Details================="
        F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("times new roman",20,"italic"),fg="gold",bg=bgcolor)
        F1.place(x=0,y=70,relwidth=1)
        cname_lbl=Label(F1,text="Customer Name",bg=bgcolor,fg="white",font=("times new roman",20,"italic")).grid(row=0,column=0,padx=20,pady=5)

        cname_txt=Entry(F1,width=20,textvariable=self.c_name,font=("arial 15"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphone_text = Label(F1, text="Phone_No", bg=bgcolor, fg="white",
                          font=("times new roman", 20, "italic")).grid(row=0, column=2, padx=20, pady=5)

        cphone_txt = Entry(F1, width=20,textvariable=self.c_phone, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=5)

        c_bill_text = Label(F1, text="Customer_Bill", bg=bgcolor, fg="white",
                            font=("times new roman", 20, "italic")).grid(row=0, column=4, padx=20, pady=5)

        c_bill_txt = Entry(F1, width=20,textvariable=self.c_bill_no, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=0, column=5, padx=10, pady=5)


        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bg=bgcolor,fg="blue",bd=10,font="arial 12 italic").grid(row=0,column=6,pady=10,padx=10)

        "+++++++++++++===========Cosmetics Frame++++====================="
        F2=LabelFrame(self.root,text="Cosmetics",bd=10,relief=GROOVE,font=("times new roman",20,"italic"),fg="gold",bg=bgcolor)
        F2.place(x=5,y=160,width=330,height=340)

        bath_soap_lbl = Label(F2, text="Bath Soap", bg=bgcolor, fg="white",
                          font=("times new roman", 20, "italic")).grid(row=0, column=0, padx=8, pady=5)

        bath_soap_txt = Entry(F2, width=20,textvariable=self.soap, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=0, column=1, padx=5, pady=5)

        face_cream_lbl = Label(F2, text="Face_cream", bg=bgcolor, fg="white",
                              font=("times new roman", 20, "italic")).grid(row=1, column=0, padx=8, pady=5)

        face_cream_txt = Entry(F2, width=20,textvariable=self.face_cream, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=1, column=1, padx=5,pady=5)

        facewash_lbl = Label(F2, text="Face_wash", bg=bgcolor, fg="white",
                               font=("times new roman", 20, "italic")).grid(row=2, column=0, padx=8, pady=5)

        face_wash_txt = Entry(F2, width=20,textvariable=self.face_wash, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=2, column=1, padx=5,
                                                                                          pady=5)

        hair_spray_lbl = Label(F2, text="hair_spray", bg=bgcolor, fg="white",
                               font=("times new roman", 20, "italic")).grid(row=3, column=0, padx=8, pady=5)

        hair_spray_txt = Entry(F2, width=20,textvariable=self.spray, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=3, column=1, padx=5,
                                                                                          pady=5)

        hair_gell_lbl = Label(F2, text="hair_gell", bg=bgcolor, fg="white",
                               font=("times new roman", 20, "italic")).grid(row=4, column=0, padx=8, pady=5)

        hair_gell_txt = Entry(F2, width=20,textvariable=self.Gell, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=4, column=1, padx=5,
                                                                                          pady=5)

        body_loshan_lbl = Label(F2, text="hair_loshan", bg=bgcolor, fg="white",
                               font=("times new roman", 20, "italic")).grid(row=5, column=0, padx=8, pady=5)

        body_loshantxt = Entry(F2, width=20,textvariable=self.loshan, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=5, column=1, padx=5,pady=5)




        "Costmetics 2nd box"

        F3 = LabelFrame(self.root, text="Groceries", bd=10, relief=GROOVE, font=("times new roman", 20, "italic"),
                        fg="gold", bg=bgcolor)
        F3.place(x=340, y=160, width=330, height=340)

        rice_lbl = Label(F3, text="Rice", bg=bgcolor, fg="white",
                                font=("times new roman", 20, "italic")).grid(row=0, column=0, padx=8, pady=5)

        rice_txt = Entry(F3, width=20,textvariable=self.rice, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=0, column=1, padx=5,
                                                                                          pady=5)
        food_oil_lbl = Label(F3, text="food_oil", bg=bgcolor, fg="white",
                                font=("times new roman", 20, "italic")).grid(row=1, column=0, padx=8, pady=5)

        food_oil_lbl = Entry(F3, width=20,textvariable=self.food_oil, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=1, column=1, padx=5,
                                                                                          pady=5)
        dal_lbl = Label(F3, text="Dal", bg=bgcolor, fg="white",
                                font=("times new roman", 20, "italic")).grid(row=2, column=0, padx=8, pady=5)

        dal_txt = Entry(F3, width=20,textvariable=self.daal, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=2, column=1, padx=5,
                                                                                          pady=5)
        wheat_lbl = Label(F3, text="wheat", bg=bgcolor, fg="white",
                                font=("times new roman", 20, "italic")).grid(row=3, column=0, padx=8, pady=5)

        wheat_txt = Entry(F3, width=20,textvariable=self.wheat, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=3, column=1, padx=5,
                                                                                          pady=5)
        sugar_lbl = Label(F3, text="Sugar", bg=bgcolor, fg="white",
                                font=("times new roman", 20, "italic")).grid(row=4, column=0, padx=8, pady=5)

        sugar_txt = Entry(F3, width=20,textvariable=self.sugar, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=4, column=1, padx=5,
                                                                                          pady=5)
        tea_lbl = Label(F3, text="tea", bg=bgcolor, fg="white",
                                font=("times new roman", 20, "italic")).grid(row=5, column=0, padx=8, pady=5)

        tea_txt = Entry(F3, width=20,textvariable=self.tea, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=5, column=1, padx=5,
                                                                                          pady=5)

        "cosmetics 3rd"
        F4 = LabelFrame(self.root, text="Cold Drinks", bd=10, relief=GROOVE, font=("times new roman", 20, "italic"),
                        fg="gold", bg=bgcolor)
        F4.place(x=675, y=160, width=330, height=340)

        maza_lbl = Label(F4, text="Maza", bg=bgcolor, fg="white",
                         font=("times new roman", 20, "italic")).grid(row=0, column=0, padx=8, pady=5)

        maza_txt = Entry(F4, width=20,textvariable=self.maza, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=0, column=1, padx=5,
                                                                                    pady=5)
        cock_lbl = Label(F4, text="Cock", bg=bgcolor, fg="white",
                             font=("times new roman", 20, "italic")).grid(row=1, column=0, padx=8, pady=5)

        cock_lbl = Entry(F4, width=20,textvariable=self.cock, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=1, column=1, padx=5,
                                                                                        pady=5)
        frooti_lbl = Label(F4, text="frooti", bg=bgcolor, fg="white",
                        font=("times new roman", 20, "italic")).grid(row=2, column=0, padx=8, pady=5)

        frooti_txt = Entry(F4, width=20,textvariable=self.frooti, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=2, column=1, padx=5,
                                                                                   pady=5)
        thumbs_up_lbl = Label(F4, text="Thumbs up", bg=bgcolor, fg="white",
                          font=("times new roman", 20, "italic")).grid(row=3, column=0, padx=8, pady=5)

        thumbs_up_txt = Entry(F4, width=20,textvariable=self.thumspup, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=3, column=1, padx=5,
                                                                                     pady=5)
        limca_lbl = Label(F4, text="limca", bg=bgcolor, fg="white",
                          font=("times new roman", 20, "italic")).grid(row=4, column=0, padx=8, pady=5)

        limca_txt = Entry(F4, width=20,textvariable=self.limca, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=4, column=1, padx=5,
                                                                                     pady=5)
        sprite_lbl = Label(F4, text="Sprite", bg=bgcolor, fg="white",
                        font=("times new roman", 20, "italic")).grid(row=5, column=0, padx=8, pady=5)

        sprite_txt = Entry(F4, width=20,textvariable=self.sprite, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=5, column=1, padx=5,
                                                                                   pady=5)
        "#==============bill area=============="
        F5 = LabelFrame(self.root, text="Bill_area", bd=10, relief=GROOVE )
        F5.place(x=1010, y=160, width=410, height=340)

        bill_title=Label(F5,text="Bill area",font="arial 15 italic",relief=GROOVE).pack(fill=X)


        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)




        "=================button frame==============="

        F6 = LabelFrame(self.root, text="Bill_menu", bd=10, relief=GROOVE, font=("times new roman", 20, "italic"),
                        fg="gold", bg=bgcolor)
        F6.place(x=5, y=505, width=1410, height=290)

        toal_cross_lbl = Label(F6, text="TOTAL COSMATICS", bg=bgcolor, fg="white",font=("times new roman", 20, "italic")).grid(row=0, column=0, padx=8, pady=5)

        toal_cross_txt = Entry(F6, width=20,textvariable=self.cosmetics_price, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=0, column=1, padx=5,
                                                                                      pady=7)
        toal_groccery_lbl = Label(F6, text="TOTAL groccery", bg=bgcolor, fg="white",
                               font=("times new roman", 20, "italic")).grid(row=1, column=0, padx=8, pady=5)

        toal_groccery_txt = Entry(F6, width=20,textvariable=self.groccery_price, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=1, column=1, padx=5,
                                                                                          pady=7)

        toal_coldrinks_lbl = Label(F6, text="TOTAL Cold drinks", bg=bgcolor, fg="white",
                                  font=("times new roman", 20, "italic")).grid(row=2, column=0, padx=8, pady=5)

        toal_coldrinks_txt = Entry(F6, width=20,textvariable=self.colddrinks_price, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=2, column=1, padx=5,
                                                                                             pady=7)


        "====tax department===="


        cosmatic_tax_lbl = Label(F6, text="COSMATICS Tax", bg=bgcolor, fg="white",
                               font=("times new roman", 20, "italic")).grid(row=0, column=2, padx=8, pady=5)

        cosmatic_tax_txt = Entry(F6, width=20,textvariable=self.cosmetic_tax_price, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=0, column=3, padx=5,
                                                                                          pady=7)
        groccery_tax_lbl = Label(F6, text="Groccery Tax", bg=bgcolor, fg="white",
                                  font=("times new roman", 20, "italic")).grid(row=1, column=2, padx=8, pady=5)

        groccery_tax_txt = Entry(F6, width=20,textvariable=self.grocerry_tax, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=1, column=3, padx=5,
                                                                                             pady=7)

        coldrinks_tax_lbl = Label(F6, text="Coldrinks Tax", bg=bgcolor, fg="white",
                                   font=("times new roman", 20, "italic")).grid(row=2, column=2, padx=8, pady=5)

        coldrinks_tax_txt = Entry(F6, width=20,textvariable=self.Cold_drinks_tax, font=("arial 15"), bd=7, relief=SUNKEN).grid(row=2, column=3, padx=5,
                                                                                              pady=7)

        BTN_F=Frame(F6,bd=7,relief=GROOVE)
        BTN_F.place(x=755,y=10,width=600,height=140)

        total_btnn=Button(BTN_F,text="Total",command=self.total,bd=5,bg="cadetblue",fg="black",pady=15).grid(row=0,column=0,padx=5,pady=5)
        Gbill_btnn = Button(BTN_F, text="Gbill",command=self.bill_area, bd=5, bg="cadetblue", fg="black", pady=15).grid(row=0, column=1,padx=5,pady=5)
        clear_btnn = Button(BTN_F, text="clear",command=self.cleardata, bd=5, bg="cadetblue", fg="black", pady=15).grid(row=0, column=2, padx=5, pady=5)
        exit_btnn = Button(BTN_F, text="exit",command=self.exitapp, bd=5, bg="cadetblue", fg="black", pady=15).grid(row=0, column=3, padx=5,
                                                                     pady=5)
        self.welcome_bill()

    def total(self):
        self.c_s_p=(self.soap.get()*40)
        self.c_fac_c=(self.face_cream.get() * 120)
        self.c_f_w=(self.face_wash.get() * 60)
        self.c_sp=(self.spray.get() * 180)
        self.c_g=(self.Gell.get() * 140)
        self.c_ls=(self.loshan.get() * 180)

        self.total_cosmetics_price=float(
             self.c_s_p+
             self.c_fac_c+
             self.c_f_w+
             self.c_sp+
             self.c_g+
             self.c_ls
             )
        self.cosmetics_price.set("Rs = "+str(self.total_cosmetics_price))
        self.c_tax=round((self.total_cosmetics_price*.005),2)
        self.cosmetic_tax_price.set("Rs = "+str(round((self.total_cosmetics_price*.005),2)))



        self.g_r=(self.rice.get() * 40)
        self.g_f=(self.food_oil.get() * 30)
        self.g_d=(self.daal.get() * 60)
        self.g_w=(self.wheat.get() * 20)
        self.g_s=(self.sugar.get() * 10)
        self.g_t=(self.tea.get() * 60)
        self.total_groccery_price=float(
            self.g_r+
            self.g_f+
            self.g_d+
            self.g_w+
            self.g_s+
            self.g_t
        )
        self.groccery_price.set("Rs = "+str(self.total_groccery_price))
        self.g_tax=round((self.total_groccery_price*.005),2)
        self.grocerry_tax.set("Rs = "+str(round((self.total_groccery_price*.005),2)))


        self.cd_m=(self.maza.get() * 10)
        self.cd_c=(self.cock.get() * 20)
        self.cd_f=(self.frooti.get() * 10)
        self.cd_ths=(self.thumspup.get() * 10)
        self.cd_l=(self.limca.get() * 10)
        self.cd_sp=(self.sprite.get() * 10)
        self.total_colddrinks_price = float(
             self.cd_m+
             self.cd_c+
             self.cd_f+
             self.cd_ths+
             self.cd_l+
             self.cd_sp
        )
        self.colddrinks_price.set("Rs = "+str(self.total_colddrinks_price))
        self.cd_tax=round((self.total_colddrinks_price*.005),2)
        self.Cold_drinks_tax.set("Rs = "+str(round((self.total_colddrinks_price*.005),2)))


        self.total_bill=(self.total_cosmetics_price+self.total_colddrinks_price+self.total_groccery_price
        +self.g_tax+self.g_tax+self.cd_tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWELCOME WEBCODE RETAIL BILL\n")
        self.txtarea.insert(END,f"\n BIll Number :{self.c_bill_no.get()} ")
        self.txtarea.insert(END,f"\n Customer Number : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n WELCOME WEBCODE RETAIL BILL :{self.c_phone.get()}")
        self.txtarea.insert(END,"\n=====================================================")
        self.txtarea.insert(END,"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END, "\n=====================================================")




    def bill_area(self):

        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("error","customer details are must")
        elif self.cosmetics_price.get()=="Rs = 0.0" and self.groccery_price.get()=="Rs = 0.0" and self.colddrinks_price.get()=="Rs = 0.0":
            messagebox.showerror("error","we dont any thing to make bill")
        else:



            a = (self.soap.get())
            list_of_cosmetics_names=["Bath soap","face_cream","face_wash","spray","gell","loshan"]
            list_of_groccery_names=["rice","foodOil","daal","wheat","sugar","tea"]
            list_of_coldrinks_names=["Maza","cock","frooti","Thumbs_up","limca","sprite"]
            list_of_cosmetics = [a, (self.face_cream.get()), (self.face_wash.get()), (self.spray.get()),
                             (self.Gell.get()), (self.loshan.get())]
            list_of_groccery=[(self.rice.get()),(self.food_oil.get()),(self.daal.get()),(self.wheat.get())
                          ,(self.sugar.get()),(self.tea.get())]
            list_of_colddrinks=[(self.maza.get()),(self.cock.get()),(self.frooti.get()),(self.thumspup.get()),(self.limca.get()),(self.sprite.get())]
            list_of_cosmetics_price=[(self.c_s_p),(self.c_fac_c),(self.c_f_w),(self.c_sp),(self.c_g),(self.c_ls)]
            list_of_grocerry_price=[(self.g_r),(self.g_f),(self.g_d),(self.g_w),(self.g_s),(self.g_t)]
            list_of_colddrinks_price=[(self.cd_m),(self.cd_c),(self.cd_f),(self.cd_ths),(self.cd_l),(self.cd_sp)]
            self.welcome_bill()
            for i in range(len(list_of_cosmetics)):
                a=list_of_cosmetics_names[i]
                b=list_of_cosmetics[i]
                c=list_of_cosmetics_price[i]
                a1=list_of_groccery_names[i]
                b1=list_of_groccery[i]
                c1=list_of_grocerry_price[i]
                a2=list_of_coldrinks_names[i]
                b2=list_of_colddrinks[i]
                c2=list_of_colddrinks_price[i]
                if list_of_cosmetics[i]!=0:
                    self.txtarea.insert(END, f"\n {a} \t\t {b}\t\t {c}")
                if list_of_groccery[i]!=0:
                    self.txtarea.insert(END, f"\n {a1} \t\t {b1}\t\t {c1}")
                if list_of_colddrinks[i]!=0:
                    self.txtarea.insert(END, f"\n {a2} \t\t {b2}\t\t {c2}")

            self.txtarea.insert(END, f"\n----------------------------------------------------")
            if self.cosmetic_tax_price.get()=="Rs = 0.0":
                pass
            else:
                self.txtarea.insert(END, f"\n Cosmetics Tax\t\t\t\t\t {self.cosmetic_tax_price.get()}")
            if self.grocerry_tax.get()=="Rs = 0.0":
                pass
            else:
                self.txtarea.insert(END, f"\n Grocarries Tax\t\t\t\t\t {self.grocerry_tax.get()}")
            if self.Cold_drinks_tax.get() == "Rs = 0.0":
                pass
            else:
                self.txtarea.insert(END, f"\n Cold drinks Tax\t\t\t\t\t {self.Cold_drinks_tax.get()}")

            a=round((self.total_bill),2)
            self.txtarea.insert(END, f"\n----------------------------------------------------")
            self.txtarea.insert(END,f"\n Total Bill : \t\t\t\t\t {a}")

            self.txtarea.insert(END, f"\n----------------------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("save bill","Do you want to save the bill?")
        if op>0:

            self.bill_data=self.txtarea.get("1.0",END)
            f1=open("bills/"+str(self.c_bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("saved",f"Bill no. {self.search_bill.get()} is saved Successfully")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==(self.c_bill_no.get()):
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present=="no":
            messagebox.showerror("Error", "Invalid no.")

    def cleardata(self):
        self.soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.spray.set(0)
        self.Gell.set(0)
        self.loshan.set(0)

        "#====================cosmetics==========+#"

        self.rice.set(0)
        self.food_oil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.tea.set(0)

        "#====================Cold drinks==========+#"

        self.maza.set(0)
        self.cock.set(0)
        self.frooti.set(0)
        self.thumspup.set(0)
        self.limca.set(0)
        self.sprite.set(0)

        "#=============total product price and Tax price===============#"
        self.cosmetics_price.set("")
        self.groccery_price.set("")
        self.colddrinks_price.set("")
        self.cosmetic_tax_price.set("")
        self.grocerry_tax.set("")
        self.Cold_drinks_tax.set("")

        "#=============customers==========++++#"
        self.c_name.set("")
        self.c_phone.set("")

        self.c_bill_no.set("")
        x = random.randint(1000, 9999)
        self.c_bill_no.set(x)
        self.search_bill.set("")
        self.welcome_bill()



    def exitapp(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()

        """if self.soap.get()!=0:
            self.txtarea.insert(End,f"\nBath soap\t\t\t {self.soap.get(a)}\t\t")"""

"""35.41"""        
"""50.06"""





root=Tk()
obj=Bill_App(root)
root.mainloop()