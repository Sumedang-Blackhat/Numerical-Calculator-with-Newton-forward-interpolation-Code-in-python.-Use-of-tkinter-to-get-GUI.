```
from tkinter import*

cal=Tk()
cal.title("Calculator")
operator=""
text_Input=StringVar()
text_Input2=StringVar()
ment1=StringVar()
ment2=StringVar()
ment3=StringVar()
ment4=StringVar()
n=0
i=0
j=0
x=[]
y=[[]]

def btnClick(numbers):
   global operator
   operator=operator+str(numbers)
   text_Input.set(operator)

def btnClearDisplay():
   global operator
   operator=""
   text_Input.set("")

def btnEqualsInput():
   global operator
   sumup=str(eval(operator))
   text_Input.set(sumup)
   operator=sumup

def btnStore():
   global i
   print(x)
   x[i]=(float(ment2.get()))
   ment2.set("")
   print(x)
   print(i)
   i=i+1
   b2=Button(cal,padx=8,pady=6,fg='yellow',font=('Ubuntu',14,'bold'),text="Store x"+str(i),command=btnStore,bg='brown').grid(row=11,column=3)

def btnStoren():
   global n
   global x
   global y
   n=int(ment1.get())
   x=[0]*n
   y = [[0 for i in range(n)] for j in range(n)]
   print(x)
   print(y)
   l3=Label(cal,text="Enter "+str(n)+" x values").grid(row=11,column=1)
   l4=Label(cal,text="Enter "+str(n)+" y values").grid(row=12,column=1)

def btnStore1():
   global j
   print(y)
   y[j][0]=(float(ment3.get()))
   ment3.set("")
   print(y)
   print(j)
   j=j+1
   b3=Button(cal,padx=8,pady=6,fg='yellow',font=('Ubuntu',14,'bold'),text="Store y"+str(j),command=btnStore1,bg='brown').grid(row=12,column=3)

def btnStore2():
   value=float(ment4.get())
   for i in range(1,n):
       for j in range(n-i):
           y[j][i]=y[j+1][i-1]-y[j][i-1]
   sum = y[0][0]
   u = (value-x[0])/(x[1]-x[0])
   for i in range(1,n):
       sum=sum+(u_cal(u,i)*y[0][i])/fact(i)
   text_Input2.set(str(round(sum,6)))

def u_cal(u, n):
   temp = u
   for i in range(1, n):
       temp = temp * (u - i)
   return temp

def fact(n):
   f = 1
   for i in range(2, n + 1):
       f *= i
   return f

txtDisplay=Entry(cal,font=('Ubuntu',20,'bold'),textvariable=text_Input,bd=5,insertwidth=20,bg='brown',justify='right').grid(columnspan=10)

btn7=Button(cal,padx=8,bd=2,fg='yellow',font=('Ubuntu',20,'bold'),text="7",command=lambda:btnClick(7),bg='brown').grid(row=1,column=0)
btn8=Button(cal,padx=8,bd=2,fg='yellow',font=('Ubuntu',20,'bold'),text="8",command=lambda:btnClick(8),bg='brown').grid(row=1,column=1)
btn9=Button(cal,padx=8,bd=2,fg='yellow',font=('Ubuntu',20,'bold'),text="9",command=lambda:btnClick(9),bg='brown').grid(row=1,column=2)
Addition=Button(cal,padx=8,bd=2,fg="yellow",font=('Ubuntu',20,'bold'),text="+",command=lambda:btnClick("+"),bg='brown').grid(row=1,column=3)
#=======================================================================================================

btn4=Button(cal,padx=8,bd=2,fg='yellow',font=('Ubuntu',20,'bold'),text="4",command=lambda:btnClick(4),bg='brown').grid(row=2,column=0)
btn5=Button(cal,padx=8,bd=2,fg='yellow',font=('Ubuntu',20,'bold'),text="5",command=lambda:btnClick(5),bg='brown').grid(row=2,column=1)
btn6=Button(cal,padx=8,bd=2,fg='yellow',font=('Ubuntu',20,'bold'),text="6",command=lambda:btnClick(6),bg='brown').grid(row=2,column=2)
Subtraction=Button(cal,padx=8,bd=2,fg="yellow",font=('Ubuntu',20,'bold'),text="-",command=lambda:btnClick("-"),bg='brown').grid(row=2,column=3)

#=======================================================================================================

btn1=Button(cal,padx=8,bd=2,fg='yellow',font=('Ubuntu',20,'bold'),text="1",command=lambda:btnClick(1),bg='brown').grid(row=3,column=0)
btn2=Button(cal,padx=8,bd=2,fg='yellow',font=('Ubuntu',20,'bold'),text="2",command=lambda:btnClick(2),bg='brown').grid(row=3,column=1)
btn3=Button(cal,padx=8,bd=2,fg='yellow',font=('Ubuntu',20,'bold'),text="3",command=lambda:btnClick(3),bg='brown').grid(row=3,column=2)
Multiply=Button(cal,padx=8,bd=2,fg="yellow",font=('Ubuntu',20,'bold'),text="*",command=lambda:btnClick("*"),bg='brown').grid(row=3,column=3)

#=======================================================================================================
btn0=Button(cal,padx=8,pady=6,bd=2,fg='yellow',font=('Ubuntu',20,'bold'),text="0",command=lambda:btnClick(0),bg='brown').grid(row=4,column=0)
btnClear=Button(cal,padx=8,pady=6,bd=2,fg='yellow',font=('Ubuntu',20,'bold'),text="C",command=btnClearDisplay,bg='brown').grid(row=4,column=1)
btnEquals=Button(cal,padx=8,pady=6,bd=2,fg='yellow',font=('Ubuntu',20,'bold'),text="=",command=btnEqualsInput,bg='brown').grid(row=4,column=2)
Division=Button(cal,padx=8,pady=6,bd=2,fg="yellow",font=('Ubuntu',20,'bold'),text="/",command=lambda:btnClick("/"),bg='brown').grid(row=4,column=3)

#___________________________________________________________________________________________________________
#-----------------------------------------------------------------------------------------------------------

l1=Label(cal,text="Application of Newton Forward Interpolation",font=('Ubuntu',20,'bold')).grid(row=7,columnspan=4)
txtDisplay2=Entry(cal,font=('Ubuntu',20,'bold'),textvariable=text_Input2,bd=5,insertwidth=10,bg='brown',justify='right').grid(row=15,columnspan=4)
l2=Label(cal,text="No. of x,y values to enter ?").grid(row=10,column=1)
e1=Entry(cal,bd=10,textvariable=ment1).grid(row=10,column=2)
b1=Button(cal,padx=8,pady=6,fg='yellow',font=('Ubuntu',14,'bold'),text="Store n",command=btnStoren,bg='brown').grid(row=10,column=3)

l3=Label(cal,text="Enter x values").grid(row=11,column=1)
e2=Entry(cal,bd=10,textvariable=ment2).grid(row=11,column=2)
b2=Button(cal,padx=8,pady=6,fg='yellow',font=('Ubuntu',14,'bold'),text="Store x"+str(0),command=btnStore,bg='brown').grid(row=11,column=3)

l4=Label(cal,text="Enter y values").grid(row=12,column=1)
e3=Entry(cal,bd=10,textvariable=ment3).grid(row=12,column=2)
b3=Button(cal,padx=8,pady=6,fg='yellow',font=('Ubuntu',14,'bold'),text="Store y"+str(0),command=btnStore1,bg='brown').grid(row=12,column=3)

l5=Label(cal,text="Enter value of x for which value is to be found").grid(row=13,column=1)
e4=Entry(cal,bd=10,textvariable=ment4).grid(row=13,column=2)
b4=Button(cal,padx=8,pady=6,fg='yellow',font=('Ubuntu',14,'bold'),text="Set&Go",command=btnStore2,bg='brown').grid(row=13,column=3)

cal.mainloop()
```