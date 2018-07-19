from youtube_dl import YoutubeDL


# Sample 1: Download a single youtube video
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=wJnBTPUQS5A']) 



# Sample 2: Download multiple youtube videos
dl = YoutubeDL()
# Put list of song urls in download function to download them, one by one
dl.download(['https://www.youtube.com/watch?v=aJOTlE1K90k', 'https://www.youtube.com/watch?v=09R8_2nJtjg'])



# Sample 3: Download audio
options = {
    'format': 'bestaudio/audio' 
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=c3jHlYsnEe0'])



# Sample 4: Search and then download the first video
options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1 
}
dl = YoutubeDL(options)
dl.download(['con điên TAMKA PKL'])


# Sample 5: Search and then download the first audio
options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1, 
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Nhớ mưa sài gòn lam trường'])