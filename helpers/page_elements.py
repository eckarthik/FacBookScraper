from selenium.webdriver.common.by import By

elements = dict(
    login_username=(By.CSS_SELECTOR,"input[name='email']"),
    login_password=(By.CSS_SELECTOR,"input[name='pass']"),
    login_button=(By.CSS_SELECTOR,"button[name='login']"),
    write_something_group=(By.XPATH,"//div[text()='Write something...']"),
    posts=(By.CSS_SELECTOR,"article a[aria-label='Open story']"),
    full_post_container=(By.CSS_SELECTOR,".story_body_container"),
    post_content=(By.CSS_SELECTOR,".story_body_container > div"),
    posted_by=(By.CSS_SELECTOR,"strong a"),
    post_reactions_count=(By.CSS_SELECTOR,"div[id*='sentence']"),
    reactions_order=(By.CSS_SELECTOR,"div[id*='sentence'] span u")
)