import json
from kivymd.uix.screen import MDScreen

from components.online_friends import OnlineAvatarImage
from components.story_widget import StoryWidget
from components.posts import Post


class HomePage(MDScreen):
    profile_pic = "https://images.unsplash.com/photo-1586716402203-79219bede43c?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=334&q=80"

    def on_enter(self):
        self.list_online_friends()
        self.list_stories()
        self.list_posts()

    def list_online_friends(self):
        with open("assets/online_friends_data.json") as f:
            data = json.load(f)
            for friend in data:
                self.ids.online_friends.add_widget(OnlineAvatarImage(avatar =data[friend]['avatar']
                
                ))

    def list_stories(self):
        with open("")