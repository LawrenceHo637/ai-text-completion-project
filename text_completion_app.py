import logging
import time

logging.basicConfig(format='%(message)s')
log = logging.getLogger(__name__)
option = 1

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
        # print("Invalid input! Please enter a valid number (1, 2, 3).\n", file=sys.stderr)
        log.warning("Invalid input! Please enter a valid number (1, 2, 3).\n")
        time.sleep(0.5)
        continue

    # Execute the chosen option
    if option == 1:
        pass
    elif option == 2:
        pass
    else:
        print("Goodbye!")
        break
