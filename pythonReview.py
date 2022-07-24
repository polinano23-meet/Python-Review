def create_youtube_video():
	title=input("Enter the video's title")
	desctiption=input("Enter a description about the video")
	video={"title":title,"description":description,"likes":0,"dislikes":0,"comments":{"username":""}}

	return video


def like():
	