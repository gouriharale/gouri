

from tkinter import *
root = Tk()




root.title("CORE BANKING")




def submit():
    conn = psycopg2.connect(host="localhost",database="core_banking",user="gouri",password="2345")

    c = conn.cursor()

    #insert into table
    
    c.execute("INSERT INTO customer(c_ssn,phone_number,address,mail_id,account_no) " +"VALUES(%s,%s,%s,%s,%s)",(c_ssn.get(),phone_number.get(),address.get(),mail_id.get(),account_no.get()))
            
    c.execute("select *from customer")
    
    row=c.fetchall()
    print(row)
    
#create text boxes
c_ssn = Entry(root,width=30)
c_ssn.grid(row=1 , column =1)

phone_number = Entry(root,width=30)
phone_number.grid(row=2 , column =1)

address = Entry(root,width=30)
address.grid(row=3 , column =1)

mail_id = Entry(root,width=30)
mail_id.grid(row=4 , column =1)

account_no = Entry(root,width=30)
account_no.grid(row=5 , column =1)


#to create labels
c_ssn_label=Label(root,text="c_ssn")
c_ssn_label.grid(row=1,column=0)

phone_number_label=Label(root,text="phone number")
phone_number_label.grid(row=2,column=0)

address_label=Label(root,text="address")
address_label.grid(row=3,column=0)

mail_id_label=Label(root,text="mail id")
mail_id_label.grid(row=4,column=0)

account_no_label=Label(root,text="account_no")
account_no_label.grid(row=5,column=0)


#to create a submit button
submit_btn = Button(root,text="add an existing account",command=submit)
submit_btn.grid(row=6 , column=1 )

root.mainloop()
