import boardPrinter
import winCheck

#global turn counter


def playGame(current, turnCounter, line1, line2, line3):
	turnTaken = False

	#make sure location is not taken
	while(turnTaken == False):
		print("Select location: ", end = "")
		location = str(input())
		location = location.lower()
		if(len(location) != 2):
			print("invalid input")
			continue
		#selected top
		if(location[0] == "t"):
			if(location[1] == "l" and line1[0] == "_"):
				line1[0] = current
				turnTaken = True

			if(location[1] == "m" and line1[1] == "_"):
				line1[1] = current
				turnTaken = True
			if(location[1] == "r" and line1[2] == "_"):
				line1[2] = current
				turnTaken = True
		#selected middle
		if(location[0] == "m"):
			if(location[1] == "l" and line2[0] == "_"):
				line2[0] = current
				turnTaken = True
			if(location[1] == "m" and line2[1] == "_"):
				line2[1] = current
				turnTaken = True
			if(location[1] == "r" and line2[2] == "_"):
				line2[2] = current
				turnTaken = True
		#selected bottom
		if(location[0] == "b"):
			if(location[1] == "l" and line3[0] == "_"):
				line3[0] = current
				turnTaken = True
			if(location[1] == "m" and line3[1] == "_"):
				line3[1] = current
				turnTaken = True
			if(location[1] == "r" and line3[2] == "_"):
				line3[2] = current
				turnTaken = True
		#user selected a spot already taken
		if (turnTaken == False):
			print("That spot is taken! Try again")
	boardPrinter.printBoard(line1, line2, line3)
	winCheck.checkWin(line1,line2,line3)
	nextTurn(current,turnCounter, line1, line2, line3)



def nextTurn(current, turnCounter, line1, line2, line3):
	turnCounter += 1
	if(turnCounter == 9):
		print("Tie Game!")
		exit()
	if(current == "X"):
		current = "O"
		print("O's Turn")
	else:
		current = "X"
		print("X's Turn")
	playGame(current, turnCounter, line1, line2, line3)


if __name__ == "__main__":
	current = "X"
	turnCounter = 0
	line1 = ["_","_","_"]
	line2 = ["_","_","_"]
	line3 = ["_","_","_"]
	print(" _______ _   _______      _______ ")
	print("|__   __(_) |__   __|    |__   __|")
	print("   | |   _  ___| | __ _  ___| | ___   ___")
	print("   | |  | |/ __| |/ _` |/ __| |/ _ \\ / _ \\")
	print("   | |  | | (__| | (_| | (__| | (_) |  __/")
	print("   |_|  |_|\\___|_|\\__,_|\\___|_|\\___/ \\___|")
	print("X's turn")
	playGame(current, turnCounter, line1, line2, line3)
