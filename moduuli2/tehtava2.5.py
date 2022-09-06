luoti = 13.3
naula = luoti * 32
leiviska = naula * 20

luodit_str = input('anna luodit: ')
naulat_str = input('anna naulat: ')
leiviskat_str = input('anna leiviskät: ')
luodit = float(luodit_str)
naulat = float(naulat_str)
leiviskat = float(leiviskat_str)

massa = luodit * luoti + naulat * naula + leiviskat * leiviska
kilot = massa // 1000
grammat = massa - kilot * 1000

print(f"massa: {kilot:1.0f} kiloa {grammat} grammaa")

