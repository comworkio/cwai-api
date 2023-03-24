from utils.gpt2 import generate_response

def main():
    while True:
        prompt = input("User: ")
        if prompt.lower() == 'quit':
            break

        response = generate_response(prompt)
        print("CWAI:", response[0])

if __name__ == '__main__':
    main()
