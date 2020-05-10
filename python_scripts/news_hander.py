import get_news

if __name__ == "__main__":

    script_directory = get_news.script_directory
    posts_directory = get_news.posts_directory
    maxitem_url = get_news.maxitem_url
    maxitem = get_news.maxitem
    latest_post_file = get_news.latest_post_file
    latest_post_id = get_news.get_latest_post_id(latest_post_file)
    item_list = []
    stories_urls_list = []
    new_items = maxitem - 200
    post_count = 0

    for i in range(new_items, maxitem):
        new_items += 1
        item_list.append(new_items)
    
    # If url are stories then 
    items_urls_list = get_news.new_items_url(item_list)

    for item in items_urls_list:

        if post_count >= 2:
            get_news.save_latest_post_id(new_post.id)
            break

        response = get_news.check_url(item)

        if isinstance(response, dict):
            new_post = get_news.Story(item)
            new_post.id = str(response['id'])
            new_post.title = response['title']
            new_post.story_url = response['url']
            new_post.story_content()
            if new_post.content != None:
                get_news.create_post(new_post.id, new_post.title, new_post.story_url, new_post.markdown)
                post_count += 1
                print(post_count)
        else:
            pass

    

# TODO        
# check if the  the link from hn showw that the story is not dead. or that the score is greater than 50
# When creating an object, the call is being redundant because it uses the same hn_url twice, once to check for story and twice to get the additional info. 
# This should not be done.
# people in Latin America who read news from websites in English get
# translation automatically by google.  Possible option is to get stories
# translated to look at what the algorithm misses and implement some time
# of improvement based entity recognition?
# Translation must include the original hyperlink in order to give the option to findout

# Test in AWS
#The latest_story_id has to be saved to a text file containing only the id and nothing else
