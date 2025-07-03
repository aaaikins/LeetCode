class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        # Add user's own tweets
        for tweet in self.tweets[userId]:
            heapq.heappush(heap, tweet)
            if len(heap) > 10:
                heapq.heappop(heap)

        # Add tweets from followees
        for followee in self.following[userId]:
            for tweet in self.tweets[followee]:
                heapq.heappush(heap, tweet)
                if len(heap) > 10:
                    heapq.heappop(heap)

        # Return tweets sorted by most recent
        return [tweetId for (_, tweetId) in sorted(heap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
        print("follow")
        print(self.following)
        print(self.tweets)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        print("unfollow")
        print(self.following)
        print(self.tweets)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)