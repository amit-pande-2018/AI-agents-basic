from smolagents import CodeAgent, LiteLLMModel, PythonInterpreterTool

# Initialize the model
model = LiteLLMModel(model_id="ollama_chat/llama3.2:3b", api_key="ollama")

# Create an agent with the Python interpreter tool
agent = CodeAgent(tools=[PythonInterpreterTool()], model=model)

# Run the agent
result = agent.run("Calculate the sum of numbers from 1 to 10. Subtract 15 from it. Multiply by 5 and give me answer.")
print(result)