from django.shortcuts import render
import mysql.connector as sql
input='',
output=''

# Create your views here.
def calculation(request):
    global input,output
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="root123",database='calculator')
        cursor = m.cursor()
        d = request.POST
        for key,value in d.items():
            if key=="input":
                input = value
            if key=="output":
                output = value
            
        c = "Insert into calculator.result Values('{}','{}')".format(input,output)
        cursor.execute(c)
        m.commit()
    
    return render(request,'calculator.html')  