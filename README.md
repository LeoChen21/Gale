# Gale

The purpose of this project is to create a way to voice interface with chatgpt or other apps without having them on the same screen. 
The goal is to optimize workflows without creating additional visible elements.

Instructions:
- run git clone https://github.com/LeoChen21/Gale <br />
- pip install -r requirements.txt <br />
- Next, add a file called secretkey.txt to the outermost folder with your personal OpenAI API key and no whitespaces. <br />
- Check out this website for more instructions on the API key: https://platform.openai.com/docs/api-reference/authentication <br />
- Run python main.py to start the script. <br />

Keywords: <br />
- hello: prints "Hello there!" <br />
- chat: opens chatgpt in a new window <br />
- exit: stops the script <br />
- "query": the question that follows is input into chatgpt's API and prints the response in a popup window.  <br />

Errors: 
- could not build wheels for pyaudio fix: sudo apt-get install portaudio19-dev <br />
- Doesn't run on WSL due to hardware being shielded
