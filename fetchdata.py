#!/usr/bin/env python

import sys, helper, csv, time

apiUrl = 'https://graph.facebook.com/'
points = {'post': 3, 'commnet': 2, 'like': 1}

""" read command line argument:
1st argument, access_token
2nd argument, page_id
3rd argument, number of post_count to read
"""
argCount = len(sys.argv)
if argCount < 4:
    print 'pass all argument (access_token page_id, post_count)'
    sys.exit()

accessToken = sys.argv[1]

pageId = sys.argv[2]

try:
    postCount = int(sys.argv[3])
except:
    print 'Invalid postCount:',sys.argv[3]
    sys.exit()

# validate accessToken
url = apiUrl+'me'+'?access_token='+accessToken
content = helper.httpReq(url)
if not content.get('id'):
    print 'Invalid accessToken:',accessToken
    sys.exit()

# validate pageId
url = apiUrl+pageId
content = helper.httpReq(url)
if not content.get('id'):
    print 'Invalid pageId:',pageId
    sys.exit()

# read page feed
print '(%s) Page Feed Fetch [start]' %(time.strftime('%Y-%m-%d %H:%M:%S'))
url = apiUrl+pageId+'/feed?access_token='+accessToken
posts =  helper.readFeed(url, postCount)
print '(%s) Page Feed Fetch [done]' %(time.strftime('%Y-%m-%d %H:%M:%S'))

print '(%s) Post Comment and Like Fetch [start]' %(time.strftime('%Y-%m-%d %H:%M:%S'))
comments, likes = helper.getPostDetails(posts)
print '(%s) Post Comment and Like Fetch [done]' %(time.strftime('%Y-%m-%d %H:%M:%S'))

print '(%s) Set Score for User [start]' %(time.strftime('%Y-%m-%d %H:%M:%S'))
userData = {}
for post in posts:
    id = post.get('from').get('id')
    score = userData.get(id, 0) + points.get('post')
    userData[id] = score

for comment in comments:
    id = comment.get('from').get('id')
    score = userData.get(id, 0) + points.get('commnet')
    userData[id] = score

for like in likes:
    id = comment.get('id')
    score = userData.get(id, 0) + points.get('like')
    userData[id] = score
users = [{'id': k, 'score': v} for k, v in userData.items()]
print '(%s) Set Score for User [end]' %(time.strftime('%Y-%m-%d %H:%M:%S'))

print '(%s) Writing CSV file [start]' %(time.strftime('%Y-%m-%d %H:%M:%S'))
fieldnames = ['id', 'score']
fileName = pageId+'.csv'
dataFile = open(fileName,'wb')
csvwriter = csv.DictWriter(dataFile, delimiter=',', fieldnames=fieldnames)
csvwriter.writerow(dict((fn,fn) for fn in fieldnames))
for row in users:
     csvwriter.writerow(row)
dataFile.close()
print '(%s) Writing CSV file [end]' %(time.strftime('%Y-%m-%d %H:%M:%S'))