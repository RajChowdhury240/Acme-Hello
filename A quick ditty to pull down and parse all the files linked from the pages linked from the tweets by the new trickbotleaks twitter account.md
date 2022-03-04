```
twitter.user.profile --user trickbotleaks |
twitter.user.tweets --yield |
scrape --refs :text | -(refs)> inet:url | wget | -> file:bytes | fileparser.parse |
-(refs)> inet:url +:fqdn^=cdn | wget | -> file:bytes | fileparser.parse
```
