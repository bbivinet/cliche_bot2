import random


def handle_response(msg: str) -> str:
    message = msg.lower()
    args = message.split()
    if(args[0] == "plot"):
        return "WIP"
    if(args[0] == "cliche"):
        return get_random_line(args)
    

"""def get_plot(msg: list(str)) -> str:
    if(len(msg) != 2):
        print("usage: plot script#")
        return "n"
    if not 1 <= int(msg[1]) <= 100:
        print("we haven't written past 100 Sohail")
        return "n" """
    
def get_random_line(msg: list) -> str:
    
    if(len(msg) == 1):
        msg.append(str(random.randint(1, 100)))
    if not 1 <= int(msg[1]) <= 100:
        return "We haven't written past 100 Sohail :("
    filename = "scripts/" + (msg[1]+".txt")
    file = open(filename, mode = "r", encoding = "utf-8")
    lines = file.read().splitlines()
    lines = list(filter(None, lines))
    file.close()
    return random.choice(lines)
    
    
    


    
     
    
    
    