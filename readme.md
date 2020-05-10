# Facebook Group Scraper

A Python Selenium based script to gather all the posts in a particular group

# Features!
Gathers the following content:
1. Post content
2. Posted by whom?
3. Reactions count
4. Reactions List (Sorted in the order of reactions count... Highest to lowest)

### Prerequisites

The following are required for this script to run.

* [Python](https://www.python.org/downloads/release/python-370/) - Preferably Python 3.5 or above
* [Python Selenium](https://pypi.org/project/selenium/) - Python Selenium

### How to run?
This script reads the credentials and the group link from the environment variables. Set your Facebook credentials and Facebook group links as the following environment variables.

```sh
export FB_EMAIL=myfacebookemail@email.com
export FB_PASSWORD=myFaceB00KPassword
export FB_GROUP_LINK=https://m.facebook.com/group/1234567890
```
Start running the scrape.py after you have set the above environment variables.
```sh
$ python scrape.py
```

### Sample Output
```json
    [
    {
        "content": "#need suggestions guys\n1 week se stl pd rha rha thora thora krke nd ab meri college ki holidays ho gyi hai toh hackerrank ke 4-7 question ho jte hai mujhse daily but then free rhet hu toh mai
ky ds algo bhi shuru krdu pdhan?\nSee translation",
        "post_owner": "Flash Joe",
        "reactions_count": "1",
        "reactions_order": [
            "Like"
        ]
    },
    {
        "content": "Hi, please suggest me best youtube channel to learn react js.",
        "post_owner": "John Doe",
        "reactions_count": "5",
        "reactions_order": [
            "Like",
            "Haha"
        ]
    },
    {
        "content": "how to run c programme in vs ..noob here",
        "post_owner": "Adam Joe",
        "reactions_count": "12",
        "reactions_order": [
        "Love",
        "Haha"
        ]
    },
    {
        "content": "How to make coding interesting i know there is no shortcut, we need to work hard but i am losing my motivation again any help?",
        "post_owner": "Man Williams",
        "reactions_count": "",
        "reactions_order": []
    }
    ]
```

### Todos

 - Gather comments and photos posted


