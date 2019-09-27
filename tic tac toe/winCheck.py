def checkWin(line1, line2, line3):
	#check horizontal
	#X wins
	if(line1[0] == "X"):
		if(line1[1] == "X"):
			if(line1[2] == "X"):
				print("X Wins!")
				exit()
	if(line2[0] == "X"):
		if(line2[1] == "X"):
			if(line2[2] == "X"):
				print("X Wins!")
				exit()
	if(line3[0] == "X"):
		if(line3[1] == "X"):
			if(line3[2] == "X"):
				print("X Wins!")
				exit()
	#O wins
	if(line1[0] == "O"):
		if(line1[1] == "O"):
			if(line1[2] == "O"):
				print("O Wins!")
				exit()
	if(line2[0] == "O"):
		if(line2[1] == "O"):
			if(line2[2] == "O"):
				print("O Wins!")
				exit()
	if(line3[0] == "O"):
		if(line3[1] == "O"):
			if(line3[2] == "O"):
				print("O Wins!")
				exit()

	#check vertical
	#X wins
	if(line1[0] == "X"):
		if(line2[0] == "X"):
			if(line3[0] == "X"):
				print("X Wins!")
				exit()
	if(line1[1] == "X"):
		if(line2[1] == "X"):
			if(line3[1] == "X"):
				print("X Wins!")
				exit()
	if(line1[2] == "X"):
		if(line2[2] == "X"):
			if(line3[2] == "X"):
				print("X Wins!")
				exit()
	#O wins
	if(line1[0] == "O"):
		if(line2[0] == "O"):
			if(line3[0] == "O"):
				print("O Wins!")
				exit()
	if(line1[1] == "O"):
		if(line2[1] == "O"):
			if(line3[1] == "O"):
				print("O Wins!")
				exit()
	if(line1[2] == "O"):
		if(line2[2] == "O"):
			if(line3[2] == "O"):
				print("O Wins!")
				exit()

	#check diagnol
	#X wins
	if(line1[0] == "X"):
		if(line2[1] == "X"):
			if(line3[2] == "X"):
				print("X Wins!")
				exit()
	if(line1[2] == "X"):
		if(line2[1] == "X"):
			if(line3[0] == "X"):
				print("X Wins!")
				exit()
	#O wins
	if(line1[0] == "O"):
		if(line2[1] == "O"):
			if(line3[2] == "O"):
				print("O Wins!")
				exit()
	if(line1[2] == "O"):
		if(line2[1] == "O"):
			if(line3[0] == "O"):
				print("O Wins!")
				exit()