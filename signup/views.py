from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
s=''
em=''
pwd=''

# Create your views here.
def signup(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="root123",database='calculator')
        cursor = m.cursor()
        d = request.POST
        for key,value in d.items():
            if key=="FirstName":
                fn = value
            if key=="LastName":
                ln = value
            if key=="Email":
                em = value
            if key=="Password":
                pwd = value
            
        c = "Insert into calculator.user Values('{}','{}','{}','{}')".format(fn,ln,em,pwd)
        cursor.execute(c)
        m.commit()
    
    return render(request,'signup.html')