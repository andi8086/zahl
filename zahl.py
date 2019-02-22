#!/usr/bin/env python3

def convert_group(number):
	ones_alone = ["mi", "bi", "tri", "quadri", "quinti", "sexti",
			"septi", "okti", "noni"]
	ones_combine = [["un"], 
			["duo"], 
			["tre", "tres"], ["quattuor"], ["quin"], 
			["sex", "ses", "se"],
			["septe", "septem", "septen"],
			["okto"],
			["nove", "novem", "noven"]]
	tens = [["dezi", "ndezi"],
		["viginti", "mviginti", "sviginti"],
		["triginta", "ntriginta", "striginta"],
		["quadraginta", "nquadraginta", "squadraginta"],
		["quinquaginta", "nquinquaginta", "squinquaginta"],
		["sexaginta", "nsexaginta"],
		["septuaginta", "nseptuaginta"],
		["oktoginta", "moktoginta", "xoktoginta"],
		["nonaginta"]]
	hundreds = [["zenti", "nzenti", "xzenti"],
			["duzenti", "nduzenti"],
			["trezenti", "ntrezenti", "strezenti"],
			["quadringenti", "nquadringenti", "squadringenti"],
			["quingenti", "nquingenti", "squingenti"],
			["seszenti", "nseszenti"],
			["septingenti", "nseptingenti"],
			["oktingenti", "moktingenti", "xoktingenti"],
			["nongenti"]]

	res = ""

	h = int(number / 100)
	z = int((number % 100) / 10)
	e = number % 10

	es = ""
	zs = ""
	hs = ""

	res = ""

	if h == 0 and z == 0:
		res =  ones_alone[e-1]
	
	elif z != 0:
		if len(tens[z-1]) == 1 or e == 0:
			res = tens[z-1][0]
		elif len(ones_combine[e-1]) == 1:
			res = ones_combine[e-1][0] + "-" + tens[z-1][0]
		else:
			# several possibilities for z sylable, find matching e syl
			zs = [[s,t[:-1]] for s in tens[z-1] for t in ones_combine[e-1] if s[0] == t[-1]]

			# no valid combination? take the first sylabels
			if len(zs) == 0:
				res = ones_combine[e-1][0] + "-" + tens[z-1][0]
			else:
				res = zs[0][1] + "-" + zs[0][0]
			#res = zs[1]+zs[0]


		if h != 0:
			res = res + "-" + hundreds[h-1][0]

	elif h != 0:
		if len(hundreds[h-1]) == 1 or e == 0:
			res = hundreds[h-1][0]
		elif len(ones_combine[e-1]) == 1:
			res = ones_combine[e-1][0] + "-" + hundreds[h-1][0]
		else:
			hs = [[s,t[:-1]] for s in hundreds[h-1] for t in ones_combine[e-1] if s[0] == t[-1]]
			if len(hs) == 0:
				res = ones_combine[e-1][0] + "-" + hundreds[h-1][0]
			else:
				res = hs[0][1] + "-" + hs[0][0]

	return res
	


anzahl_nullen = input("Natürliche Anzahl Nullen?")

an = 0

try:
	an = int(anzahl_nullen)
except ValueError:
	print("Das war keine natürliche Zahl! ")

print("10^" + str(an) + "   ", end = '')


m = int(an / 6)
n = (an % 6) >= 3
o = (an % 3)

if m < 1:
	print("Das sollten wir auch ohne Programm lesen können!")
	exit(0)

if n == True:
	print("Million ^ " + str(m) + ",5", end='')
else:
	print("Million ^ " + str(m), end='')

numstr = convert_group(m)[:-1]

s = (numstr[0].upper())
numstr = s + numstr[1:]

if n == False:
	numstr = numstr + "illion"
	if o > 0:
		numstr = ["Zehn ", "Hundert "][o-1] + numstr + "en"
else:
	numstr = numstr + "illiarde"
	if o > 0:
		numstr = ["Zehn ", "Hundert "][o-1] + numstr + "n"


print("    " + numstr)
