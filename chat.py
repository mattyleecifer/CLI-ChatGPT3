import openai, pyperclip, sys
from IPython.display import clear_output

openai.api_key = "sk-yourkeyhere"

# model = "text-chat-davinci-002-20221122"
model = "text-davinci-003"
# model = "text-curie-001"
# model = "text-babbage-001"
# model = "text-ada-001"

def chat():
    text = "Answer like you are ChatGPT.\n"
    totalcount = 0
    while True:
        clear_output()
        try:
            print(text + "\nTokencount: " + str(tokencount) + "\nTotal: " + str(totalcount) + "\n")
        except:
            print(text + "\n")
        userinput = input("User: ")
        if userinput.startswith("!"):
            text = "Answer like you are ChatGPT.\n"
            tokencount = 0
            totalcount = 0
            print("Chat reset!\n")
        elif userinput.startswith("@"):
            tokencount = 0
            output = add_number_to_line(text, 0)
            print(output + "\n")
            editchoice = input("What lines do you want to remove? Enter range (eg. 1:4) or list (eg. 1,4,5)")
            if ":" in editchoice:
                editchoice = editchoice.split(":")
                editchoice = [int(x) for x in editchoice]
                text = removerange(editchoice, text)
            elif "," in editchoice:
                editchoice = editchoice.split(",")
                editchoice = [int(x) for x in editchoice]
                text = removesingle(editchoice, text)
            else:
                print("Nothing changed!")
        else:
            text = text + "User: " + userinput + "\nChatGPT: "
            response, tokencount = getresponse(text, 0.6, 2000, 1, 0.0, 0.0)
            text = text + response + "\n"
            totalcount = totalcount + tokencount

def removesingle(s, t):
    # s is a set of the single numbers to remove
    t = t.split('\n')
    removed_list = [item for index, item in enumerate(t) if index not in s]
    result = "\n".join(removed_list)
    return result

def removerange(s, t):
    # s is range of numbers to delete
    t = t.split('\n')
    start = s[0]
    end = s[1]
    del t[start:end]
    result = "\n".join(t)
    return result

def add_number_to_line(s, num):
    lines = s.split('\n')
    result = ''
    for i in range(len(lines)):
        result += str(num + i) + '. ' + lines[i] + '\n'
    return result

def getresponse(text, temp, max_tokens, top_p, f_p, p_p):
    response = openai.Completion.create(
        model=model,  # text-ada-001 text-babbage-001 text-curie-001 text-davinci-003
        prompt=text,
        temperature=temp,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=f_p,
        presence_penalty=p_p
    )
    tokencount = response["usage"]["total_tokens"]
    response = response["choices"][0]["text"].replace("<|im_end|>", '')
    return response, tokencount

if __name__ == '__main__':
    chat()
