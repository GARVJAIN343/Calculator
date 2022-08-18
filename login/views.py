from django.shortcuts import render
import mysql.connector as sql
em=''
pwd=''

# Create your views here.
def login(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="root123",database='calculator')
        cursor = m.cursor()
        d = request.POST
        for key,value in d.items():
            if key=="Email":
                em = value
            if key=="Password":
                pwd = value
            
        c = "Select * from user where Email='{}' and Password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request, 'error.html')
        else:
            return render(request,'calculator.html')
        m.commit()
    
    return render(request,'login.html')