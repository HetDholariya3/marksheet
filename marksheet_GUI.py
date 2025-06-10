import tkinter as tk
from tkinter import messagebox
import mysql.connector


class InvalidEnrollmentError(Exception):
    pass

class InvalidMarkError(Exception):
    pass

class InvalidSemesterError(Exception):
    pass

root = tk.Tk()
root.geometry("900x800")
root.title("Student Marksheet")

header_label = tk.Label(root, text="STUDENT MARKSHEET", bg="black", fg="white", font=("calibri", 30, "bold"), width=30)
header_label.grid(row=0, column=0, columnspan=2, sticky="n")

tk.Label(root, text='First Name', font=('Arial', 14), anchor="w", width=15).grid(row=1, column=0, sticky="w")
tk.Label(root, text='Last Name', font=('Arial', 14), anchor="w", width=15).grid(row=1, column=1, sticky="w")

e1 = tk.Entry(root, font=('Arial', 12), bd=2, relief="solid", width=25)
e2 = tk.Entry(root, font=('Arial', 12), bd=2, relief="solid", width=25)
e1.grid(row=2, column=0)
e2.grid(row=2, column=1)

tk.Label(root, text='Enrollment No.', font=('Arial', 14), anchor="w", width=20).grid(row=3, column=0, sticky="w")
tk.Label(root, text='Division', font=('Arial', 14), anchor="w", width=20).grid(row=3, column=1, sticky="w")
tk.Label(root, text='sem', font=('Arial', 14), anchor="w", width=20).grid(row=3, column=2, sticky="w")

enroll_entry = tk.Entry(root, font=('Arial', 12), bd=2, relief="solid", width=25)
div_entry = tk.Entry(root, font=('Arial', 12), bd=2, relief="solid", width=25)
sem_entry = tk.Entry(root, font=('Arial', 12), bd=2, relief="solid", width=25)
enroll_entry.grid(row=4, column=0)
div_entry.grid(row=4, column=1)
sem_entry.grid(row=4, column=2)

tk.Label(root, text='DS Marks', font=('Arial', 14), anchor="w", width=20).grid(row=5, column=0, sticky="w")
tk.Label(root, text='Laravel Marks', font=('Arial', 14), anchor="w", width=20).grid(row=6, column=0, sticky="w")
tk.Label(root, text='C Language Marks', font=('Arial', 14), anchor="w", width=20).grid(row=7, column=0, sticky="w")
tk.Label(root, text='Java Marks', font=('Arial', 14), anchor="w", width=20).grid(row=8, column=0, sticky="w")
tk.Label(root, text='Python Marks', font=('Arial', 14), anchor="w", width=20).grid(row=9, column=0, sticky="w")

m1 = tk.Entry(root, font=('Arial', 12), bd=2, relief="solid", width=25)
m2 = tk.Entry(root, font=('Arial', 12), bd=2, relief="solid", width=25)
m3 = tk.Entry(root, font=('Arial', 12), bd=2, relief="solid", width=25)
m4 = tk.Entry(root, font=('Arial', 12), bd=2, relief="solid", width=25)
m5 = tk.Entry(root, font=('Arial', 12), bd=2, relief="solid", width=25)

m1.grid(row=5, column=1)
m2.grid(row=6, column=1)
m3.grid(row=7, column=1)
m4.grid(row=8, column=1)
m5.grid(row=9, column=1)


my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="marksheet"
)
# print(my_db)
mycursor = my_db.cursor()
# mycursor.execute("create database marksheet")
# mycursor.execute("create table results (fname varchar(50), lname varchar(50), enrollment int(20), division varchar(10), semester int(10), ds float(50), laravel float(50), c_language float(50), java float(50), python float(50))")

result_label = tk.Label(root, font=('Arial', 12), bd=2, relief="solid", width=50, height=16)
result_label.grid(row=14, column=3)

# Functions
def insert():
    try:
        fname = e1.get()
        lname = e2.get()
        enrollment = enroll_entry.get()
        division = div_entry.get().upper()
        semester = sem_entry.get()
        
        if len(enrollment) != 14 or not enrollment.isdigit():
            raise InvalidEnrollmentError("Enrollment number must be exactly 14 digits.")
        
        try:
            semester = int(semester)
            if semester not in [1, 2, 3, 4, 5, 6]:
                raise InvalidSemesterError("Semester must be between 1 and 6.")
        except ValueError:
            raise InvalidSemesterError("Semester must be a valid number between 1 and 6.")
        
        try:
            ds = float(m1.get())
            laravel = float(m2.get())
            c_language = float(m3.get())
            java = float(m4.get())
            python = float(m5.get())
                        
            if ds < 0 or ds > 100:
                raise InvalidMarkError(f"Invalid Marks! DS Marks must be a number between 0 and 100.")
            if laravel < 0 or laravel > 100:
                raise InvalidMarkError(f"Invalid Marks! Laravel Marks must be a number between 0 and 100.")
            if c_language < 0 or c_language > 100:
                raise InvalidMarkError(f"Invalid Marks! C Language Marks must be a number between 0 and 100.")
            if java < 0 or java > 100:
                raise InvalidMarkError(f"Invalid Marks! Java Marks must be a number between 0 and 100.")
            if python < 0 or python > 100:
                raise InvalidMarkError(f"Invalid Marks! Python Marks must be a number between 0 and 100.")
        except ValueError:
            raise InvalidMarkError("Please enter valid numeric values for all marks.")
        
        sql = "INSERT INTO results(fname, lname, enrollment, division, semester, ds, laravel, c_language, java, python) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (fname, lname, enrollment, division, semester, ds, laravel, c_language, java, python)
        mycursor.execute(sql, val)
        my_db.commit()
        messagebox.showinfo("Success", "Record inserted successfully!")
        
    except InvalidEnrollmentError as e:
        messagebox.showerror("Invalid Enrollment", str(e))
    except InvalidMarkError as e:
        messagebox.showerror("Invalid Marks", str(e))
    except InvalidSemesterError as e:
        messagebox.showerror("Invalid Semester", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

def show():
    try:
        mycursor.execute("SELECT * FROM results")
        result = mycursor.fetchall()
        display_text = ""
        for i in result:
            display_text += f"{i}\n"
        messagebox.showinfo("Results", display_text)
    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")

def update():
    try:
        fname = input("Enter name for which you want to update details: ")        
        new_enroll = input("Enternew enrollment number (must be 14 digits): ")
        if len(new_enroll) != 14 or not new_enroll.isdigit():
            raise InvalidEnrollmentError("Enrollment number exactly 14 digits.")
        
        new_division = input("Enter new division: ")
        new_semester = input("Enter new semester (1-6): ")

        try:
            new_semester = int(new_semester)
            if new_semester not in [1, 2, 3, 4, 5, 6]:
                raise InvalidSemesterError("Semester must be between 1 and 6.")
        except ValueError:
            raise InvalidSemesterError("Semester must be a valid number between 1 and 6.")

        new_ds = float(input("Enter new DS Marks (0-100): "))
        new_laravel = float(input("Enter new Laravel Marks (0-100): "))
        new_c = float(input("Enter the C Language Marks (0-100): "))
        new_java = float(input("Enter new Java Marks (0-100): "))
        new_python = float(input("Enter new Python Marks (0-100): "))

        try:
            if new_ds < 0 or new_ds > 100:
                raise InvalidMarkError(f"Invalid Marks! DS Marks must be a number between 0 and 100.")
            if new_laravel < 0 or new_laravel > 100:
                raise InvalidMarkError(f"Invalid Marks! Laravel Marks must be a number between 0 and 100.")
            if new_c < 0 or new_c > 100:
                raise InvalidMarkError(f"Invalid Marks! C Language Marks must be a number between 0 and 100.")
            if new_java < 0 or new_java > 100:
                raise InvalidMarkError(f"Invalid Marks! Java Marks must be a number between 0 and 100.")
            if new_python < 0 or new_python > 100:
                raise InvalidMarkError(f"Invalid Marks! Python Marks must be a number between 0 and 100.")
        except ValueError:
            raise InvalidMarkError("Please enter valid numeric values for all marks.")
        
        sql = "update results set enrollment = %s, division = %s, semester = %s, ds = %s, laravel = %s, c_language = %s, java = %s, python = %s where fname = %s "
        val = (new_enroll, new_division, new_semester, new_ds, new_laravel, new_c, new_java, new_python, fname)
        mycursor.execute(sql,val)
        my_db.commit()
        
        messagebox.showinfo("Success", f"Student record for {fname} updated successfully.")
    except InvalidEnrollmentError as e:
        messagebox.showerror("Invalid Enrollment", str(e))
    except InvalidSemesterError as e:
        messagebox.showerror("Invalid Semester", str(e))
    except InvalidMarkError as e:
        messagebox.showerror("Invalid Marks", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"error occurred: {str(e)}")

def delete():
    try:
        fname = input("Enter first name of the student to delete: ")
        sql = "DELETE FROM results WHERE fname = %s"
        val = (fname,)
        mycursor.execute(sql, val)
        my_db.commit()
        messagebox.showinfo("Success", f"Student record for {fname} deleted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")

def show_result():
    try:
        fname = input("Enter name for make result ")
        mycursor.execute("SELECT * FROM results WHERE fname = %s", (fname,))
        result = mycursor.fetchone()

        if result:
            #extract marks 
            mark1 = result[5]  
            mark2 = result[6]  
            mark3 = result[7]  
            mark4 = result[8]  
            mark5 = result[9]  

            def check_pass_fail(mark):
                if mark >= 30:
                    return "Pass" 
                else:
                    return "Fail"

            pass_fail_1 = check_pass_fail(mark1)
            pass_fail_2 = check_pass_fail(mark2)
            pass_fail_3 = check_pass_fail(mark3)
            pass_fail_4 = check_pass_fail(mark4)
            pass_fail_5 = check_pass_fail(mark5)

            total_marks = mark1 + mark2 + mark3 + mark4 + mark5
            percentage = (total_marks / 500) * 100

            #overall result
            if pass_fail_1 == "Pass" and pass_fail_2 == "Pass" and pass_fail_3 == "Pass" and pass_fail_4 == "Pass" and pass_fail_5 == "Pass":
                overall_result = "Pass"
            else:
                overall_result = "Fail"

            full_name = f"{result[0]} {result[1]}"  
            enrollment_no = result[2]  
            division = result[3]  
            semester = result[4]
            
            
            if overall_result == "Fail":
                result_label.config(
                    text=f"Name: {full_name}\nEnrollment No: {enrollment_no}\nDivision: {division}\nSemester: {semester}\n\n"
                        f"DS Marks: {mark1} | {pass_fail_1}\n"
                        f"Laravel Marks: {mark2} | {pass_fail_2}\n"
                        f"C Language Marks: {mark3} | {pass_fail_3}\n"
                        f"Java Marks: {mark4} | {pass_fail_4}\n"
                        f"Python Marks: {mark5} | {pass_fail_5}\n\n"
                        f"Total Marks: {total_marks}\n"
                        f"Percentage: {percentage:.2f}%\n"
                        f"Overall Result: {overall_result}",
                    fg="red"
                )
            else:
                result_label.config(
                    text=f"Name: {full_name}\nEnrollment No: {enroll_entry.get()}\nDivision: {division}\nSemester: {semester}\n\n"
                        f"DS Marks: {mark1} | {pass_fail_1}\n"
                        f"Laravel Marks: {mark2} | {pass_fail_2}\n"
                        f"C Language Marks: {mark3} | {pass_fail_3}\n"
                        f"Java Marks: {mark4} | {pass_fail_4}\n"
                        f"Python Marks: {mark5} | {pass_fail_5}\n\n"
                        f"Total Marks: {total_marks}\n"
                        f"Percentage: {percentage:.2f}%\n"
                        f"Overall Result: {overall_result}",
                    fg="green"
                )
        else:
            messagebox.showerror("Error", f"Student with first name '{fname}' not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Buttons
btn_insert = tk.Button(root, text="Insert Record", font=('Arial', 14), command=insert)
btn_insert.grid(row=10, column=0, columnspan=2, pady=10)

btn_show = tk.Button(root, text="Show All Records", font=('Arial', 14), command=show)
btn_show.grid(row=11, column=0, columnspan=2, pady=10)

btn_update = tk.Button(root, text="Update Record", font=('Arial', 14), command=update)
btn_update.grid(row=12, column=0, columnspan=2, pady=10)

btn_delete = tk.Button(root, text="Delete Record", font=('Arial', 14), command=delete)
btn_delete.grid(row=13, column=0, columnspan=2, pady=10)

btn_show_result = tk.Button(root, text="Show Result", font=('Arial', 14), command=show_result)
btn_show_result.grid(row=14, column=0, columnspan=2, pady=10)

root.mainloop()
