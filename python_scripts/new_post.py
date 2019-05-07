import os

folder = os.path.dirname(os.path.abspath(__file__)) 
posts_location= '../noticia/content/posts/'
file_name = 'test2.md'

new_post = os.path.join(folder, posts_location, file_name)

post_header = """--- \ntitle: "Write Test post with Python" \ndate: 2019-04-18T15:16:29-05:00 \ndraft: false \n---""" 

text = """\nThis is a lot of text, and there has to be another lot in the sence that the essence is missing""" 

with open(new_post, 'w') as file:
    file.write(''.join([post_header, text]))