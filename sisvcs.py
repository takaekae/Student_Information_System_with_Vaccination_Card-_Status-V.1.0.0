import mysql.connector as mysql
import qrcode
import os
import time
from stdiomask import getpass
from rich.console import Console
from rich.theme import Theme

#color of the system
color_theme = Theme({
    'tb':"#7fffd4", #topbar color
    'f':"#FF847C",# frame color
    't':"#FECEAB", #text color
    'n':"#FF847C" #notification color
})
rc= Console(theme = color_theme)


#Sytem Clear
clear=lambda: os.system('cls')


# connect to sisvcs database
try:
    condb = mysql.connect(host='localhost', user='root', password = '', database = 'sisvcs')
    mydb = condb.cursor(buffered=True)

except Exception as error:
    print(error)
    
    
                                                                                    #@Copyright JOHN LLOYD D> DE SAPE



#Loading bar function
def loading_bar():
    clear()
    rc.print("""
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••___•••••[/tb]
          [tb]|      [t]Student Vaccination System with Vaccination Card Status[/t] [f]-[/f]  [f]|_|[/f]  [f]X[/f] |[/tb]
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]         
          [f]•                [t]█▀█ █░░ █▀▀ ▄▀█ █▀ █▀▀   █░█░█ ▄▀█ █ ▀█▀[/t]                •[/f]  
          [f]•                [t]█▀▀ █▄▄ ██▄ █▀█ ▄█ ██▄   ▀▄▀▄▀ █▀█ █ ░█░[/t]                •[/f]
          [f]•                                                                        •[/f] 
""")
    for i in range(0,100):
        print("\r\t\t\t\t\tLoading... {}%".format(i), end="")
        time.sleep(0.1)
    print("\r\t\t\t\t\tLoading... 100%")
    time.sleep(1)
    clear()
    
    
    
                                                                                #@Copyright JOHN LLOYD D> DE SAPE   
    
#Update the student's Information
def update(student_id):
    clear()
    rc.print("""
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••___•••••[/tb]
          [tb]|     [t]Student Vaccination System with Vaccination Card Status[/t]  [f]-[/f]  [f]|_|[/f]  [f]X[/f] |[/tb]
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]     
          [tb]•                     [t]█░█ █▀█ █▀▄ ▄▀█ ▀█▀ █▀▀ ▀█[/t]                         •[/tb]
          [tb]•                     [t]█▄█ █▀▀ █▄▀ █▀█ ░█░ ██▄ ░▄[/t]                         •[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
        
""")
    mydb.execute(f"DELETE from student WHERE student_id = '{student_id}'")
    fullname = str(rc.input("\t\t\t\t[t]Fullname[/t] [n]:[/n] "))
    course_year_section = str(rc.input("\t\t\t\t[t]Course Year & Section[/t] [n]:[/n] "))
    student_id = str(rc.input("\t\t\t\t[t]Student Id[/t] [n]:[/n] "))
    password = str(getpass("\t\t\t\tPassword : "))
    age = str(rc.input("\t\t\t\t[t]Age[/t] [n]:[/n] "))
    gender = str(rc.input("\t\t\t\t[t]Gender[/t] [n]:[/n] "))
    address = str(rc.input("\t\t\t\t[t]Address[/t] [n]:[/n] "))
    mobile_no = str(rc.input("\t\t\t\t[t]Mobile No.[/t] [n]:[/n] "))
    vac_manufacturer = str(rc.input("\t\t\t\t[t]Vaccination Manufacturer [n]:[/n] "))
    #generating a qrcode for the student
    qrcode_design = qrcode.QRCode(version=1, box_size=40, border=3)
    qrcode_design.add_data(f"""
Eastern Visayas State University

Fullname : {fullname}
Student ID : {student_id}
Course Section & Year : {course_year_section}
Age : {age}
Gender : {gender}
Address : {address}
Mobile Number : {mobile_no}
Vaccination Manufacturer : {vac_manufacturer}
"""
        )
    qrcode_design.make(fit=True)
    generate_qrcode = qrcode_design.make_image(fill_color="#000000", back_color="#9e9b9b")
    generate_qrcode.save('hello.png')
    generate_qrcode.show()
        

    data="INSERT INTO student(fullname,course_year_section, student_id, password, age, gender, address, mobile_no, vac_manufacturer) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        
    query_val=(fullname, course_year_section,student_id, password, age, gender, address, mobile_no, vac_manufacturer)
        
        
    mydb.execute(data, query_val)
    condb.commit()
    clear()
    rc.print("""
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••___•••••[/tb]
          [tb]|     [t]Student Vaccination System with Vaccination Card Status [/t] [f]-[/f]  [f]|_|[/f]  [f]X[/f] |[/tb]
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [tb]•                                                                        •[/tb]  
          [tb]•                             [t]█▀▄ █▀█ █▄░█ █▀▀[/t]                           •[/tb] 
          [tb]•                             [t]█▄▀ █▄█ █░▀█ ██▄[/t]                           •[/tb]
          [tb]•                                                                        •[/tb]
          [f]•                                                                        •[/f]
          [f]•                         [t]Please save your Qrcode[/t]                        •[/f]
          [f]•                    [t]Press([n]B[/n]) to Exit and ([n]L[/n]) to Login[/t]                   •[/f]
          [tb]••••••••••[f]••••••••••[/f]•••••••••[tb]••••••••••[/tb]••••••••••[f]••••••••••[/f]••••••••[tb]•••••••[/tb]
""")
    choice = str(rc.input("\t  [t]Option[/t] [n]:[/n] ")).lower()
    if choice == "e":
        student_session(student_id)
    elif choice == "l":
        login()
    else:
        invalid()
        
    
                                                                                    #@Copyright JOHN LLOYD D> DE SAPE   
#Invalid or invalid credentials
def invalid():
    clear()
    rc.print("""
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••___•••••[/tb]
          [tb]|     [t]Student Vaccination System with Vaccination Card Status[/t]  [f]-[/f]  [f]|_|[/f]  [f]X[/f] |[/tb]
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [tb]•                                                                        •[/tb]
          [tb]•                        [t]█ █▄░█ █░█ ▄▀█ █░░ █ █▀▄[/t]                        •[/tb]
          [tb]•                        [t]█ █░▀█ ▀▄▀ █▀█ █▄▄ █ █▄▀[/t]                        •[/tb]
          [tb]•                                                                        •[/tb]
          [f]•                                                                        •[/f]
          [f]•                       [t]Please wait for[/t] ([n]5[/n]) [t]seconds[/t]                      •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]                                                                       
          [tb]••••••••••[f]••••••••••[/f]•••••••••[tb]••••••••••[/tb]••••••••••[f]••••••••••[/f]••••••••[tb]•••••••[/tb]
""")
    #seconds before to proceed to main function
    time.sleep(3)
    main()
    
#Deleting existing student only Admin can remove a student from the database
def remove():
    clear()
    rc.print("""
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••___•••••[/tb]
          [tb]|     [t]Student Vaccination System with Vaccination Card Status[/t]  [f]-[/f]  [f]|_|[/f]  [f]X[/f] |[/tb]
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [tb]•              [t]▄▀█ █▀▄ █▀▄▀█ █ █▄░█   █▀█ ▄▀█ █▄░█ █▀▀ █░░[/t]               •[/tb]
          [tb]•              [t]█▀█ █▄▀ █░▀░█ █ █░▀█   █▀▀ █▀█ █░▀█ ██▄ █▄▄[/t]               •[/tb]
          [f]•                                                                        •[/f]
          [f]•                    [t]Delete Existing Student Account[/t]                     •[/f]
""")
    mydb.execute("SELECT fullname, student_id FROM student")
    rc.print("""
          [t]•+--------|Fullname|-------------------------------|Student ID|---------+•[/t]
""")
    for view in mydb:
        student = list(view)
        for show in student:
            print(f"                    {show}",end="")
        print("\n")  
    id = str(rc.input("\n\t  [t]Student ID[t] [n]:[/n] "))
    mydb.execute(f"DELETE from student WHERE student_id = '{id}'")
    condb.commit()
            
    if mydb.rowcount < 1:
        clear()
        invalid()
    else:
        clear()
        rc.print("""
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••___•••••[/tb]
          [tb]|     [t]Student Vaccination System with Vaccination Card Status[/t]  [f]-[/f]  [f]|_|[/f]  [f]X[/f] |[/tb]
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [tb]•              [t]▄▀█ █▀▄ █▀▄▀█ █ █▄░█   █▀█ ▄▀█ █▄░█ █▀▀ █░░[/t]               •[/tb]
          [tb]•              [t]█▀█ █▄▀ █░▀░█ █ █░▀█   █▀▀ █▀█ █░▀█ ██▄ █▄▄[/t]               •[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                       [t]Student has been deleted[/t]                         •[/f]
          [tb]•                       Type any key to [n]continue[n]                         •[/tb]
          [f]•                                                                        •[/f]
          [tb]••••••••••[f]••••••••••[/f]•••••••••[tb]••••••••••[/tb]••••••••••[f]••••••••••[/f]••••••••[tb]•••••••[/tb]
       
""")
        choice = str(rc.input("\t  [t]Type[/t] [n]:[/n] ")).lower()
        admin_session()
        
#View all data from the database      
def database():
    clear()
    try:
        rc.print("""
[tb]•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••___•••••[/tb]
[tb]|                        [t]Student Vaccination System with Vaccination Card Status[/t]                    [f]-  |_|  X[/f] [tb]|[/tb]
[tb]•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
[f]•                                                                                                             •[/f]
[f]•                                                                                                             •[/f]
[tb]•                                 [t]▄▀█ █▀▄ █▀▄▀█ █ █▄░█   █▀█ ▄▀█ █▄░█ █▀▀ █░░[/t]                                 •[/tb]
[tb]•                                 [t]█▀█ █▄▀ █░▀░█ █ █░▀█   █▀▀ █▀█ █░▀█ ██▄ █▄▄[/t]                                 •[/tb]
[f]•                                                                                                             •[/f]
[f]•                                        [t]Student's Database[/t][t]([/t][n]UPDATE[/n][t])[/t]                                           •[/f]
                         [t]Type[/t][t]([/t][n]L[/n])[t]to Logout and Type [/t][t]([/t][n]D[/n][t])[/t] [t]to remove a existing Student[/t]
[t]•••|FULLNAME|••|STUDENT ID|••|PASS|••|AGE|••|GENDER|••|ADDRESS|••|MOBILE NUMBER|••|VACCINATION MANUFACTURER|•••[/t] 

          
        
""")
                                                                                #@Copyright JOHN LLOYD D> DE SAPE        
        mydb.execute("SELECT fullname, student_id, password, age, gender, address, mobile_no, vac_manufacturer FROM student")
        for view in mydb:
            lol=list(view)
            for show in lol:
                print(f"{show}",end =" ")
            print("\n")
        choice=str(rc.input("\n\t  [t]Type[/t] [n]:[/n] ")).lower()
        
        if choice == "l":
            main()
        elif choice == "d":
            remove()
        else:
            invalid()
    
    except Exception as error:
        print(f"Failed {error}")
        
#View the student's information    
def student_information(student_id):
    clear()
    rc.print("""
          [tb]•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••___•••••[/tb]
          [tb]|                         [t]Student Vaccination System with Vaccination Card Status[/t]                    [f]-  |_|  X[/f] [tb]|[/tb]
          [tb]•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••[/tb]
          [f]•                                                                                                             •[/f]
          [f]•                                                                                                             •[/f]
          [tb]•               [t]█▀ ▀█▀ █░█ █▀▄ █▀▀ █▄░█ ▀█▀ ▀ █▀   █ █▄░█ █▀▀ █▀█ █▀█ █▀▄▀█ ▄▀█ ▀█▀ █ █▀█ █▄░█[/t]                •[/tb]
          [tb]•               [t]▄█ ░█░ █▄█ █▄▀ ██▄ █░▀█ ░█░ ░ ▄█   █ █░▀█ █▀░ █▄█ █▀▄ █░▀░█ █▀█ ░█░ █ █▄█ █░▀█[/t]                •[/tb]
          [f]•                                          [t]Type ([n]B[/n]) to back[/t]                                                   •[/f]
          [f]•                                                                                                             •[/f]
          [tb]•                                                                                                             •[/tb]
          [tb]•                                                                                                             •[/tb]    
        """)
    student_id = (str(student_id),)
    mydb.execute ("SELECT fullname, student_id, password, age, gender, address, mobile_no, vac_manufacturer FROM student WHERE student_id = %s", student_id)
    info = mydb.fetchall()
    rc.print("""
                        [n]|[/n][t]FULLNAME[/t][n]|[/n][t]STUDENT ID[/t][n]|[/n][t]PASSWORD[/t][n]|[/n][t]AGE[/t][n]|[/n][t]GENDER[t][n]|[/n][t]ADDRESS[/t][n]|[/n][t]MOBILE NUMBER[/t][n]|[/n][t]VACCINATION MANUFACTURER[/t][n]|[/n][/t]

""")
    for view in info:
        show=list(view)
        for data in show:
            print(f"\t{data}",end =" ")
    back = str(rc.input("\n\t  [t]Type[/t] [n]:[/n] ")).lower()
    if back == "b":
        student_session(student_id)
    else:
        invalid()     
           
#Student's session or menu       
def student_session(student_id):
    clear()
    try:
        rc.print("""
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••___•••••[/tb]
          [tb]|     [t]Student Vaccination System with Vaccination Card Status  [/t][f]-[/f]  [f]|_|[/f]  [f]X[/f] |[/tb]
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [tb]•         [t]█▀ ▀█▀ █░█ █▀▄ █▀▀ █▄░█ ▀█▀ ▀ █▀   █▀▄▀█ █▀▀ █▄░█ █░█[/t]          •[/tb]
          [tb]•         [t]▄█ ░█░ █▄█ █▄▀ ██▄ █░▀█ ░█░ ░ ▄█   █░▀░█ ██▄ █░▀█ █▄█[/t]          •[/tb]
          [f]•                                                                        •[/f]
          [tb]•                    [t][[n]1[/n]][t]. View your information[/t]                          •[/tb]
          [tb]•                    [t][[n]2[/n]][t]. Update your information[/t]                        •[/tb]
          [tb]•                    [t][[n]3[/n]][t]. Logout[/t]                                         •[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [tb]••••••••••[f]••••••••••[/f]•••••••••[tb]••••••••••[/tb]••••••••••[f]••••••••••[/f]••••••••[tb]•••••••[/tb]
""")
        option = str(rc.input("\t  [t]Option[/t] [n]:[/n] "))
        
                                                                            #@Copyright JOHN LLOYD D> DE SAPE       
        if option == "1":
            student_information(student_id)    
        elif option == "2":
            update(student_id)
        elif option == "3":
            main()
        else:
            invalid(student_session)
                
                
    except Exception as error:
        print(f"Failed {error}")
    
#Admin session or menu           
def admin_session():
    clear()
    try:
        
        rc.print("""
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••___•••••[/tb]
          [tb]|     [t]Student Vaccination System with Vaccination Card Status  [/t][f]-[/f]  [f]|_|[/f]  [f]X[/f] |[/tb]
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [tb]•              [t]▄▀█ █▀▄ █▀▄▀█ █ █▄░█   █▀█ ▄▀█ █▄░█ █▀▀ █░░[/t]               •[/tb]
          [tb]•              [t]█▀█ █▄▀ █░▀░█ █ █░▀█   █▀▀ █▀█ █░▀█ ██▄ █▄▄[/t]               •[/tb]
          [f]•                               [n]Main Menu[/n]                                •[/f]
          [f]•                                                                        •[/f]
          [tb]•                    [t][[n]1[/n]][t]. Remove Existing Student[/t]                        •[/tb]
          [tb]•                    [t][[n]2[/n]][t]. View all Data[/t]                                  •[/tb]
          [tb]•                    [t][[n]3[/n]][t]. Logout[/t]                                         •[/tb]
          [f]•                                                                        •[/f]
          [tb]••••••••••[f]••••••••••[/f]•••••••••[tb]••••••••••[/tb]••••••••••[f]••••••••••[/f]••••••••[tb]•••••••[/tb]
""")
        option=rc.input(str("\t  [t]Option[/t] [n]:[/n] "))
        if option == "1":
            remove()
        elif option== "2":
           database()
        elif option == "3":
            main()
        else:
            invalid()
                
    except Exception as error:
        print(f"Failed {error}")
                                                                                    #@Copyright JOHN LLOYD D> DE SAPE                                                      
#Student's Login        
def student_login():
    clear()
    try:
        rc.print("""
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••___•••••[/tb]
          [tb]|     [t]Student Vaccination System with Vaccination Card Status [/t] [f]-[/f]  [f]|_|[/f]  [f]X[/f] |[/tb]
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [tb]•                          [t]█░░ █▀█ █▀▀ █ █▄░█[/t]                            •[/tb]
          [tb]•                          [t]█▄▄ █▄█ █▄█ █ █░▀█[/t]                            •[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
""")
        student_id = str(rc.input("\t\t\t\t[t]Student ID[/t] [n]:[/n] "))
        password = str(getpass("\t\t\t\tPassword : ")) 
        query_val = (student_id, password)
        mydb.execute("SELECT student_id from student WHERE student_id = %s AND password = %s ", query_val)
        

        if mydb.rowcount <= 0: #which there is no result
            clear()
            invalid()
        else:      
            student_session(student_id)
#@Copyright JOHN LLOYD D> DE SAPE
    except Exception as error:
        print("Failed", error)
#Admin Login        
def admin_login():
    clear()
    try:
        rc.print("""
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••___•••••[/tb]
          [tb]|     [t]Student Vaccination System with Vaccination Card Status  [/t][f]-[/f]  [f]|_|[/f]  [f]X[/f] |[/tb]
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [tb]•                          [t]█░░ █▀█ █▀▀ █ █▄░█[/t]                            •[/tb]
          [tb]•                          [t]█▄▄ █▄█ █▄█ █ █░▀█[/t]                            •[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
""")
        username = str(rc.input("\t\t\t\t[t]username[/t] [n]:[/n] "))
        password = str(getpass("\t\t\t\tPassword : ")) 
        query_val = (username, password)
        mydb.execute("SELECT username from admin WHERE username = %s AND password = %s ", query_val)
                                                                        #@Copyright JOHN LLOYD D> DE SAPE       

        if mydb.rowcount <= 0: #which there is no result
            clear()
            rc.print("""
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••___•••••[/tb]
          [tb]|     [t]Student Vaccination System with Vaccination Card Status[/t]  [f]-[/f]  [f]|_|[/f]  [f]X[/f] |[/tb]
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [tb]•                        [t]█ █▄░█ █░█ ▄▀█ █░░ █ █▀▄[/t]                        •[/tb]
          [tb]•                        [t]█ █░▀█ ▀▄▀ █▀█ █▄▄ █ █▄▀[/t]                        •[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                       [t]Please wait for[/t] ([n]5[/n]) [t]seconds[/t]                      •[/f]
          [tb]•                                                                        •[/tb]
          [tb]•                                                                        •[/tb]                                                                       
          [tb]••••••••••[f]••••••••••[/f]•••••••••[tb]••••••••••[/tb]••••••••••[f]••••••••••[/f]••••••••[tb]•••••••[/tb]
""")
            time.sleep(5)
            main()
        else:      
            admin_session()

    except Exception as error:
        print("Failed", error)
#login menu        
def login():
    clear()
    rc.print("""

          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••___•••••[/tb]
          [tb]|     [t]Student Vaccination System with Vaccination Card Status[/t]  [f]-[/f]  [f]|_|[/f]  [f]X[/f] |[/tb]
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [tb]•                             [[n]1[/n]]. [t]Student[/t]                               •[/tb]
          [tb]•                             [[n]2[/n]]. [t]Admin[/t]                                 •[/tb]
          [tb]•                             [[n]3[/n]]. [t]Back[/t]                                  •[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [tb]••••••••••[f]••••••••••[/f]•••••••••[tb]••••••••••[/tb]••••••••••[f]••••••••••[/f]••••••••[tb]•••••••[/tb]

""")
    choice = str(rc.input("\t  [t]Option[/t] [n]:[/n] "))
    if choice == "1":
        student_login()
    elif choice == "2":
        admin_login()
    elif choice == "3":
        main()
    else:
        invalid()
        login()
#students registration    
def register():
    try:
        clear()
        rc.print("""
          [tb]•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••___•••••[/tb]
          [tb]|          [t]Student Vaccination System with Vaccination Card Status[/t]    [n]-  |_|  X[/n] [tb]|[/tb]
          [tb]•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••[/tb]
          [f]•                                                                               •[/f]
          [f]•                                                                               •[/f]
          [f]•                                                                               •[/f]
          [tb]•   [t]█▀ ▀█▀ █░█ █▀▄ █▀▀ █▄░█ ▀█▀   █▀█ █▀▀ █▀▀ █ █▀ ▀█▀ █▀█ ▄▀█ ▀█▀ █ █▀█ █▄░█ [/t]  •[/tb] 
          [tb]•   [t]▄█ ░█░ █▄█ █▄▀ ██▄ █░▀█ ░█░   █▀▄ ██▄ █▄█ █ ▄█ ░█░ █▀▄ █▀█ ░█░ █ █▄█ █░▀█ [/t]  •[/tb] 
          [f]•                                                                               •[/f]
          [f]•                               [t] █▀▀ █▀█ █▀█ █▀▄▀█[/t]                              •[/f]
          [f]•                               [t] █▀░ █▄█ █▀▄ █░▀░█[/t]                              •[/f]
""")
        fullname = str(rc.input("\t\t\t\t[t]Fullname[/t] [n]:[/n] "))
        course_year_section = str(rc.input("\t\t\t\t[t]Course Year & Section[/t] [n]:[/n] "))
        student_id = str(rc.input("\t\t\t\t[t]Student Id[/t] [n]:[/n] "))
        password = str(getpass("\t\t\t\tPassword : "))
        age = str(rc.input("\t\t\t\t[t]Age[/t] [n]:[/n] "))
        gender = str(rc.input("\t\t\t\t[t]Gender[/t] [n]:[/n] "))
        address = str(rc.input("\t\t\t\t[t]Address[/t] [n]:[/n] "))
        mobile_no = str(rc.input("\t\t\t\t[t]Mobile No.[/t] [n]:[/n] "))
        vac_manufacturer = str(rc.input("\t\t\t\t[t]Vaccination Manufacturer [n]:[/n] "))
        #generating a qrcode for the student
        qrcode_design = qrcode.QRCode(version=1, box_size=40, border=3)
        qrcode_design.add_data(f"""
Eastern Visayas State University

Fullname : {fullname}
Student ID : {student_id}
Course Section & Year : {course_year_section}
Age : {age}
Gender : {gender}
Address : {address}
Mobile Number : {mobile_no}
Vaccination Manufacturer : {vac_manufacturer}
"""
        )
        qrcode_design.make(fit=True)
        generate_qrcode = qrcode_design.make_image(fill_color="#000000", back_color="#9e9b9b")
        generate_qrcode.save('hello.png')
        generate_qrcode.show()
        

        data="INSERT INTO student(fullname,course_year_section, student_id, password, age, gender, address, mobile_no, vac_manufacturer) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        
        query_val=(fullname, course_year_section,student_id, password, age, gender, address, mobile_no, vac_manufacturer)
        
        
        mydb.execute(data, query_val)
        condb.commit()
        clear()
        rc.print("""
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••___•••••[/tb]
          [tb]|     [t]Student Vaccination System with Vaccination Card Status[/t]  [f]-[/f]  [f]|_|[/f]  [f]X[/f] |[/tb]
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [tb]•                             [t]█▀▄ █▀█ █▄░█ █▀▀[/t]                           •[/tb] 
          [tb]•                             [t]█▄▀ █▄█ █░▀█ ██▄[/t]                           •[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                         [t]Please save your [n]Qrcode[n][/t]                        •[/f]
          [tb]•                    [t]Press[/t]([n]E[/n]) [t]to Exit and[/t] ([n]L[/n]) [t]to Login[/t]                   •[/tb]
          [tb]•                                                                        •[/tb]
          [tb]••••••••••[f]••••••••••[/f]•••••••••[tb]••••••••••[/tb]••••••••••[f]••••••••••[/f]••••••••[tb]•••••••[/tb]
""")
        choice = str(rc.input("\t  [t]Option[/t] [n]:[/n] ")).lower()
        if choice == "e":
            main()
        elif choice == "l":
            login()
            
    except Exception as error:
        print(f"Failed ××× {error}")
#The main menu   
def main():
    clear()
    rc.print("""
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••___•••••[/tb]
          [tb]|     [t]Student Vaccination System with Vaccination Card Status  [/t][f]-[/f]  [f]|_|[/f]  [f]X[/f] |[/tb]
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [tb]•                            [t][[n]1[/n]]. Login[/t]                                  •[/tb]
          [tb]•                            [t][[n]2[/n]]. Register[/t]                               •[/tb]
          [tb]•                            [t][[n]3[/n]]. Exit[/t]                                   •[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f] 
          [f]•                                                                        •[/f]
          [tb]••••••••••[f]••••••••••[/f]•••••••••[tb]••••••••••[/tb]••••••••••[f]••••••••••[/f]••••••••[tb]•••••••[/tb]
""")
    choice = str(rc.input("\t  [t]Option[/t] [n]:[/n] "))
    
    if choice == "1":
        login()
    elif choice == "2":
        register()
    elif choice == "3":
        exit()
    else:
        invalid()
        main()
loading_bar()
main()
#@Copyright JOHN LLOYD D> DE SAPE