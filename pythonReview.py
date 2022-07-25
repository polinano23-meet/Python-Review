def create_youtube_video(title,description):
	title=input("enter the video title")
	description=input("enter a description for the video")
	video={"title":title,"description":description,"likes":0,"dislikes":0,"comments":{"username":""}}

	return video


def like(video):
	if "likes" in video:
		video["likes"] +=1;

	return video


def dislike(video):
	if "dislikes" in video:
		video["dislikes"] +=1;

	return video


def add_comment(youtubevideo,username,comment_text):
	youtubevideo["comments"][username]:comment_text

	return youtubevideo

new_video = create_youtube_video("Hey world","A song's music video")
for L in range(496):
	like(new_video)
print(new_video)

