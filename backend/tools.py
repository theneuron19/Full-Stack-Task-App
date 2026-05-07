import re

class BaseTool:
    name = ""
    def execute(self, input_data: str):
        raise NotImplementedError()

class TextProcessorTool(BaseTool):
    name = "TextProcessorTool"
    def execute(self, input_data: str):
        if "uppercase" in input_data.lower():
            res = input_data.upper()
        elif "lowercase" in input_data.lower():
            res = input_data.lower()
        else:
            res = f"Word count: {len(input_data.split())}"
        return res

class CalculatorTool(BaseTool):
    name = "CalculatorTool"
    def execute(self, input_data: str):
        # Basic regex to extract numbers and operator
        match = re.search(r'(\d+)\s*([\+\-\*\/])\s*(\d+)', input_data)
        if match:
            a, op, b = match.groups()
            return str(eval(f"{a}{op}{b}"))
        return "Error: Could not parse arithmetic expression."

class WeatherMockTool(BaseTool):
    name = "WeatherMockTool"
    def execute(self, input_data: str):
        city = input_data.split("in")[-1].strip() or "Unknown City"
        return f"The weather in {city} is 22°C and Sunny."