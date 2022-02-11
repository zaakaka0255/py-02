
from tkinter import *
main = Tk()
main.geometry("800x600")
main.title("โปรแกรมหาพื้นที่สามเหลี่ยม โดย ภาสกรณ์ แสนปาง")

lb1 = Label(main, text="คะแนนเก็บ ", font = ("Cooper Blac", 18))
lb1.place(x=20, y=50)
lb2 = Label(main, text="กลางภาค ", font = ("Cooper Blac", 18))
lb2.place(x=100, y=80,width=200, height=30)
lb3 = Label(main, text="ปลายภาค ", font = ("Cooper Blac", 18))
lb3.place(x=150, y=90,)
lb4 = Label(main, text="จิตพิสัย ", font = ("Cooper Blac", 18))
lb4.place(x=200, y=110)
lb5 = Label(main, text="คำตอบ", font = ("Cooper Blac", 18))
lb5.place(x=250, y=130)
lb6 = Label(main, font = ("Cooper Blac", 18))
lb6.place(x=300, y=150)