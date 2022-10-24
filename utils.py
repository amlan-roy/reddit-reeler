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

tempPost = Post(
    username='AskReddit',
    title='Android fans, what are the primary reasons why you will never ever switch to an Iphone?',
    postText="",
    subreddit='SultanofAmerica',
    upvotes='46.7k',
    commentsCount='28.9k'
    )

tempComments = [
    BodyText(
        username='BotJovi35',
        text="1. Android has direct access to your phone's file explorer \n\n2. Third party apps not on the app store\n\n3. I like the UI better",
        upvotes='2.3k'),
    BodyText(
        username='enty6003',
        text="If I'm paying for an expensive device, I'm going to be the admin",
        upvotes='6.9k'),
    BodyText(
        username='thenewbae',
        text="A friend once said \"apple treats its phone owners like users, android treats them like admins\" . That's the most succinct version of it. I like being in control. I want to do all the little settings myself and it be easy doing it and plugging to computer being easy and all of it.",
        upvotes='137'),
]