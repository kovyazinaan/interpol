age = int(input())
if age <= 12: a = 'ребенок'
elif 13 < age <= 17: a = "подросток"
elif 18 < age <=64: a = 'взрослый'
else: a = 'пожилой человек'
print ("Значит, ты {}!".format(a))