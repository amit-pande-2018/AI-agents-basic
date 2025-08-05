import streamlit as st
import time
from datetime import datetime
from smolagents import CodeAgent, LiteLLMModel, PythonInterpreterTool

# Page configuration
st.set_page_config(
    page_title="SmoLAgents Chat",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }

    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
    }

    .user-message {
        background-color: #f0f2f6;
        border-left-color: #667eea;
    }

    .agent-message {
        background-color: #e8f4fd;
        border-left-color: #4facfe;
    }

    .code-block {
        background-color: #2d3748;
        color: #e2e8f0;
        padding: 1rem;
        border-radius: 8px;
        font-family: 'Courier New', monospace;
        margin: 0.5rem 0;
    }

    .status-indicator {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        padding: 0.5rem;
        margin-bottom: 1rem;
    }

    .example-query {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 5px;
        padding: 0.5rem;
        margin: 0.25rem 0;
        cursor: pointer;
        transition: background-color 0.2s;
    }

    .example-query:hover {
        background-color: #ffeaa7;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def initialize_agent():
    """Initialize the SmoLAgents agent (cached to avoid reinitializing)"""
    try:
        # Initialize the model
        model = LiteLLMModel(model_id="ollama_chat/llama3.2:3b", api_key="ollama")

        # Create an agent with the Python interpreter tool
        agent = CodeAgent(tools=[PythonInterpreterTool()], model=model)

        return agent, None
    except Exception as e:
        return None, str(e)


def add_message_to_history(role, content, timestamp=None):
    """Add a message to the chat history"""
    if timestamp is None:
        timestamp = datetime.now().strftime("%H:%M:%S")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.session_state.messages.append({
        "role": role,
        "content": content,
        "timestamp": timestamp
    })


def display_chat_message(message):
    """Display a single chat message"""
    role = message["role"]
    content = message["content"]
    timestamp = message["timestamp"]

    if role == "user":
        st.markdown(f"""
        <div class="chat-message user-message">
            <strong>You ({timestamp}):</strong><br>
            {content}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-message agent-message">
            <strong>🤖 Agent ({timestamp}):</strong><br>
            {content}
        </div>
        """, unsafe_allow_html=True)


def run_agent_query(agent, query):
    """Run a query through the agent and return the result"""
    try:
        with st.spinner("🤖 Agent is thinking and executing code..."):
            result = agent.run(query)
        return result, None
    except Exception as e:
        return None, str(e)


def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🤖 Python in English BOT</h1>
        <p>Powered by Llama 3.2 with Python Interpreter</p>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar for agent info and controls
    with st.sidebar:
        st.header("🔧 Agent Configuration")

        # Initialize agent
        agent, error = initialize_agent()

        if agent:
            st.markdown("""
            <div class="status-indicator">
                <strong>✅ Agent Status:</strong> Ready<br>
                <strong>🧠 Model:</strong> ollama_chat/llama3.2:3b<br>
                <strong>🛠️ Tools:</strong> PythonInterpreterTool
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error(f"❌ Failed to initialize agent: {error}")
            st.info("Make sure Ollama is running and the Llama 3.2 model is available.")

        st.header("📝 Example Queries")
        st.markdown("Click on any example to try it:")

        example_queries = [
            "Calculate the sum of numbers from 1 to 10. Subtract 15 from it. Multiply by 5 and give me answer.",
            "Generate a list of prime numbers up to 50",
            "Create a simple plot using matplotlib",
            "Calculate the factorial of 10",
            "Solve the quadratic equation: x² + 5x + 6 = 0",
            "Generate 10 random numbers and calculate their mean and standard deviation",
            "Create a fibonacci sequence up to the 20th term"
        ]

        for i, query in enumerate(example_queries):
            if st.button(f"📋 Example {i + 1}", key=f"example_{i}", help=query, use_container_width=True):
                st.session_state.example_query = query

        # Clear chat button
        if st.button("🗑️ Clear Chat", type="secondary", use_container_width=True):
            if "messages" in st.session_state:
                st.session_state.messages = []
            st.rerun()

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # Add welcome message
        add_message_to_history("assistant", """
        Welcome to SmoLAgents Chat! 🚀

        I'm a CodeAgent powered by Llama 3.2 with Python interpreter capabilities. I can help you with:

        • **Mathematical calculations** and analysis
        • **Data processing** and visualization  
        • **Code execution** and debugging
        • **Statistical computations**
        • **Problem solving** with Python

        Try asking me to solve problems, run calculations, or execute Python code!
        """)

    # Display chat history
    st.header("💬 Chat History")

    # Create a container for messages
    chat_container = st.container()

    with chat_container:
        for message in st.session_state.messages:
            display_chat_message(message)

    # Handle example query selection
    if hasattr(st.session_state, 'example_query'):
        st.session_state.user_input = st.session_state.example_query
        del st.session_state.example_query

    # Chat input
    st.header("✍️ Your Message")

    # Create two columns for input and button
    col1, col2 = st.columns([4, 1])

    with col1:
        user_input = st.text_area(
            "Ask me anything...",
            value=st.session_state.get('user_input', ''),
            placeholder="e.g., Calculate the sum of numbers from 1 to 100",
            height=100,
            key="chat_input"
        )

    with col2:
        st.write("")  # Add some spacing
        st.write("")  # Add some spacing
        send_button = st.button("🚀 Send", type="primary", use_container_width=True)

    # Process user input
    if send_button and user_input.strip():
        if not agent:
            st.error("❌ Agent not initialized. Please check the sidebar for errors.")
            return

        # Add user message to history
        add_message_to_history("user", user_input)

        # Get agent response
        result, error = run_agent_query(agent, user_input)

        if result:
            # Add agent response to history
            add_message_to_history("assistant", result)
        else:
            # Add error message
            error_msg = f"❌ **Error occurred:** {error}\n\nPlease check your Ollama setup or try a different query."
            add_message_to_history("assistant", error_msg)

        # Clear the input and rerun to show new messages
        st.session_state.user_input = ""
        st.rerun()

    # Instructions at the bottom
    with st.expander("ℹ️ How to Use", expanded=False):
        st.markdown("""
        ### Getting Started

        1. **Make sure Ollama is running** on your system
        2. **Ensure the Llama 3.2 model is installed** (`ollama pull llama3.2:3b`)
        3. **Type your question** in the text area above
        4. **Click Send** or try one of the example queries from the sidebar

        ### What You Can Ask

        - Mathematical calculations and problem solving
        - Data analysis and statistical computations
        - Code generation and execution
        - Algorithm implementations
        - Visualization requests (matplotlib, etc.)

        ### Tips for Better Results

        - Be specific about what you want
        - Ask for step-by-step solutions
        - Request code explanations when needed
        - Try breaking complex problems into smaller parts
        """)


if __name__ == "__main__":
    main()