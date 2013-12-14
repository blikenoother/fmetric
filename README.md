# fmetric

fmetric is a python script to fetch facebook users who interacts with facebook page.
This sciprt reads all public post including comment on post and like via graph api.
It will generate csv file which includs user id and score of interaction.

## Usage

First, download source code:

```html
git clone git@github.com:blikenoother/fmetric.git
```

Now, move to the direcotry

```html
cd fmetric
```

Now run the following command

```html
nohup python fetchdata.py ACCESS_TOKEN PAGE_ID POST_COUNT &
```

Description:

`ACCESS_TOKEN` valide facebook app access token (this is not app secret, its a token when a user
permits app)
`PAGE_ID` facebook page id (to get page id, http://graph.facebook.com/PAGE_NAME)
`POST_COUNT` number of posts to read

Example to read 50 post and get user id detail for facebook page:

```html
nohup python fetchdata.py XXXXXXXX 20531316728 50 &
```

It will generate a csv file with page id, like 20531316728.csv for above example

Copyright (c) 2013, Chirag (blikenoother -[at]- gmail [dot] com)