import random

def generate_compliment():

compliments = [

"You're amazing!",

"You light up the room.",

"You're a true star!",

"You're incredible just as you are.",

"You have a heart of gold."

]

return random.choice(compliments)

def main():

print("Compliment Generator\n")

while True:

input("Press Enter to receive a compliment (or type 'quit' to exit): ")

print(generate_compliment(), "\n")

if input().lower() == 'quit':

break

if __name__ == "__main__":

main()
