import sys
import time
import os
import speech_recognition as sr
import pyaudio
import random
import getpass
import pygame
key = 'NamanIsTheBest'
_image_library = {}
def get_image (path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image
def note(toNote):
    file = open("C:\\Documents and Settings\\Naman Chhaparia\\My Documents\\Rainmeter\\Skins\\Iron Man\\Notes\\notes.txt", "a")
    file.write("NEW NOTE : " + toNote + "\n----------------------------------------")
    file.close()
def timer(minutes):
    minutes = int(minutes)
    if minutes < 0:
        say("Invalid value for minutes, should be greater than or equal to 0")
    seconds = minutes * 60
    if minutes == 1:
        unit_word = " minute"
    else:
        unit_word = " minutes"
    try:
        if minutes > 0:
            say("Setting a timer for " + str(minutes) + unit_word + ", sir")
            time.sleep(seconds)
        say("time up,. time up,. time up,. time up,. time up")
    except KeyboardInterrupt:
        say("Exiting timer, sir")
def write(text):
    black = (0, 0, 0)
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    label = myfont.render(text, 1, black)
    screen.blit(label, (120, 20))
    pygame.display.flip()
    #time.sleep(4)
def get_pass():
    text = ''
    done = False
    shifton = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return text
                    done = True
                    break
                elif event.key == pygame.K_BACKSPACE:
                    text = text[0:-1]
                elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    shifton = True
                else:
                    if shifton == True:
                        text += chr(event.key).upper()
                        shifton = False
                    else:
                        text += chr(event.key)
def say(text) :
    file = open('say.vbs', 'w')
    file.write('dim sapi : set sapi = CreateObject("sapi.spvoice") : sapi.Speak "' + text + '"')
    file.close()
    os.system('say.vbs')
    print ("Janus : " + text)
def getArray(operand):
    retval = []
    x = 0
    y = 0
    i = 0
    for char in operand:
        operand = operand.lower()
        if char == '.' or char == '_' or char == '-' or char == '(' or char == ')' or char == '[' or char == ']' or char == ' ':
            i = 1
            retval.append(operand[x : y])
            x = y + 1
            y += 1
        else:
            y += 1
    if i == 0:
        retval.append(operand)
    return retval
def playDefiniteSong(reqSong):
    reqSong = getArray(reqSong)
    path = 'c:\\docume~1\\namanc~1\\desktop\\naman\\mymusi~1\\'
    songs = os.listdir(path)
    i = 0
    for oneSong in songs:
        i = 0
        oneSongWords = getArray(oneSong)
        for word in reqSong:
            if word in oneSongWords:
              i += 1
            if i >= len(reqSong):
              os.system('start ' + path + oneSong)
def playSong():
    path = "c:\\docume~1\\namanc~1\\desktop\\naman\\mymusi~1\\";
    ch = random.choice(os.listdir(path));
    os.system('start ' + path + ch);
def type(to_type):
   for char in to_type:
      sys.stdout.write(char);
      sys.stdout.flush();
      time.sleep(0.05);
def to_wiki(data):
    data_len=len(data);
    run=0;
    ctrlx=0;
    retval='';
    while(ctrlx==0):
        run+=1;
        a=data[0:1];
        data=data[1:data_len];
        if(a==' '):
            retval=retval+'_';
        elif(run>data_len):
            ctrlx=1;
        else:
            retval=retval+a;
    return retval;
def to_search(data):
    data_len=len(data);
    run=0;
    ctrlx=0;
    retval='';
    while(ctrlx==0):
        run+=1;
        a=data[0:1];
        data=data[1:data_len];
        if(a==' '):
            retval=retval+'+';
        elif(run>data_len):
            ctrlx=1;
        else:
            retval=retval+a;
    return retval;
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Janus - AI')
done = False
clock = pygame.time.Clock()
x = 30
y = 30
r=sr.Recognizer()
screen.fill((255, 255, 255))
screen.blit(get_image('black_mic.png'), (x, y))
pygame.display.flip()
clock.tick(60)
say("Welcome, sir.")
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            toSay = ["Exiting, sir.", "Bye-bye, sir.", "See ya later, sir.", "Nice talking to you, sir !!"]
            toSayInd = random.randrange(0, 3)
            say(toSay[toSayInd])
            done = True
    screen.fill((255, 255, 255))
    screen.blit(get_image('black_mic.png'), (x, y))
    pygame.display.flip()
    clock.tick(60)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RETURN] :
        with sr.Microphone() as source:          
            screen.fill((255, 255, 255))
            screen.blit(get_image('red_mic.png'), (x, y))
            pygame.display.flip()
            clock.tick(60)
            inp=r.listen(source)
            try:
                screen.fill((255, 255, 255))
                screen.blit(get_image('recog.png'), (x, y))
                pygame.display.flip()
                clock.tick(60)
                audio=r.recognize_google(inp)
                audio = audio.lower()
                print ("User : " + audio)
                screen.fill((255, 255, 255))
                screen.blit(get_image('speaker.png'), (x, y))
                pygame.display.flip()
                clock.tick(60)
                if(audio=="bye bye")|(audio=="see you later")|(audio=="exit"):
                             toSay = ["Exiting, sir.", "Bye-bye, sir.", "See ya later, sir.", "Nice talking to you, sir !!"]
                             toSayInd = random.randrange(0, 3)
                             say(toSay[toSayInd])
                             done = True
                elif(audio=="hi")|(audio=="hi genes"):
                             toSay = ["Hello, sir.", "Hi there, sir.", "Hey, sir."]
                             toSayInd = random.randrange(0, 2)
                             say(toSay[toSayInd])
                elif(audio=="who are you"):
                                say("I am Janus, an artificial intelligence system designed by Naman Chapparria at TechNo Times Inc")
                elif(audio=="shutdown computer"):
                                 ctrl=1;
                                 say("Sure, sir. Your computer will shutdown in,. 10,. 9,. 8,. 7,. 6,. 5,. 4,. 3,. 2,. 1")
                                 os.system("shutdown -s -f -t 01");
                elif(audio=="open browser"):
                                 say("Opening Citrio browser, sir")
                                 os.system("start citrio.exe");
                elif(audio=="open facebook"):
                                 say("Opening the Facebook website, sir")
                                 os.system("start https://facebook.com");
                elif(audio=="open whatsapp"):
                                 say("Opening WhatsApp web, sir")
                                 os.system("start https://web.whatsapp.com");
                elif(audio=="open wikipedia"):
                                 say("Opening the wikipedia website, sir")
                                 os.system("start https://en.wikipedia.org/wiki/Main_Page");
                elif((audio.startswith("who is norman"))|(audio.startswith("who is naman"))|(audio.startswith("who is Noman"))):
                                 say("Naman Chapparria is a masterming programmer and my creator. He is the Founder and CEO of TechNo Times Inc, thanks for asking, now taking you to the TechNo Times Website")
                                 os.system("start http://technotimesme.weebly.com");
                elif(audio=="open scratch"):
                                 say("Opening scratch, sir")
                                 os.system("start c:\\docume~1\\namanc~1\\desktop\\scratch");
                elif(audio.startswith("google")):
                                 audio_len=len(audio);
                                 audio_ret=audio[7:audio_len];
                                 audio_ret_final=to_search(audio_ret);
                                 say("Initiating Google search for " + audio_ret + ", sir");
                                 file_bat=open("google_search.bat","w");
                                 file_bat.write("start https://google.co.in/search?q="+audio_ret_final+"\n");
                                 file_bat.close();
                                 os.system("google_search.bat");
                elif(audio.startswith("wiki")):
                                 audio_len=len(audio);
                                 audio_ret=audio[5:audio_len];
                                 audio_ret_final=to_wiki(audio_ret);
                                 say("Initiating Wikipedia search for " + audio_ret + ", sir");
                                 file_bat=open("wiki_search.bat","w");
                                 file_bat.write("start https://wikipedia.org/wiki/Special:Search/"+audio_ret_final+"\n");
                                 file_bat.close();
                                 os.system("wiki_search.bat");
                elif(audio=="open up the mailbox"):
                                 screen.fill((255, 255, 255))
                                 screen.blit(get_image('speaker.png'), (x, y))
                                 pygame.display.flip()
                                 clock.tick(60)
                                 say("Opening up the mailbox, sir.")
                                 os.system("start https://mail.google.com")
                                 os.system("start https://mail.yandex.com")
                                 '''say("The access to the mailbox is restricted to master Naman. Please enter the password to gain access")
                                 screen.fill((255, 255, 255))
                                 screen.blit(get_image('pass.png'), (x, y))
                                 pygame.display.flip()
                                 clock.tick(60)
                                 passwd = get_pass()
                                 if passwd == key :
                                      screen.fill((255, 255, 255))
                                      screen.blit(get_image('accurate_pass.png'), (x, y))
                                      pygame.display.flip()
                                      clock.tick(60)
                                      say("Opening up the mailbox, sir.")
                                      os.system("start https://mail.google.com")
                                 else :
                                      screen.fill((255, 255, 255))
                                      screen.blit(get_image('inaccurate_pass.png'), (x, y))
                                      pygame.display.flip()
                                      clock.tick(60)
                                      say("Password inaccurate. Access denied.")'''
                elif(audio=="namaste"):
                                 say("Namaste, sir")
                elif(audio=="tum kaun ho"):
                                 say("Mei Janus hoo. mujhko Naman Chapparria nai TechNo Times Inc. mei bun aia tha")
                elif(audio=="say hi to my friends"):
                                 say("Hello, dear friends. If you are master Naman's friends, then you are my friends as well.")
                elif(audio=="hello")|(audio=="hello genes"):
                                 say("Hello, sir")
                elif audio == "open up the main folder":
                                  screen.fill((255, 255, 255))
                                  screen.blit(get_image('speaker.png'), (x, y))
                                  pygame.display.flip()
                                  clock.tick(60)
                                  say("Opening up the main folder, sir.")
                                  os.system("start c:\\docume~1\\namanc~1\\desktop\\naman")
                                  '''say("The access to the main folder is restricted to master Naman. Please enter the password to gain access")
                                  screen.fill((255, 255, 255))
                                  screen.blit(get_image('pass.png'), (x, y))
                                  pygame.display.flip()
                                  clock.tick(60)
                                  passwd = get_pass()
                                  if passwd == key :
                                      screen.fill((255, 255, 255))
                                      screen.blit(get_image('accurate_pass.png'), (x, y))
                                      pygame.display.flip()
                                      clock.tick(60)
                                      say("Opening up the main folder, sir.")
                                      os.system("start c:\\docume~1\\namanc~1\\desktop\\naman")
                                  else :
                                      screen.fill((255, 255, 255))
                                      screen.blit(get_image('inaccurate_pass.png'), (x, y))
                                      pygame.display.flip()
                                      clock.tick(60)
                                      say("Password inaccurate. Access denied.")'''
                elif(audio=="open my movies"):
                                  say("Sure, sir")
                                  os.system("start c:\\docume~1\\namanc~1\\desktop\\naman\\movies");
                elif(audio=="open my music"):
                                  say("Sure, sir")
                                  os.system("start c:\\docume~1\\namanc~1\\desktop\\naman\\mymusi~1");
                elif audio == "what are you doing":
                                  toSay = ["Nothing much, getting bored by you, sir.", "I'm chatting with my friends on the Internet, sir.", "Multi tasking. Ha ha ha. I'm funny, ain't I, sir?", "A little of everything, and quite a bit of nothing, sir !!"];
                                  toSayInd = random.randrange(0, 4);
                                  say(toSay[toSayInd])
                elif audio == "open up the codex":
                                  screen.fill((255, 255, 255))
                                  screen.blit(get_image('speaker.png'), (x, y))
                                  pygame.display.flip()
                                  clock.tick(60)
                                  say("Opening up the Codex, sir.")
                                  os.system("start C:\\Codex")
                                  '''say("The access to the Codex is restricted to master Naman. Please enter the password to gain access")
                                  screen.fill((255, 255, 255))
                                  screen.blit(get_image('pass.png'), (x, y))
                                  pygame.display.flip()
                                  clock.tick(60)
                                  passwd = get_pass()
                                  if passwd == key :
                                      screen.fill((255, 255, 255))
                                      screen.blit(get_image('accurate_pass.png'), (x, y))
                                      pygame.display.flip()
                                      clock.tick(60)
                                      say("Opening up the Codex, sir.")
                                      os.system("start C:\\Codex")
                                  else :
                                      screen.fill((255, 255, 255))
                                      screen.blit(get_image('inaccurate_pass.png'), (x, y))
                                      pygame.display.flip()
                                      clock.tick(60)
                                      say("Password inaccurate. Access denied.")'''
                elif audio == "open up the study":
                                  screen.fill((255, 255, 255))
                                  screen.blit(get_image('speaker.png'), (x, y))
                                  pygame.display.flip()
                                  clock.tick(60)
                                  say("Opening up the study, sir.")
                                  os.system("start C:\\docume~1\\namanc~1\\desktop\\study")
                                  '''say("The access to the study is restricted to master Naman. Please enter the password to gain access")
                                  screen.fill((255, 255, 255))
                                  screen.blit(get_image('pass.png'), (x, y))
                                  pygame.display.flip()
                                  clock.tick(60)
                                  passwd = get_pass()
                                  if passwd == key :
                                      screen.fill((255, 255, 255))
                                      screen.blit(get_image('accurate_pass.png'), (x, y))
                                      pygame.display.flip()
                                      clock.tick(60)
                                      say("Opening up the study, sir.")
                                      os.system("start C:\\docume~1\\namanc~1\\desktop\\study")
                                  else :
                                      screen.fill((255, 255, 255))
                                      screen.blit(get_image('inaccurate_pass.png'), (x, y))
                                      pygame.display.flip()
                                      clock.tick(60)
                                      say("Password inaccurate. Access denied.")'''
                elif audio == "open notes":
                                  screen.fill((255, 255, 255))
                                  screen.blit(get_image('speaker.png'), (x, y))
                                  pygame.display.flip()
                                  clock.tick(60)
                                  say("Opening up the notes, sir.")
                                  os.system("start C:\\codex\\python\\janus\\notes.txt")
                                  '''say("The access to the notes is restricted to master Naman. Please enter the password to gain access")
                                  screen.fill((255, 255, 255))
                                  screen.blit(get_image('pass.png'), (x, y))
                                  pygame.display.flip()
                                  clock.tick(60)
                                  passwd = get_pass()
                                  if passwd == key :
                                      screen.fill((255, 255, 255))
                                      screen.blit(get_image('accurate_pass.png'), (x, y))
                                      pygame.display.flip()
                                      clock.tick(60)
                                      say("Opening up the notes, sir.")
                                      os.system("start C:\\codex\\python\\janus\\notes.txt")
                                  else :
                                      screen.fill((255, 255, 255))
                                      screen.blit(get_image('inaccurate_pass.png'), (x, y))
                                      pygame.display.flip()
                                      clock.tick(60)
                                      say("Password inaccurate. Access denied.")'''
                elif (audio == "i'm getting bored")|(audio == "i am getting bored"):
                                  toSay = ["Me too, sir.", "It indeed is a boring day, sir.", "I'm gonna try my best to entertain you, sir."];
                                  toSayInd = random.randrange(0, 3)
                                  say(toSay[toSayInd])
                elif audio == "play a song" :
                                  say("Playing any random song, sir")
                                  playSong();
                elif (audio == "you are funny") | (audio == "you're funny") :
                                  toSay = ["Pleased that you find me humorous, sir", "Thank you, sir. A secret, I've been watching Comedy Nights on Colors channel."];
                                  toSayInd = random.randrange(0, 2);
                                  say(toSay[toSayInd])
                elif audio.startswith("play"):
                    argument = audio[5:len(audio)]
                    say('Playing song ' + argument)
                    playDefiniteSong(argument)
                elif audio == "open up your code" or audio == "open up your coat":
                                  screen.fill((255, 255, 255))
                                  screen.blit(get_image('speaker.png'), (x, y))
                                  pygame.display.flip()
                                  clock.tick(60)
                                  say("Opening up my code, sir")
                                  os.system("start C:\\Python27\\Lib\\idlelib\\idle.pyw c:\\codex\\python\\Janus\\janus.py")
                                  '''say("The access to my code is restricted to master Naman. Please enter the password to gain access")                               
                                  screen.fill((255, 255, 255))
                                  screen.blit(get_image('pass.png'), (x, y))
                                  pygame.display.flip()
                                  clock.tick(60)
                                  passwd = get_pass()
                                  if passwd == key :
                                      screen.fill((255, 255, 255))
                                      screen.blit(get_image('accurate_pass.png'), (x, y))
                                      pygame.display.flip()
                                      clock.tick(60)
                                      say("Opening up my code, sir")
                                      os.system("start C:\\Python27\Lib\idlelib\idle.pyw c:\\codex\\python\\Janus\\janus.py")
                                  else :
                                      screen.fill((255, 255, 255))
                                      screen.blit(get_image('inaccurate_pass.png'), (x, y))
                                      pygame.display.flip()
                                      clock.tick(60)
                                      say("password inaccurate. Access denied.")'''
                elif audio == "open up the control panel":
                                  say("Opening ip the control panel, sir")
                                  os.system("start control")
                elif audio.startswith('set a timer for'):
                                  minutes = audio[16:audio.index(' m')]
                                  timer(minutes)
                elif audio.startswith('remove drive'):
                                  drive = audio[13:]
                                  todo = "start c:\\codex\\removedrive\\win32\\removedrive.exe " + drive + ":"
                                  os.system(todo)
                                  say("Drive " + drive + " removed successfully, sir")
                elif audio == "open up the task manager" :
                                  say("Opening task manager, sir")
                                  os.system("start taskmgr")
                elif audio == "open blue j":
                                  say("Opening blue j, sir.")
                                  os.system("c:\\docume~1\\namanc~1\\desktop\\bluej")
                elif audio.startswith("note down"):
                    audio = audio[5:len(audio)]
                    try:
                        note(audio)
                        screen.fill((255, 255, 255))
                        screen.blit(get_image('done.png'), (x, y))
                        pygame.display.flip()
                        clock.tick(60)
                        say("Noted down successfully, sir")
                    except Exception as e:
                        screen.fill((255, 255, 255))
                        screen.blit(get_image('error.png'), (x, y))
                        pygame.display.flip()
                        clock.tick(60)
                        print(e)
                        say("an error occured. please try again, sir")
                elif audio.startswith("weather "):
                    say("Sure, sir")
                    audio_ret_final=to_search(audio);
                    file_bat=open("google_search.bat","w");
                    file_bat.write("start https://google.co.in/search?q="+audio_ret_final+"\n");
                    file_bat.close();
                    os.system("google_search.bat");
                elif audio == "open my text editor":
                    say("opening sublime text editor, sir.")
                    os.system("c:\\progra~1\\sublim~1\\sublime_text")
                elif audio == "restart computer":
                    ctrl=1;
                    say("Sure, sir. Your computer will restart in,. 10,. 9,. 8,. 7,. 6,. 5,. 4,. 3,. 2,. 1")
                    os.system("shutdown -r -t 01")
                elif audio == "restart your self":
                    say("Restarting my services, sir.")
                    os.system("start c:\\codex\\python\\janus\\janus.py")
                    done = True
                else:
                    say("Sorry, sir. I did not understand what you just said")
            except Exception as e:
                screen.fill((255, 255, 255))
                screen.blit(get_image('error.png'), (x, y))
                pygame.display.flip()
                clock.tick(60)
                print(e)
                say("an error occured. please try again, sir")
