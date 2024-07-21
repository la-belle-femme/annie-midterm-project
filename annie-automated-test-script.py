import unittest
from chatbot import chat_with_gpt, function_descriptions

class TestChatbot(unittest.TestCase):
    def test_function_calls(self):
        test_cases = {
            "What time is it?": "get_current_datetime",
            "What's the battery status of this device?": "get_battery_status",
            "Give me the top headlines for technology in the UK.": "get_top_headlines",
            "What's the weather like in New York?": "get_weather",
            "What's the capital of France?": "get_wolfram_short_answer",
        }

        for prompt, expected_function in test_cases.items():
            with self.subTest(prompt=prompt):
                messages = [{"role": "user", "content": prompt}]
                response = chat_with_gpt(messages)
                
                self.assertIsNotNone(response, f"No response received for prompt: {prompt}")
                
                function_call = response.choices[0].message.get("function_call")
                self.assertIsNotNone(function_call, f"No function call for prompt: {prompt}")
                
                actual_function = function_call.get("name")
                self.assertEqual(actual_function, expected_function, 
                                 f"Expected {expected_function}, but got {actual_function} for prompt: {prompt}")

    def test_function_descriptions(self):
        expected_functions = [
            "get_current_datetime",
            "get_battery_status",
            "get_top_headlines",
            "get_weather",
            "get_wolfram_short_answer"
        ]

        actual_functions = [func["name"] for func in function_descriptions]

        self.assertEqual(set(actual_functions), set(expected_functions), 
                         "Function descriptions do not match expected functions")

if __name__ == "__main__":
    unittest.main()