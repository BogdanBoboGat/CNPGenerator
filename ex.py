#!/usr/bin/python3
import names
import random

class human():
	def __init__(self, day = list(range(1, 32)), month = list(range(1, 13)), year = list(range(1900, 2021)), place = '', sex = ''):
		location = {
			'Alba' : '01',
			'Arad' : '02',
			'Argeș' : '03',
			'Bacău' : '04',
			'Bihor' : '05',
			'Bistrița-Năsăud' : '06',
			'Botoșani' : '07',
			'Brașov' : '08',
			'Brăila' : '09',
			'Buzău' : '10',
			'Caraș-Severin' : '11',
			'Cluj' : '12',
			'Constanța' : '13',
			'Covasna' : '14',
			'Dâmbovița' : '15',
			'Dolj' : '16',
			'Galați' : '17',
			'Gorj' : '18',
			'Harghita' : '19',
			'Hunedoara' : '20',
			'Ialomița' : '21',
			'Iași' : '22',
			'Ilfov' : '23',
			'Maramureș' : '24',
			'Mehedinți' : '25',
			'Mureș' : '26',
			'Neamț' : '27',
			'Olt' : '28',
			'Prahova' : '29',
			'SatuMare' : '30',
			'Sălaj' : '31',
			'Sibiu' : '32',
			'Suceava' : '33',
			'Teleorman' : '34',
			'Timiș' : '35',
			'Tulcea' : '36',
			'Vaslui' : '37',
			'Vâlcea' : '38',
			'Vrancea' : '39',
			'București' : '40',
			'București-Sector1' : '41',
			'București-Sector2' : '42',
			'București-Sector3' : '43',
			'București-Sector4' : '44',
			'București-Sector5' : '45',
			'București-Sector6' : '46',
			'Călărași' : '51',
			'Giurgiu' : '52'
		}
		key_location = list(location.keys())
		val_location = list(location.values())
		
		self.year = random.choice(year)
		self.month = random.choice(month)
		self.day = random.choice(day)
		self.ran = random.choice(list(range(1, 1000)))

		if place in list(location.keys()):
			self.location = location[place]
		else:
			self.location = random.choice(list(location.values()))

		if self.year <= 1999:
			if sex == 'male':
				self.sex = 1
			elif sex == 'female':
				self.sex = 2
			else:
				self.sex = random.choice([1, 2])
		
		elif self.year <= 2099:
			if sex == 'male':
				self.sex = 5
			elif sex == 'female':
				self.sex = 6
			else:
				self.sex = random.choice([5, 6])




human = human()
print(human.sex, human.year, human.month, human.day, human.location, human.ran)
