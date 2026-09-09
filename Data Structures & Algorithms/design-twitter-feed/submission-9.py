class Twitter:

    def __init__(self):

        # a global time counter
        self.time = 0
        self.twitter = {}
        # map between followers and followees
        self.follower_map = {}

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId in self.twitter:
            self.twitter[userId].append((-self.time, tweetId))
        else:
            self.twitter[userId] = [(-self.time, tweetId)]
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        news_feed = []
        cntr = 10

        if userId in self.twitter:
            for elem in self.twitter[userId]:
                heapq.heappush(heap, elem)

        if userId in self.follower_map:
            for u in self.follower_map[userId]:
                for elem in self.twitter[u]:
                    heapq.heappush(heap, elem)

        while (cntr != 0):
            if len(heap) > 0:
                time, elem = heapq.heappop(heap)
                news_feed.append(elem)
            else:
                break

            cntr-=1

        return news_feed[:10]

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId in self.follower_map:
            self.follower_map[followerId].add(followeeId)
        else:
            self.follower_map[followerId] = set()
            self.follower_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower_map[followerId]:
            self.follower_map[followerId].remove(followeeId)

        
