#list of letters in the alphabet
alphList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#main function
def main():
    inputted = input("Write what you want moved ")
    amount = input("How much do you want to shift it? ")
    amount = int(amount)
    temp = ""
    #iterates through the letters that the user inputs
    for i in range(0,len(inputted)):
        if inputted[i]==" ":
           temp+=" "
        else:
            index = alphList.index(inputted[i])+amount
            while index>25:
                index-=26
            if inputted[i].islower():
                temp+=alphList[index]
            else:
                temp+=alphList[index].upper()
    print(temp)
    #recalls at the end
    main()
main()