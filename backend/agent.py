from tools import TextProcessorTool, CalculatorTool, WeatherMockTool

class AgentController:
    def __init__(self):
        self.tools = {
            "text": TextProcessorTool(),
            "calc": CalculatorTool(),
            "weather": WeatherMockTool()
        }

    def process(self, user_input: str):
        steps = []
        steps.append(f"Step 1: Received input '{user_input}'")
        
        # Intent Parsing Logic
        selected_key = None
        if any(word in user_input.lower() for word in ["+", "-", "*", "/", "calculate"]):
            selected_key = "calc"
        elif "weather" in user_input.lower():
            selected_key = "weather"
        else:
            selected_key = "text"

        tool = self.tools[selected_key]
        steps.append(f"Step 2: Selected tool: {tool.name}")
        
        try:
            result = tool.execute(user_input)
            steps.append(f"Step 3: Tool result: {result}")
        except Exception as e:
            result = f"Error: {str(e)}"
            steps.append(f"Step 3: Execution failed.")

        steps.append("Step 4: Returning result to user")
        return result, tool.name, steps