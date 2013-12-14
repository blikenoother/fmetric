# fmetric

fmetric is a python script to fetch facebook users and interaction score with facebook page.
This sciprt reads all recent public post including comment on post and like using facebook graph api.
It will generate csv file which includs user id and score of interaction.

## Usage

First, download source code:
```html
git clone git@github.com:blikenoother/fmetric.git
```

Now, move to the direcotry, run the following command
```html
cd fmetric
nohup python fetchdata.py ACCESS_TOKEN PAGE_ID POST_COUNT &
```

### Description:

`ACCESS_TOKEN` valide facebook app access token (you can get access token at [developers.facebook.com](https://developers.facebook.com/tools/explorer))  
`PAGE_ID` facebook page id (to get page id, http://graph.facebook.com/PAGE_NAME)  
`POST_COUNT` number of posts to read  
`&` to run python script in background

Example to read 50 post and get engaged user id for http://facebook.com/facebook page:

```html
nohup python fetchdata.py XXXXXXXX 20531316728 50 &
```

It will generate a csv file with page id, like 20531316728.csv for above example

### Score detail:

1 point for like on post
2 point for writing comment on post
3 point for writing post

You can edit points allocation at line number 4 (`points = {'post': 3, 'commnet': 2, 'like': 1}`) in fetchdata.py

### Logs:

You can check logs or any error in nohup.out which will be generated when you execute the script.

Copyright (c) 2013, Chirag (blikenoother -[at]- gmail [dot] com)