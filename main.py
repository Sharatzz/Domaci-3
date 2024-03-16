#2.
#
# list = [1, 2, 2, 2,2,2, 4, 4]
# max_proizvod = 1
# el = list[0]
#
# for _ in list:
#     p = 1
#     for x in list:
#
#         if _ == x:
#             p = p *_
#
#
#
#     if p >= max_proizvod:
#
#         max_proizvod = p
#         el = _
#
#
# print(max_proizvod)
# li = [el]*int(max_proizvod**(1/el))
# print(li)

#3 ZADATAK

# list = [1,3,8,21,15,18,59]
# max_list = []
# pom_list = []
# i = 1
# list_duz = len(list)
# a = list[0]
# mode = True
# while i < list_duz:
#     b = list[i]
#     if mode:
#         if a<b:
#             pom_list.append(a)
#         else:
#             pom_list.append(a)
#             if len(pom_list) > len(max_list):
#                 max_list = pom_list
#             pom_list = []
#         mode = False
#     else:
#         if a>b:
#             pom_list.append(a)
#         else:
#             pom_list.append(a)
#             if len(pom_list) > len(max_list):
#                 max_list = pom_list
#             pom_list = []
#         mode = True
#     a = b
#     i += 1
# print(max_list)

#4 ZADATAK

# str = 'aabaaac'
#
# strlen = len(str)-1
# br = 0
# for i in range(0,strlen):
#    if str[i] == str[i+1]:
#        br += 1
#
# print(br)


#1 ZADATAK:
# str_zadatak = 'Print only the words that end with the chosen letter in those sentences. Example can contains one or more sentences.'
# letter = 's'
#
# def get_words_ends_with_letter(str, letter):
#
#     list = str_zadatak.split()
#     list_rijeci = []
#
#     for _ in list:
#         if letter == _[-1]:
#             list_rijeci.append(_)
#
#         if _[-1] == '.':
#             if letter == _[-2]:
#                 list_rijeci.append(_)
#
#     print(list_rijeci)
#
#     pomocna_list = []
#     konacna_lista = []
#
#
#     for _ in list_rijeci:
#
#         if _[-1]== '.':
#             pomocna_list.append(_[:-1])
#             pomocna_list.append(len(pomocna_list))
#             konacna_lista.append(tuple(pomocna_list))
#             pomocna_list = []
#         else:
#             pomocna_list.append(_)
#
#     print(konacna_lista)
#
# get_words_ends_with_letter(str_zadatak,letter)

#5 ZADATAK
# niz = [{'naziv':'Español para principiantes', 'br_pozitivni':1000,'br_negativni':10},
# {'naziv':'Philophize This!', 'br_pozitivni':500,'br_negativni': 30}, {'naziv':'Science VS. ',
# 'br_pozitivni':600,'br_negativni': 45}]
#
#
#
# max_ime = niz[0]['naziv']
# najgori_odnos = niz[0]['br_pozitivni'] / niz[0]['br_negativni']
#
# for _ in niz:
#
#     trenutni_odnos = _['br_pozitivni'] / _['br_negativni']
#
#     if trenutni_odnos <= najgori_odnos:
#         najgori_odnos = trenutni_odnos
#         max_ime = _['naziv']
#
#
# print(max_ime)


#6 ZADATAK


# class Televizor:
#
#     def __init__(self):
#
#
#         self.kanali = []
#         self.broj_tekucih_kanala = 0
#         self.naziv_kanala = ''
#         self.jacina_tona = 5
#
#
#
#     def set_jacina_tona(self, jacina):
#         if jacina >= 0 and jacina <= 10:
#             self.jacina_tona = jacina
#         else:
#             print('Jacina je neispravna')
#
#     def get_jacina_tona(self):
#         return self.jacina_tona
#
#     def set_naziv_kanala(self, ime):
#
#         self.naziv_kanala = ime
#
#     def get_naziv_kanala(self):
#         return self.naziv_kanala
#
#     def set_broj_tekuceg_kanala(self,broj):
#
#         if broj > 0 and broj <= len(self.kanali):
#             self.broj_tekucih_kanala = broj
#         else:
#             print('Broj  je neispravan')
#
#
#     def get_broj_tekuceg_kanala(self):
#         return self.broj_tekucih_kanala
#
#
#     def dodaj_kanal(self, naziv_kanala):
#
#         self.kanali.append(naziv_kanala)
#
#     def obrisi_kanal(self, naziv_kanala):
#         self.kanali.remove(naziv_kanala)
#
#     def pojacaj_ton(self):
#         self.jacina_tona += 1
#
#     def ime_kanala(self, broj_kanala):
#
#         print('Kanal je : {}'.format(self.kanali[broj_kanala-1]))
#
#
#
# tv = Televizor()
#
# tv.dodaj_kanal('Crna Gora')
#
# tv.ime_kanala(1)

#7 ZADATAK

# class Book:
#
#     def __init__(self,naslov,autor,godina_izdanja, broj_kopija):
#         self.naslov = naslov
#         self.autor = autor
#         self.godina_izdanja = godina_izdanja
#         self.broj_kopija_u_inventaru = broj_kopija
#
#     def set_naslov(self, naslov):
#         self.naslov = naslov
#
#     def get_naslov(self):
#         return self.naslov
#
#     def set_autor(self,autor):
#         self.autor = autor
#
#     def get_autor(self):
#         return self.autor
#
#     def set_godina_izdanja(self,godina):
#         self.godina_izdanja = godina
#
#     def get_godina_izdanja(self):
#         return self.godina_izdanja
#
#     def set_broj_kopija(self,broj):
#         self.broj_kopija_u_inventaru = broj
#
#     def get_broj_kopija(self):
#         return self.broj_kopija_u_inventaru
#
# class Library:
#
#     def __init__(self):
#         self.inventar = []
#
#     def dodaj_knjigu(self,knjiga):
#         self.inventar.append(knjiga)
#
#     def obrisi_knjigu(self, knjiga):
#         if knjiga in self.inventar:
#             self.inventar.remove(knjiga)
#         else:
#             print('Knjige nema')

#8 ZADATAK:

# class Player:
#
#     def __init__(self,x,y,width, height,health):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.health = health
#
#
#     def set_x_kord(self,x):
#         self.x = x
#     def get_x_kor(self):
#         return self.x
#
#     def set_y_kord(self, y):
#         self.y = y
#
#     def get_y_kor(self):
#         return self.y
#
#     def set_width(self, width):
#         self.width = width
#     def get_width(self):
#         return self.width
#
#     def set_height(self, height):
#         self.height = height
#     def get_height(self):
#         return self.height
#
#     def set_health(self, health):
#
#         if health < 0 or health > 100:
#             print('Error')
#         else:
#             self.health = health
#     def get_health(self):
#         return  self.health
#
# class Enemy:
#
#     def __init__(self, x, y, width, height, health):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.health = health
#
#     def set_x_kord(self, x):
#         self.x = x
#
#     def get_x_kor(self):
#         return self.x
#
#     def set_y_kord(self, y):
#         self.y = y
#
#     def get_y_kor(self):
#         return self.y
#
#     def set_width(self, width):
#         self.width = width
#
#     def get_width(self):
#         return self.width
#
#     def set_height(self, height):
#         self.height = height
#
#     def get_height(self):
#         return self.height
#
#     def set_health(self, health):
#
#         if health < 0 or health > 100:
#             print('Error')
#         else:
#             self.health = health
#
#     def get_health(self):
#         return self.health
#
#
#
# p = Player(10,10,10,10,10)
# e = Enemy(10,10,10,10,10)
# e2 = Enemy(10,10,10,10,10)
#
# def check_collision(player, enemy):
#
#     if player.x == enemy.x:
#         return True
#     else:
#         return False
#
# def decreate_health(player, enemy):
#
#     if check_collision(player,enemy):
#         player.health -= 1
#         enemy.health -= 1
#     else:
#         pass
#

#import random
#9 ZADATAK
# class Turnir:
#     def __init__(self, naziv_turnira, broj_rundi):
#         self.naziv_turnira = naziv_turnira
#         self.lista_igraca = []
#         self.broj_rundi = broj_rundi
#
#     # Getteri i setteri
#     def get_naziv_turnira(self):
#         return self.naziv_turnira
#
#     def set_naziv_turnira(self, naziv_turnira):
#         self.naziv_turnira = naziv_turnira
#
#     def get_lista_igraca(self):
#         return self.lista_igraca
#
#     def set_lista_igraca(self, lista_igraca):
#         self.lista_igraca = lista_igraca
#
#     def get_broj_rundi(self):
#         return self.broj_rundi
#
#     def set_broj_rundi(self, broj_rundi):
#         if broj_rundi >0 and broj_rundi < 10:
#             self.broj_rundi = broj_rundi
#         else:
#             print("Error")
#
#
#     def dodaj_igraca(self, ime_igraca):
#         nova_torka = (ime_igraca, 0)
#         self.lista_igraca.append(nova_torka)
#
#
#     def obrisi_igraca(self, ime_igraca):
#         for igrac in self.lista_igraca:
#             if igrac[0] == ime_igraca:
#                 self.lista_igraca.remove(igrac)
#             else:
#                 print("Igrač nije pronađen.")
#
#     def prikazi_najboljeg_igraca(self):
#         if not self.__lista_igraca:
#             print('Error')
#         else:
#             najbolji_bodovi = 0
#             najbolji_igrac = None
#             for igrac in self.__lista_igraca:
#                 if igrac[1] > najbolji_bodovi:
#                     najbolji_bodovi = igrac[1]
#                     najbolji_igrac = igrac

#10 ZADATAK


# class Color:
#     def __init__(self, red, green, blue):
#         self.red = self.validate_color(red)
#         self.green = self.validate_color(green)
#         self.blue = self.validate_color(blue)
#
#     def validate_color(self, color):
#         if 0 <= color <= 255:
#             return color
#
#
#     def get_red(self):
#         return self.red
#
#     def set_red(self, red):
#         validated_red = self.validate_color(red)
#         self.red = validated_red
#
#     def get_green(self):
#         return self.green
#
#     def set_green(self, green):
#         validated_green = self.validate_color(green)
#         self.green = validated_green
#
#     def get_blue(self):
#         return self.blue
#
#     def set_blue(self, blue):
#         validated_blue = self.validate_color(blue)
#         self.blue = validated_blue
#
#     def add_red(self, change):
#         new_red = self.red + change
#         if 0 <= new_red <= 255:
#             self.red = new_red
#         else:
#             print("0 - 255.")
#
#     def add_green(self, change):
#         new_green = self.green + change
#         if 0 <= new_green <= 255:
#             self.green = new_green
#         else:
#             print("0 - 255.")
#
#     def add_blue(self, change):
#         new_blue = self.blue + change
#         if 0 <= new_blue <= 255:
#             self.blue = new_blue
#         else:
#             print("0 - 255.")
#
# #11 ZADATAK
#
# class AlphaColor(Color):
#     def __init__(self, red, green, blue, alpha):
#         self.red = self.validate_color(red)
#         self.green = self.validate_color(green)
#         self.blue = self.validate_color(blue)
#         self.alpha = self.validate_alpha(alpha)
#
#     def validate_color(self, color):
#         if 0 <= color <= 255:
#             return color
#         else:
#             print("Error")
#
#     def validate_alpha(self, alpha):
#         if 0 <= alpha <= 1:
#             return alpha
#         else:
#             print("Error")
#
#
#     def get_alpha(self):
#         return self.alpha
#
#     def set_alpha(self, alpha):
#         validated_alpha = self.validate_alpha(alpha)
#         self.alpha = validated_alpha
#
#     def update_color(self, alpha):
#         current_red = self.red
#         current_green = self.green
#         current_blue = self.blue
#
#         new_red = current_red - current_red * alpha
#         new_green = current_green - current_green * alpha
#         new_blue = current_blue - current_blue * alpha
#
#         self.red = new_red
#         self.green = new_green
#         self.blue = new_blue
#
# 12 ZADATAK
# class Company:
#     def __init__(self, name, area, balance, max_num_of_employees):
#         self.name = name
#         self.area = area
#         self.employees = []
#         self.balance = self.validate_balance(balance)
#         self.max_num_of_employees = max_num_of_employees
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_area(self):
#         return self.area
#
#     def set_area(self, area):
#         self.area = area
#
#     def get_balance(self):
#         return self.balance
#
#     def set_balance(self, balance):
#         if balance >= 0:
#             self.balance = balance
#
#     def get_max_num_of_employees(self):
#         return self.max_num_of_employees
#
#     def set_max_num_of_employees(self, max_num_of_employees):
#         if max_num_of_employees >= 0:
#             self.max_num_of_employees = max_num_of_employees
#
#     def add_employee(self, employee):
#         if len(self.employees) < self.max_num_of_employees:
#             self.employees.append(employee)
#         else:
#             print("Maximum number of employees reached.")