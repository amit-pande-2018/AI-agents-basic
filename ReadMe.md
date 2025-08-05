first install pycharm in your machine

Then set up a new python project. It will ask for setup. Install python 3.11 and ask it to install poetry via pip.

poetry add smolagents --extras toolkit

It gives this error:

You must provide an api_key to work with nebius API or log in with `hf auth
login`.

The solution is to create a huggingface account. Then click on your icon on top right and in the menu select access 
token. Generate a new token for use and copy it and save it somewhere locally safe.

Click `hf auth login` on the terminal in pycharm and enter your access token. 

Now you are able to use Huggingface.

This will be able to run smol_agent1.py for a few times but then it will start asking for money. 

Either we can pay money and get credits in Huggingface account. The other option is to run the LLM locally on the same laptop. 

`poetry add ollama`

The command above will install Ollama. 

Method 1: Automatic (Recommended)
On Windows/Mac, Ollama typically starts automatically after installation and runs in the background.
Method 2: Manual Start
If it's not running, open terminal/command prompt and run:
bashollama serve
This starts the Ollama server on http://localhost:11434

Now, although ollama is running it is not yet running a LLM model. 

Make sure that ollama is running on latest version. Otherwise uninstall and install latest from their website.
(sometimes a restart of laptop may be required)

We want to locally run a small LLM We choose Gemma3n from Google

`ollama pull gemma3n`

`poetry add "smolagents[litellm,toolkit]"`

Use `poetry show` to see what all is instaled.


I am getting wierd pydantic warnings like 
`PydanticSerializationUnexpectedValue(Expected 9 fields but got 5: Expected `Message` - serialized value may not be as expected [input_value=Message(content='The solu...er_specific_fields=None), input_type=Message])
  PydanticSerializationUnexpectedValue(Expected `StreamingChoices` - serialized value may not be as expected [input_value=Choices(finish_reason='st...r_specific_fields=None)), input_type=Choices])
`
The versions of pydantic and openai are not matching. 

One solution is to install latest version of both. If that doesn't work type - `poetry show smolagents --tree` and it will show you exact which version of openai i can use. Use the exact version solved my problem. 

 `poetry add openai@1.68.2`
