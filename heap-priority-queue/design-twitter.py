class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.users = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        heappush(self.tweets[userId], tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for user in self.tweets:
            for tweet in self.tweets[user]:
                feed.append(tweet)
        feed.sort(reverse=True)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followeeId].append(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.users[followeeId]:
            self.users[followeeId].remove(followerId)
            heappop(self.tweets[followeeId])


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)