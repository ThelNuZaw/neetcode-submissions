class Twitter:

    def __init__(self):
        self.time = 0
        self.store_tweet = defaultdict(list)
        self.store_follow = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.store_tweet[userId].append([self.time, tweetId])
        self.time -= 1 # to make maxheap based on time(most recent store at the top)

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        self.store_follow[userId].add(userId)
        for followeeId in self.store_follow[userId]:
            if followeeId in self.store_tweet:
                index = len(self.store_tweet[followeeId]) - 1 
                time, tweetId = self.store_tweet[followeeId][index]
                heap.append([time, tweetId, followeeId, index - 1])
        heapq.heapify(heap)

        while heap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.store_tweet[followeeId][index]
                heapq.heappush(heap, [time, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.store_follow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.store_follow[followerId]:
            self.store_follow[followerId].remove(followeeId)
