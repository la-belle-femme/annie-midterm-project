Project 1: AI Chatbot with Function Calling features
Instructions
This project aims to develop a chatbot using the OpenAI API implements function calling to connect the chatbot to external data sources. Students will be provided a list of libraries and APIs that can be easily attached to the chatbot to expand its ability. 

Libraries and APIs: 
•	datetime - Python library that can return the current time and date. 
•	psutil - Python library that can return the battery status of the device the script is running on. 
•	NewsAPI - News aggregation API that can return the current top headlines. 
•	OpenWeatherMap API - Weather API that returns current weather based on location. 
•	Wolfram Alpha Short Answers API - Answer engine that returns factual information
Project Tasks: 
1.	Conversational Chatbot 
a.	Make a loop where the prompt and response pairs are appended to the message list
2.	Data Retrieval Functions 

a.	Set up accounts and API keys for the chosen data source APIs.
b.	Use the Python libraries and APIs within functions to return the desired data. 
3.	Function Description 
a.	Detail the intended use of the functions in natural language so the model can understand when to use the functions properly. 
b.	Determine what arguments (if any) are necessary for each function. 
4.	Function Calling Implementation 
a.	Use the response object to call the function(s) chosen by the model. 
b.	Append the function result to the message list for the model to generate the natural language response. 
5.	Documentation 
a.	Create detailed documentation explaining the generation steps, assumptions, and decisions.
b.	Include comments in the code to make it more understandable and maintainable. 
6.	Testing and Validation 
a.	Test the function calling with multiple prompts that invoke different (or multiple) functions to be called. 
b.	Validate the results against the expected outcomes. 
c.	BONUS: Automate the testing using a dictionary of prompts and expected function calls.


Requirements (e.g., Python version, libraries)
a. I installed python 3.12.2, but python 3.8 and above works well for the project.Installation steps (e.g., cloning the repository, installing dependencies)
b. I installed the following libraries and APIs: -

- datetime: A Python standard library that provides functions to handle dates and times.

- psutil: A cross-platform library for retrieving information on running processes and system utilization.
pip install psutil
- NewsAPI: An API to fetch current top headlines.```bash
pip install newsapi-python
- OpenWeatherMap API: Provides current weather information based on location.
- Wolfram Alpha Short Answers API: Delivers factual information in response to queries.
Environment Setup
created a `.env` file in the root of the project directory with the following keys:
- `OPENAI_API_KEY`: my API key for accessing OpenAI services.
- `NEWS_API_KEY`: my API key for NewsAPI.
- `OPENWEATHER_API_KEY`: my API key for OpenWeatherMap.
- `WOLFRAM_APP_ID`: my app ID for Wolfram Alpha.

## Setup Instructions

## Detailed instructions on how I set up the project environment:

## 1- Set up my development environment:
a. Created a new directory for my project: mkdir"name_of_my_directory", cd "name_of_my_directory"

## 2- Virtual Environment

a. Set up a virtual environment by creating a virtual environment with the command: python -m venv chatbot_env

b. Activated the virtual environment with command: chatbot_env\Scripts\activate

## 3- Installed required libraries with command:pip install openai psutil requests newsapi-python wolframalpha python-dotenv

## 4- Signed up and obtained API keys from websites:

- <https://openai.com/>,
- <https://newsapi.org/>,
- <https://openweathermap.org/>,
- <https://developer.wolframalpha.com/>

## 5- Environment Variables.

a.In the same working directory, I created a .env file to set up my environment variables,

b.Added to my .env file the following :

OPENAI_API_KEY=my_openai_api_key_here

NEWS_API_KEY=my_newsapi_key_here

OPENWEATHER_API_KEY=my_openweathermap_api_key_here

WOLFRAM_APP_ID=my_wolfram_alpha_app_id_here

## 6- Created the first script called annie-midterm-project.py

## 7- Created the automated test script called annie-automated-test_script.py

## 8- On my terminal, Ran python annie-midterm-project.py and python annie-automated-test_script.py.

## 9-When prompted entered the following questions:

."What time is it?"

."What's the battery status of this device?"

."Give me the top headlines for technology in the US."

."What's the weather like in New York?"

."What's the capital of Cameroon?"

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



