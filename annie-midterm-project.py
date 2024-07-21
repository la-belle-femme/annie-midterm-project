from dotenv import load_dotenv
load_dotenv("C:\\CanCode\\FUNCTION-CALLING-ASSIGNMENT\\function_calling_chatbot\\adapi.env")


import openai
import os
import datetime
import psutil
import requests
from newsapi import NewsApiClient
import wolframalpha
import json
import sys
import unittest

# Set up API keys from environment variables for security
openai.api_key = os.getenv("OPENAI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
WOLFRAM_APP_ID = os.getenv("WOLFRAM_APP_ID")

# Initialize API clients
news_client = NewsApiClient(api_key=NEWS_API_KEY)
wolfram_client = wolframalpha.Client(WOLFRAM_APP_ID)

# Data retrieval functions

def get_current_datetime():
    """Return the current date and time."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_battery_status():
    """Return the current battery status of the device."""
    battery = psutil.sensors_battery()
    if battery:
        return f"Battery percentage: {battery.percent}%, Power plugged in: {battery.power_plugged}"
    return "Battery information not available."

def get_top_headlines(country='us', category='general'):
    """
    Return top headlines from NewsAPI.
    
    Args:
    country (str): The 2-letter ISO 3166-1 code of the country.
    category (str): The category of news (e.g., business, technology).
    """
    try:
        headlines = news_client.get_top_headlines(country=country, category=category)
        if headlines['articles']:
            return "\n".join([f"- {article['title']}" for article in headlines['articles'][:5]])
        return "No headlines available."
    except Exception as e:
        return f"Error fetching news: {str(e)}"

def get_weather(city):
    """
    Return current weather for a given city using OpenWeatherMap API.
    
    Args:
    city (str): The name of the city to get weather information for.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': OPENWEATHER_API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            return f"Weather in {city}: {data['weather'][0]['description']}, Temperature: {data['main']['temp']}°C"
        return f"Error: {data['message']}"
    except Exception as e:
        return f"Error fetching weather: {str(e)}"

def get_wolfram_short_answer(query):
    """
    Return a short answer from Wolfram Alpha.
    
    Args:
    query (str): The question to ask Wolfram Alpha.
    """
    try:
        res = wolfram_client.query(query)
        return next(res.results).text
    except Exception as e:
        return f"Error querying Wolfram Alpha: {str(e)}"

# Function descriptions for OpenAI function calling
function_descriptions = [
    {
        "name": "get_current_datetime",
        "description": "Get the current date and time",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "get_battery_status",
        "description": "Get the current battery status of the device",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "get_top_headlines",
        "description": "Get top news headlines for a specific country and category",
        "parameters": {
            "type": "object",
            "properties": {
                "country": {
                    "type": "string",
                    "description": "The 2-letter ISO 3166-1 code of the country you want headlines for. Default is 'us'."
                },
                "category": {
                    "type": "string",
                    "description": "The category you want headlines for. Options are: business, entertainment, general, health, science, sports, technology. Default is 'general'."
                }
            },
            "required": []
        }
    },
    {
        "name": "get_weather",
        "description": "Get current weather information for a specific city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The name of the city to get weather information for"
                }
            },
            "required": ["city"]
        }
    },
    {
        "name": "get_wolfram_short_answer",
        "description": "Get a short answer to a question using Wolfram Alpha",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The question to ask Wolfram Alpha"
                }
            },
            "required": ["query"]
        }
    }
]

def chat_with_gpt(messages):
    """
    Send a request to the OpenAI API and return the response.
    
    Args:
    messages (list): The conversation history.
    
    Returns:
    dict: The API response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
            functions=function_descriptions,
            function_call="auto"
        )
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    """Main function to run the chatbot."""
    messages = [{"role": "system", "content": "You are a helpful assistant with access to various functions to provide up-to-date information."}]
    
    print("Welcome to the AI Chatbot! Type 'quit' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Add user message to the conversation history
        messages.append({"role": "user", "content": user_input})
        
        # Get response from OpenAI API
        response = chat_with_gpt(messages)
        
        if response:
            response_message = response.choices[0].message
            
            # Check if the model wants to call a function
            if response_message.get("function_call"):
                function_name = response_message["function_call"]["name"]
                function_args = json.loads(response_message["function_call"]["arguments"])
                
                # Call the appropriate function
                if function_name == "get_current_datetime":
                    function_response = get_current_datetime()
                elif function_name == "get_battery_status":
                    function_response = get_battery_status()
                elif function_name == "get_top_headlines":
                    function_response = get_top_headlines(**function_args)
                elif function_name == "get_weather":
                    function_response = get_weather(**function_args)
                elif function_name == "get_wolfram_short_answer":
                    function_response = get_wolfram_short_answer(**function_args)
                else:
                    function_response = f"Error: Unknown function '{function_name}'"
                
                # Add the function response to the conversation history
                messages.append({
                    "role": "function",
                    "name": function_name,
                    "content": function_response
                })
                
                # Get a new response from the API, now including the function response
                second_response = chat_with_gpt(messages)
                if second_response:
                    assistant_response = second_response.choices[0].message['content']
                    print("Assistant:", assistant_response)
                    messages.append({"role": "assistant", "content": assistant_response})
                else:
                    print("Sorry, I couldn't generate a response. Please try again.")
            else:
                # If no function call, just print the response
                assistant_response = response_message['content']
                print("Assistant:", assistant_response)
                messages.append({"role": "assistant", "content": assistant_response})
        else:
            print("Sorry, I couldn't generate a response. Please try again.")

def run_tests():
    """Run automated tests for the chatbot."""
    loader = unittest.TestLoader()
    start_dir = '.'
    suite = loader.discover(start_dir, pattern="test_*.py")

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_tests()
    else:
        main()