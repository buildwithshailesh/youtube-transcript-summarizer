import time
import streamlit as st
from llm import summarize_transcript


st.set_page_config(
    page_title="YouTube Video Summarizer",
    page_icon=":movie_camera:",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("YouTube Video Summarizer")

st.markdown(
    """
    This app summarizes the transcript of a YouTube video using OpenAI's ChatGPT model.
    Enter a YouTube video URL below to get a concise summary of its content.
    """
)

st.caption(
    "Powered by LangChain • OpenAI • YoutubeAPI"
    )

st.caption("Note: The summary is generated based on the video's transcript and may not capture all details accurately.")

with st.form(key="youtube_form"):
    youtube_url = st.text_input("YouTube Video URL", placeholder="Enter a YouTube video URL here...")
    submit_button = st.form_submit_button(label="Get Summary")

if submit_button:
    if youtube_url:
        with st.spinner("Fetching transcript and generating summary..."):
            try:
                start_time = time.time()

                summary = summarize_transcript(youtube_url)
                st.success("Summary generated successfully!")
                execution_time = time.time() - start_time
                st.caption(f"Execution time: {execution_time:.2f} seconds")
                st.markdown("### Summary:")
                st.write(summary)

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid YouTube video URL.")