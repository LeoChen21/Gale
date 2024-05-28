def chat():
    print("chat")
    
function_map = {
  "chat": chat,
}

def getFunc(input):
    func = function_map.get(input)
    
    if(func):
        func()
    else:
        print("Instruction " + input + " not understood")
        
