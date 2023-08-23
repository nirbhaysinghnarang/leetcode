class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        self.ansArr = []
        self.hs = set()

        def getHostName(s):
            s = s.replace("http://", "")
            s = s.split('/')[0]
            return s
        
        def helper(url):
            self.hs.add(url)
            self.ansArr.append(url)
            hostName = getHostName(url)
            urls = htmlParser.getUrls(url)
            for nxt in urls:
                if nxt in self.hs: continue
                nxtHostName = getHostName(nxt)
                if hostName == nxtHostName:
                    helper(nxt)

        helper(startUrl)
        return self.ansArr