#complete Banking System Project Flask App from Scratch 
from flask import Flask,render_template, request, redirect,url_for
from pin_validation import check_security_pin
import sys
app=Flask(__name__)
import sqlite3 
conn=sqlite3.connect('banking.db')
cur=conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS user( id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,email TEXT NOT NULL,mo_no TEXT NOT NULL,father_name TEXT NOT NULL,mother_name TEXT NOT NULL,aadhar TEXT NOT NULL,mpin TEXT NOT NULL)""")
conn.commit()
conn.close()
print("database table created successfully")
@app.route('/',methods=['GET','POST'])
def main():
    if request.method=='POST':
        pin=request.form.get('mpin')
        conn=sqlite3.connect('banking. db')
        cur=conn.cursor()
        cur.execute("SELECT mpin FROM user WHERE  mpin =?",(pin,))
        result=cur.fetchone()
        conn.close()
        if result:
            return redirect ('/signup')
    return render_template('main.html')   
@app.route('/signup',methods=['GET','POST'])    
def signup():
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        mo_no=request.form.get('number')
        father_name=request.form.get('f_name')
        mother_name=request.form.get('m_name')
        mpin=request.form.get('m_pin')
        aadhar=request.form.get('aadhar_no')
        try:
            conn=sqlite3.connect('banking.db')
            
            cur=conn.cursor()
            cur.execute("INSERT INTO user(name,email,mo_no,father_name,mother_name,aadhar, mpin)VALUES (?,?,?,?,?,?,?)",(name,email,mo_no,father_name,mother_name,aadhar,mpin))
            conn.commit()
        except sqlite3.IntegrityError:
            return "user already exists"   
        finally:
            conn.close()
        return redirect('/')  
    return render_template('signup.html')     
    
if __name__==('__main__'):
                app.run(debug=True)
