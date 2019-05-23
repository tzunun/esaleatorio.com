# Es Aleatorio (esaleatorio.com)
esaleatorio.com is a website build using primarilly AWS technologies.  At its proper implementation.  It obtains news from the site news.ycombinator.com (Hacker News) removes all the clutter from them and using AWS Machine Learning translate the text to Spanish.  Renders mostly text and builds a website that still has the important information from the submitted news.  A link is also provided to the original url of the story in case the script doesn't parse the text correctly.

The result is a text mostly site that renders fast and efficiently regardeless of the device being used to view it. 

The site esaleatorio.com and the subdomain forum.esaleatorio.com are live.

## List of AWS used in this site
**Route53**: DNS and domain registration.  Hosted zone used to properly point domain and subdomains.

**CloudFront**:  CDN to cache the site closer to the intended audience (Latin America mostly)

**Certificate Manager**:  To obtain an SSl certificate, for the site and possibly subdomains.

**S3**:  Storage bucket to host the static site

**Lightsail**:  VPS running Ubuntu 18.04LTS.  A docker image runs discourse in order to provide the ability to comment the stories.  Discourse is available in the subdomain forum.esaleatorio.com

**CodeCommit**:  Git repository (set up ssh-key authentication, somehow ed25519 keys are not supported)

**CodeBuild**:  Build the website, upload the pages to the S3 bucket, and make the CloudFront dispose of the old files.

**IAM**: To manage roles an permissions in the whole process.

## Still in the future
**Lightsail**: Second VPS to keep the site updated by running a script to gather the new stories and push them to CodeCommit.  It could possibly contain a PostgreSQL database to store the text from the stories and the translations to Spanish in order to collect data for phase 2 of this project which is NLP to test certain conjecture I have on how to improve Machine Learning assisted language translation (English - Spanish)

**AWS Machine Learning**:  To translate the stories from English to Spanish.

**CodeDeploy**:  To automate the deploy process.

## Other software
**Hugo**: To generate the static site.

Theme: Terminal

**Discourse**: To enable comments on the stories.

# Installation
I used the default Anaconda distribution of Python3. These instructions work as they are in Ubuntu and most other Linux distributions. Windows users would have to select the Anaconda command option from the Windows menu, otherwise it is unlikely to work properly from the command prompt or PowerShell.

The following libraries are needed and in order to install them make sure the appropriate python environment is active and run the following commands:
```shell
pip install html2text
pip install readability-lxml
```