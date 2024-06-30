# Gale

The purpose of this project is to create a way to voice interface with chatgpt or other apps without having them on the same screen. 
The goal is to optimize workflows without creating additional visible elements.

Instructions:
run git clone https://github.com/LeoChen21/Gale <br />
pip install -r requirements.txt
Next, add a file called secretkey.txt to the outermost folder with your personal OpenAI API key and no whitespaces.
Check out this website for more instructions on the API key: https://platform.openai.com/docs/api-reference/authentication
Run python main.py to start the script. 

Keywords:
hello: prints "Hello there!"
chat: opens chatgpt in a new window
exit: stops the script
"query": the question that follows is input into chatgpt's API and prints the response in a popup window. 

Errors: could not build wheels for pyaudio fix: sudo apt-get install portaudio19-dev
Doesn't run on WSL due to hardware being shielded
