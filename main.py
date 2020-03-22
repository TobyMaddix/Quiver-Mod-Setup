import setup

helpScreens = {"syntax":"""Here is an example of what too type:
testcommand \"teststring\""""}

def console_input_parse(input):
    paramList = []
    quoteActive = False
    temp01 = ""
    #turns the input into a readable list
    for x in input:
        if (x == " " and quoteActive == False):#checks for spaces and if we are in a quote
            paramList.append(temp01)
            temp01 = ""
        elif (x == "\"" or x == "\'"):#checks if we are in a quote, handles quotes
            if (quoteActive):
                quoteActive = False
                if (temp01 == ""):
                    paramList.append(temp01)#makes sure that if there is nothing, it is counted
            else:
                quoteActive = True
        else:
            temp01 = temp01 + x
    if (len(temp01) != 0):#checks to make sure we aren't copying a blank
        paramList.append(temp01)#does a final copy to makes sure we got everything
    return paramList

def console_input_execute(paramList):
    if (paramList[0] == "mod"):
        if (paramList[1] == "setup"):
            setupmod = setup.mod(paramList[2],"resource\createmod.zip")
            setupmod.mod_extract()
            del setupmod
            return True
    elif (paramList[0] == "help"):
        print("================================================================")
        print(shared_ui_help(paramList[1],helpScreens))
        print("================================================================")
        return True
    else:
        return False       

def shared_ui_help(screentype,screens):
    for x in screens:
        if (x == screentype):
            return screens.get(x)

while True:
    userInput = input("USER: ")
    userParams = console_input_parse(userInput)
    if (console_input_execute(userParams)):
        print("command successful")
    else:
        print("command failed")

print("================================================================")
print(shared_ui_help("syntax",{"syntax":"""Here is an example of what too type:
testcommand \"teststring\""""}))
print("================================================================")