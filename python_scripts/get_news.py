import os
import requests
import html2text
from datetime import datetime
from readability import Document

script_directory = os.path.dirname(os.path.abspath(__file__)) 
posts_directory = 'content/posts/'
maxitem_url = 'https://hacker-news.firebaseio.com/v0/maxitem.json'

class Story: 

    '''Create a story markdown, by first obtaining information from news.ycombinator using the item number 
    the json response contains the id, stroy title and the the story url. 
    Using that url we are able to get the story content and the this gets converted to markdown in order to be translated to Spanish.

    The markdown convertion helps to get the story in a format that can then be saved a posted almost immediately.''' 

    def __init__(self, url): 
        self.id = ''
        self.title = '' 
        self.content = None
        self.markdown = '' 
        self.story_url = '' 
    
    def story_content(self): 
        response = requests.get(self.story_url, timeout=20) 
        try: 
            if response.ok: 
                self.content = Document(response.content).summary() 
                self.story_markdown()
        except: 
            pass
    
    def story_markdown(self): 
        ''' Will return the story's text in markdown format ''' 
        print('Creating markdown ...') 
        html_to_markdown = html2text.HTML2Text() 
        html_to_markdown.ignore_links = False 
        self.markdown = html_to_markdown.handle(self.content) 
    

def new_items_url(items):
    base_url = "https://hacker-news.firebaseio.com/v0/item/"
    """ Generator of urls, each url will return a dictionary containing information about the story including the story's source url. """
    for item in items:
        yield ''.join([base_url, str(item), '.json'])

def check_url(url):
    """ Return the actual story url, the one that was submitted to HN. """
    try:
        response = requests.get(url, timeout=20)
        if response.ok and isinstance((response.json()), dict):
            if response.json()['type'] == 'story' and response.json()['url']:
                return response.json()
            else:
                return 'empty'
    except:
        pass  # This is intentional I don't want to keep track of failed urls

def create_post(story_id, story_title, story_url, story_markdown_content):
    today = datetime.today().strftime('%Y-%m-%d')
    file_name = ''.join(['post-', story_id, '.md'])
    new_post = os.path.join(posts_directory, file_name)
    post_header = ''.join(['---\ntitle: ', '\"', story_title, '\"', ' \ndate: ', str(today), ' \ndraft: false \n---\n\n'])
    post_content = ''.join([post_header, 'Story source:', '\n\n', story_url, '\n\n\n', story_markdown_content]) 

    with open(new_post, 'w') as file:
        file.write(post_content)

def get_latest_post_id(file):
    with open(file, 'r') as f:
        return int(f.read())

# save the new latest_post
def save_latest_post_id(post_id):
    with open('latest_post_id', 'w') as file:
        file.write(post_id)
        

if __name__ == "__main__":
    item_list = []
    post_count = 0
    stories_urls_list = []
    file = '/home/antonio/Repos/esaleatorio.com/python_scripts/latest_post_id'

    # Best stories url, in HN items are stories
    maxitem = requests.get(maxitem_url, timeout=20).json()
    latest_post_id = get_latest_post_id(file)
    new_items = maxitem - 200

    for i in range(new_items, maxitem):
        new_items += 1
        item_list.append(new_items)
    
    # If url are stories then 
    items_urls_list = new_items_url(item_list)

    post_count = 0
    for item in items_urls_list:
        response = check_url(item)
        if isinstance(response, dict):
            new_post = Story(item)
            new_post.id = str(response['id'])
            new_post.title = response['title']
            new_post.story_url = response['url']
            new_post.story_content()
            if post_count <=10 and new_post.content != None:
                print(post_count)
                create_post(new_post.id, new_post.title, new_post.story_url, new_post.markdown)
                post_count += 1
        else:
            pass

        if post_count > 10:
            save_latest_post_id(item)
            break
    

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
