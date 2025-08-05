from smolagents import CodeAgent, LiteLLMModel
import smolagents.models as m



import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

model=LiteLLMModel(model_id="ollama_chat/llama3.2:3b", api_key="ollama")

agent = CodeAgent(
    tools=[],
    model=model,
    add_base_tools=True,
    additional_authorized_imports=[
        'sympy', 'numpy', 'sys', 'wikipedia', 'scipy', 'requests', 'bs4'
    ],
    max_steps=2,  # Limit to 2 attempts

)

result = agent.run("Solve the quadratic equation 2*x+3x^2=33?")
print(result)

