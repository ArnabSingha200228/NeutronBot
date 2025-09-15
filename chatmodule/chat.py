from youtube_transcript_api import YouTubeTranscriptApi

video_id = "LzqLlqMVaizPF3jb"
transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
print(transcript[:5])
