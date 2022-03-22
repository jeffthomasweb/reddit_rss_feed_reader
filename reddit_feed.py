import feedparser
from bs4 import BeautifulSoup
import lxml

#Reddit forums (subreddits) have RSS feeds tied to each one. To get the RSS feed address for a 
#subreddit, just add .rss to the end of the subreddit's website address. So for example the RSS 
#for the Rust subreddit would be (use with quotes) "https://reddit.com/r/rust.rss"
#Function reddit_rss() get the RSS feed post titles and summaries.


#Enter subreddit RSS website address in quotes for the function on line 51.
def reddit_rss(rss_address):
    a = feedparser.parse(rss_address)
    #I tried using a for loop to make this cleaner but I was receiving typing errors when doing this.
    #The \ character at the end of each line allows us to go to the next line without terminal 
    #errors. If we didn't use the \ character the code would be all on one line and harder to read.  
    #This is all one string object.
    summary_list = a.entries[0].title + '. ' + a.entries[0].summary + a.entries[0].link +  '.\n' + '\n' \
    + a.entries[1].title + '. ' + a.entries[1].summary + a.entries[1].link + ' .\n' + '\n' \
    + a.entries[2].title + '. ' + a.entries[2].summary + a.entries[2].link + ' .\n' + '\n' \
    + a.entries[3].title + '. ' + a.entries[3].summary + a.entries[3].link + ' .\n' + '\n' \
    + a.entries[4].title + '. ' + a.entries[4].summary + a.entries[4].link + ' .\n' + '\n' \
    + a.entries[5].title + '. ' + a.entries[5].summary + a.entries[5].link + ' .\n' + '\n' \
    + a.entries[6].title + '. ' + a.entries[6].summary + a.entries[6].link + ' .\n' + '\n' \
    + a.entries[7].title + '. ' + a.entries[7].summary + a.entries[7].link + ' .\n' + '\n' \
    + a.entries[8].title + '. ' + a.entries[8].summary + a.entries[8].link + ' .\n' + '\n' \
    + a.entries[9].title + '. ' + a.entries[9].summary + a.entries[9].link + ' .\n' + '\n' \
    + a.entries[10].title + '. ' + a.entries[10].summary + a.entries[10].link + ' .\n' + '\n' \
    + a.entries[11].title + '. ' + a.entries[11].summary + a.entries[11].link + ' .\n' + '\n' \
    + a.entries[12].title + '. ' + a.entries[12].summary + a.entries[12].link + ' .\n' + '\n' \
    + a.entries[13].title + '. ' + a.entries[13].summary + a.entries[13].link + ' .\n' + '\n' \
    + a.entries[14].title + '. ' + a.entries[14].summary + a.entries[14].link + ' .\n' + '\n' \
    + a.entries[15].title + '. ' + a.entries[15].summary + a.entries[15].link + ' .\n' + '\n' \
    + a.entries[16].title + '. ' + a.entries[16].summary + a.entries[16].link + ' .\n' + '\n' \
    + a.entries[17].title + '. ' + a.entries[17].summary + a.entries[17].link + ' .\n' + '\n' \
    + a.entries[18].title + '. ' + a.entries[18].summary + a.entries[18].link + ' .\n' + '\n' \
    + a.entries[19].title + '. ' + a.entries[19].summary + a.entries[19].link + ' .\n' + '\n' \
    + a.entries[20].title + '. ' + a.entries[20].summary + a.entries[20].link + ' .\n' + '\n' \
    + a.entries[21].title + '. ' + a.entries[21].summary + a.entries[21].link + ' .\n' + '\n' \
    + a.entries[22].title + '. ' + a.entries[22].summary + a.entries[22].link + ' .\n' + '\n' \
    + a.entries[23].title + '. ' + a.entries[23].summary + a.entries[23].link + ' .\n' + '\n' \
    + a.entries[24].title + '. ' + a.entries[24].summary + a.entries[24].link + ' .\n' + '\n'
   
    #The RSS Feed data has some HTML tags in the summary section. Use BeautifulSoup to remove 
    #the HTML.
    soup = BeautifulSoup(summary_list, "lxml")
    print(soup.text)

    return soup.text

reddit_rss("https://reddit.com/r/python.rss")

#Different programming subredit addresses below. Copy and paste into function parameter of reddit_rss() .
#"https://reddit.com/r/rust.rss"
#"https://reddit.com/r/programming.rss"
#"https://reddit.com/r/java.rss"
#"https://reddit.com/r/django.rss"
#"https://reddit.com/r/python.rss"
#"https://reddit.com/r/flask.rss"
