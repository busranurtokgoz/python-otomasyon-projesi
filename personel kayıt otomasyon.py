from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import mysql.connector


class personelKayit(QDialog):
    def __init__(self, parent=None):
        super(personelKayit, self).__init__(parent)
        grid = QGridLayout()
        grid.addWidget(QLabel("Ad"), 0, 0)
        grid.addWidget(QLabel("Soyad"), 1, 0)
        grid.addWidget(QLabel("Yaş"), 2, 0)
        grid.addWidget(QLabel("Cinsiyeti"), 3, 0)
        grid.addWidget(QLabel("Personel Ekle"), 4, 0)
        grid.addWidget(QLabel("Personel Çıkar"), 5, 0)
        grid.addWidget(QLabel("Personel Devir Hızı"), 6, 0)

        self.etiket = ""
        self.liste = []
        self.cikanliste = []

        self.adi = QLineEdit()
        self.soyadi = QLineEdit()
        self.yas = QLineEdit()
        self.personelEkle = QLineEdit()
        self.personelCikar = QLineEdit()
        self.personeldevirhizi = QLineEdit()
        self.kadin = QRadioButton("Kadın")
        self.erkek = QRadioButton("Erkek")
        self.cinsiyet = QButtonGroup(self)
        self.cinsiyet.addButton(self.kadin)
        self.cinsiyet.addButton(self.erkek)
        temizle = QPushButton("Temizle")
        temizle.clicked.connect(self.temizle)
        kaydet = QPushButton("Kaydet")
        kaydet.clicked.connect(self.kaydet)
        kayitAktar = QPushButton("Kaydı Aktar")
        kayitAktar.clicked.connect(self.kayitAktar)
        ekle = QPushButton("Ekle")
        ekle.clicked.connect(self.ekle)
        cikar = QPushButton("Çıkar")
        cikar.clicked.connect(self.cikar)
        hesapla = QPushButton("Hesapla")
        hesapla.clicked.connect(self.hesapla)

        grid.addWidget(self.adi, 0, 1)
        grid.addWidget(self.soyadi, 1, 1)
        grid.addWidget(self.yas, 2, 1)
        grid.addWidget(self.erkek, 3, 1)
        grid.addWidget(self.kadin, 3, 2)
        grid.addWidget(self.personeldevirhizi, 6, 1)
        grid.addWidget(self.personelEkle, 4, 1)
        grid.addWidget(self.personelCikar, 5, 1)

        grid.addWidget(temizle, 7, 0)
        grid.addWidget(kaydet, 7, 1)
        grid.addWidget(ekle, 8, 0)
        grid.addWidget(cikar, 8, 1)
        grid.addWidget(hesapla, 8, 2)
        grid.addWidget(kayitAktar, 0, 3, 6, 1)

        grid.addWidget(QLabel("Ad"), 0, 6)
        grid.addWidget(QLabel("Soyad"), 1, 6)
        grid.addWidget(QLabel("Yaş"), 2, 6)
        grid.addWidget(QLabel("Cinsiyet"), 3, 6)
        grid.addWidget(QLabel("Personel Ekle"), 4, 6)
        grid.addWidget(QLabel("Personel Çıkar"), 5, 6)
        grid.addWidget(QLabel("Personel Devir Hızı"), 6, 6)

        self.adiLabel = QLabel()
        self.soyadiLabel = QLabel()
        self.yasLabel = QLabel()
        self.personelEkleLabel = QLabel()
        self.personelCikarLabel = QLabel()
        self.cinsiyetLabel = QLabel()
        self.personeldevirhiziLabel = QLabel()
        grid.addWidget(self.adiLabel, 0, 6)
        grid.addWidget(self.soyadiLabel, 1, 6)
        grid.addWidget(self.yasLabel, 2, 6)
        grid.addWidget(self.cinsiyetLabel, 3, 6)
        grid.addWidget(self.personelEkleLabel, 4, 6)
        grid.addWidget(self.personelCikarLabel, 5, 6)
        grid.addWidget(self.personeldevirhiziLabel, 6, 6)

        self.setLayout(grid)
        self.setWindowTitle("Personel Kayıt Programı")
        self.resize(400, 400)

    def temizle(self):
        self.adi.setText("")
        self.soyadi.setText("")
        self.yas.setText("")
        self.personelEkle.setText("")
        self.personelCikar.setText("")
        self.personeldevirhizi.setText("")

    def kaydet(self):
        adi = self.adi.text()
        soyadi = self.soyadi.text()
        yas = self.yas.text()
        personelEkle = self.personelEkle.text()
        personelCikar = self.personelCikar.text()
        personeldevirhizi = self.personeldevirhizi.text()
        cinsiyet = ""
        if self.kadin.isChecked() == True:
            cinsiyet = "Kadın"
        elif self.erkek.isChecked() == True:
            cinsiyet = "Erkek"
        baglanti = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="programlama2")
        isaretci = baglanti.cursor()
        isaretci.execute(''' INSERT INTO personel(adi,soyadi,yas,cinsiyet,personelEkle,personelCikar,personeldevirhizi)
VALUES("%s","%s","%d","%s","%d","%d","%d") ''' % (
        adi, soyadi, yas, cinsiyet, personelEkle, personelCikar, personeldevirhizi))
        baglanti.commit()
        baglanti.close()

    def kayitAktar():
        pass

    def ekle(self):
        personelEkle = self.personelEkle.text()
        self.personelEkle.append(kisi)
        print(self.liste)

    def cikar(self):
        personelCikar = self.personelCikar.text()
        self.personelCikar.append(kisi)
        print(self.cikanliste)

    def hesapla():
        alinan = len(self.liste)
        cikan = len(self.cikanliste)
        sonuc = alinan / cikan * 100
        self.personeldevirhizi.setText("<font color='purple'>%d</font>" % sonuc)


uyg = QApplication([])
pencere = personelKayit()
pencere.show()
uyg.exec_()

