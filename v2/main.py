from runtime import RunTime

runtime = RunTime()

while True:

    user_input = input("You: ")

    if user_input.strip().lower() == "exit":

        break

    response = runtime.step(user_input)

    print(f"Assistant: {response}")

