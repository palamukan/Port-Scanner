import os
import vulners

def port_taraması():
    hedef_ip = raw_input("Ip adresini giriniz: ")
    os.system("nmap -oX çıktı.xml " + hedef_ip)

def searchsploit():
    ip_adresi = raw_input("İp adresini giriniz: ")
    çıktı = input("Çıktı adını giriniz: ")
    os.system("searchsploit" + " -v" + çıktı.xml)

def burut_fors():
    çıktı_adı = input("Çıktı adınızı giriniz: ")
    dizin = input("Dizin giriniz: ")
    wl = input("wl adı giriniz: ")
    os.system("brutespray.py " "--file çıktı_adı.xml " "-U dizin/wl.txt " "-P dizin/wl.txt " "--threads 5 " "--hosts 5")

def vulners():
    api = input("Api key'i giriniz: ")
    servis = input("Tarama yapmak istediğiniz servisi yazınız: ")
    vulners_api = vulners.Vulners(api_key="api")
    tarama = vulners_api.search("servis", limit=3)

    print(tarama)

port_taraması
searchsploit
burut_fors
vulners


print("""""""""""""""""""""""""""""""""""""""""
***************************************************************************************************************************************************

1-)Port taraması için 'nmap' yazınız.
2-)Searchsploit ile exploit kontrolü için 'exploit_scan' yazınız.
3-)Burut fors saldırısı için 'burut' yazınız.
4-) Vulners'da tarama yapmak için 'vulners' yazınız.

Brutespray, searchsploit ve Medusa araçlarının sisteminizde yüklü olması gerekmektedir, tavsiye olarak Parrot, Kali vb. distrolarda çalıştırınız.

***************************************************************************************************************************************************
""""""""""""""""""""""""""""""""""""""""""""")

while True:
    işlem = input("Hangi işlemi yapmak istiyorsunuz: ")
    if (işlem == "nmap"):
        port_taraması()
    elif (işlem == "exploit_scan"):
        searchsploit()
    elif (işlem == "burut"):
        burut_fors()
    elif (işlem == "vulners"):
        vulners()
    else:
        print("Hatalı tuşlama yaptınız..")
