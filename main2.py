while True:
    kirish = str(input("Xaridor ismi >>> "))
    ism1 = kirish[0::].capitalize()
    print(f"Assalamu alaykum hurmatli {ism1}!\n'Break House'  do'koniga tashrif buyurganingiz uchun tashakkur!\nBizning shiorimiz -> Biz bilan vaqtingizni tejang,Alo narx va Alo sifat!")
    malumotlar = []
    kirish_qismi1 = str(input("Mahsulot nomi >>> "))
    kirish_qismi2 = int(input(f"{kirish_qismi1} soni >>> "))
    kirish_qismi3 = int(input(f"{kirish_qismi1} narxi >>> "))
    kirish_qismi4 = str(input("Sotuv yakunlansinmi >>> "))
    if kirish_qismi4 == "Yo'q" or "yo'q" or "yoq" or "Yoq":
        print("Unday bo'lsa davom etamiz!")
    if kirish_qismi4 == "Ha" or "ha" or "xa" or "Xa":
        print("Spiska yakunlandi!\nXaridingiz uchun rahmat!\nMurojaat uchun tel: +998(90)-550-23-24")
        print("                    +998(97)-955-23-24")
        print("                    +998(97)-242-23-24")
        print("                    +998(97)-629-23-24")
        print(f"Telegram kanalimiz: {https://t.me/Stroy_Materiallar}")
        print(f"Jami summa >>> {kirish_qismi2 * kirish_qismi3} ming so'm")
        break
    a1 = malumotlar.append(kirish_qismi1)
    a2 = malumotlar.append(kirish_qismi2)
    a3 = malumotlar.append(kirish_qismi3)
    print(malumotlar)

