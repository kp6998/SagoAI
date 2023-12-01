import openai
import os

def CallAPI(prompt):
    # Retrieve the OpenAI API key from an environment variable
    openai.api_key = "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"

    # Ensure that the API key is available
    if openai.api_key is None:
        raise ValueError("OpenAI API key is not set.")

    # Generate text using GPT-3 through the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-002",  # Specify the engine
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract the generated text from the response
    generated_text = response.choices[0].text

    # Return the generated text
    return generated_text
