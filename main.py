###############################
###   Mehmet Kahya - 2024   ###
###  Kisisel Kayit Sistemi  ###
##     Python - SQLite3     ###
###############################

# Gerekli Kütüphaneler
import os
import time
import sqlite3
from sqlite3 import Error

# Veritabanı Oluşturma
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Veritabanı Bağlantısı Başarılı")
    except Error as e:
        print(e)
    return conn

# Tablo Oluşturma
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("Tablo Oluşturuldu")
    except Error as e:
        print(e)
        
    
# Veri Ekleme
def insert_data(conn, insert_data_sql):
    try:
        c = conn.cursor()
        c.execute(insert_data_sql)
        conn.commit()
        print("Veri Eklendi")
    except Error as e:
        print(e)
    
# Veri Listeleme
def select_data(conn, select_data_sql):
    try:
        c = conn.cursor()
        c.execute(select_data_sql)
        rows = c.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)
        
# Veri Güncelleme
def update_data(conn, update_data_sql):
    try:
        c = conn.cursor()
        c.execute(update_data_sql)
        conn.commit()
        print("Veri Güncellendi")
    except Error as e:
        print(e)
        
# Veri Silme
def delete_data(conn, delete_data_sql):
    try:
        c = conn.cursor()
        c.execute(delete_data_sql)
        conn.commit()
        print("Veri Silindi")
    except Error as e:
        print(e)
        
# Veritabanı Bağlantısı
database = "kisisel-kayit-sistemi.db"
conn = create_connection(database)

# Tablo Oluşturma
sql_create_table = """CREATE TABLE IF NOT EXISTS kisiler (
                        id integer PRIMARY KEY,
                        ad text NOT NULL,
                        soyad text NOT NULL,
                        telefon text NOT NULL,
                        email text NOT NULL,
                        adres text NOT NULL
                    );"""
create_table(conn, sql_create_table)

# Menü
while True:
    print("\n1. Yeni Kayıt Ekle")
    print("2. Kayıtları Listele")
    print("3. Kayıt Güncelle")
    print("4. Kayıt Sil")
    print("5. Çıkış")
    secim = input("Seçiminiz: ")
    
    if secim == "1":
        ad = input("Ad: ")
        soyad = input("Soyad: ")
        telefon = input("Telefon: ")
        email = input("E-Mail: ")
        adres = input("Adres: ")
        sql_insert_data = "INSERT INTO kisiler (ad, soyad, telefon, email, adres) VALUES ('{}', '{}', '{}', '{}', '{}')".format(ad, soyad, telefon, email, adres)
        insert_data(conn, sql_insert_data)
        
    elif secim == "2":
        sql_select_data = "SELECT * FROM kisiler"
        select_data(conn, sql_select_data)
        
    elif secim == "3":
        id = input("ID: ")
        ad = input("Ad: ")
        soyad = input("Soyad: ")
        telefon = input("Telefon: ")
        email = input("E-Mail: ")
        adres = input("Adres: ")
        sql_update_data = "UPDATE kisiler SET ad = '{}', soyad = '{}', telefon = '{}', email = '{}', adres = '{}', WHERE id = {}".format(ad, soyad, telefon, email, adres, id)
        update_data(conn, sql_update_data)
        
    elif secim == "4":
        id = input("ID: ")
        sql_delete_data = "DELETE FROM kisiler WHERE id = {}".format(id)
        delete_data(conn, sql_delete_data)
        
    elif secim == "5":
        conn.close()
        print("Program Sonlandırılıyor...")
        time.sleep(1)
        break
        
    else:
        print("Hatalı Seçim")
        
    input("Devam etmek için ENTER tuşuna basınız...")
    os.system("clear")
    
# Program Sonu
if conn:
    conn.close()
    print("Veritabanı Bağlantısı Kapatıldı")
    print("Program Sonlandı")