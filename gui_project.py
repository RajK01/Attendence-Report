from tkinter import *
import os
import glob
import csv
import codecs
        

class MyWindow:
    def __init__(self, master):
        self.master = master
        master.title("Student Attendance Report")
        self.tname_data = StringVar()

        Label(self.master, text="Genrate Attendance: ").grid(row=0, column=0,padx=10)
        Label(self.master, text="Enter name of Teacher:  ").grid(row=1,column=0,padx=10)
        Entry(root, textvariable=self.tname_data, width=40, font=('calibre', 10, 'normal')).grid(row=1,column=1, columnspan=2)
        Button(root, text="Generate Attendance", command=self.generate_attendance).grid(row=1,column=3, padx=10)

    def generate_attendance(self):
        if (os.path.exists('Student_Attendance2.csv')):
            Label(self.master, text = "Report already created!!", fg='red').grid(row=1,column=4, padx=10)
        else:
            pathname = os.getcwd()
            csv_files = glob.glob(os.path.join(pathname, "*.csv"))

            # Count csv files in current folder to get Total Working days
            total_attendance = len(csv_files)

            teacher = self.tname_data.get()
            data = []  # Contains non-repeated all attendance data
            dict_student = {}  # To store student data
            for file in csv_files:
                csv_reader = csv.reader(codecs.open(file, 'r', 'UTF-16le'))
                next(csv_reader)
                stud_present = [] # Attendance of that day
                for line in csv_reader:
                    row = line[0].split("\t")
                    if row[0] not in stud_present:
                        stud_present.append(row[0])
                        row.append(line[1])
                        data.append(row)

                        # to get total students dict
                        if row[0] not in dict_student.keys() and 'Guest' not in row[0] and row[0] != teacher:
                            dict_student[row[0]] = [0]
            
            # calculate present attendace
            for row in data:
                if row[0] in dict_student.keys():
                    dict_student[row[0]][0] += 1

            print("No. of Students: ", len(dict_student))

            # to calculate rest data
            for attendance in dict_student.values():
                # calculate absent days
                present = attendance[0]
                absent = total_attendance-present
                attendance.append(absent)

                # calculate percentage
                percent = round((present/total_attendance)*100, 2)
                attendance.append(percent)

            # Creating rows/lines to write in csv
            rows = [[name] + datalist for name, datalist in dict_student.items()]
            with open('Student_Attendance2.csv', 'w', newline='') as new_file:
                csv_writer = csv.writer(new_file)
                csv_writer.writerow(["Name", "Present", "Absent", "Percentage"])
                for row in rows:
                    csv_writer.writerow(row)
                Label(self.master, text = "Attendace report created Successfully!!", fg='green').grid(row=1,column=4, padx=10) 
        Button(self.master, text="Get Specific Student\n Attendance Details", command=self.get_attendance).grid(row=3,column=0,padx=10, pady=(6,40))

    def get_attendance(self):
        self.clicked = StringVar()
        Label(self.master,text="Select the Student Name: ").grid(row=4, column=0)
        Entry( self.master , textvariable= self.clicked ).grid(row=4, column=1)
        Button( self.master , text = "Get Details", command=self.show).grid(row=4, column=2)

    def show(self):
        details = [["Name", "Present","Absent", "Percent"]]
        csv_reader = csv.reader(open('Student_Attendance2.csv', 'r'))
        next(csv_reader)
        for line in csv_reader:
            if (line[0]==self.clicked.get()):
                details.append(line)

        trows = len(details)
        tcols = len(details[0])
        for i in range(5, trows+5):
            for j in range(tcols):
                self.cell = Entry(root)
                # print(i,j)
                self.cell.grid(row=i,column=j)
                self.cell.insert(END, details[i-5][j])

root = Tk()
root.geometry("900x600")
my_gui = MyWindow(root)

root.mainloop()
