```
for $item in $rows {
    
    /* handle users w/o @@q3mcco35auwcstmt.onion */
    if ($item.to.find("@") = $lib.null) {
        $item.to = $lib.str.concat($item.to, "@q3mcco35auwcstmt.onion")
    }
    if ($item.from.find("@") = $lib.null) {
        $item.from = $lib.str.concat($item.from, "@q3mcco35auwcstmt.onion")
    }
    ($touser, $tosite) = $item.to.split("@", 1)
    ($fruser, $frsite) = $item.from.split("@", 1)

    $toacct = ($tosite, $touser)
    $fracct = ($frsite, $fruser)

    [ inet:web:mesg=($fracct, $toacct, $item.ts) :text=$item.body ]
    [ +#vtx.story.contileaks ]
    {
        -> inet:web:acct [ .seen=$item.ts +#vtx.story.contileaks ]
        -> inet:user  [ .seen=$item.ts +#vtx.story.contileaks ]
    }
}
| scrape --refs :text |
{ -(refs)> * [ .seen=$item.ts +#vtx.story.contileaks ] }
```
