#!/usr/bin/env python3

import sys

sylsep = ""

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

	ls = ""
	lead = [] 
	
	if h == 0 and z == 0:
		return  ones_alone[e-1]
	
	if h != 0:
		lead = hundreds[h-1]

	if z != 0:
		lead = tens[z-1]

	if len(lead) == 1 or e == 0:
		res = lead[0]
	elif len(ones_combine[e-1]) == 1:
		res = ones_combine[e-1][0] + sylsep + lead[0]
	else:
		# several possibilities for z sylable, find matching e syl
		ls = [[s[1:],t] for s in lead for t in ones_combine[e-1] if s[0] == t[-1]]

		# no valid combination? take the first sylabels
		if len(ls) == 0:
			res = ones_combine[e-1][0] + sylsep + lead[0]
		else:
			res = ls[0][1] + sylsep + ls[0][0]

	if z != 0 and h != 0:
			res = res + sylsep + hundreds[h-1][0]

	return res
	

if len(sys.argv) > 1:
	if any("-s" in t for t in sys.argv):
		sylsep = "-"

anzahl_nullen = input("Natürliche Anzahl Nullen?")

an = 0

try:
	an = int(anzahl_nullen)
except ValueError:
	print("Das war keine natürliche Zahl! ")

print("10^" + anzahl_nullen + "   ", end = '')


m = str(int(an // 6))
n = (an % 6) >= 3
o = (an % 3)

if int(m) == 0:
	print("Das sollten wir auch ohne Programm lesen können!")
	exit(0)

if n == True:
	print("Million ^ " + m + ",5", end='')
else:
	print("Million ^ " + m, end='')

numstr = ""

while len(m) > 0:
	if len(m) > 3:
		p = int(m[-3:])
		m = m[:-3]
	else:
		p = int(m)
		m = ""
	r = ""
	if p == 0:
		r = "ni"
	else:
		r = convert_group(p)[:-1] + "i"
	numstr = r + sylsep + "lli" + sylsep + numstr

s = (numstr[0].upper())
numstr = s + numstr[1:]

if n == False:
	numstr = numstr + "on"
else:
	numstr = numstr + "arde"

if o > 0:
	if n == False:
		numstr = numstr + "e"
	numstr = ["Zehn ", "Hundert "][o-1] + numstr + "n"

print("    " + numstr)
