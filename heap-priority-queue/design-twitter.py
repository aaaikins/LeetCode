class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.users = defaultdict(list)
        # self.feed = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append(tweetId)
        # self.feed.append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for user in self.users[userId]:
            for tweet in self.tweets[user]:
                res.append(tweet)
        res.extend(self.tweets[userId])
        # self.feed.reverse()
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # self.users[followeeId].append(followerId)
        self.users[followerId].append(followeeId)
        print("follow")
        print(self.users)
        print(self.tweets)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        # if self.users[followeeId]:
        #     self.feed.remove(self.tweets[followeeId])
        #     self.users[followeeId].remove(followerId)
        #     heappop(self.tweets[followeeId])
        # self.users[followeeId].remove(followerId)
        self.users[followerId].remove(followeeId)
        print("unfollow")
        print(self.users)
        print(self.tweets)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)