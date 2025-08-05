from smolagents import CodeAgent, InferenceClientModel

# Initialize a model (using Hugging Face Inference API)
model = InferenceClientModel()  # Uses a default model

# Create an agent with no tools
agent = CodeAgent(tools=[], model=model)

# Run the agent with a task
result = agent.run("Calculate the sum of numbers from 1 to 10")

#result = agent.run("Calculate the sum of numbers from 1 to 10. Substract 15 from it. Multiply by 5 and give me answer.")
print(result)

