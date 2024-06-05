import webbrowser
    
website_map = {
  "chat": 'https://chatgpt.com/',
  "gem": 'https://gemini.google.com/app'
}

def getFunc(input):
    words = input.split()
    url = website_map.get(words[0])
    
    if(url):
        webbrowser.open(url)
    else:
        print("Instruction " + url + " not understood")
    
    if(len(words) > 1):
        question = " ".join(words[1:])
