# <<<<<<<<<<<<<<<<<<<<<<<<<<<DOCUMENTATION SECTION>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
Name: Amrita 1.0
Author: Sombit Pramanik
Usage: Start the program and when it says "I am listening," you can ask your query.
Functionalities: This program seamlessly works with the OpenAPI key and other API keys, saving time in the programming journey.
Limitations: This AI is not trained by us. It is a combination of multiple AIs that are professionally trained in their respective fields and companies.

List of AI used in this project:
    - Open AI
    - Weather API
    - News API
    ...
"""
# <<<<<<<<<<<<<<<<<<<<<<<< IMPORTING SYSTEM LIBRARIES >>>>>>>>>>>>>>>>>>>>>>>>>>>>
import os
import datetime
import time
import subprocess
import platform

# <<<<<<<<<< CHECKING FOR THE REQUIRED LIBRARY INSTALLED ON THE MACHINE >>>>>>>>>>>>>
required_libraries = ['speech_recognition', 'pyttsx3', 'webbrowser', 'openai', 'json', 'requests']

missing_libraries = []
for library in required_libraries:
    try:
        __import__(library)
    except ImportError:
        missing_libraries.append(library)

if missing_libraries:
    print(f"The following libraries are missing: {', '.join(missing_libraries)}")

    answer = input("Do you want to install the missing libraries? (y/n): ")
    if answer.lower() == 'y':
        for library in missing_libraries:
            subprocess.check_call(['pip', 'install', library])
    else:
        print(f"Please install the required libraries manually.\nMissing libraries are : {library}")
        exit()

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<STARTING OF THE PROGRAM>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# {{{{{{{{{{{{{{ Import the required packages }}}}}}}}}}}}}}}}}}}}}
import speech_recognition as sr
import pyttsx3
import webbrowser
import openai
import requests
import json

# {{{{{{{{{{{{{{{ DECLARATION OF GLOBAL VARIABLES AND REQUIRED MACROS }}}}}}}}}}}}}}}}}}}}}}}
apikey = "Replace it with your OpenAI API Key "
ptsystem = platform.system()
current_time = datetime.datetime.now().strftime("%I:%M %p")
current_time2 = datetime.datetime.now().strftime("%H")
chatstr = ""


# {{{{{{{{{{{{{{{{{{{{ DEFINITIONS FOR ALL USER-DRIVEN FUNCTIONS }}}}}}}}}}}}}}}}}}
def say(txt):
    """
    Outputs voice from the AI.

    Args:
        txt (str): The text to be spoken.
    """
    engine = pyttsx3.init()
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume + 0.25)  # Increase the volume by 25%
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Index 1 is for a female voice
    engine.say(txt)
    engine.runAndWait()


def take_command():
    """
    Listens to user's voice input and converts it into text.

    Returns:
        str: The recognized text.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1  # Default is 0.8
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            return query
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand."
        except sr.RequestError:
            return "Sorry, I'm having trouble accessing the Google Speech Recognition service."


def ai(prompt):
    """
    Outputs: Reply from Open AI Generative Intelligence.

    Args:
        prompt (str): The text to be recognized by Google Speech-to-Text.
    """
    text1 = f"Open AI Response for prompt: {prompt}\n*********\n\n"
    openai.api_key = apikey
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text1 += response["choices"][0]["text"]
    print(text1)
    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")
    if "write the code" in user_say.lower() or "write a code" in user_say.lower():
        with open(f"OpenAI/{''.join(prompt.split('intelligence')[1:30])}.txt", "w") as f:
            f.write(text1)
    return text1


def chat(prompt):
    """
        Outputs: Reply from Open AI Generative Intelligence.

        Args:
            prompt (str): The text to be recognized by Google Speech-to-Text.
    """
    global chatstr
    chatstr += f"Sombit: {prompt}\nAmrita: "
    openai.api_key = apikey
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatstr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response["choices"][0]["text"])
    chatstr += f"{response['choices'][0]['text']}\n"
    print(chatstr)
    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")
    if "write the code" in user_say.lower() or "write a code" in user_say.lower():
        with open(f"OpenAI/{''.join(prompt.split('code')[1:30])}.txt", "w") as f:
            f.write(chatstr)

    return response["choices"][0]["text"]


def get_news(api_key):
    # Make API request to fetch news data
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"  # Replace 'in' with your desired country code
    response = requests.get(url)

    if response.status_code == 200:
        news_data = response.json()
        articles = news_data['articles']

        # Extract and display the latest news headlines
        for article in articles:
            title = article['title']
            source = article['source']['name']
            print(f"{source}: {title}")
            say(f"{source}: {title}")
    else:
        print("Failed to fetch news data.")
        say("Failed to fetch news data.")


def get_weather(api_key):
    # Make API request to fetch weather data
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q=ghatal"  # Replace with your desired location
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        # Extract relevant information from the weather data
        temperature = weather_data['current']['temp_c']
        humidity = weather_data['current']['humidity']
        condition = weather_data['current']['condition']['text']

        # Display or use the weather information as desired
        print(f"Current temperature: {temperature}°C")
        say(f"Current temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        say(f"Humidity: {humidity}%")
        print(f"Condition: {condition}")
        say(f"Condition: {condition}")
    else:
        print("Failed to fetch weather data.")


# Existing list of favorite sites
sites = [
    ["YouTube", "https://m.youtube.com"],
    ["Wikipedia", "https://www.wikipedia.com"],
    ["Google", "https://www.google.com"],
    ["Amazon", "https://www.amazon.in"],
    ["My Account", "https://www.myaccount.google.com"],
    ["Email", "https://www.gmail.com"],
    ["Check my Emails", "https://www.gmail.com"],
    ["WhatsApp", "https://web.whatsapp.com"],
    ["Check Messages", "https://web.whatsapp.com"],
    ["GPT Chat", "https://chat.openai.com"],
    ["Open AI", "https://chat.openai.com"]
]

time1s = [
    ["1 minutes", 60],
    ["2 minutes", 120],
    ["3 minutes", 180],
    ["4 minutes", 240],
    ["5 minutes", 300],
    ["6 minutes", 360],
    ["7 minutes", 420],
    ["8 minutes", 480],
    ["9 minutes", 540],
    ["10 minutes", 600]
]

# Collection of System Apps for All Favorite Operating systems
if ptsystem == "Windows":
    apps = [
        ["Music Player", "start wmplayer"],
        ["File Explorer", "explorer"],
        ["Notepad", "notepad"],
        ["Calculator", "calc"],
        ["Task Manager", "taskmgr"],
        ["Set an alarm", "start ms-clock"],
        ["Clock", "start ms-clock"]
    ]
elif ptsystem == "Linux":
    apps = [
        ["Music Player", "rhythmbox"],
        ["File Manager", "nautilus"],
        ["Text Editor", "gedit"],
        ["Calculator", "gnome-calculator"],
        ["System Monitor", "gnome-system-monitor"]
    ]
elif ptsystem == "Darwin":  # macOS
    apps = [
        ["Music Player", "open -a Music"],
        ["Finder", "open -a Finder"],
        ["Text Editor", "open -a TextEdit"],
        ["Calculator", "open -a Calculator"],
        ["Activity Monitor", "open -a 'Activity Monitor'"]
    ]
else:
    print("Add apps manually; we don't know your operating system")
    say("Add apps manually; we don't know your operating system")
    apps = []  # No specific apps defined for other operating systems

#       <<<<<<<<<<<<<<<<<<<<<<<<<<<<<< EXECUTION OF MAIN PROGRAM >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
if __name__ == '__main__':
    # Greet the user based on the time of day
    if int(current_time2) < 12:
        say("Good morning, sir! How may I help you today?")
    elif int(current_time2) < 17:
        say("Good afternoon, sir! How may I help you today?")
    else:
        say("Good evening, sir! How may I help you today?")

    # Start of the AI Speech system
    while True:
        say("I am listening...")
        user_say = take_command()
        if "exit" in user_say.lower() or "stop" in user_say.lower() or "terminate" in user_say.lower():
            if int(current_time2) < 12:
                say("Goodbye, sir. Have a nice day.")
            elif int(current_time2) < 17:
                say("Goodbye, sir. Have a nice day.")
            else:
                say("Good night, sir. Sweet dreams.")
            break
        elif "the time".lower() in user_say.lower():
            say(f"Sir, the time is {current_time}")
        elif "check for news updates" in user_say.lower() or "tell me about the news" in user_say.lower():
            # Call the function and pass your news API key
            get_news('6a0daf37543944bda7fd8375fb7a8f67')
        elif "the weather".lower() in user_say.lower():
            # Call the function and pass your weather API key
            get_weather('6cd47505c61946949ad180125230406')

        elif "using Artificial Intelligence".lower() in user_say.lower():
            print("I am using Artificial Intelligence to perform tasks, sir.\n")
            say("I am using Artificial Intelligence to perform tasks, sir.")
            text = ai(prompt=user_say)
            print(text)
        # elif "wait for some time" in user_say.lower() or "wait" in user_say.lower():
        #     say("Sir, I will go to sleep for 2 minute.")
        #     time.sleep(120)
        #     say("Welcome back, sir.")
        for time1 in time1s:
            if f"sleep for {time1[0]}".lower() in user_say.lower():
                say(f"Slipping for {time1[0]},sir.")
                time.sleep(time1[1])
        else:
            print("Chatting...\n")
            chat(user_say)
            print(chatstr)

        # Open favorite sites based on the user's input
        for site in sites:
            if f"open {site[0]}".lower() in user_say.lower():
                say(f"Opening {site[0]} for you, sir.")
                webbrowser.open(site[1])

        # Open system apps based on the user's input
        for app in apps:
            if f"open {app[0]}".lower() in user_say.lower():
                say(f"Opening {app[0]} for you, sir.")
                os.system(app[1])
