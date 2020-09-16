from facebook_scraper import get_posts

for post in get_posts('ThaiPBSFan',pages=50):
    Ntext = post['text'][:100]
    if ('แกนนำ'in Ntext):
        print(Ntext)
        print('Likes: ',post['likes'])
        print('post: ',post['post_url'])
        print('link: ',post['link'])
        print('----------------------------------------')