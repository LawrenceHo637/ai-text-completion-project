# Capstone Project: AI-Powered Text Completion
## Setup
This program uses Google's gemma-3-1b-it model, directly loaded from (https://huggingface.co/google/gemma-3-1b-it).

## Usage
Users can use the program by running the text_completion_app.py file. Once running, the program will give the user three options to choose from:
1. Enter Prompt
2. Settings
3. Exit
Users can pick an option by inputing a corrsponding number (i.e., 1, 2, 3)
1. Enter Prompt
   - The program will ask the user to enter a prompt which will be sent to the AI model to generate a response.
   - The program will ensure the prompt is not empty and will continue to ask the user for a prompt unitl they type "exit."
   - Once the model generates a response, it will be printed to standard output for the user to see.
2. Settings
   - This option allows the user to change the model parameters.
   - Parameters include:
       - max_new_tokens         Controls response length
       - do_sample              Enables sampling for creativity
       - top_k                  Limits the model to sampling from the k most probable tokens at each generation step
       - top_p                  Keeps the most probable tokens whose total probability mass exceeds p.
       - temperature            Controls output randomness
       - repetition_penality    Helps avoid repetition by penalizing repeated phrases
   - The program will ensure the user's input is a valid value for each parameter.
3. Exit
   - Exits the program when selected by the user

## Dependencies
This program has the following dependencies:
- transformers library to import the tokenizer and gemma-3-1b-it model.
- torch library to run the AI model with the GPU if cuda is available.
- logging library to display errors when invalid input or errors occur.
- time library to ensure error messages are displayed before the program continues as usual.
- triton,which the gemma-3-1b-it model uses
  - Supported Platforms:
    - Linux
  - Supported Hardware:
    - NVIDIA GPUs (Compute Capability 8.0+)
    - AMD GPUs (ROCm 6.2+)
    - Under development: CPUs
