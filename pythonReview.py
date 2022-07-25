def create_youtube_video(title,description):
	video={"title":title,"description":description,"likes":0,"dislikes":0,"comments":{}}

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
	youtubevideo["comments"][username]=comment_text

	return youtubevideo

new_video = create_youtube_video("Hey world","A song's music video")
print(new_video)
add_comment(new_video,"polina","hey")
for L in range(495):
	like(new_video)
print(new_video)

