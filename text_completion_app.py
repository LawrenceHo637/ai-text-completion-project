from transformers import AutoTokenizer, AutoModelForCausalLM
import logging
import time

# Load AI model (https://huggingface.co/deepseek-ai/DeepSeek-R1)
tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-R1", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("deepseek-ai/DeepSeek-R1", trust_remote_code=True)
model.eval()

# Set up logger for displaying error messages
logging.basicConfig(format='%(message)s')
log = logging.getLogger(__name__)
option = 1

# Dictionary to store the model's parameter settings
settings = {
    "max_new_tokens": 200,      # Controls response length
    "do_sample": True,          # Enable sampling for creativity
    "top_k": 50,                # Top-k sampling (randomized narrowing)  deterministic vs variety
    "top_p": 0.95,              # Nucleus sampling (0 - 1), deterministic vs diversity
    "temperature": 0.8,         # Controls randomness
    "repetition_penalty": 1.1,  # Helps avoid repetition by penalizing repeated phrases
    "num_return_sequences": 1   # Number of outputs generated
}

while option != 3:
    try:
        # Display menu of options
        print("What would you like to do?")
        print("\t1. Enter Prompt")
        print("\t2. Settings")
        print("\t3. Exit")
        option = int(input("Pick one of the above.\nValid options are [1, 2, 3]: "))

        if option < 1 or option > 3:
            raise ValueError
    except ValueError:
        log.warning("Invalid Selection! Please enter a valid number (1, 2, 3).\n")
        time.sleep(0.5)
        continue

    # Execute the chosen option
    if option == 1:
        # Take user prompt and pass it to the model
        try:
            prompt = input("Enter a prompt: ")
            inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

            outputs = model.generate(
                **inputs,
                max_new_tokens=settings["max_new_tokens"],
                do_sample=settings["do_sample"],
                top_k=settings["top_k"],
                top_p=settings["top_p"],
                temperature=settings["temperature"],
                repetition_penalty=settings["repetition_penalty"],
                num_return_sequences=settings["num_return_sequences"]
            )

            generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
            print(generated_text)
        except ValueError:
            pass

    elif option == 2:
        # Change model generation settings
        parameter = 1

        while parameter != 8:
            # Show which parameters the user can change
            try:
                print("Which setting would you like to change?")
                print("\t1. max_new_tokens")
                print("\t2. do_sample")
                print("\t3. top_k")
                print("\t4. top_p")
                print("\t5. temperature")
                print("\t6. repetition_penalty")
                print("\t7. num_return_sequences")
                print("\t8. Exit")
                parameter = int(input("Pick one of the above.\nValid options are [1, 2, 3, 4, 5, 6, 7, 8]: "))

                if parameter < 1 or parameter > 8:
                    raise ValueError
            except ValueError:
                log.warning("Invalid Selection! Please enter a valid number (1, 2, 3, 4, 5, 6, 7, 8).\n")
                time.sleep(0.5)
                continue

            if parameter == 1:
                # Change max_new_tokens
                try:
                    print(f"max_new_tokens\t current value: {settings["max_new_tokens"]}")
                    change = int(input("Enter a number: "))

                    if change < 1:
                        raise ValueError
                except ValueError:
                    log.warning("Invalid Input! Please enter a positive whole number.\n")
                    time.sleep(0.5)
                    continue
                else:
                    settings["max_new_tokens"] = change

            elif parameter == 2:
                # Change do_sample
                try:
                    print(f"do_sample\t current value: {settings["do_sample"]}")
                    change = input("Enter T/F: ").upper()

                    if change != "T" or change != "F":
                        raise ValueError
                except ValueError:
                    log.warning("Invalid Input! Valid input is T or F.\n")
                    time.sleep(0.5)
                    continue
                else:
                    if change == "T":
                        settings["do_sample"] = True
                    else:
                        settings["do_sample"] = False

            elif parameter == 3:
                # Change top_k
                try:
                    print(f"top_k\t current value: {settings["top_k"]}")
                    change = int(input("Enter a number: "))

                    if change < 0:
                        raise ValueError
                except ValueError:
                    log.warning("Invalid Input! Please enter a non-negative whole number.\n")
                    time.sleep(0.5)
                    continue
                else:
                    settings["top_k"] = change

            elif parameter == 4:
                # Change top_p
                try:
                    print(f"top_p\t current value: {settings["top_p"]}")
                    change = float(input("Enter a number: "))

                    if change < 0.0 or change > 1.0:
                        raise ValueError
                except ValueError:
                    log.warning("Invalid Input! Please enter a non-negative number between 0.0 and 1.0 inclusive.\n")
                    time.sleep(0.5)
                    continue
                else:
                    settings["top_p"] = change

            elif parameter == 5:
                # Change temperature
                try:
                    print(f"temperature\t current value: {settings["temperature"]}")
                    change = float(input("Enter a number: "))

                    if change < 0.0 or change > 2.0:
                        raise ValueError
                except ValueError:
                    log.warning("Invalid Input! Please enter a non-negative number between 0.0 and 2.0 inclusive.\n")
                    time.sleep(0.5)
                    continue
                else:
                    settings["temperature"] = change

            elif parameter == 6:
                # Change repetition_penalty
                try:
                    print(f"repetition_penalty\t current value: {settings["repetition_penalty"]}")
                    change = float(input("Enter a number: "))

                    if change < 1.0:
                        raise ValueError
                except ValueError:
                    log.warning("Invalid Input! Please enter a non-negative number greater than or equal to 1.0.\n")
                    time.sleep(0.5)
                    continue
                else:
                    settings["repetition_penalty"] = change

            elif parameter == 7:
                # Change num_return_sequences
                try:
                    print(f"num_return_sequences\t current value: {settings["num_return_sequences"]}")
                    change = int(input("Enter a number: "))

                    if change < 1:
                        raise ValueError
                except ValueError:
                    log.warning("Invalid Input! Please enter a whole number greater than or equal to 1.\n")
                    time.sleep(0.5)
                    continue
                else:
                    settings["num_return_sequences"] = change

            else:
                break
    else:
        print("Goodbye!")
        break
