# EmailScraper
A scrapy script to spider a website and scrape all emails using a regex. EmailScraper outputs the email and the url it was found in JSON format. The output is generated as the website is spidered and does not contain duplicates. 
# Requirements
Scrapy
```
pip install scrapy
```
# Usage
Scrape all emails from example.com and save the output to emails.json, and only print status of spider (not every GET request). 
```
scrapy runspider EmailScraper.py -a url=http://example.com/ -o emails.json -L INFO
```

# License 
MIT License
