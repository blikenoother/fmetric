import urllib2, json

def httpReq(url):
    content = {}
    try:
        response = urllib2.urlopen(url)
        content = response.read()
        content = json.loads(content)
    except: pass
    
    return content

def readFeed(url, postCount, posts=[]):
    content = httpReq(url)
    if content.get('data'):
        for post in content.get('data'):
            posts.append(post)
            if len(posts) > (postCount-1): return posts

    if content.get('paging', {}).get('next'):
        url = content.get('paging').get('next')
        readFeed(url, postCount, posts)
    
    return posts

def getPostDetails(posts):
    comments = []
    likes = []
    for post in posts:
        # comments
        if post.get('comments', {}).get('data'):
            for comment in post.get('comments').get('data'):
                comments.append(comment)
        
        if post.get('comments', {}).get('paging', {}).get('next'):
            url = post.get('comments').get('paging').get('next')
            pagingData(url, comments)
        
        # likes
        if post.get('likes', {}).get('data'):
            for like in post.get('likes').get('data'):
                likes.append(like)
        
        if post.get('likes', {}).get('paging', {}).get('next'):
            url = post.get('likes').get('paging').get('next')
            pagingData(url, likes)

    return comments, likes

def pagingData(url, data=[]):
    content = httpReq(url)
    if content.get('data'):
        for c in content.get('data'):
            data.append(c)
    if content.get('paging', {}).get('next'):
        url = content.get('paging', {}).get('next')
        pagingData(url, data)
    return