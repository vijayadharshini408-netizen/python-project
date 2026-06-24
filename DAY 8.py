print("WELCOME TO LOVE CALCULATOR")
name_1 = input("ENTER YOUR NAME : ")
name_2 = input("ENTER YOUR PATNER NAME : ")
def calculate_love_score(name_1, name_2):
    combined = name_1 + name_2
    combined = combined.lower()
    print(combined)
    true_score= combined.count("t")+combined.count("r")+combined.count("u")+combined.count("e")
    print(true_score)
    love_score = combined.count("l")+combined.count("o")+combined.count("v")+combined.count("e")
    print(love_score)
    score= int(str(true_score) + str(love_score))
    if score < 10 or score > 90:
      print("Your love is terrible 😢")
    elif score < 40 or score > 85:
      print("Your love is bad 😬")
    elif score < 65 or score > 76:
      print("Your love is ok 🙂")
    else:
        print("Your love is great")    
calculate_love_score(name_1, name_2)   