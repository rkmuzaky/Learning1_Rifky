kalimat = "ini adalah kalimat" #ini adalah kalimat
paragraf = """ini adalah paragraf.
Paragraf terdiri dari beberapa baris.""" #ini adalah paragraf.
print(kalimat) #ini adalah kalimat
print(paragraf) #ini adalah paragraf.
                #Paragraf terdiri dari beberapa baris.

kalimat = "abcdefghijklmnopqrstuvwxyz"
print(kalimat [:5]) #abcde
print(kalimat [5:10]) #fghij
print(kalimat [21:]) #vwxyz
print(kalimat [-10:-1]) #qrstuvwxy
print(kalimat [-10:]) #qrstuvwxyz

kalimat = "Halo, semua. Saya adalah programer Python "
print(kalimat.upper()) #HALO, SEMUA. SAYA ADALAH PROGRAMER PYTHON
print(kalimat.lower()) #halo, semua. saya adalah programer python
print(kalimat.capitalize()) #Halo, semua. saya adalah programer python
print(kalimat.title()) #Halo, Semua. Saya Adalah Programer Python
print(kalimat.swapcase()) #hALO, SEMUA. sAYA ADALAH PROGRAMER pYTHON
print(kalimat.replace("Python", "Java")) #Halo, semua. Saya adalah programer Java
print(kalimat.replace("a", "i")) #Hilo, semui. Siyi idilih progrimer Python
print(kalimat.strip()) #Halo, semua. Saya adalah programer Python
print(kalimat.split('.')) #['Halo, semua', ' Saya adalah programer Python ']

kalimat = "Halo, semua. Saya adalah programer Python. " 
tambahan = "Saya sedang belajar Python. Mohon bimbingannya."
print(kalimat + tambahan) #Halo, semua. Saya adalah programer Python. Saya sedang belajar Python. Mohon bimbingannya.

kalimat = "Halo, semua. Saya adalah programer \"Python\". "
tambahan = "Saya sedang belajar \"Python\". Mohon bimbingannya."
print(kalimat + tambahan) #Halo, semua. Saya adalah programer "Python". Saya sedang belajar "Python". Mohon bimbingannya.

umur = 21
rumah = 3
mobil = 5
emas = 10
kalimat = "Saya berumur {} tahun, rumah saya ada {}, mobil saya ada {}, dan emas saya ada {} kilogram"
print(kalimat.format(umur, rumah, mobil, emas)) #Saya berumur 21 tahun, rumah saya ada 3, mobil saya ada 5, dan emas saya ada 10 kilogram
