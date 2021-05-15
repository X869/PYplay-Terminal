UpgoSensor=0
PYplay=1
print("Welcome to PYplay! An Open Source Python app! Type help to see commands.")

while(PYplay==1):
	userinput=input("~/PYplay ")

	if(userinput=="help"):
		print("Print, CPyCOOTH, HappyPY, A, B, Aminus, Bminus, PheeC, EmersePheePY, DaffMsG, Laa, Loo, LisTen, DoNotTypeThisCommand, UpgoVM, PYplayTerm2")

	if(userinput=="UpgoTerm"):
		UpgoSensor=5
		PYplay=0
	
	if(userinput=="Print"):
		print("Well, You got what you wanted something printed!")
	
	if(userinput!="Print"):
		if(userinput!="CPyCOOTH"):
			print("Unknown command ", userinput, "Too many arguments?")
	
	
while(UpgoSensor==5):
	print("Welcome To Upgo VM Terminal! A Terminal that allows you to mess with PYplay without breaking it. Type Downgo to go into regular PheePY terminal")
	userinput2=input("~/UpgoVM")

if(userinput2=="Downgo"):
	PYplay=1
