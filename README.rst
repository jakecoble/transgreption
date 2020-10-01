See the original spec at http://doc.bmndr.com/transgreption

## To-do list

1. I'm not sure if this is even a problem but it seemed to break things when the metadoc contained a link to its own megadoc. I (dreev) stuck in what I've called an anti-inception hack in url_transforms.py to just make any links to transgreption itself just intentionally break. It would be nice to handle that better somehow!

2. maybe a special case for accidentally linking to private google docs or dropbox docs? currently it just shows the login screens for google docs / dropbox. would be better to see a red error, like you do if you accidentally link to a private github repo.

3. and then pie in the sky that probably isn't worth it but, like, if it loaded the skeleton of the page instantly and then showed spinners for each document until they were ready, that'd be kind of amazing...