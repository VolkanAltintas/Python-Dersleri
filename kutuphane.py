def yazdir(imlec):
    komut ="Select * from veri"
    imlec.execute(komut)
    bilgiler=imlec.fetchall()
    print(bilgiler)

def listele():
    print('Listeleme işlemi yapıldı...')

def topla(a,b):
    return a+b

def komutCalistir(imlec,komut,db):
    imlec.execute(komut)
    db.commit()