# Amrita 1.0

## Introduction
Amrita 1.0 is an AI-powered program developed by Sombit Pramanik. It is designed to seamlessly work with various APIs, including OpenAI, Weather API, News API, and more. This program allows users to interact with the AI through voice commands, saving time in the programming journey.

## Functionalities
- Voice recognition: The program can listen to user queries through a microphone and convert them into text.
- Voice output: The program can respond to user queries by generating voice output using the pyttsx3 library.
- OpenAI integration: The program leverages OpenAI's generative intelligence to provide intelligent responses and carry out tasks.
- Weather information: Users can obtain current weather information for a specified location using the Weather API.
- News updates: Users can fetch and read the latest news headlines using the News API.
- Open websites: Users can open their favorite websites by simply issuing voice commands.
- System apps: Users can open system applications on different operating systems.

## Limitations
- The AI used in this project is not trained by the developers. It is a combination of multiple professionally trained AIs from various companies.
- The program relies on external APIs for weather information and news updates, which may have limitations or restrictions based on the API providers' terms of service.

## Installation and Setup
To run this program, make sure you have the following libraries installed:
- speech_recognition
- pyttsx3
- webbrowser
- openai
- json
- requests

If any of the above libraries are missing, you can install them using the following command:



## Usage
1. Start the program.
2. When prompted with "I am listening," you can ask your query or give a command.
3. The program will process your query, provide responses, and perform various tasks based on the command.

## Examples
- User: "What's the time?"
  - Amrita: "Sir, the time is [current_time]."

- User: "Check for news updates."
  - Amrita: Fetches the latest news headlines and reads them out.

- User: "Tell me about the weather."
  - Amrita: Retrieves and provides current weather information for a specified location.

- User: "Open YouTube."
  - Amrita: Opens the YouTube website in the default web browser.

- User: "Open Music Player."
  - Amrita: Opens the Music Player application based on the user's operating system.

- User: "Exit" or "Stop" or "Terminate"
  - Amrita: Stops the program and says goodbye to the user.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
