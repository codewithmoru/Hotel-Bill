from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("hotel bill")
root["bg"] = "red"
operator = ""
text_input = StringVar()


def add():
	f = text_input1.get()
	s = text_input2.get()
	t = text_input3.get()
	fk = text_input4.get()
	fi = text_input5.get()
	si = text_input6.get()
	se = text_input7.get()
	e = text_input8.get()
	n = text_input9.get()
	te = text_input10.get()
	el = text_input11.get()
	tw = text_input12.get()
	th = text_input13.get()
	ft = text_input14.get()
	fn = text_input15.get()
	lN = text_input16.get()
	e2 = text_input.get()
	messagebox.showinfo(
	    "Total",
	    ('Name :', (lN), 'Mobail No :', (e2), '\t\n\n=', f * 5 + s * 50 +
	     t * 50 + fk * 120 + fi * 150 + si * 20 + se * 15 + e * 30 + n * 20 +
	     te * 20 + el * 30 + tw * 200 + th * 250 + ft * 200 + fn * 20))


def bttnClear():
	global operator
	operator = ""
	text_input1.set("")
	text_input2.set("")
	text_input3.set("")
	text_input4.set("")
	text_input5.set("")
	text_input6.set("")
	text_input7.set("")
	text_input8.set("")
	text_input9.set("")
	text_input10.set("")
	text_input11.set("")
	text_input12.set("")
	text_input13.set("")
	text_input14.set("")
	text_input15.set("")
	text_input16.set("")
	text_input.set("")


messagebox.showwarning("warning", "Place Roted Your Divice")


def tap():
	messagebox.showinfo("About", 'Mr.Moreshwar Mahale')


#declaring variables
text_input1 = IntVar()
text_input2 = IntVar()
text_input3 = IntVar()
text_input4 = IntVar()
text_input5 = IntVar()
text_input6 = IntVar()
text_input7 = IntVar()
text_input8 = IntVar()
text_input9 = IntVar()
text_input10 = IntVar()
text_input11 = IntVar()
text_input12 = IntVar()
text_input13 = IntVar()
text_input14 = IntVar()
text_input15 = IntVar()
text_input16 = StringVar()
text_input = IntVar()

l1 = Label(root, text="Mahale hotel bill", bg="blue", fg="white",
           bd="3px").pack()

lN = Label(root, text="Name :", bg="black", fg="white",
           bd="2px").place(x="2", y="100")

e1 = Entry(root, bd="2px", width="25",
           textvariable=text_input16).place(x="190", y="100")

la = Label(root, text="Mobail NO :", bg="black", fg="white",
           bd="2px").place(x="920", y="100")

e2 = Entry(root, bd="2px", width="15", textvariable=text_input).place(x="1200",
                                                                      y="100")

l = Label(root, text="Veg Food :", bg="blue", fg="white",
          bd="3px").place(x="2", y="200")

l2 = Label(root,
           text="Roti",
           bg="black",
           fg="white",
           bd="2px",
           height="1",
           width="4").place(x="5", y="300")

e1 = Entry(root, bd="2px", width="5", textvariable=text_input1).place(x="230",
                                                                      y="300")

l3 = Label(root,
           text="Daal",
           bg="black",
           fg="white",
           bd="2px",
           height="1",
           width="4").place(x="5", y="400")

e2 = Entry(root, bd="2px", width="5", textvariable=text_input2).place(x="230",
                                                                      y="400")

l4 = Label(root,
           text="Chawal",
           bg="black",
           fg="white",
           bd="2px",
           height="1",
           width="6").place(x="5", y="500")

e3 = Entry(root, bd="2px", width="5", textvariable=text_input3).place(x="230",
                                                                      y="500")

l5 = Label(root,
           text="Paneer",
           bg="black",
           fg="white",
           bd="2px",
           height="1",
           width="5").place(x="5", y="600")

e4 = Entry(root, bd="2px", width="5", textvariable=text_input4).place(x="230",
                                                                      y="600")

l6 = Label(root,
           text="Kajukatli",
           bg="black",
           fg="white",
           bd="2px",
           height="1",
           width="7").place(x="5", y="700")

e5 = Entry(root, bd="2px", width="5", textvariable=text_input5).place(x="230",
                                                                      y="700")

l = Label(root, text="Drinks :", bg="blue", fg="white",
          bd="3px").place(x="600", y="200")

l2 = Label(root,
           text="Lassi",
           bg="black",
           fg="white",
           bd="2px",
           height="1",
           width="4").place(x="600", y="300")

e1 = Entry(root, bd="2px", width="5", textvariable=text_input6).place(x="890",
                                                                      y="300")

l3 = Label(root,
           text="Coffee",
           bg="black",
           fg="white",
           bd="2px",
           height="1",
           width="4").place(x="600", y="400")

e2 = Entry(root, bd="2px", width="5", textvariable=text_input7).place(x="890",
                                                                      y="400")

l4 = Label(root,
           text="Faluda",
           bg="black",
           fg="white",
           bd="2px",
           height="1",
           width="6").place(x="600", y="500")

e3 = Entry(root, bd="2px", width="5", textvariable=text_input8).place(x="890",
                                                                      y="500")

l5 = Label(root,
           text="Papssi",
           bg="black",
           fg="white",
           bd="2px",
           height="1",
           width="5").place(x="600", y="600")

e4 = Entry(root, bd="2px", width="5", textvariable=text_input9).place(x="890",
                                                                      y="600")

l6 = Label(root,
           text="Badam Milk",
           bg="black",
           fg="white",
           bd="2px",
           height="1",
           width="9").place(x="600", y="700")

e5 = Entry(root, bd="2px", width="5", textvariable=text_input10).place(x="890",
                                                                       y="700")

l = Label(root, text="Nonvage Food :", bg="blue", fg="white",
          bd="3px").place(x="1150", y="200")

l2 = Label(root,
           text="Biryani",
           bg="black",
           fg="white",
           bd="2px",
           height="1",
           width="5").place(x="1200", y="300")

e1 = Entry(root, bd="2px", width="5",
           textvariable=text_input11).place(x="1500", y="300")

l3 = Label(root,
           text="Cikan",
           bg="black",
           fg="white",
           bd="2px",
           height="1",
           width="4").place(x="1200", y="400")

e2 = Entry(root, bd="2px", width="5",
           textvariable=text_input12).place(x="1500", y="400")

l4 = Label(root,
           text="Matton",
           bg="black",
           fg="white",
           bd="2px",
           height="1",
           width="6").place(x="1200", y="500")

e3 = Entry(root, bd="2px", width="5",
           textvariable=text_input13).place(x="1500", y="500")

l5 = Label(root,
           text="Legpise",
           bg="black",
           fg="white",
           bd="2px",
           height="1",
           width="5").place(x="1200", y="600")

e4 = Entry(root, bd="2px", width="5",
           textvariable=text_input14).place(x="1500", y="600")

l6 = Label(root,
           text="BoilEgas",
           bg="black",
           fg="white",
           bd="2px",
           height="1",
           width="9").place(x="1200", y="700")

e5 = Entry(root, bd="2px", width="5",
           textvariable=text_input15).place(x="1500", y="700")

l = Button(root, text="Total :", bg="blue", fg="white", bd="3px",
           command=add).place(x="5", y="850")

but1 = Button(root,
              text="clear",
              bg="blue",
              fg="white",
              bd='2px',
              command=bttnClear).place(x="400", y="850")

but2 = Button(root,
              text="Exit",
              bg="blue",
              fg="white",
              bd='2px',
              command=root.quit).place(x="800", y="850")

but = Button(root, text="?", bg="blue", fg="white", bd='2px',
             command=tap).place(x="2059", y="50")

l1 = Label(root, text='FOOD', bg='yellow').place(x='1750', y='50')
l1 = Label(root, text='Roti :  5rs', bg='red').place(x='1750', y='100')
l1 = Label(root, text='Daal :  50rs', bg='red').place(x='1750', y='150')
l1 = Label(root, text='Chawal : 50rs', bg='red').place(x='1750', y='200')
l1 = Label(root, text='Paneer : 120rs', bg='red').place(x='1750', y='250')
l1 = Label(root, text='Kajukatli : 150rs', bg='red').place(x='1750', y='300')
l1 = Label(root, text='DRINKS', bg='yellow').place(x='1750', y='350')
l1 = Label(root, text='Lassi : 20rs', bg='red').place(x='1750', y='400')
l1 = Label(root, text='Coffee : 15rs', bg='red').place(x='1750', y='450')
l1 = Label(root, text='Faluda : 30rs', bg='red').place(x='1750', y='500')
l1 = Label(root, text='Papssi : 20rs', bg='red').place(x='1750', y='550')
l1 = Label(root, text='Badam Milk : 20rs', bg='red').place(x='1750', y='600')
l1 = Label(root, text='NONVAGE FOOD', bg='yellow').place(x='1750', y='650')
l1 = Label(root, text='Biryani : 30rs', bg='red').place(x='1750', y='700')
l1 = Label(root, text='Chikan : 200rs', bg='red').place(x='1750', y='750')
l1 = Label(root, text='Matton : 250rs', bg='red').place(x='1750', y='800')
l1 = Label(root, text='Legpise : 200rs', bg='red').place(x='1750', y='850')
l1 = Label(root, text='BoilEages : 20rs', bg='red').place(x='1750', y='900')

root.mainloop()
