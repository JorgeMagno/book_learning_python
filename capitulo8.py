import random

while True:
	print ("Bem-vindo ao jogo")
	number_to_guess = random.randint(1,10)
	count_number_of_tries = 1
	guess = int(input('Escolha um número entre 1 and 10: '))
	while number_to_guess != guess:
		if guess == -1:
			print ("O número é ",number_to_guess)
		print('Desculpe, número errado')
		if count_number_of_tries == 4:
			break
		if guess < number_to_guess:
			print('O número é maior')
		else:
			print('O número é menor')
		if (guess == number_to_guess - 1) or (guess == number_to_guess + 1):
			print("VOCÊ ERROU POR UM!")
		guess = int(input('Tente novamente: '))
		if guess != -1:
			count_number_of_tries += 1
	if number_to_guess == guess:
		print('Você venceu!!!')
		print('Você precisou de', count_number_of_tries , 'tentativas para vencer')
	else:
		print("Sorry - Perdeu :(")
		print('O número era ',number_to_guess)
	resp = input('Game Over! Quer jogar de novo? S ou N ')
	if resp == "N" or resp == "n":
		print ("Adeus!")
		break
