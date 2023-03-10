# Harshavardhan P
# Sri Krish International School
# e-Nursery (Plant purchase)
# Computer Science Project


#######################################################################################################################################################################

# Importing all modules
from tkinter import *
import tkinter.messagebox
import datetime

#######################################################################################################################################################################

# Defining all functions
def close_window():
    Home.destroy()
    Login.destroy()
    Sign_up.destroy()
    Plant_Details.destroy()
    Plant_View.destroy()
    Final_View.destroy()
    Admin_Login.destroy()
    Admin_Prog.destroy()
    Update_Availability.destroy()
    Add_Plant.destroy()
    Rem_Plant.destroy()
    Orders_Page.destroy()
    Order_Display.destroy()

def swap(page):
    try:
        Home.withdraw()
        Login.withdraw()
        Sign_up.withdraw()
        Plant_Details.withdraw()
        Plant_View.withdraw()
        Final_View.withdraw()
        Admin_Login.withdraw()
        Admin_Prog.withdraw()
        Update_Availability.withdraw()
        Add_Plant.withdraw()
        Rem_Plant.withdraw()
        Orders_Page.withdraw()
        Order_Display.withdraw()
    except:
        pass
    if page=='Home':
        Home.deiconify()
    elif page=='Login':
        Password_.delete('1.0','end')
        Login.deiconify()
    elif page=='Signup':
        UsernameT.delete('1.0','end')
        PasswordT.delete('1.0','end')
        ContactT.delete('1.0','end')
        EmailT.delete('1.0','end')
        AddressT1.delete('1.0','end')
        AddressT2.delete('1.0','end')
        AddressT3.delete('1.0','end')
        PincodeT.delete('1.0','end')
        Sign_up.deiconify()
    elif page=='Plant Details':
        Plant_Details.deiconify()
    elif page=='Plant View':
        Plant_View.deiconify()
    elif page=='Final View':
        Final_View.deiconify()
    elif page=='Admin Login':
        Admin_Login.deiconify()
        Admin_Pass.delete('1.0','end')
    elif page=='Admin Prog':
        Admin_Prog.deiconify()
    elif page=='Update Availability':
        Update_Availability.deiconify()
    elif page=='Add Plant':
        Serial_NoT.delete('1.0','end')
        Plant_Name.delete('1.0','end')
        Initial_Stock.delete('1.0','end')
        Price.delete('1.0','end')
        Scn_Name.delete('1.0','end')
        Desc.delete('1.0','end')
        Add_Plant.deiconify()
    elif page=='Remove Plant':
        Rem_Plant.deiconify()
    elif page=='Orders Page':
        Orders_Page.deiconify()
    elif page=='Order Display':
        Order_Display.deiconify()

def admin_login():
    password=Admin_Pass.get('1.0','end-1c')
    if password=='harsha1234':
        swap('Admin Prog')
    else:
        tkinter.messagebox.showinfo('Incorrect Password','''Password entered was incorrect.
Please verify and enter correct password.''')
    Admin_Pass.delete('1.0','end')

def login():
    file=open('Login Details.txt','r')
    login_details=file.readlines()
    Data=[]
    Username_list=[]
    i=0
    while i<len(login_details):
        line=[login_details[i],login_details[i+1]]
        Data.append(line)
        Username_list.append(login_details[i])
        i+=3
    file.close()
    username=Username_.get('1.0','end-1c')+'\n'
    password=Password_.get('1.0','end-1c')+'\n'
    if username in Username_list:
        pass_check=0
        for i in Data:
            if i[0]==username and i[1]==password:
                swap('Plant Details')
                pass_check=1
                Username_.delete('1.0','end')
                Password_.delete('1.0','end')
                login2(username,password)
                break
            elif i[0]==username and i[1]!=password:
                continue
        if pass_check==0:
            tkinter.messagebox.showinfo('Incorrect Password','''Password entered was incorrect.
Please verify and enter correct password.''')
            Password_.delete('1.0','end')
    else:
        tkinter.messagebox.showinfo('Username Error','''Username not found in system.
Please verify and re-enter or if not registered
please Register''')

def login2(username,password):
    file=open('Customer Details.txt','r')
    data=file.readlines()
    i=0
    while i<len(data):
        if data[i]==username and data[i+1]==password:
            Contact=data[i+2]
        i+=9
    name.set(username[:-1])
    contact.set(Contact[:-1])

def checkS():
    global value1
    value1+=1
    value1%=2

def register_phase1():
    global value1
    if value1==0:
        tkinter.messagebox.showinfo('Confirmation','Please press the "Confirm" check button to Confirm your registration.')
    elif value1==1:
        Username1=UsernameT.get('1.0','end-1c')
        Password1=PasswordT.get('1.0','end-1c')
        Contact1=ContactT.get('1.0','end-1c')
        Email1=EmailT.get('1.0','end-1c')
        Address1=AddressT1.get('1.0','end-1c')
        Address2=AddressT2.get('1.0','end-1c')
        Address3=AddressT3.get('1.0','end-1c')
        Pincode1=PincodeT.get('1.0','end-1c')
        Reg_List=[Username1,Password1,Contact1,Email1,Address1,Address2,Address3,Pincode1]
        default=['Username','Password','Contact','Email Id','Address','Address','Address','Pincode']
        t=0
        for i in range(len(Reg_List)):
            if len(Reg_List[i])==0:
                tkinter.messagebox.showinfo('Registration Error',default[i]+' is not filled.')
                t=1
                break
            if i==2 or i==7:
                try:
                    a=int(Reg_List[i])
                except:
                    t=1
                    tkinter.messagebox.showinfo('Only Numeric','This slot needs a numeric velue.')
                    if i==2:
                        ContactT.delete('1.0','end')
                    if i==7:
                        PincodeT.delete('1.0','end')
                        break
        file=open('Login Details.txt.','r')
        if t==0:
            data=file.readlines()
            Details_List=[]
            Username_List=[]
            i=0
            m=0
            Username1+='\n'
            Password1+='\n'
            file.close()
            while i<len(data):
                Details_List.append([data[i],data[i+1]])
                Username_List.append(data[i])
                i+=3
            if Username1 in Username_List:
                for i in Details_List:
                    if i[0]==Username1:
                        if i[1]==Password1:
                            PasswordT.delete('1.0','end')
                            tkinter.messagebox.showinfo('Change Details','''The username and password are already taken.
Pls choose a different username or password.''')
                            break
                        else:
                            m=1
                    else:
                        continue
            else:
                m=1
            if m==1:
                register_phase2()

def register_phase2():
    file1=open('Login Details.txt','a')
    file1.write(UsernameT.get('1.0','end-1c'))
    file1.write('\n')
    file1.write(PasswordT.get('1.0','end-1c'))
    file1.write('\n \n')
    file1.close()
    file2=open('Customer Details.txt','a')
    file2.write(UsernameT.get('1.0','end-1c')+'\n')
    file2.write(PasswordT.get('1.0','end-1c')+'\n')
    file2.write(ContactT.get('1.0','end-1c')+'\n')
    file2.write(EmailT.get('1.0','end-1c')+'\n')
    file2.write(AddressT1.get('1.0','end-1c')+'\n')
    file2.write(AddressT2.get('1.0','end-1c')+'\n')
    file2.write(AddressT3.get('1.0','end-1c')+'\n')
    file2.write(PincodeT.get('1.0','end-1c')+'\n')
    file2.write('\n')
    file2.close()
    tkinter.messagebox.showinfo('Registration Succesful','''You have been successfully registered
to Green Stop. Login to purchase.''')
    swap('Home')

tree_2=0
flower_2=0
edible_2=0

def select(event):
    S=(Plant_List.curselection())[0]
    line=Plant_List.get(S)
    view_set(line[:3])
    swap('Plant View')

def search1():
    global tree_2
    global flower_2
    global edible_2
    if tree_2==0:
        T='N'
    else:
        T='Y'
    if flower_2==0:
        F='N'
    else:
        F='Y'
    if edible_2==0:
        E='N'
    else:
        E='Y'
    file=open('Plant Details.txt','r')
    data=file.readlines()
    file.close()
    check_list=[]
    for i in range(0,len(data)-1,10):
        d=data[i+5][:-1]
        e=data[i+6][:-1]
        f=data[i+7][:-1]
        sub_check=[d,e,f]
        if sub_check==[T,F,E]:
            check_list.extend([data[i],data[i+1],data[i+4]])
        else:
            continue
    search2(check_list)

def search2(check_list):
    search_element=SearchT.get('1.0','end-1c')
    display=[]
    for i in check_list:
        if search_element in i:
            display.append(i)
        else:
            continue
    display_set=[]
    file=open('Plant Details.txt','r')
    data=file.readlines()
    for i in range(0,len(data),10):
        sub=data[i:i+9]
        for j in display:
            if j in sub:
                display_set.append(sub[0][:3])
                break
            else:
                continue
    Plant_List.delete(0,END)
    for i in display_set:
        for j in range(0,len(data),10):
            if data[j][:-1]==i:
                a=data[j][:-1]
                b=data[j+1][:-1]
                c=data[j+4][:-1]
                line=a+(chr(32)*4)+b+(chr(32)*(18-len(b)))+c
                Plant_List.insert(END,line)
                break
            else:
                continue
    file.close()

def view_set(SNo):
    file=open('Plant Details.txt','r')
    data=file.readlines()
    for i in range(0,len(data),10):
        if data[i]==(SNo+'\n'):
            view_details=data[i:i+9]
        else:
            continue
    plant_name.set(view_details[1][:-1])
    botan_name.set(view_details[4][:-1])
    price.set('Rs.'+view_details[3][:-1])
    stock.set(view_details[2][:-1])
    if view_details[5][:-1]=='Y':
        treeVL.set('Tree/Big plant')
    else:
        treeVL.set('Short plant')
    if view_details[6][:-1]=='Y':
        flowerVL.set('Flowering plant')
    else:
        flowerVL.set('Non-Flowering plant')
    if view_details[7][:-1]=='Y':
        edibleVL.set('Edible (fruits/veges)')
    else:
        edibleVL.set('Non Edible')
    d=''
    t=view_details[8][:-1]
    while True:
        if len(t)>50:
            for j in range(50,0,-1):
                if t[j]==chr(32):
                    break
                else:
                    continue
            a=t[:j]
            t=t[j+1:]
            d+=(a+'\n')
        else:
            d+=t
            break
    descVL.set(d)
    file.close()

def add_cart():
    plant_temp=plant_name.get()
    file=open('Plant Details.txt','r')
    data=file.readlines()
    file.close()
    for i in range(1,len(data),10):
        if data[i]==(plant_temp+'\n'):
            j=data[i-1][:-1]
            break
        else:
            continue
    no=No_VT.get('1.0','end-1c')
    if no in '   ':
        pass
    else:
        k=0
        not_present=0
        while True:
            if Cart_List.get(k) in '      ':
                k+=1
                break
            elif Cart_List.get(k)[:3]==j:
                not_present=1
                a=Cart_List.get(k)
                Cart_List.delete(k)
                line=a[:39]+no
                Cart_List.insert(k,line)
                break
            else:
                k+=1
                continue
        if not_present==0:
            line=j+(chr(32)*8)+plant_temp+((28-len(plant_temp))*chr(32))+no
            Cart_List.insert(END,line)
            No_VT.delete('1.0','end')
        swap('Final View')

global tree_1
global flower_1
global edible_1
tree_1=0
flower_1=0
edible_1=0
confirm_1=0

def tree1():
    global tree_1
    tree_1+=1
    tree_1%=2

def flower1():
    global flower_1
    flower_1+=1
    flower_1%=2

def edible1():
    global edible_1
    edible_1+=1
    edible_1%=2

def confirm():
    global confirm_1
    confirm_1+=1
    confirm_1%=2

def add_phase1():
    global confirm_1
    if confirm_1==0:
        tkinter.messagebox.showinfo('Confirm Plant Addition','''Please confirm the addition of the plant by
by pressing the "Confirm" box.''')
    else:
        Serial1=Serial_NoT.get('1.0','end-1c')
        Name1=Plant_Name.get('1.0','end-1c')
        Initial1=Initial_Stock.get('1.0','end-1c')
        Price1=Price.get('1.0','end-1c')
        Botan1=Scn_Name.get('1.0','end-1c')
        Desc1=Desc.get('1.0','end-1c')
        Plant_Add_List=[Serial1,Name1,Initial1,Price1,Botan1,Desc1]
        default=['Serial No','Plant Name','Initial Stock','Price','Botanical Name','Description']
        t=1
        for i in range(len(Plant_Add_List)):
            if len(Plant_Add_List[i])==0:
                t=0
                tkinter.messagebox.showinfo('Registration Error',default[i]+' is not filled.')
                break
        if t==1:
            try:
                a=int(Serial1)
                b=int(Initial1)
                c=int(Price1)
            except:
                t=0
                tkinter.messagebox.showinfo('Numeric Value','Serial No,Initial Stock and Price fields take only numeric value.')
        if t==1:
            file=open('Plant Details.txt','r')
            data=file.readlines()
            file.close()
            m=0
            n=0
            while m<len(data):
                if data[m]==(Serial1+'\n'):
                    tkinter.messagebox.showinfo('Serial No. Error','''The Serial is already assigned to
a different plant. Please change''')
                    Serial_No.delete('1.0','end')
                else:
                    if data[m+1]==(Name1+'\n'):
                        tkinter.messagebox.showinfo('Plant Name Error','This plant already exists in records (Plant Name).')
                        Plant_Name.delete('1.0','end')
                    else:
                        if data[m+2]==(Botan1+'\n'):
                            tkinter.messagebox.showinfo('Botanical Name Error','This plant already exists in records (Botanical Name).')
                            Scn_Name.delete('1.0','end')
                        else:
                            n=1
                m+=10
            if n==1:
                add_phase2()

def add_phase2():
    global tree_1
    global flower_1
    global edible_1
    Serial1=Serial_NoT.get('1.0','end-1c')
    Name1=Plant_Name.get('1.0','end-1c')
    Initial1=Initial_Stock.get('1.0','end-1c')
    Price1=Price.get('1.0','end-1c')
    Botan1=Scn_Name.get('1.0','end-1c')
    Desc1=Desc.get('1.0','end-1c')
    if tree_1==1:
        Tree1='Y'
    else:
        Tree1='N'
    if flower_1==1:
        Flower1='Y'
    else:
        Flower1='N'
    if edible_1==1:
        Edible1='Y'
    else:
        Edible1='N'
    Desc1=Desc.get('1.0','end-1c')
    file=open('Plant Details.txt','a')
    file.write(Serial1+'\n')
    file.write(Name1+'\n')
    file.write(Initial1+'\n')
    file.write(Price1+'\n')
    file.write(Botan1+'\n')
    file.write(Tree1+'\n')
    file.write(Flower1+'\n')
    file.write(Edible1+'\n')
    file.write(Desc1+'\n')
    file.write('\n')
    file.close()
    tkinter.messagebox.showinfo('Successfully Added','The plant was successfully added to the records.')
    swap('Admin Prog')
    if tree_1==1:
        Tree_Check.deselect()
    if flower_1==1:
        Flower_Check.deselect()
    if edible_1==1:
        Edible_Check.deselect()

def logout():
    name.set('')
    contact.set('')
    Cart_List.delete(0,END)
    Plant_List.delete(0,END)
    SearchT.delete('1.0','end')
    Tree_S.deselect()
    Flower_S.deselect()
    Edible_S.deselect()
    global tree_2
    global flower_2
    global edible_2
    if tree_2==1:
        tree_2=0
    if flower_2==1:
        flower_2=0
    if edible_2==1:
        edible_2=0
    swap('Home')

def guest():
    name.set('Guest')
    contact.set('Not Applicable')
    swap('Plant Details')

def tree2():
    global tree_2
    tree_2+=1
    tree_2%=2

def flower2():
    global flower_2
    flower_2+=1
    flower_2%=2

def edible2():
    global edible_2
    edible_2+=1
    edible_2%=2

def increase():
    SNo = Serial_NoU.get('1.0','end-1c')
    Inc = IncreaseT.get('1.0','end-1c')
    file=open('Plant Details.txt','r')
    data=file.readlines()
    file.close()
    for i in range(0,len(data),10):
        if data[i]==(SNo+'\n'):
            break
        else:
            continue
    updated=[]
    for j in range(0,len(data),10):
        if j==i:
            updated.extend(data[i:i+2]+[str(int(data[i+2])+int(Inc))+'\n']+data[i+3:i+10])
        else:
            try:
                updated.extend(data[j:j+10])
            except:
                updated.extend(data[j:])
    file=open('Plant Details.txt','w')
    for k in updated:
        file.write(k)
    file.close()
    tkinter.messagebox.showinfo('Increased','The stock value has been increased.')
    swap('Admin Prog')
    Serial_NoU.delete('1.0','end')
    IncreaseT.delete('1.0','end')

def upd_stock():
    SNo = Serial_NoU.get('1.0','end-1c')
    Upd = Upd_StockT.get('1.0','end-1c')
    file=open('Plant Details.txt','r')
    data=file.readlines()
    file.close()
    for i in range(0,len(data),10):
        if data[i]==(SNo+'\n'):
            break
        else:
            continue
    updated=[]
    for j in range(0,len(data),10):
        if j==i:
            updated.extend(data[i:i+2]+[(Upd+'\n')]+data[i+3:i+10])
        else:
            try:
                updated.extend(data[j:j+10])
            except:
                updated.extend(data[j:])
    file=open('Plant Details.txt','w')
    for k in updated:
        file.write(k)
    file.close()
    tkinter.messagebox.showinfo('Updated','The stock value has been updated.')
    swap('Admin Prog')
    Serial_NoU.delete('1.0','end')
    Upd_StockT.delete('1.0','end')

def remove():
    global value
    if value==1:
        SNo=Serial_No.get('1.0','end-1c')
        file=open('Plant Details.txt','r')
        data=file.readlines()
        file.close()
        for i in range(0,len(data),10):
            if data[i]==(SNo+'\n'):
                break
            else:
                continue
        updated=[]
        for j in range(0,len(data),10):
            if j==i:
                continue
            else:
                try:
                    updated.extend(data[j:j+10])
                except:
                    updated.extend(data[j:])
        file=open('Plant Details.txt','w')
        for k in updated:
            file.write(k)
        file.close()
        tkinter.messagebox.showinfo('Removed','The details of the plant has been removed from the records.')
        swap('Admin Prog')
        Serial_No.delete('1.0','end')
        ConfirmB1.deselect()
    else:
        tkinter.messagebox.showinfo('Confirmation Required','Press the "Confirm" check button to confirm the removal.')

def buy():
    if name.get()=='Guest':
        tkinter.messagebox.showinfo('Guest User','''Guest users cannot place orders.
Please login before placing an order.''')
    else:
        a=Cart_List.get(0)
        if a in '      ':
            tkinter.messagebox.showinfo('Empty Cart','Sorry! Your cart is empty.')
        else:
            answer = tkinter.messagebox.askyesno('Are You Sure ??','''This action cannot be reversed. Please verify twice
before confirming your order. This purchase cannot
be edited either. Are you sure ??''')
            if answer==False:
                pass
            else:
                t=0
                data=[]
                while True:
                    if Cart_List.get(t) in '     ':
                        t+=1
                        break
                    else:
                        a=Cart_List.get(t)
                        data+=[a[:3]+a[38:]]
                        t+=1
                file=open('Orders.txt','a')
                file.write(name.get()+'\n')
                file.write(contact.get()+'\n')
                file.write('Pending'+'\n')
                z=datetime.datetime.now()
                file.write(str(z.year)+'-'+str(z.month)+'-'+str(z.day)+' '+str(z.hour)+':'+str(z.minute)+':'+str(z.second)+'.'+str(z.microsecond)+'\n')
                for i in data:
                    file.write(i[:3]+'\n')
                    file.write(i[4:]+'\n')
                file.write('\n')
                file.close()

global pending
global completed
pending=0
completed=0

def complete():
    global completed
    completed+=1
    completed%=2

def pend():
    global pending
    pending+=1
    pending%=2

def search_order():
    Order_List.delete(0,END)
    global pending
    global completed
    file=open('Orders.txt','r')
    data=file.readlines()
    file.close()
    pend_list=[]
    complete_list=[]
    for i in range(len(data)):
        A=[]
        if data[i][:-1]=='Pending':
            A=[data[i-2][:-1],data[i-1][:-1],'Pending',data[i+1][:-1]]
            j=2
            while True:
                try:
                    if data[i+j]!='\n':
                        A.append(data[i+j][:-1])
                        A.append(data[i+j+1][:-1])
                        j+=2
                    else:
                        j+=2
                        break
                except:
                    break
            pend_list.append(A)
    for i in range(len(data)):
        A=[]
        if data[i][:-1]=='Completed':
            A=[data[i-2][:-1],data[i-1][:-1],'Completed',data[i+1][:-1]]
            j=2
            while True:
                try:
                    if data[i+j]!='\n':
                        A.append(data[i+j][:-1])
                        A.append(data[i+j+1][:-1])
                        j+=2
                    else:
                        j+=2
                        break
                except:
                    break
            complete_list.append(A)
    Final_Orders_List=[]
    if pending==1:
        Final_Orders_List.extend(pend_list)
    if completed==1:
        Final_Orders_List.extend(complete_list)
    for i in Final_Orders_List:
        line=i[0]+(chr(32)*(20-len(i[0])))+i[1]+(chr(32)*3)+i[2]+(chr(32)*(12-len(i[2])))+i[3]
        Order_List.insert(END,line)

def select_order(event):
    OD_List.delete(0,END)
    line=Order_List.get(Order_List.curselection()[0])
    Cus_Name.set(line.split()[0])
    Cus_Contact.set(line.split()[1])
    Cus_Time.set(line.split()[3]+chr(32)+line.split()[4])
    status=line.split()[2]
    file1=open('Orders.txt','r')
    file2=open('Customer Details.txt','r')
    data1=file1.readlines()
    data2=file2.readlines()
    file1.close()
    file2.close()
    temp_list=[]
    for i in range(0,len(data1)):
        if data1[i][:-1]==Cus_Name.get():
            if data1[i+1][:-1]==Cus_Contact.get() and data1[i+3][:-1]==Cus_Time.get():
                j=4
                while True:
                    try:
                        if data1[i+j]=='\n':
                            j+=2
                            break
                        else:
                            temp_list.append([data1[i+j],data1[i+j+1]])
                            j+=2
                            continue
                    except:
                        break
                break
            else:
                continue
        else:
            continue
    p=0
    while p<(len(data2)-1):
        if data2[p][:-1]==Cus_Name.get() and data2[p+2][:-1]==Cus_Contact.get():
            Cus_Email.set(data2[p+3][:-1])
            Cus_Address.set(data2[p+4]+data2[p+5]+data2[p+6]+data2[p+7][:-1])
            file3=open('Plant Details.txt','r')
            data3=file3.readlines()
            file3.close()
            for i in range(0,len(data3)-1,10):
                m=0
                for j in temp_list:
                    if data3[i]==j[0]:
                        m=1
                        break
                    else:
                        continue
                if m==1:
                    OD_List.insert(END,data3[i][:-1]+(chr(32)*3)+data3[i+1][:-1]+(chr(32)*(20-len(data3[i+1][:-1])))+j[1][:-1])
            p+=9
        else:
            p+=9
            continue
    if status=='Pending':
        Comp_OD = Button(Order_Display,text='Done',font='Bahnshrift 15',height=1,width=8,command=lambda: order_done())
        Comp_OD.place(x=30,y=350)
    else:
        try:
            Comp_OD.destroy()
        except:
            pass
    swap('Order Display')

def stock_update(flag):
    orders_txt=open('Orders.txt','r')
    plants_txt=open('Plant Details.txt','r')
    data=orders_txt.readlines()
    orders_txt.close()
    p=flag+4
    stk_upd_list=[]
    while True:
        try:
            if data[p]!='\n':
                stk_upd_list.append(data[p][:-1]+chr(32)+data[p+1][:-1])
                p+=2
            else:
                p+=2
                break
        except:
            break
    data=plants_txt.readlines()
    plants_txt.close()
    i=0
    while i<len(stk_upd_list):
        s=0
        while s<len(data):
            if stk_upd_list[i][:3]==data[s][:-1]:
                data[s+2]=str(int(data[s+2][:-1])-int(stk_upd_list[i][4:]))+'\n'
            s+=10
        i+=1
    plants_txt=open('Plant Details.txt','w')
    plants_txt.write(data)
    plants_txt.close()

def order_done():
    answer=tkinter.messagebox.askyesno('Are You Sure ??','''This action cannot be reversed.
Are you sure the order is completed ??''')
    if answer==False:
        pass
    else:
        file=open('Orders.txt','r')
        data=file.readlines()
        file.close()
        a=Cus_Name.get()
        b=Cus_Contact.get()
        c=Cus_Time.get()
        p=0
        while p<(len(data)-1):
            if data[p][:-1]==a and data[p+1][:-1]==b and data[p+3][:-1]==c:
                flag=p
                p+=1
                break
            else:
                p+=1
                continue
        data[flag+2]='Completed'+'\n'
        file=open('Orders.txt','w')
        for i in data:
            file.write(i)
        stock_update(flag)
        tkinter.messagebox.showinfo('Completed Order',' The order has been recorded as Completed')
        swap('Orders Page')

#######################################################################################################################################################################

# Creating all windows

#1 Creating Home Page
Home = Tk()
Home.title('Home Page')
Home.geometry('600x400+383+184')
Home.resizable(0,0)
Home.configure(bg='White')
Home.protocol('WM_DELETE_WINDOW',close_window)

#2 Creating Login Page
Login = Tk()
Login.title('Login Page')
Login.geometry('600x400+383+184')
Login.resizable(0,0)
Login.configure(bg='White')
Login.protocol('WM_DELETE_WINDOW',close_window)
Login.withdraw()

#3 Creating Sign-up Page 
Sign_up = Tk()
Sign_up.title('Sign up Page')
Sign_up.geometry('600x520+383+124')
Sign_up.resizable(0,0)
Sign_up.configure(bg='White')
Sign_up.protocol('WM_DELETE_WINDOW',close_window)
Sign_up.withdraw()

#4 Creating Plant Details Page
Plant_Details = Tk()
Plant_Details.title('Plant Details Page')
Plant_Details.geometry('700x500+333+134')
Plant_Details.resizable(0,0)
Plant_Details.configure(bg='White')
Plant_Details.protocol('WM_DELETE_WINDOW',close_window)
Plant_Details.withdraw()

#5 Creating Plant View Page
Plant_View = Tk()
Plant_View.title('Plant View Page')
Plant_View.geometry('600x400+383+184')
Plant_View.resizable(0,0)
Plant_View.configure(bg='White')
Plant_View.protocol('WM_DELETE_WINDOW',close_window)
Plant_View.withdraw()

#6 Creating Final View Page (Wishlist and Purchase confirmation)
Final_View = Tk()
Final_View.title('Final View Page')
Final_View.geometry('700x500+333+134')
Final_View.resizable(0,0)
Final_View.configure(bg='White')
Final_View.protocol('WM_DELETE_WINDOW',close_window)
Final_View.withdraw()

#7 Creating Admin Login Page
Admin_Login = Tk()
Admin_Login.title('Admin Login Page')
Admin_Login.geometry('600x400+383+184')
Admin_Login.resizable(0,0)
Admin_Login.configure(bg='White')
Admin_Login.protocol('WM_DELETE_WINDOW',close_window)
Admin_Login.withdraw()

#8 Creating Admin Programs Page
Admin_Prog = Tk()
Admin_Prog.title('Admin Programs')
Admin_Prog.geometry('600x400+383+184')
Admin_Prog.resizable(0,0)
Admin_Prog.configure(bg='White')
Admin_Prog.protocol('WM_DELETE_WINDOW',close_window)
Admin_Prog.withdraw()

#9 Creating Update Availability Page
Update_Availability = Tk()
Update_Availability.title('Update Availability')
Update_Availability.geometry('600x400+383+184')
Update_Availability.resizable(0,0)
Update_Availability.configure(bg='White')
Update_Availability.protocol('WM_DELETE_WINDOW',close_window)
Update_Availability.withdraw()

#10 Creating Add New Plant Page
Add_Plant = Tk()
Add_Plant.title('Add Planet')
Add_Plant.geometry('600x520+383+124')
Add_Plant.resizable(0,0)
Add_Plant.configure(bg='White')
Add_Plant.protocol('WM_DELETE_WINDOW',close_window)
Add_Plant.withdraw()

#11 Creating Remove Plant Page
Rem_Plant = Tk()
Rem_Plant.title('Remove Plant')
Rem_Plant.geometry('600x400+383+184')
Rem_Plant.resizable(0,0)
Rem_Plant.configure(bg='White')
Rem_Plant.protocol('WM_DELETE_WINDOW',close_window)
Rem_Plant.withdraw()

#12 Creating Orders Page
Orders_Page = Tk()
Orders_Page.title('Orders Page')
Orders_Page.geometry('700x500+333+134')
Orders_Page.resizable(0,0)
Orders_Page.configure(bg='White')
Orders_Page.protocol('WM_DELETE_WINDOW',close_window)
Orders_Page.withdraw()

#13 Creating Order Display
Order_Display = Tk()
Order_Display.title('Order Display')
Order_Display.geometry('600x400+383+184')
Order_Display.resizable(0,0)
Order_Display.configure(bg='White')
Order_Display.protocol('WM_DELETE_WINDOW',close_window)
Order_Display.withdraw()

#######################################################################################################################################################################

# Elements of each window (Buttons and Labels)

#1 Home Page

Page_Heading1 = Label(Home,text='GREEN STOP',font='Elephant 40 bold')
Page_Heading1.configure(bg='White',fg='Green',)
Page_Heading1.place(x=84,y=28)

Page_subHeading1 = Label(Home,text='The Plant Store',font='Elephant 18')
Page_subHeading1.configure(bg='White',fg='Green')
Page_subHeading1.place(x=202,y=98)

User_Entry = Label(Home,text='  Enter as Customer   -',font='Bahnschrift 15',bg='White')
User_Entry.place(x=78,y=196)

Admin_Entry = Label(Home,text='  Enter as User            -',font='Bahnschrift 15',bg='White')
Admin_Entry.place(x=78,y=270)

Login_B = Button(Home,text='Login',font='Bahnschrift 15',command=lambda: swap('Login'),width=8,height=1)
Login_B.place(x=298,y=189)

Signup_B = Button(Home,text='Sign Up',font='Bahnschrift 15',command=lambda: swap('Signup'),width=8,height=1)
Signup_B.place(x=408,y=189)

Login_Admin_B = Button(Home,text='Admin Login',font='Bahnschrift 15',command=lambda: swap('Admin Login'),width=11,height=1)
Login_Admin_B.place(x=330,y=262)

Admin_Contact = Label(Home,text='For queries contact us @ 9094717606',font='Bahndhrift 13',bg='White',fg='Brown')
Admin_Contact.place(x=170,y=330)

Admin_Email = Label(Home,text='(or) email green.stop@gmail.com',font='Bahnshrift 13',bg='White',fg='Brown')
Admin_Email.place(x=188,y=350)

#2 Login Page

Page_Heading1 = Label(Login,text='USER  LOGIN',font='Elephant 28 bold')
Page_Heading1.configure(bg='White',fg='Green')
Page_Heading1.place(x=140,y=40)

Username = Label(Login,text='  Username  : ',font='Bahnschrift 15',bg='White')
Username.place(x=117,y=140)

Password = Label(Login,text='  Password   : ',font='Bahnschrift 15',bg='White')
Password.place(x=117,y=200)

Username_ = Text(Login,font='Bahnschrift 15',height=1,width=19,bd=2)
Username_.place(x=251,y=140)

Password_ = Text(Login,font='Bahnschrift 15',height=1,width=19,bd=2)
Password_.place(x=251,y=200)

Login_B2 = Button(Login,text='Login',font='Bahnschrift 15',command=lambda: login(),width=10,height=1)
Login_B2.place(x=240,y=260)

Signup_mess = Label(Login,text='First time? Register now (or) scroll as guest',font='Bahnschrift 12',bg='White')
Signup_mess.place(x=40,y=335)

Signup_B = Button(Login,text='Sign Up',font='Bahnschrift 12',command=lambda: swap('Signup'),width=7,height=1)
Signup_B.place(x=385,y=330)

Guest = Button(Login,text='Guest',font='Bahnschrift 12',command=lambda: guest(),width=7,height=1)
Guest.place(x=480,y=330)

#3 Sign Up Page

Page_Heading1 = Label(Sign_up,text='SIGN UP',font='Elephant 28 bold',bg='White',fg='Green',height=1)
Page_Heading1.place(x=200,y=10)

UsernameL = Label(Sign_up,text='Username   :',font='Bahnschrift 15',bg='White')
UsernameL.place(x=100,y=70)
UsernameT = Text(Sign_up,font='Bahnschrift 15',bg='White',width=20,height=1,bd=2)
UsernameT.place(x=260,y=70)

PasswordL = Label(Sign_up,text='Password    :',bg='White',font='Bahnschrift 15')
PasswordL.place(x=100,y=105)
PasswordT = Text(Sign_up,font='Bahnshrift 15',bg='White',width=20,height=1,bd=2)
PasswordT.place(x=260,y=105)

ContactL = Label(Sign_up,text='Contact       :',bg='White',font='Bahnshrift 15')
ContactL.place(x=100,y=140)
ContactT = Text(Sign_up,font='Bahnshrift 15',bg='White',width=20,height=1,bd=2)
ContactT.place(x=260,y=140)

EmailL = Label(Sign_up,text='Email id  :',bg='White',font='Bahnshrift 15',height=1)
EmailL.place(x=60,y=175)
EmailT = Text(Sign_up,font='Bahnshrift 15',bg='White',width=30,height=1,bd=2)
EmailT.place(x=205,y=175)

AddressL = Label(Sign_up,text='Address         :',font='Bahnshrift 15',height=1,bg='White')
AddressL.place(x=100,y=210)
AddressL1 = Label(Sign_up,text='Address line 1 : ',font='Bahnshrift 15',height=1,bg='White')
AddressL1.place(x=70,y=240)
AddressL2 = Label(Sign_up,text='Address line 2 : ',font='Bahnshrift 15',height=1,bg='White')
AddressL2.place(x=70,y=270)
AddressL3 = Label(Sign_up,text='Address line 3 : ',font='Bahnshrift 15',height=1,bg='White')
AddressL3.place(x=70,y=300)
AddressT1 = Text(Sign_up,font='Bahnshrift 15',height=1,width=28,bd=2)
AddressT1.place(x=215,y=240)
AddressT2 = Text(Sign_up,font='Bahnshrift 15',height=1,width=28,bd=2)
AddressT2.place(x=215,y=270)
AddressT3 = Text(Sign_up,font='Bahnshrift 15',height=1,width=28,bd=2)
AddressT3.place(x=215,y=300)

PincodeL = Label(Sign_up,text=' Pincode           :',font='Bahnshrift 15',height=1,bg='White')
PincodeL.place(x=100,y=340)
PincodeT = Text(Sign_up,font='Bahnshrift 15',bd=2,height=1,width=20)
PincodeT.place(x=260,y=340)

Confirm_Mess = Label(Sign_up,text='''Confirm that your registration is at
your own risk, and you will abide
by the Guidelines and Customer Terms
of Green Stop.''',font='Bahnshrift 11',bg='White')
Confirm_Mess.place(x=60,y=380)

value1=0

ConfirmB = Checkbutton(Sign_up,text='Confirm',font='Bahnshrift 13',command=lambda: checkS(),width=20,height=1,bg='White')
ConfirmB.place(x=100,y=460)

Register = Button(Sign_up,text='Register',font='Bahnshrift 15',height=1,width=10,command=lambda: register_phase1())
Register.place(x=380,y=390)

Back = Button(Sign_up,text='Back',font='Bahnshrift 15',height=1,width=5,command=lambda: swap('Home'))
Back.place(x=410,y=440)

#4 Plant Details Page

Page_Heading1 = Label(Plant_Details,text='PLANT  DETAILS',font='Elephant 28 bold')
Page_Heading1.configure(bg='White',fg='Green')
Page_Heading1.place(x=155,y=10)

SearchL = Label(Plant_Details,text='Search    :',font='Bahnshrift 15',height=1,bg='White')
SearchL.place(x=114,y=80)

SearchT = Text(Plant_Details,font='Bahnshrift 15',height=1,width=28,bd=2)
SearchT.place(x=219,y=80)

SearchB = Button(Plant_Details,text='Go',font='Bahnshrift 10 bold',width=3,command=lambda: search1())
SearchB.place(x=538,y=79)

Tree_S = Checkbutton(Plant_Details,text='Tree/Big Plant',font='Bahnshrift 12',command=lambda: tree2(),bg='White')
Tree_S.place(x=25,y=110)

Flower_S = Checkbutton(Plant_Details,text='Flowering Plant',font='Bahnshrift 12',command=lambda: flower2(),bg='White')
Flower_S.place(x=250,y=110)

Edible_S = Checkbutton(Plant_Details,text='Edible(Fruits/Vegetables)',font='Bahnshrift 12',command=lambda: edible2(),bg='White')
Edible_S.place(x=470,y=110)

Plant_Canvas = Canvas(Plant_Details,height=50,width=200)
Plant_Canvas.place(x=49,y=150)

Scroll = Scrollbar(Plant_Canvas)
Scroll.pack(side=RIGHT,fill=Y)

Plant_List = Listbox(Plant_Canvas,font='Courier 14',yscrollcommand=Scroll.set,height=11,width=53)
Plant_List.bind('<Double-1>',select)

Plant_List.pack(side=LEFT)
Scroll.config(command=Plant_List.yview)

CartB = Button(Plant_Details,text='Cart',font='Bahnshrift 15',height=1,width=10,command=lambda: swap('Final View'))
CartB.place(x=50,y=432)

Back = Button(Plant_Details,text='Log Out',font='Bahnshrift 13',height=1,width=10,command=lambda: logout())
Back.place(x=550,y=435)

#5 Plant View Page

Page_Heading1 = Label(Plant_View,text='PLANT VIEW',font='Elephant 28 bold')
Page_Heading1.configure(bg='White',fg='Green')
Page_Heading1.place(x=155,y=30)

plant_name = StringVar(Plant_View)
botan_name = StringVar(Plant_View)
price = StringVar(Plant_View)
stock = StringVar(Plant_View)

plant_name.set('Mango')
botan_name.set('Mangifera indica')
price.set('Rs.0')
stock.set('0')

Plant_NameVL = Label(Plant_View,text='Plant Name        :',font='Bahnshrift 14',height=1,width=15,bg='White')
Plant_NameVL.place(x=25,y=90)
Plant_NameVT = Label(Plant_View,textvariable=plant_name,font='Bhanshrift 14',height=1,width=20,anchor='w',bg='White')
Plant_NameVT.place(x=200,y=90)

Scn_NameVL = Label(Plant_View,text='Botanical Name :',font='Bahnshrift 14',height=1,width=15,bg='White')
Scn_NameVL.place(x=25,y=135)
Scn_NameVT = Label(Plant_View,textvariable=botan_name,font='Bahnshrift 14',height=1,width=20,anchor='w',bg='White')
Scn_NameVT.place(x=200,y=135)

PriceVL = Label(Plant_View,text='Price :',font='Bahnshrift 14',height=1,bg='White')
PriceVL.place(x=430,y=90)
PriceVT = Label(Plant_View,textvariable=price,font='Bahnshrift 14',height=1,anchor='w',width=7,bg='White')
PriceVT.place(x=490,y=90)

StockVL = Label(Plant_View,text='Stock :',font='Bahnshrift 14',height=1,bg='White')
StockVL.place(x=430,y=135)
StockVT = Label(Plant_View,textvariable=stock,font='Bahnshrift 14',height=1,anchor='w',width=7,bg='White')
StockVT.place(x=490,y=135)

treeVL = StringVar(Plant_View)
flowerVL = StringVar(Plant_View)
edibleVL = StringVar(Plant_View)

treeVL.set('Short Plant')
flowerVL.set('Non-flowering')
edibleVL.set('Non-edible plant')

TreeVL = Label(Plant_View,textvariable=treeVL,font='Bahnshrift 13',height=1,bg='White')
TreeVL.place(x=40,y=180)

FlowerVL = Label(Plant_View,textvariable=flowerVL,font='Bahnshrift 13',height=1,bg='White')
FlowerVL.place(x=240,y=180)

EdibleVL = Label(Plant_View,textvariable=edibleVL,font='Bahnshrift 13',height=1,bg='White')
EdibleVL.place(x=440,y=180)

descVL = StringVar(Plant_View)

DescVL = Label(Plant_View,textvariable=descVL,font='Bahnshrift 14',height=4,width=46)
DescVL.place(x=43,y=225)

No_VL = Label(Plant_View,text='No.    :',font='Bahnshrift 15',bg='White',height=1)
No_VL.place(x=53,y=345)
No_VT = Text(Plant_View,font='Bahnshrift 15',bg='White',height=1,width=6,bd=2)
No_VT.place(x=120,y=345)

Add_Cart = Button(Plant_View,text='Add To Cart',font='Bahnshrift 15',height=1,width=14,command=lambda: add_cart())
Add_Cart.place(x=235,y=338)

Back = Button(Plant_View,text='Back',font='Bahnshrift 14',height=1,width=10,command=lambda: swap('Plant Details'))
Back.place(x=447,y=338)

#6 Final View Page

Page_Heading1 = Label(Final_View,text='CART AND PURCHASE',font='Elephant 28 bold')
Page_Heading1.configure(bg='White',fg='Green')
Page_Heading1.place(x=100,y=20)

name = StringVar(Final_View)
name.set('')

UsernameFL = Label(Final_View,text='Name      :',font='Bahnshrift 15',height=1,bg='White')
UsernameFL.place(x=80,y=100)
UsernameFT = Label(Final_View,textvariable=name,font='Bahnshrift 15',height=1,width=40,anchor='w',bg='White')
UsernameFT.place(x=180,y=100)

contact = StringVar(Final_View)
contact.set('')

ContactFL = Label(Final_View,text='Contact   :',font='Bahnshrift 15',height=1,bg='White')
ContactFL.place(x=80,y=140)
ContactFT = Label(Final_View,textvariable=contact,font='Bahnshrift 15',height=1,width=40,anchor='w',bg='White')
ContactFT.place(x=180,y=140)

Cart_Canvas = Canvas(Final_View,height=20,width=200)
Cart_Canvas.place(x=49,y=190)

Scroll_C = Scrollbar(Cart_Canvas)
Scroll_C.pack(side=RIGHT,fill=Y)

Cart_List = Listbox(Cart_Canvas,font='Courier 15',yscrollcommand=Scroll.set,height=10,width=48)

Cart_List.pack(side=LEFT)
Scroll_C.config(command=Cart_List.yview)

Log_Out = Button(Final_View,text='Log Out',font='Bahnshrift 12',height=1,width=10,command=lambda: logout())
Log_Out.place(x=40,y=437)

Buy_Cart = Button(Final_View,text='Buy Cart',font='Bahnshrift 15',height=1,width=15,command=lambda: buy())
Buy_Cart.place(x=270,y=435)

Back = Button(Final_View,text='Back',font='Bahnshrift 12',height=1,width=10,command=lambda: swap('Plant Details'))
Back.place(x=558,y=437)

#7 Admin Login Page

Page_Heading1 = Label(Admin_Login,text='ADMIN  LOGIN',font='Elephant 28 bold')
Page_Heading1.configure(bg='White',fg='Green')
Page_Heading1.place(x=130,y=50)

Admin_PassL = Label(Admin_Login,text='Password  :',font='Bahnshrift 15',height=1,bg='White')
Admin_PassL.place(x=130,y=160)

Admin_Pass = Text(Admin_Login,font='Bahnshrift 15',bd=2,height=1,width=20)
Admin_Pass.place(x=250,y=160)

Enter = Button(Admin_Login,text='Login',font='Bahnshrift 15',height=1,width=10,command=lambda: admin_login())
Enter.place(x=245,y=220)

Back = Button(Admin_Login,text='Back',font='Bahnshrift 15',height=1,width=10,command=lambda: swap('Home'))
Back.place(x=245,y=280)

#8 Admin Program Page

Page_Heading1 = Label(Admin_Prog,text='ADMIN  PROGRAMS',font='Elephant 28 bold',height=2)
Page_Heading1.configure(bg='White',fg='Green')
Page_Heading1.place(x=70,y=23)

Upd_Avail = Button(Admin_Prog,text='Update Availability',font='Bahnshrift 15',height=1,width=20,command=lambda: swap('Update Availability'))
Upd_Avail.place(x=185,y=130)

New_Entry = Button(Admin_Prog,text='Add New Plant',font='Bahnshrift 15',height=1,width=20,command=lambda: swap('Add Plant'))
New_Entry.place(x=185,y=190)

Rem_Entry = Button(Admin_Prog,text='Remove Plant',font='Bahnshrift 15',height=1,width=20,command=lambda: swap('Remove Plant'))
Rem_Entry.place(x=185,y=250)

Orders = Button(Admin_Prog,text='Orders',font='Bahnshrift 15',height=1,width=20,command=lambda: swap('Orders Page'))
Orders.place(x=185,y=310)

Back = Button(Admin_Prog,text='Back',font='Bahnshrift 12',height=1,width=10,command=lambda: swap('Admin Login'))
Back.place(x=480,y=350)

#9 Update Availability Page

Page_Heading1 = Label(Update_Availability,text='UPDATE  AVAILABILITY',font='Elephant 28',height=2)
Page_Heading1.configure(bg='White',fg='Green')
Page_Heading1.place(x=30,y=25)

Serial_NoL = Label(Update_Availability,text='Serial No.  :',font='Bahnshrift 15',bg='White',height=1)
Serial_NoL.place(x=125,y=130)
Serial_NoU = Text(Update_Availability,font='Bahnshrift 15',height=1,width=20,bd=2)
Serial_NoU.place(x=240,y=130)

IncreaseL = Label(Update_Availability,text='Increase Stock By :',font='Bahnshrift 15',bg='White',height=1)
IncreaseL.place(x=140,y=190)
IncreaseT = Text(Update_Availability,font='Bahnshrift 15',height=1,width=10,bd=2)
IncreaseT.place(x=320,y=190)
IncreaseB = Button(Update_Availability,text='Increase',font='Bahnshrift 15',height=1,width=10,command=lambda: increase())
IncreaseB.place(x=260,y=230)

Upd_StockL = Label(Update_Availability,text='Update Stock To   :',font='Bahnshrift 15',bg='White',height=1)
Upd_StockL.place(x=140,y=290)
Upd_StockT = Text(Update_Availability,font='Bahnshrift 15',height=1,width=10,bd=2)
Upd_StockT.place(x=320,y=290)
Upd_StockB = Button(Update_Availability,text='Update',font='Bahnshrift 15',height=1,width=10,command=lambda: upd_stock())
Upd_StockB.place(x=260,y=330)

Back = Button(Update_Availability,text='Back',font='Bahnshrift 12',height=1,width=10,command=lambda: swap('Admin Prog'))
Back.place(x=480,y=350)

#10 Add New Plant Page

Page_Heading1 = Label(Add_Plant,text='ADD PLANT',font='Elephant 28',height=2,bg='White',fg='Green')
Page_Heading1.place(x=170,y=0)

Serial_NoL = Label(Add_Plant,text='Serial No.   :',font='Bahnshrift 15',bg='White',height=1)
Serial_NoL.place(x=125,y=85)
Serial_NoT = Text(Add_Plant,font='Bahnshrift 15',height=1,width=20,bd=2)
Serial_NoT.place(x=245,y=85)

Plant_NameL = Label(Add_Plant,text='Plant Name :',font='Bahnshrift 15',bg='White',height=1)
Plant_NameL.place(x=125,y=125)
Plant_Name = Text(Add_Plant,font='Bahnshrift 15',bd=2,height=1,width=20)
Plant_Name.place(x=245,y=125)

Initial_StockL = Label(Add_Plant,text='Initial Stock     :',font='Bahnshrift 15',bg='White',height=1)
Initial_StockL.place(x=165,y=165)
Initial_Stock = Text(Add_Plant,font='Bahnshrift 15',bd=2,height=1,width=10)
Initial_Stock.place(x=310,y=165)

PriceL = Label(Add_Plant,text='Price              :',font='Bahnshrift 15',bg='White',height=1)
PriceL.place(x=165,y=205)
Price = Text(Add_Plant,font='Bahnshrift 15',bd=2,height=1,width=10)
Price.place(x=310,y=205)

Scn_NameL = Label(Add_Plant,text='Botanical Name :',font='Bahnshrift 15',bg='White',height=1)
Scn_NameL.place(x=65,y=245)
Scn_Name = Text(Add_Plant,font='Bahnshrift 15',bd=2,height=1,width=28)
Scn_Name.place(x=225,y=245)

Tree_Check = Checkbutton(Add_Plant,text='Tree/Big Plant',font='Bahnshrift 15',width=19,bg='White',command=lambda: tree1())
Tree_Check.place(x=19,y=285)

Flower_Check = Checkbutton(Add_Plant,text='Flowering',font='Bahnshrift 15',width=15,bg='White',command=lambda: flower1())
Flower_Check.place(x=20,y=325)

Edible_Check = Checkbutton(Add_Plant,text='Edible(Fruit/Vegetable)',font='Bahnshrift 15',width=25,bg='White',command=lambda: edible1())
Edible_Check.place(x=23,y=365)

DescL = Label(Add_Plant,text='Description:',font='Bahnshrift 15',bg='White',height=1)
DescL.place(x=20,y=405)
Desc = Text(Add_Plant,font='Bahnshrift 15',bd=2,height=4,width=28)
Desc.place(x=130,y=405)

ConfirmAddL = Label(Add_Plant,text='''Are you sure the details of the plant
are correct and you want to add
it to the system ??''',font='Bahnshrift 12',bg='White')
ConfirmAddL.place(x=300,y=285)

ConfirmAdd = Checkbutton(Add_Plant,text='Confirm',font='Bahnshrift 15',width=15,height=1,bg='White',command=lambda: confirm())
ConfirmAdd.place(x=325,y=350)

Add = Button(Add_Plant,text='Add',font='Bahnshrift 16',height=1,width=9,command=lambda: add_phase1())
Add.place(x=464,y=408)

Back = Button(Add_Plant,text='Back',font='Bahnshrift 12',height=1,width=10,command=lambda: swap('Admin Prog'))
Back.place(x=470,y=470)

#11 Remove Plant Page

Page_Heading1 = Label(Rem_Plant,text='REMOVE PLANT',font='Elephant 28',height=2,bg='White',fg='Green')
Page_Heading1.place(x=113,y=25)

Serial_NoL = Label(Rem_Plant,text='Serial No.  :',font='Bahnshrift 15',bg='White',height=1)
Serial_NoL.place(x=125,y=140)
Serial_No = Text(Rem_Plant,font='Bahnshrift 15',height=1,width=20,bd=2)
Serial_No.place(x=240,y=140)

ConfirmL = Label(Rem_Plant,text='''Are you sure u want to remove this plant from the system ??
This action cannot be reversed by the system.''',font='Bahnshrift 13',bg='White')
ConfirmL.place(x=80,y=200)

value=0

def checkR1():
    global value
    value+=1
    value%=2

ConfirmB1 = Checkbutton(Rem_Plant,text='Confirm',font='Bahnshrift 15',command=lambda: checkR1(),width=20,height=1,bg='White')
ConfirmB1.place(x=175,y=260)

ConfirmB2 = Button(Rem_Plant,text='Remove',font='Bahnshrift 15',width=20,height=1,command=lambda: remove())
ConfirmB2.place(x=175,y=300)

Back = Button(Rem_Plant,text='Back',font='Bahnshrift 12',height=1,width=10,command=lambda: swap('Admin Prog'))
Back.place(x=480,y=350)

#12 Orders Page

Page_Heading1 = Label(Orders_Page,text='ORDERS',font='Elephant 28 bold',bg='White',fg='Green')
Page_Heading1.place(x=250,y=15)

SearchOL = Label(Orders_Page,text='Search    :',font='Bahnshrift 15',height=1,bg='White')
SearchOL.place(x=114,y=80)

SearchOT = Text(Orders_Page,font='Bahnshrift 15',height=1,width=28,bd=2)
SearchOT.place(x=219,y=80)

SearchOB = Button(Orders_Page,text='Go',font='Bahnshrift 10 bold',width=3,command=lambda: search_order())
SearchOB.place(x=538,y=79)

Pending = Checkbutton(Orders_Page,text='Pending',font='Bahnshrift 15',height=1,width=15,bg='White',command=lambda: pend())
Pending.place(x=130,y=115)

Completed = Checkbutton(Orders_Page,text='Completed',font='Bahnshrift 15',height=1,width=15,bg='White',command=lambda: complete())
Completed.place(x=380,y=115)

Orders_Canvas = Canvas(Orders_Page,height=50,width=200)
Orders_Canvas.place(x=49,y=155)

Scroll_O = Scrollbar(Orders_Canvas)
Scroll_O.pack(side=RIGHT,fill=Y)

Order_List = Listbox(Orders_Canvas,font='Courier 11',yscrollcommand=Scroll_O.set,height=15,width=65)
Order_List.bind('<Double-1>',select_order)

Order_List.pack(side=LEFT)
Scroll_O.config(command=Order_List.yview)

Back = Button(Orders_Page,text='Back',font='Bahnshrift 12',height=1,width=10,command=lambda: swap('Admin Prog'))
Back.place(x=558,y=437)

#13 Order Display

Page_Heading1 = Label(Order_Display,text='ORDER DISPLAY',font='Elephant 27 bold',bg='White',fg='Green',height=1)
Page_Heading1.place(x=110,y=15)

Cus_Name = StringVar(Order_Display)
Cus_Contact = StringVar(Order_Display)
Cus_Email = StringVar(Order_Display)
Cus_Address = StringVar(Order_Display)
Cus_Time = StringVar(Order_Display)

Name_OL = Label(Order_Display,textvariable=Cus_Name,font='Bahnshrift 14',height=1,width=25,bg='White')
Name_OL.place(x=40,y=90)

Contact_OL = Label(Order_Display,textvariable=Cus_Contact,font='Bahnshrift 14',height=1,width=25,bg='White')
Contact_OL.place(x=380,y=90)

Email_OL = Label(Order_Display,textvariable=Cus_Email,font='Bahnshrift 14',height=1,width=25,bg='White')
Email_OL.place(x=170,y=135)

Address_OL = Label(Order_Display,textvariable=Cus_Address,font='Bahnshrift 13',height=3,width=25,bg='White')
Address_OL.place(x=170,y=180)

OD_Canvas = Canvas(Order_Display,height=25,width=140)
OD_Canvas.place(x=50,y=250)

Scroll_OD = Scrollbar(OD_Canvas)
Scroll_OD.pack(side=RIGHT,fill=Y)

OD_List = Listbox(OD_Canvas,font='Courier 14',yscrollcommand=Scroll_OD.set,height=4,width=44)
OD_List.pack(side=LEFT)

Scroll_OD.config(command=OD_List.yview)

Back_OD = Button(Order_Display,text='Back',font='Bahnshrift 15',height=1,width=8,command=lambda: swap('Orders Page'))
Back_OD.place(x=480,y=350)

#######################################################################################################################################################################

# Mainloop all pages

Home.mainloop()                 #1
Login.mainloop()                #2
Sign_up.mainloop()              #3
Plant_Details.mainloop()        #4
Plant_View.mainloop()           #5
Final_View.mainloop()           #6
Admin_Login.mainloop()          #7
Admin_Prog.mainloop()           #8
Update_Availability.mainloop()  #9
Add_Plant.mainloop()            #10
Rem_Plant.mainloop()            #11
Orders_Page.mainloop()          #12
Order_Display                   #13

#End of program

#######################################################################################################################################################################
#######################################################################################################################################################################
