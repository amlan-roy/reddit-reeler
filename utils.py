class Post:
    def __init__(self, username, title, postText, subreddit,upvotes,commentsCount):
        self.username = username
        self.title = title
        self.postText = postText
        self.subreddit = subreddit
        self.upvotes = upvotes
        self.commentsCount = commentsCount

class BodyText:
    def __init__(self, username, text, upvotes) -> None:
        super().__init__()
        self.text = text
        self.username = username
        self.upvotes = upvotes

tempPost = Post(username='taklabhalu',title='A friend has told me that they want to kill someone.',postText="Im 16, and recently a friend has told me that they're planning to murder one of our classmates, a girl. At first I thought they were joking, but they've talked about it more than once and I'm sure they are serious about it. This friend was in love with said girl, but got rejected and never really moved on. I don't know what to do.  \n\n\n**Update**: I called the girl (where I live it's very late, so meeting in person wasn't an option) and told her everything. It took some convincing, but she finally said she trusted my word and would tell her parents. We plan to talk to the school and the police tomorrow. ",
subreddit='offmychest',upvotes='3.2k',commentsCount=222)
