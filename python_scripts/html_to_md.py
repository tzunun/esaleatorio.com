import requests
import html2text

# URL of the story that will be translated.
url = ''
# html2text initial settings to convert html to md
html = html2text.HTML2Text()
html.ignore_links = False

# Get the site data
response = requests.get(url)

# Extract the text from the response
html_text = response.text

# Convert the html to markdownconverted 
markdown_text = html.handle(html_text)

# The makrdown text can then be sent to be translated as it does not contain
# enough cruff from the original website, most extra characters have been
# eliminated and the md  format suits better the way a blog expects a new
# post, this in turn keeps everything looking like a website.
# Still to do is the iframe for the comments 
# Data storage of both the original url, html text and markdown_text

