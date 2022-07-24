#__________________E M P L O Y E E   D E T A I L S   M A N A G E M E N T   M O D U L E____________________
import mysql.connector as m
mycon = m.connect(host='localhost', user='varsha',
                          passwd='Var@123#', database='emp_mgmt')
cur=mycon.cursor()
if mycon.is_connected()== True:
    pass
else:
    print('something went wrong !!!\n error in connecting database')
#_______________________________________Required Functions_________________________________________________
#____________________________ FUNCTION TO INSERT RECORD TO THE DATABASE____________________________________
def insert_record():
    ans = 'y'
    while (ans == 'Y' or ans == "y"):
        print('enter the details of employee to be inserted')
        cur.execute("select max(emp_id) from emp_mgmt ".format())
        data = cur.fetchone()
        eid =data[0]+1
        print('New employee id               : ',eid)
        nam = input('employee name                 : ').title()
        print('select departmant  -------->')
        print('\t\t\t -----------------')
        print("\t\t\t|DEPARTMENT NAMES |")
        print('\t\t\t -----------------')
        print("\t\t\t|1.MEDIA\t  |\n\t\t\t|2.MARKETING\t  |")
        print("\t\t\t|3.INFRASTRUCTURE |\n\t\t\t|4.FINANCE\t  |\n\t\t\t|5.HUMAN RESOURCE |")
        print('\t\t\t ----------------')
        dept= input('employee department name      : ').upper()
        sal = input('employee salary               : ')
        dsg = input('employee designation          : ').title()
        dob = input('employee date of birth        : ')
        doj = input('employee date of joining job  : ')
        phn = int(input('employee contact number       : '))
        cty= input('employee city                  : ').title()
        ctry= input('employee country              : ').title()
        emil= input('employee email                : ')      
        st="insert into emp_mgmt values('{}','{}','{}','{}','{}','{}','{}',{},'{}','{}','{}')".format(eid,nam,dept,sal,dsg,dob,doj,phn,cty,ctry,emil)
        cur.execute(st)
        mycon.commit()
        mycon.close()
        print()
        print(nam, 'details have been saved :) ')
        print()
        ans = input('Do you want to enter more records \n' +
                    'if yes then press y \n' +
                    'otherwise enter any key : ')
        print()
#____________________________ FUNCTION TO UPDATE RECORD TO THE DATABASE_____________________________________
ans = 'y'
def update_record():
    ans = 'y'
    while (ans == 'Y' or ans == "y"):
        print("enter emlpoyee id whose details you are going to update")
        eid= input('employee id: ')
        print('Previous details employee with employee id ',eid,' : ')
        cur.execute("select * from emp_mgmt where emp_id like '{}' ".format(eid))
        data = cur.fetchone()
        dts=('employee id                   : ','employee name                 : '
             ,'employee department           : ','employee salary               : '
             ,'employee designation          : ','employee date of birth        : ',
             'employee date of joining job  : ','employee contact number       : '
             ,'employee city                 : ','employee country              : ',
             'employee email                : ')
        j=0
        for i in data:
            print(dts[j],i)
            j+=1
        print()
        print('Enter emlpoyee details to be updated ------> ')
        print()
        nam = input('employee name                 : ')
        dept= input('employee department           : ')
        sal = input('employee salary               : ')
        dsg = input('employee designation          : ')
        dob = input('employee date of birth        : ')
        doj = input('employee date of joining job  : ')
        phn = int(input('employee contact number       : '))
        cty= input('employee city                  : ')
        ctry= input('employee country              : ')
        emil= input('employee email                : ')
        sy = "update emp_mgmt set emp_name='{}',emp_department='{}',emp_salary='{}',emp_dsgn='{}',emp_DOB='{}',emp_DOJ_job='{}',emp_contact='{}',emp_city='{}',emp_country='{}',emp_email='{}' where emp_id='{}'".format(
            nam,dept,sal,dsg,dob,doj,phn,cty,ctry,emil,eid)
        cur.execute(sy)
        mycon.commit()
        print(nam, "details has been successfully updated")
        mycon.close()
        print('--------------------------------------------------------------:)')
        print()
        ans = input('Do you want to update more records \n' +
                    'if yes then press y \n' +
                    'otherwise enter any key : ')
#____________________________ FUNCTION TO DELETE RECORD FROM THE DATABASE_____________________________________
def delete_record():
        ans = 'y'
        while (ans == 'Y' or ans == "y"):
            print("enter emlpoyee id whose details you are going to delete")
            eid= input('employee id: ')
            print('details employee with employee id ',eid,' : ')
            cur.execute("select * from emp_mgmt where emp_id like '{}' ".format(eid))
            data = cur.fetchone()
            dts=('employee id                   : ','employee name                 : '
             ,'employee department           : ','employee salary               : '
             ,'employee designation          : ','employee date of birth        : ',
             'employee date of joining job  : ','employee contact number       : '
             ,'employee city                 : ','employee country              : ',
             'employee email                : ')
            j=0
            for i in data:
                print(dts[j],i)
                j+=1
            print('Is this record you are going to delete')
            anser=input('if yes then press y \n' +
                    'otherwise enter any key')
            if (anser == 'y' or anser == 'Y'):
                cur.execute("delete from emp_mgmt where emp_id like '{}' ".format(eid))
                print('record deleted')
                mycon.commit()
                mycon.close()
                ans = input('Do you want to delete more records \n' +
                    'if yes then press y \n' +
                    'otherwise enter any key')
            else:
                print('entered id may be mistyped!!!')
                delete_record()
#search section
def search_module():
    print('----------------------------------------------------------------------------------------------------------------')
    print("\t\t            ______WELCOME in the Search Section______")
    print('----------------------------------------------------------------------------------------------------------------')
    print("\t\t                            GUIDE")
    print('\t\t\t----------------------------------------------')
    print("\t\t\t|DEPARTMENT NAMES | Department Codes\t     |")
    print('\t\t\t----------------------------------------------')
    print("\t\t\t|1.MEDIA\t  |  101\t\t     |\n\t\t\t|2.MARKETING\t  |  202\t\t     |")
    print("\t\t\t|3.INFRASTRUCTURE |  303\t\t     |\n\t\t\t|4.FINANCE\t  |  404\t\t     |\n\t\t\t|5.HUMAN RESOURCE |  505\t\t     |")
    print('\t\t\t----------------------------------------------')
    while True:
        sea=int(input("\n\t\t\tHey!!! enter the code of your prefrence---"))
        print('----------------------------------------------------------------------------------------------------------------')
        if sea==101:
            print('\t\t                  WELCOME In MEDIA SECTION ')
            print('----------------------------------------------------------------------------------------------------------------')
            print('\t\t\tNOTE~There are two section 1.SEARCH BY NAME\n\t\t\t\t\t\t   2.SEARCH BY EMPLOYEE ID')
            sear=int(input('\t\t\tPRESS THE INDEX NO. OF YOUR CHOICE---'))
            if sear==1:
                name =str(input("Enter name of employee  or starting letter-"))
                import mysql.connector as sql
                mycon=sql.connect(host="localhost",user="varsha",passwd="Var@123#",database ="emp_mgmt")
                if mycon.is_connected()==True:
                    cur=mycon.cursor()
                    cur.execute("select * from emp_mgmt where emp_name like'{}%'".format(name))
                    data=cur.fetchall()
                    for i in data:
                        print(i)
                    mycon.close()
                else:
                    print('not connected ')
                print('----------------------------------------------------------------------------------------------------------------')
                hy=int(input("\nDO YOU WANT TO SEARCH FURTHER OR BIND UP HERE\nif YES press 1 & if NO type 2---- "))
                if hy==1:
                    print("\t\t\t\tTAKING YOU AT STARTING POINT")
                elif sear==2:
                    print('----------------------------------------------------------------------------------------------------------------')
                    print('--------------------------------------------------------------------bye-----------------------------------------')
                    print('----------------------------------------------------------------------------------------------------------------')
                    break
                else:
                    print("THAT NO. IS NOT A CHOICE START AGAIN!")
            elif sear==2:
                num =str(input("Enter num of employee  or starting number-"))
                import mysql.connector as sql
                mycon=sql.connect(host="localhost",user="varsha",passwd="Var@123#",database ="emp_mgmt")
                if mycon.is_connected()==True:
                    cur=mycon.cursor()
                    cur.execute("select * from emp_mgmt where emp_id like'{}%'".format(num))
                    data=cur.fetchall()
                    for i in data:
                        print(i)
                    mycon.close()
                print('----------------------------------------------------------------------------------------------------------------')
                hy=int(input("\nDO YOU WANT TO SEARCH FURTHER OR BIND UP HERE\nif YES press 1 & if NO type 2---- "))
                if hy==1:
                    print("\t\t\t\tTAKING YOU AT STARTING POINT")
                elif hy==2:
                    print('----------------------------------------------------------------------------------------------------------------')
                    print('--------------------------------------------------------------------bye-----------------------------------------')
                    print('----------------------------------------------------------------------------------------------------------------')
                    break
                else:
                    print("THAT NO. IS NOT A CHOICE START AGAIN!")
            else:
               print ("\n\t\t\t\t    |SORRY!!!wrong index|")
        elif sea==202:
            print('\t\t                  WELCOME In MARKETING SECTION ')
            print('----------------------------------------------------------------------------------------------------------------')
            print('\t\t\tNOTE~There are two section 1.SEARCH BY NAME\n\t\t\t\t\t\t   2.SEARCH BY EMPLOYEE ID')   
            sear=int(input('\t\t\tPRESS THE INDEX NO. OF YOUR CHOICE---'))
            if sear==1:
                import mysql.connector as sql
                mycon=sql.connect(host="localhost",user="varsha",passwd="Var@123#",database ="emp_mgmt")
                if mycon.is_connected()==True:
                    cur=mycon.cursor()
                    cur.execute("select * from emp_mgmt where emp_name like'{}%'".format(name))
                    data=cur.fetchall()
                    for i in data:
                        print(i)
                    mycon.close()
                print('----------------------------------------------------------------------------------------------------------------')
                hy=int(input("\nDO YOU WANT TO SEARCH FURTHER OR BIND UP HERE\nif YES press 1 & if NO type 2---- "))
                if hy==1:    
                    print("\t\t\t\tTAKING YOU AT STARTING POINT")
                elif hy==2:
                    print('----------------------------------------------------------------------------------------------------------------')
                    print('--------------------------------------------------------------------bye-----------------------------------------')
                    print('----------------------------------------------------------------------------------------------------------------')
                    break
                else:
                    print("THAT NO. IS NOT A CHOICE START AGAIN!")
            elif sear==2:
                num =str(input("Enter num of employee  or starting number-"))
                import mysql.connector as sql
                mycon=sql.connect(host="localhost",user="varsha",passwd="Var@123#",database ="emp_mgmt")
                if mycon.is_connected()==True:
                    cur=mycon.cursor()
                    cur.execute("select * from emp_mgmt where emp_id like'{}%'".format(num))
                    data=cur.fetchall()
                    for i in data:
                        print(i)
                    mycon.close()
                print('----------------------------------------------------------------------------------------------------------------')
                hy=int(input("\nDO YOU WANT TO SEARCH FURTHER OR BIND UP HERE\nif YES press 1 & if NO type 2---- "))
                if hy==1:
                    print("\t\t\t\tTAKING YOU AT STARTING POINT")
                elif hy==2:
                    print('----------------------------------------------------------------------------------------------------------------')
                    print('--------------------------------------------------------------------bye-----------------------------------------')
                    print('----------------------------------------------------------------------------------------------------------------')
                    break
                else:
                    print("THAT NO. IS NOT A CHOICE START AGAIN!")
            else:
                print ("\n\t\t\t\t    |SORRY!!!wrong index|")    
        elif sea==303:
            print('\t\t                  WELCOME In INFRASTRUCTURE SECTION ')
            print('----------------------------------------------------------------------------------------------------------------')
            print('\t\t\tNOTE~There are two section 1.SEARCH BY NAME\n\t\t\t\t\t\t   2.SEARCH BY EMPLOYEE ID')   
            sear=int(input('\t\t\tPRESS THE INDEX NO. OF YOUR CHOICE---'))
            if sear==1:    
                import mysql.connector as sql
                mycon=sql.connect(host="localhost",user="varsha",passwd="Var@123#",database ="emp_mgmt")
                if mycon.is_connected()==True:
                    cur=mycon.cursor()
                    cur.execute("select * from emp_mgmt where emp_name like'{}%'".format(name))
                    data=cur.fetchall()
                    for i in data:
                        print(i)
                    mycon.close()
                print('----------------------------------------------------------------------------------------------------------------')
                hy=int(input("\nDO YOU WANT TO SEARCH FURTHER OR BIND UP HERE\nif YES press 1 & if NO type 2---- "))
                if hy==1:    
                    print("\t\t\t\tTAKING YOU AT STARTING POINT")
                elif hy==2:
                    print('----------------------------------------------------------------------------------------------------------------')
                    print('--------------------------------------------------------------------bye-----------------------------------------')
                    print('----------------------------------------------------------------------------------------------------------------')
                    break
                else:
                    print("THAT NO. IS NOT A CHOICE START AGAIN!")
            elif sear==2:
                num =str(input("Enter num of employee  or starting number-"))
                import mysql.connector as sql
                mycon=sql.connect(host="localhost",user="varsha",passwd="Var@123#",database ="emp_mgmt")
                if mycon.is_connected()==True:
                    cur=mycon.cursor()
                    cur.execute("select * from emp_mgmt where emp_id like'{}%'".format(num))
                    data=cur.fetchall()
                    for i in data:
                        print(i)
                    mycon.close()
                print('----------------------------------------------------------------------------------------------------------------')
                hy=int(input("\nDO YOU WANT TO SEARCH FURTHER OR BIND UP HERE\nif YES press 1 & if NO type 2---- "))
                if hy==1:
                    print("\t\t\t\tTAKING YOU AT STARTING POINT")
                elif hy==2:
                    print('----------------------------------------------------------------------------------------------------------------')
                    print('--------------------------------------------------------------------bye-----------------------------------------')
                    print('----------------------------------------------------------------------------------------------------------------')
                    break
                else:
                    print("THAT NO. IS NOT A CHOICE START AGAIN!")
            else:
                print ("\n\t\t\t\t    |sorry!!!wrong index|")
        elif sea==404:
            print('\t\t                  WELCOME In FINANCE SECTION ')
            print('----------------------------------------------------------------------------------------------------------------')
            print('\t\t\tNOTE~There are two section 1.SEARCH BY NAME\n\t\t\t\t\t\t   2.SEARCH BY EMPLOYEE ID')   
            sear=int(input('\t\t\tPRESS THE INDEX NO. OF YOUR CHOICE---'))
            if sear==1:    
               import mysql.connector as sql
               mycon=sql.connect(host="localhost",user="varsha",passwd="Var@123#",database ="emp_mgmt")
               if mycon.is_connected()==True:
                   cur=mycon.cursor()
                   cur.execute("select * from emp_mgmt where emp_name like'{}%'".format(name))
                   data=cur.fetchall()
                   for i in data:
                       print(i)
                   mycon.close()
               print('----------------------------------------------------------------------------------------------------------------')
               hy=int(input("\nDO YOU WANT TO SEARCH FURTHER OR BIND UP HERE\nif YES press 1 & if NO type 2---- "))
               if hy==1:    
                   print("\t\t\t\tTAKING YOU AT STARTING POINT")
               elif hy==2:
                   print('----------------------------------------------------------------------------------------------------------------')
                   print('--------------------------------------------------------------------bye-----------------------------------------')
                   print('----------------------------------------------------------------------------------------------------------------')
                   break
               else:
                   print("THAT NO. IS NOT A CHOICE START AGAIN!")
            elif sear==2:
                num =str(input("Enter num of employee  or starting number-"))
                import mysql.connector as sql
                mycon=sql.connect(host="localhost",user="varsha",passwd="Var@123#",database ="emp_mgmt")
                if mycon.is_connected()==True:
                    cur=mycon.cursor()
                    cur.execute("select * from emp_mgmt where emp_id like'{}%'".format(num))
                    data=cur.fetchall()
                    for i in data:
                        print(i)
                    mycon.close()
                print('----------------------------------------------------------------------------------------------------------------')
                hy=int(input("\nDO YOU WANT TO SEARCH FURTHER OR BIND UP HERE\nif YES press 1 & if NO type 2---- "))
                if hy==1:
                    print("\t\t\t\tTAKING YOU AT STARTING POINT")
                elif hy==2:
                    print('----------------------------------------------------------------------------------------------------------------')
                    print('--------------------------------------------------------------------bye-----------------------------------------')
                    print('----------------------------------------------------------------------------------------------------------------')
                    break
                else:
                    print("THAT NO. IS NOT A CHOICE START AGAIN!")
            else:
                print ("\n\t\t\t\t    |sorry!!!wrong index|")
        elif sea==505:
            print('\t\t                  WELCOME In HUMAN RESOURCE SECTION ')
            print('----------------------------------------------------------------------------------------------------------------')
            print('\t\t\tNOTE~There are two section 1.SEARCH BY NAME\n\t\t\t\t\t\t   2.SEARCH BY EMPLOYEE ID')   
            sear=int(input('\t\t\tPRESS THE INDEX NO. OF YOUR CHOICE---'))
            if sear==1:    
                import mysql.connector as sql
                mycon=sql.connect(host="localhost",user="varsha",passwd="Var@123#",database ="emp_mgmt")
                if mycon.is_connected()==True:
                    cur=mycon.cursor()
                    cur.execute("select * from emp_mgmt where emp_name like'{}%'".format(name))
                    data=cur.fetchall()
                    for i in data:
                        print(i)
                    mycon.close()
                print('----------------------------------------------------------------------------------------------------------------')
                hy=int(input("\nDO YOU WANT TO SEARCH FURTHER OR BIND UP HERE\nif YES press 1 & if NO type 2---- "))
                if hy==1:    
                    print("\t\t\t\tTAKING YOU AT STARTING POINT")
                elif hy==2:
                    print('----------------------------------------------------------------------------------------------------------------')
                    print('--------------------------------------------------------------------bye-----------------------------------------')
                    print('----------------------------------------------------------------------------------------------------------------')
                    break
                else:
                    print("THAT NO. IS NOT A CHOICE START AGAIN!")
            elif sear==2:
                num =str(input("Enter num of employee  or starting number-"))
                import mysql.connector as sql
                mycon=sql.connect(host="localhost",user="varsha",passwd="Var@123#",database ="emp_mgmt")
                if mycon.is_connected()==True:
                    cur=mycon.cursor()
                    cur.execute("select * from emp_mgmt where emp_id like'{}%'".format(num))
                    data=cur.fetchall()
                    for i in data:
                        print(i)
                    mycon.close()
                print('----------------------------------------------------------------------------------------------------------------')
                hy=int(input("\nDO YOU WANT TO SEARCH FURTHER OR BIND UP HERE\nif YES press 1 & if NO type 2---- "))
                if hy==1:
                    print("\t\t\t\tTAKING YOU AT STARTING POINT")
                elif hy==2:
                    print('----------------------------------------------------------------------------------------------------------------')
                    print('--------------------------------------------------------------------bye-----------------------------------------')
                    print('----------------------------------------------------------------------------------------------------------------')
                    break
                else:
                    print("THAT NO. IS NOT A CHOICE START AGAIN!")
            else:
                print ("\n\t\t\t\t    |sorry!!!wrong index|")
        else:
            print("SORRY,YOU'VE CHOOSEN A WRONG CODE")

#_________________________OUTLOOK ON THE CONSOLE SCREEN OF EMP_MGMT SYSTEM____________________________           
print()
print('*'*100)
print('           W E L C O M E   T O   E M P L O Y E E   M A N A G E M E N T   S Y S T E M ')
print('*'*100)
print()
def modules():
    print('                    ..................Choose your module................')
    print()
    print('                    ----------------------------------------------------')
    print('                   |                 MODULE               | MODULE CODE |')
    print('                    ----------------------------------------------------')
    print('                   | 1.Insert New Employee Record         |      1      |')
    print('                   | 2.Update Employee record             |      2      |')
    print('                   | 3.Delete Employee record             |      3      |') 
    print('                   | 4.Search employee record             |      4      |')
    print('                   | 5.Exit                               |      5      |')
    print('                    ----------------------------------------------------')
    print()
    module_choice=int(input('Enter the code of your preference : '))
    ans = 'y'
    while (ans == 'Y' or ans == "y"):
        if module_choice == 1:
            insert_record()
        elif module_choice == 2:
            update_record()
        elif module_choice == 3:
            delete_record()
        elif module_choice==4:
            search_module()
        elif module_choice==5:
                break
        else:
            print('You have entered wrong code .')
            ans = input('Do you want to enter the module code again \n if yes then press y \n' +
                        'otherwise enter any key : ')
modules()        
