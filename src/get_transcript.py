from youtube_transcript_api import YouTubeTranscriptApi
from logger import logger
import time

def get_transcript(youtube_video_url):
    """
    Fetches the transcript of a Youtube video given its URL.
    """

    if "youtube.com/watch?v=" not in youtube_video_url:
        raise ValueError("Invalid YouTube video URL. Please provide a valid URL.")

    logger.info(f"Fetching transcript for video URL: {youtube_video_url}")

    start_time = time.perf_counter()

    try:
        video_id = youtube_video_url.split("v=")[1].split("&")[0]

        youtube_transcript_api = YouTubeTranscriptApi()

        transcript_list = youtube_transcript_api.fetch(video_id)

        logger.info(f"Transcript fetched successfully for video ID: {video_id}")

        transcript_text = " ".join(snippet.text.strip() for snippet in transcript_list)

        return transcript_text
    
    except Exception as e:
        print(f"Error fetching transcript: {e}")


if __name__ == "__main__":
    youtube_video_url = "https://www.youtube.com/watch?v=2dRvcgskIxY"
    transcript = get_transcript(youtube_video_url)
    print(transcript)