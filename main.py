import random, os, pyfiglet
#pip install pyfiglet
from os import path
result = pyfiglet.figlet_format("D e e p x", font = "3-d" ) 

cwd=os.getcwd()
chars = """ 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""	
def main_folder_check():
	if os.path.isdir("edmessage"):
		pass
	else:
		os.mkdir("edmessage")
		main()
def hash_Message(Dmessage):
	global chars
	dr_text= Dmessage
	dr_message=""
	for letter in dr_text:
		index=rkey.index(letter)
		dr_message+=chars[index]
	print("\nHASH TO TEXT MESSAGE\n \t\t\t ",dr_message)	


def text_to_hash(Emessage):
	global chars, rkey 
	text = Emessage
	app_text = ""
	#encript
	for letter in text:
		index=chars.index(letter)
		app_text+=rkey[index]
	print("\nTEXT TO HASH MESSAGE\n \t\t\t ",app_text)

def check_key_exist(keys):
	global chars, rkey,cwd,result
	if not os.path.isdir(keys):
		os.mkdir(keys)
		os.chdir(keys)
		chars= list(chars)
		key = chars.copy()
		random.shuffle(key)
		for i in key:
			data = "".join(key)
		with open("key.txt","w") as f:
			f.write(str(data))
			f.close()
	else:
		os.chdir(keys)
		with open("key.txt","r") as f2:
			join_data = f2.read()
			f2.close()
			
		rkey=list(join_data)
		
		while True:
			check=input(" 1 : chek hash message  \n 2 : text to hash  \n 3 : exit \n 4 : another key\n > ")
			if check == "1":
				#dcript
				#os.system("clear")
				Dmessage=input("enter your hash message : ")
				hash_Message(Dmessage)
				

			elif check =="2":
				#os.system("clear")
				Emessage=input("enter your text message : ")
				text_to_hash(Emessage)
				
			elif check == "3":
				exit()
			elif check == "4":
				os.system("clear")
				os.chdir(cwd)
				main()
			else:
				continue

def main():
	global result
	print(result)
	main_folder_check()
	os.chdir("edmessage")
	keys = input("enter your key : ")
	check_key_exist(keys)
main()
