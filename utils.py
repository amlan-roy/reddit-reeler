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
    username='taklabhalu',
    title='A friend has told me that they want to kill someone.',
    postText="Im 16, and recently a friend has told me that they're planning to murder one of our classmates, a girl. At first I thought they were joking, but they've talked about it more than once and I'm sure they are serious about it. This friend was in love with said girl, but got rejected and never really moved on. I don't know what to do.  \n\n\n**Update**: I called the girl (where I live it's very late, so meeting in person wasn't an option) and told her everything. It took some convincing, but she finally said she trusted my word and would tell her parents. We plan to talk to the school and the police tomorrow. ",
    subreddit='offmychest',
    upvotes='3.2k',
    commentsCount=222
    )

tempComments = [
    BodyText(
        username='taklabhalu_1',
        text="Im 16, and recently a friend has told me that they're planning to murder one of our classmates, a girl. At first I thought they were joking, but they've talked about it more than once and I'm sure they are serious about it. This friend was in love with said girl, but got rejected and never really moved on. I don't know what to do.  \n\n\n**Update**: I called the girl (where I live it's very late, so meeting in person wasn't an option) and told her everything. It took some convincing, but she finally said she trusted my word and would tell her parents. We plan to talk to the school and the police tomorrow. ",
        upvotes='111'),
    BodyText(
        username='taklabhalu_2',
        text="Native Russian here.\n\nFrom the circle of my (fairly young) friends and acquaintances, no one is this much delusional to hold him in high regard. Majority of his supporters are post-USSR or/and as old as he is. People who support him are people who watch the TV and biased news sources because they cannot possibly doubt their leader.  As I've said in a different thread, a brainwashed group of people who only can worship a political figure would grow up to worship a political figure.\n\nHe's most likely the guy who's behind all of this, not many can achieve his level of usurping leadership and maintain it with smart shutting down of the opposition. It'll take years for someone to achieve this level again, especially later down the line when the USSR survivors naturally die of old age. Younger people are wiser and weren't as conditioned despite the grip he has on the media outlets. Internet and easy communication makes it hard to shut down all sources of information.\n\nRight now only an idiot wouldn't recognize that this invasion is an absolutely insane decision. We're suffering from it, we, the poor and the middle class, who wants the same as people of Ukraine - we just want peace and to mind our own business. Economics is gonna go to shit, and only we suffer from it. Certain services refuse us or plan to refuse us and choose to actively hurt us because they think it'll potentially make him backpedal. It won't. He never cared about the people. Anyone sane is capable of comprehending that. The only thing he did is terrorize his own people so we won't be able to speak out against him, and it lead to some people straight up hating *all* Russians as if we agree with the decisions. We do not. We do not want war.\n\nI wish I could move out, but I cannot. I'm just a poor student trapped in a horrible situation. I always hated this country and I'm ashamed to live here. So are many of my acquaintances. We're powerless.",
        upvotes='111'),
]