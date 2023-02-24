# CLI-ChatGPT3
This is basically just emulating ChatGPT in the command line. The original prompt instructs GPT-3 to 'Answer like you are ChatGPT' (I know, super creative) and then the script basically loops and keeps a log of all the inputs and outputs so you can maintain a chat conversation.

<img src="https://github.com/mattyleecifer/CLI-ChatGPT3/blob/main/gptsarcasm.png" alt="GPT being sarcastic" width = "600" />

Each loop contains every other loop - this means that it can get expensive very quickly. 

I've added some extra commands to make this less of an issue:
- Starting a line with ! will erase the entire log and start over
- Starting a line with @ with enter an edit mode where you can either choose to delete a range of lines (eg. 1:5) or individual lines (eg. 1,4,5,8)
- I know I said individual lines above, but you will need to add a ',' if you want to delete an single individual line (eg. 1,). Sorry.

Fun fact, most of this program was written using this program. I made the original loop and then used it to write the other functions eg. removesingle(), removerange(), and add_number_to_line().

# Requirements
You will need Python and the OpenAI package (pip install openai).

You will also need to obtain an [OpenAI API key](https://platform.openai.com/account/api-keys) and enter it into line 3 of the script where it says openai.api_key = "yourkeyhere"

# Todo
I'm planning to add these features shortly:
- scrape web pages/search results
- scan files and store prompts

Feel free to contact me if you have any ideas!
