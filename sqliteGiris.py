import sqlite3
#import kutuphane
from kutuphane import komutCalistir, listele, topla, yazdir

db=sqlite3.connect('deneme.db')

imlec=db.cursor()



"""
komut="CREATE TABLE IF NOT EXISTS veri(ad,soyad,yas)"
imlec.execute(komut)

komut="INSERT INTO veri VALUES('Ahmet','Avcu',18)"
imlec.execute(komut)
db.commit()

komut="Select * from veri"
imlec.execute(komut)
"""
"""
bilgiler=imlec.fetchall()
print(bilgiler)

for bilgi in imlec:
    print(bilgi)

komut="select * from veri where ad=?"
imlec.execute(komut,('Erhan',))
bilgi=imlec.fetchone()

print("İsim :"+str(bilgi[0]))
print("Soyisim :"+str(bilgi[1]))
print("Yaş :"+str(bilgi[2]))

komut="select * from veri"
imlec.execute(komut)
bilgiler=imlec.fetchmany(3)
print(bilgiler)


komut="UPDATE veri SET yas=? where ad=?"
imlec.execute(komut,(20,'Erhan'))
db.commit()

komut ="Select * from veri"
imlec.execute(komut)
bilgiler=imlec.fetchall()
print(bilgiler)


komut="Delete from veri where ad=?"
imlec.execute(komut,('Volkan',))
db.commit()
"""
#komut="INSERT INTO veri VALUES('Ayça','Topçu',18)"
komutCalistir(imlec,"INSERT INTO veri VALUES('Bahadır','Akkaşoğlu',22)",db)
yazdir(imlec)
