import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from get_transcript import get_transcript
from logger import logger
import time


load_dotenv()  #loads all enrivtonment variables from .env file

prompt = """ You are Youtube video summarizer. You will be given a Youtube video transcript and you will summarize it in a few sentences."""

def summarize_transcript(url):
    """
    Summarizes a given youtube video transcript using OpenAI's ChatGPT model.
    """
    if "youtube.com/watch?v=" not in url:
        raise ValueError("Invalid YouTube video URL. Please provide a valid URL.")

    logger.info(f"Summarizing transcript for video URL: {url}")
    start_time = time.perf_counter()

    # Initialize the ChatOpenAI model
    chat_models = ChatOpenAI(
        model = "gpt-3.5-turbo",
        temperature = 0,
        openai_api_key = os.getenv("OPENAI_API_KEY")
    )

    # Create a prompt for the model
    full_prompt = f"{prompt}\n\nTranscript:\n{get_transcript(url)}"

    # Get the summary from the model
    response = chat_models.invoke(full_prompt)

    execution_time = time.perf_counter() - start_time
    logger.info(f"Summary generated successfully in {execution_time:.2f} seconds for video URL: {url}")
    
    return response.content

if __name__ == "__main__":
    youtube_video_url = "https://www.youtube.com/watch?v=2dRvcgskIxY"
    summary = summarize_transcript(youtube_video_url)
    print(summary)