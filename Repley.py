
import openai


openai.api_key = ""


def ReplyIt(query, chat_log=None):
    """
    This function takes a user's query, and an optional chat_log context, 
    and generates a response using OpenAI's API.
    
    Args:
    query (str): The user's question or statement.
    chat_log (str): The conversation history or context.
    
    Returns:
    str: The AI-generated response.
    """
    prompt = f'{chat_log}You: {query}\nIchchha: '
    
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            temperature=0.5,
            max_tokens=40,
            top_p=0.3,
            frequency_penalty=0.5,
            presence_penalty=0
        )
        answer = response.choices[0].text.strip()
        return answer
    except openai.error.RateLimitError:
       
        print("Rate limit exceeded. Please check your API usage or consider upgrading your plan.")
        return "I'm currently experiencing high demand. Please give me a moment and try again."
    except openai.error.OpenAIError as e:
        
        print(f"An error occurred: {e}")
        return "Apologies, I'm having some technical difficulties ."
