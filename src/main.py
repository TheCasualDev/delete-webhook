import requests
import colorama
import time
import os

colorama.init()
os.system("cls")

print(colorama.Fore.LIGHTBLUE_EX + "\nWELCOME TO THE MOST BASIC WEBHOOK REMOVER BY JACK (⌐■_■) \n" + colorama.Fore.RESET)
	
def main():

	# delete webhook logic
	
	webhook = input("Please add the webhook link you wish to delete: " + colorama.Fore.LIGHTYELLOW_EX)
	response = requests.delete(webhook)

	print("")

	if response.status_code in range(200, 299):
		print(colorama.Back.GREEN + colorama.Fore.LIGHTWHITE_EX + " Success ")
	elif response.status_code in range(400, 499):
		print(colorama.Back.RED + colorama.Fore.LIGHTWHITE_EX + " Error: On Client ")
	elif response.status_code in range(500, 599):
		print(colorama.Back.RED + colorama.Fore.LIGHTWHITE_EX + " Error: On Server ")
	
	# restart logic

	restart = input( colorama.Fore.RESET + colorama.Back.RESET + "\nWould you like to run again? [y/n] " + colorama.Fore.LIGHTYELLOW_EX)

	if restart in ["y", "Y"]:
		print(colorama.Fore.RESET + colorama.Back.RESET)
		main()

	else:
		print(colorama.Fore.LIGHTRED_EX + "Exiting...")
		time.sleep(1)
		os.system("cls")
		exit()


main()