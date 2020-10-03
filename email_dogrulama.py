from tkinter import *
import tkinter as tk
import smtplib
import random
import string

root = tk.Tk()
root.title('Email Doğrulama')
root.geometry('300x200')
root.maxsize(300,200)
root.minsize(300,200)

smtp = smtplib.SMTP('smtp.gmail.com' , 587)
smtp.starttls()
smtp.login("mail" , "sifre")
mail_adres = "mail_adresi"


def dogrulama_kodu():
    alfabe = string.ascii_letters + string.digits
    uzunluk = 9
    p =  ''.join(random.choice(alfabe) for i in range(uzunluk))
    p.strip()
    return p

sayi = dogrulama_kodu()

def dogrula():
    kullanici = kullanici_harf_girisi.get()
    i = 0
    m = 0
    if sayi == kullanici:
        i = i+1
        basarili = Toplevel(root)
        basarili.title("Başarılı")
        basarili.geometry("200x200")
        Label(basarili, text ="Giriş başarılı!", font=('verdana',10,'bold')).place(x=50, y=100)
        if i == 1:
            dogrula.config(state=DISABLED)
    else:
        m = m+1
        basarisiz = Toplevel(root)
        basarisiz.title("Başarısız")
        basarisiz.geometry("200x200")
        Label(basarisiz, text="Giriş başarısız!", font=('verdana',10,'bold')).place(x=50, y=100)
        if m == 1:
            dogrula.config(state=DISABLED)

def gonder():
    gidecek_email = email_girisi.get()
    smtp.sendmail(mail_adres, gidecek_email , sayi)

baslik = tk.Label(root, text="Email ile Doğrulama", fg="black", font=('verdana',10,'bold')).place(x=100, y=30)
email_girisi_text = tk.Label(root, text="Email:", fg="black")
email_girisi_text.place(x=5, y=70)
email_girisi = tk.Entry(root, text="", width="20")
email_girisi.place(x=50, y=70)
gonder = tk.Button(root, text="Gönder", command=gonder)
gonder.place(x=200, y=70)

kullanici_harf_girisi_text = tk.Label(root, text="Kod:", fg="black")
kullanici_harf_girisi_text.place(x=5, y=100)
kullanici_harf_girisi = tk.Entry(root, text="", width="20")
kullanici_harf_girisi.place(x=50, y=100)
dogrula = tk.Button(root, text="Dogrula", command=dogrula)
dogrula.place(x=200, y=100)

root.mainloop()
