from selenium import webdriver
from helpers.page_actions import FacebookActions
import os,time,json

class ScrapeFacebookGroup:
    """Get the posts from the facebook group"""

    def __init__(self):
        """Initialize the driver and other required stuffs"""

        self.geckodriver_path = os.path.dirname(os.path.abspath(__file__))+"/chromedriver.exe"
        print(self.geckodriver_path)
        self.driver = webdriver.Chrome(executable_path=self.geckodriver_path)
        # self.group_link = "https://m.facebook.com/groups/581328005804298/?ref=group_browse"
        self.group_link = os.environ['FB_GROUP_LINK']
        self.username = os.environ['FB_EMAIL']
        self.password = os.environ['FB_PASSWORD']
        self.actions = FacebookActions(self.driver)
        self.actions.login_to_facebook(username=self.username,password=self.password)
        self.links = set() #To store the links of all the posts obtained after scrolling to the end of the page
        self.posts = []
        self.scroll_count = 4 #How many times to scroll down?

    def navigate_to_group(self):
        """Navigate to the facebook group"""

        self.actions.navigate_to_group(group_link=self.group_link)

    def collect_posts_in_group(self):
        """Collect all the posts in the group"""

        while self.scroll_count:
            posts = self.actions.get_posts()
            for post in posts:
                post_url = post.get_attribute("href")
                self.links.add(post_url)
            self.actions.scroll_to_end()
            time.sleep(10) #For the scroll to complete
            self.scroll_count = self.scroll_count - 1

        print("Collected - ",len(self.links)," post links. Starting to collect the post contents")

        for link in self.links:
            self.actions.open_post(link)
            post = {}
            post['content'] = self.actions.get_post_content()
            post['post_owner'] = self.actions.get_post_owner_name()
            post['reactions_count'] = self.actions.get_post_reactions_count()
            post['reactions_order'] = self.actions.get_post_reactions_order()
            self.posts.append(post)


scraper = ScrapeFacebookGroup()
time.sleep(10)
scraper.navigate_to_group()
scraper.collect_posts_in_group()
print("Collected - ",len(scraper.posts)," posts")
print("\n Collected Posts \n")
print(json.dumps(scraper.posts,sort_keys=True,indent=4))