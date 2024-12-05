name_dict = {}

def name_adder():
    name = input("What's your name?\n")
    bid = int(input("How much is your bid?($)\n"))
    name_dict[name] = bid

while True:
    name_adder()
    answer = input("Is there anyone else who wants to bid? yes/no\n")
    if answer.lower() == "no":
        break
max_name=""
max_bid=0
for i in name_dict:
    if name_dict[i]>max_bid:
        max_name=i
        max_bid=name_dict[i]
print(f"{max_name} is winner with {max_bid}$ bid.")