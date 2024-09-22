import mysql.connector as s
mycon = s.connect(host= 'localhost', user= 'root', password= 'mysql', database= 'server' )
mycur = mycon.cursor()
def insert():
    while True:
        try:
            Id = int(input('Enter number: '))
            name = input('Enter the name: ')
            lname = input('Enter the last name: ')
            pno = int(input('enter phone number: '))
            bdate = input('enter birthdate(yyyymmdd): ')
            jdate = input('enter join date(yyyymmdd): ')
            dist = input('enter district: ')
            state = input('enter state: ')
            values = (Id, name, lname, pno, bdate, jdate, dist, state)
            sql = 'INSERT INTO STUDENT(ID, NAME, LNAME, PHONENO, BIRTHDATE, JOINDATE, DISTRICT, STATE) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
            sql1 = 'SELECT * FROM STUDENT'
            mycur.execute(sql, values)
            mycon.commit()
            mycur.execute(sql1)
            r = mycur.fetchall()
            for i in r:
                for j in i:
                    print((str(j)).center(15), end= '')
                print()
            break
        except ValueError:
            print('INVALID ONLY NUMERIC')

def display():
    sql = 'select * from student'
    mycur.execute(sql)
    r = mycur.fetchall()
    for i in r:
        for j in i:
            print((str(j)).center(15), end= '')
        print()

def courdisplay():
    sql = 'select * from courses'
    mycur.execute(sql)
    r = mycur.fetchall()
    for i in r:
        for j in i:
            print((str(j)).center(15), end= '')
        print()

def courinsert():
    while True:
        try:
            cid = int(input('Enter courses id: '))
            clas = input('Enter the classes: ')
            dura = input('Enter the duration: ')
            fee = int(input('enter the fees: '))
            values = (cid, clas, dura, fee)
            sql = 'INSERT INTO COURSES VALUES(%s, %s, %s, %s)'
            sql1 = 'SELECT * FROM COURSES'
            mycur.execute(sql, values)
            mycon.commit()
            mycur.execute(sql1)
            r = mycur.fetchall()
            for i in r:
                for j in i:
                    print((str(j)).center(15), end= '')
                print()
        except ValueError:
            print('INVALID NUMERIC ONLY')

def enrolldisplay():
    sql = 'select student.ID, student.NAME, student.LNAME, student.COURID, courses.CLASSES from student, courses where student.courid = courses.courid'
    mycur.execute(sql)
    r = mycur.fetchall()
    for i in r:
        for j in i:
            print((str(j)).center(15), end= '')
        print()
def enrollinsert():
    cid = int(input('enter the courid: '))
    if cid >= 200 or cid < 208:
        name = input('enter first name: ')
        lname = input('enter last name: ')
        val = (cid, name, lname)
        sql = 'update student set courid = %s where name = %s and lname = %s'
        sql1 = 'select student.ID, student.NAME, student.LNAME,student.COURID, courses.CLASSES from student, courses where student.courid = courses.courid'
        mycur.execute(sql, val)
        mycon.commit()
        mycur.execute(sql1)
        r = mycur.fetchall()
        for i in r:
            for j in i:
                print((str(j)).center(15), end = ' ')
            print()
    else:
        print('not existing')
def feedisplay():
    sql = 'select * from fees'
    mycur.execute(sql)
    r = mycur.fetchall()
    for i in r:
        for j in i:
            print((str(j)).center(15), end = ' ')
        print()
def feeinsert():
    cid = int(input('enter the courid: '))
    if cid >= 200 or cid < 208:
        cid = int(input('enter courses id: '))
        fee = int(input('enter courses fee: '))
        val = (cid, fee)
        sql = 'insert into fees(COURID, FEE), values(%s,%s)'
        sql1 = 'select courid, fee from fees'
        mycur.execute(sql, val)
        mycon.commit()
        mycur.execute(sql1)
        r = mycur.fetchall()
        for i in r:
            for j in i:
                print((str(j)).center(15), end = ' ')
            print()
    else:
        print('not existing')
def installinsert():
    while True:
        try:
            cid = int(input('enter the courid: '))
            if cid >= 200 or cid < 208:
                while True:
                    try:
                        F_install = int(input('enter First installment: '))
                        val = (F_install, cid)
                        sql = 'update fees set FIRSTINSTALL = %s where COURID = %s'
                        S_install = int(input(('enter Second installment: ')))
                        val1 = (S_install, cid)
                        sql1 = 'update fees set SECONDINSTALL = %s where courid = %s'
                        T_install = int(input('enter Third installment: '))
                        val2 = (T_install, cid)
                        sql2 = 'update fees set THIRDINSTALL = %s where courid = %s'
                        sql0 = 'select FIRSTINSTALL, SECONDINSTALL, THIRDINSTALL from fees'
                    except ValueError:
                        print('INVALID ONLY NUMERIC')
                mycur.execute(sql, val)
                mycon.commit()
                mycur.execute(sql1, val1)
                mycon.commit()
                mycur.execute(sql2, val2)
                mycon.commit()
                mycur.execute(sql0)
                r = mycur.fetchall()
                for i in r:
                    for j in i:
                        print((str(j)).center(15), end = ' ')
                    print()
            else:
                print('not existing')
        except ValueError:
            print('INVALID ONLY NUMERIC')
def enquirydisplay():
    sql = 'select * from enquiry'
    mycur.execute(sql)
    r = mycur.fetchall()
    for i in r:
        for j in i:
            print((str(j)).center(15), end = ' ')
        print()

def enquiryinsert():
    while True:
        try:
            no = int(input('enter SLNO: '))
            name = input('enter name: ')
            place = input('enter place: ')
            ph = int(input('enter phone number: '))
            cour = input('enter course: ')
            status = input('enter status: ')
            val = (no, name, place, ph, cour, status)
            sql = 'insert into enquiry values(%s, %s, %s, %s, %s, %s)'
            mycur.execute(sql,val)
            mycon.commit()
            r = mycur.fetchall()
            for i in r:
                for j in i:
                    print((str(j)).center(15), end = ' ')
                print()
        except ValueError:
            print('INVALID ONLY NUMERIC')

def placedisplay():
    sql = 'select * from placement where STATUS = "Placed"'
    mycur.execute(sql)
    r = mycur.fetchall()
    for i in r:
        for j in i:
            print((str(j)).center(15), end = ' ')
        print()

def notplacedisplay():
    sql = 'select * from placement where STATUS = "Not Placed"'
    mycur.execute(sql)
    r = mycur.fetchall()
    for i in r:
        for j in i:
            print((str(j)).center(15), end = ' ')
        print()
def placeinsert():
    while True:
        try:
            ID = int(input('enter Student Id: '))
            name = input('enter name: ')
            cour = input('enter course: ')
            inter = int(input('enter number of interviews: '))
            val = (ID, name, cour,inter)
            sql = 'insert into placement(STUDENTID, NAME, COURSE, INTERVIEWS) values(%s,%s,%s,%s)'
            mycur.execute(sql,val)
            mycon.commit()
            r = mycur.fetchall()
            for i in r:
                for j in i:
                    print((str(j)).center(15), end = ' ')
                print()
        except ValueError:
            print('INVALID ONLY NUMERIC')
def alldisplay():
    sql = 'select * from placement'
    mycur.execute(sql)
    r = mycur.fetchall()
    for i in r:
        for j in i:
            print((str(j)).center(15), end = ' ')
        print()

def updatestatus():
    while True:
        try:
            opt = int(input('enter 1.) For placed, 2.) Not placed or 3.) Exit: '))
            if opt == 1:
                name = input('enter NAME:')
                status = 'PLACED'
                sql0 = 'update placement set STATUS = %s where NAME = %s '
                val = (status, name)
                mycur.execute(sql0,val)
                mycon.commit()
            if opt == 2:
                name = input('enter NAME:')
                status = 'NOT PLACED'
                sql0 = 'update placement set STATUS = %s where NAME = %s '
                val = (status, name)
                mycur.execute(sql0, val)
                mycon.commit()
            if opt >= 3:
                break
        except ValueError:
            print('INVALID ONLY NUMERIC')

def updateadmission():
    while True:
        try:
            opt = int(input(''' 
UPDATE:
1.) FIRST NAME UPDATE
2.) LAST NAME UPDATE
3.) PHONE NUMBER UPDATE
4.) BIRTHDATE UPDATE
5.) JOIN DATE UPDATE
6.) DISTRICT UPDATE
7.) STATE UPDATE
8.) EXIT
Enter option: '''))
            if opt == 1:
                ID = int(input('enter ID: '))
                if ID>= 101 or ID < 106:
                    name = input('enter NAME:')
                    sql0 = 'update student set NAME = %s where ID = %s '
                    val = (name, ID)
                    mycur.execute(sql0,val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')
            if opt == 2:
                ID = int(input('enter ID: '))
                if ID>= 101 or ID < 106:
                    lname = input('enter LAST NAME:')
                    sql0 = 'update student set LNAME = %s where ID = %s '
                    val = (lname, ID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')
            if opt == 3:
                ID = int(input('enter ID: '))
                if ID>= 101 or ID < 106:
                    bdate = input('enter BIRTHDATE(yyyymmdd): ')
                    sql0 = 'update student set BIRTHDATE = %s where ID = %s '
                    val = (bdate, ID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')
            if opt == 4:
                ID = int(input('enter ID: '))
                if ID>= 101 or ID < 106:
                    lname = input('enter LAST NAME:')
                    sql0 = 'update student set JOINDATE = %s where ID = %s '
                    val = (lname, ID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')
            if opt == 5:
                ID = int(input('enter ID: '))
                if ID>= 101 or ID < 106:
                    ph = int(input('enter PHONE NUMBER: '))
                    sql0 = 'update student set PHONENO = %s where ID = %s '
                    val = (ph, ID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')
            if opt == 6:
                ID = int(input('enter ID: '))
                if ID>= 101 or ID < 106:
                    dist = input('enter DISTRICT:')
                    sql0 = 'update student set DISTRICT = %s where ID = %s '
                    val = (dist, ID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')
            if opt == 7:
                ID = int(input('enter ID: '))
                if ID>= 101 or ID < 106:
                    state = input('enter STATE:')
                    sql0 = 'update student set STATE = %s where ID = %s '
                    val = (state, ID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')
            if opt >= 8:
                break
        except ValueError:
            print('INVALID ONLY NUMERIC')

def deladmission():
    while True:
        try:
            ID = int(input('enter id: '))
            if ID >= 100 or ID < 106:
                sql = 'delete from student where ID = %s'
                val = (ID,)
                mycur.execute(sql, val)
                mycon.commit()
                break
            else:
                print('ID DOES NOT EXIST')
        except ValueError:
            print('INVALID NUMERIC ONLY')

def updatecourses():
    while True:
        try:
            opt = int(input('''
UPDATION
1.) CLASS UPDATE
2.) DURATION UPDATE
3.) FEE UPDATE
4.) EXIT
Enter option: '''))
            if opt == 1:
                CID = int(input('enter COURID: '))
                if CID>= 101 or CID < 106:
                    clas = input('enter CLASS:')
                    sql0 = 'update courses set CLASSES = %s where COURID = %s '
                    val = (clas, CID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')
            if opt == 2:
                CID = int(input('enter COURID: '))
                if CID>= 101 or CID < 106:
                    clas = input('enter CLASS:')
                    sql0 = 'update courses set CLASSES = %s where COURID = %s '
                    val = (clas, CID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')
            if opt == 3:
                CID = int(input('enter COURID: '))
                if CID>= 101 or CID < 106:
                    dura = input('enter DURATION:')
                    sql0 = 'update courses set DURATION = %s where COURID = %s '
                    val = (dura, CID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')
            if opt == 4:
                CID = int(input('enter COURID: '))
                if CID>= 101 or CID < 106:
                    fee = int(input('enter CLASS:'))
                    sql0 = 'update courses set FEE = %s where COURID = %s '
                    val = (fee, CID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')
            if opt >= 5:
                break
        except ValueError:
            print('INVALID ONLY NUMERIC')

def delcourses():
    while True:
        try:
            ID = int(input('enter id: '))
            if ID >= 100 or ID < 106:
                sql = 'delete from courses where COURID = %s'
                val = (ID,)
                mycur.execute(sql, val)
                mycon.commit()
                break
            else:
                print('ID DOES NOT EXIST')
        except ValueError:
            print('INVALID NUMERIC ONLY')
def updateenquiry():
    while True:
        try:
            opt = int(input('''
    UPDATION
    1.) NAME UPDATE
    2.) PLACE UPDATE
    3.) PHONE NUMBER UPDATE
    4.) COURSES
    5.) STATUS
    6.) EXIT
    Enter option: '''))
            if opt == 1:
                SLID = int(input('enter SLNO: '))
                if SLID >= 101 or SLID < 106:
                    name = input('enter NAME:')
                    sql0 = 'update enquiry set NAME = %s where SLNO = %s '
                    val = (name, SLID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')
            if opt == 2:
                SLID = int(input('enter SLNO: '))
                if SLID >= 101 or SLID < 106:
                    place = input('enter PLACE:')
                    sql0 = 'update enquiry set PLACE = %s where SLNO = %s '
                    val = (place, SLID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')
            if opt == 3:
                SLID = int(input('enter SLNO: '))
                if SLID >= 101 or SLID < 106:
                    ph = int(input('enter PHONE NUMBER: '))
                    sql0 = 'update enquiry set PHONENO = %s where SLNO = %s '
                    val = (ph, SLID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')

            if opt == 3:
                SLID = int(input('enter SLNO: '))
                if SLID >= 101 or SLID < 106:
                    cour = input('enter COURSES:')
                    sql0 = 'update enquiry set COURSES = %s where SLNO = %s '
                    val = (cour, SLID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')

            if opt == 3:
                SLID = int(input('enter SLNO: '))
                if SLID >= 101 or SLID < 106:
                    status = input('enter STATUS:')
                    sql0 = 'update enquiry set STATUS = %s where SLNO = %s '
                    val = (status, SLID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')

            if opt >= 6:
                break
        except ValueError:
            print('INVALID ONLY NUMERIC')

def delenqiry():
    while True:
        try:
            ID = int(input('enter id: '))
            if ID >= 100 or ID < 106:
                sql = 'delete from enquiry where SLNO = %s'
                val = (ID,)
                mycur.execute(sql, val)
                mycon.commit()
                break
            else:
                print('ID DOES NOT EXIST')
        except ValueError:
            print('INVALID NUMERIC ONLY')
def updateplacement():
    while True:
        try:
            opt = int(input('''
UPDATION
1.) NAME UPDATE
2.) COURSE UPDATE
3.) INTERVIEW UPDATE
4.) EXIT
Enter option: '''))
            if opt == 1:
                SID = int(input('enter STUDENTID: '))
                if SID>= 101 or SID < 106:
                    name = input('enter NAME:')
                    sql0 = 'update placement set NAME = %s where STUDENTID = %s '
                    val = (name, SID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')
            if opt == 2:
                SID = int(input('enter STUDENTID: '))
                if SID>= 101 or SID < 106:
                    place = input('enter PLACE:')
                    sql0 = 'update placement set PLACE = %s where STUDENTID = %s '
                    val = (place, SID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')
            if opt == 3:
                SID = int(input('enter STUDENTID: '))
                if SID>= 101 or SID < 106:
                    inter = input('enter INTERVIEW:')
                    sql0 = 'update placement set INTERVIEWS = %s where STUDENTID = %s '
                    val = (inter, SID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')
            if opt >= 4:
                break
        except ValueError:
            print('INVALID ONLY NUMERIC')
def delplacement():
    while True:
        try:
            ID = int(input('enter id: '))
            if ID >= 100 or ID < 106:
                sql = 'delete from placement where STUDENT4ID = %s'
                val = (ID,)
                mycur.execute(sql, val)
                mycon.commit()
                break
            else:
                print('ID DOES NOT EXIST')
        except ValueError:
            print('INVALID NUMERIC ONLY')

def updatfees():
    while True:
        try:
            opt = int(input('''
    UPDATION
    1.) FEES UPDATE
    2.) FIRST INSTALLMENT UPDATE
    3.) SECOND INSTALLMENT UPDATE
    4.) THIRD INSTALLMENT
    5.) EXIT
    Enter option: '''))
            if opt == 1:
                SLID = int(input('enter COURID: '))
                if SLID >= 101 or SLID < 106:
                    fee = int(input('enter FEES:'))
                    sql0 = 'update fees set NAME = %s where SLNO = %s '
                    val = (fee, SLID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')
            if opt == 2:
                SLID = int(input('enter COURID: '))
                if SLID >= 101 or SLID < 106:
                    ph = int(input('enter FIRST INSTALLMENT: '))
                    sql0 = 'update fees set FIRSTINSTALL = %s where SLNO = %s '
                    val = (ph, SLID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')
            if opt == 3:
                SLID = int(input('enter COURID: '))
                if SLID >= 101 or SLID < 106:
                    ph = int(input('enter SECOND INSTALLMENT: '))
                    sql0 = 'update fees set SECONDINSTALL = %s where SLNO = %s '
                    val = (ph, SLID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')
            if opt == 4:
                SLID = int(input('enter COURID: '))
                if SLID >= 101 or SLID < 106:
                    ph = int(input('enter THIRD INSTALLMENT: '))
                    sql0 = 'update fees set THIRDINSTALL = %s where SLNO = %s '
                    val = (ph, SLID)
                    mycur.execute(sql0, val)
                    mycon.commit()
                    print('UPDATED!')
                else:
                    print('ID DOES NOT EXIST')

            if opt >= 5:
                break
        except ValueError:
            print('INVALID ONLY NUMERIC')
def delfees():
    while True:
        try:
            ID = int(input('enter id: '))
            if ID >= 100 or ID < 106:
                sql = 'delete from fees where COURID = %s'
                val = (ID,)
                mycur.execute(sql, val)
                mycon.commit()
                break
            else:
                print('ID DOES NOT EXIST')
        except ValueError:
            print('INVALID NUMERIC ONLY')


def menu():
    print(''' S-Technologies
1. ADMISSION
2. COURSES
3. ENROLLED COURSES
4. FEES
5. ENQUIRY
6. PLACEMENT
7. EXIT
''')
    while True:
        try:
            opt = int(input('enter option 1/2/3/4/5/6/7: '))
            if opt == 1:
                print('''ADMISSION
1.) Enter details of the Student
2.) Display the details of the Student
3.) Update the details of the student
4.) Delete the details of student
5.) EXIT''')
                while True:
                    try:
                        cho = int(input('enter option (ADMISSION): '))
                        if cho == 1:
                            insert()
                        if cho == 2:
                            display()
                        if cho == 3:
                            updateadmission()
                        if cho == 4:
                            deladmission()
                        if cho >= 5:
                            print('EXITED')
                            break
                    except ValueError:
                        print('INVALID ONLY NUMERIC')

            if opt == 2:
                print('''COURSES
1.) Enter details of the Courses
2.) Display the details of the Courses
3.) Update the placement details for the students
4.) Delete the placement details 
5.) EXIT''')
                while True:
                    try:
                        cho1 = int(input('enter option (COURSES): '))
                        if cho1 == 1:
                            courinsert()
                        if cho1 == 2:
                            courdisplay()
                        if cho1 == 3:
                            updatecourses()
                        if cho1 == 4:
                            delcourses()
                        if cho1 >= 5:
                            print('EXITED')
                            break
                    except ValueError:
                        print('INVALID ONLY NUMERIC')

            if opt == 3:
                print('''COURSES ENROLLED
1.) Display the students with courses 
2.) Enter the courses for students 
3.) EXIT''')
                while True:
                    try:
                        cho2 = int(input('enter option (COURSES ENROLLED): '))
                        if cho2 == 1:
                            enrolldisplay()
                        if cho2 == 2:
                            enrollinsert()
                        if cho2 >= 3:
                            print('EXITED')
                            break
                    except ValueError:
                        print('INVALID ONLY NUMERIC')

            if opt == 4:
                print('''FEES
1.) Display the Fees and Installment
2.) Enter to upload the Fees or Installment
3.) Update the placement details for the students
4.) Delete the placement details 
5.) EXIT ''')
                while True:
                    try:
                        cho3 = int(input('enter option (FEES): '))
                        if cho3 == 1:
                            feedisplay()
                        if cho3 == 2:
                            while True:
                                try:
                                    n = int(input('enter to upload fees(1) or installment(2): '))
                                    if n == 1:
                                        feeinsert()
                                    if n == 2:
                                        installinsert()
                                    if n >= 3:
                                        print('EXITED')
                                        break
                                except ValueError:
                                    print('INVALID ONLY NUMERIC')
                        if cho3 == 3:
                            updatfees()
                        if cho3 == 4:
                            delfees()
                        if cho3 >= 5:
                            print('EXITED')
                            break
                    except ValueError:
                        print('INVALID ONLY NUMERIC')
            if opt == 5:
                print('''ENQUIRY
1.) Display the Enquiry List
2.) Enter the Details of the Enquiry List
3.) Update the placement details for the students
4.) Delete the placement details 
5.) EXIT''')
                while True:
                    try:
                        cho4 = int(input('enter option (ENQUIRY): '))
                        if cho4 == 1:
                            enquirydisplay()
                        if cho4 == 2:
                            enquiryinsert()
                        if cho4 == 3:
                            updateenquiry()
                        if cho4 == 4:
                            delenqiry()
                        if cho4 >= 4:
                            print('EXITED')
                            break
                    except ValueError:
                        print('INVALID ONLY NUMERIC')
            if opt == 6:
                print('''PLACEMENT
1.) Display the Students who got PLACED
2.) Display the Students who didn't get Placed
3.) Display ALL the Students in the Placement section
4.) Enter Placed or Not Placed for students in Placement section
5.) Enter the placement details for the students
6.) Update the placement details for the students
7.) Delete the placement details 
8.) EXIT''')
                while True:
                    try:
                        cho5 = int(input('enter option (PLACEMENT): '))
                        if cho5 == 1:
                            placedisplay()
                        if cho5 == 2:
                            notplacedisplay()
                        if cho5 == 3:
                            alldisplay()
                        if cho5 == 4:
                            updatestatus()
                        if cho5 == 5:
                            placeinsert()
                        if cho5 == 6:
                            updateplacement()
                        if cho5 == 7:
                            delplacement()
                        if cho5 >= 8:
                            print('EXITED')
                            break
                    except ValueError:
                        print('INVALID ONLY NUMERIC')
            if opt >= 7:
                print('EXITED')
                break
        except ValueError:
            print('INVALID ONLY NUMERIC')
            continue
menu()