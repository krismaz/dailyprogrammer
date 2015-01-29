#!/bin/bash
#Hooooo balls

cat $1 | convert -pointsize 36 -kerning -7 -font courier text:-  -trim +repage \
              -bordercolor white -border 10x10 -blur 0x3 -threshold 90% text.jpg

curl -F userfile=@text.jpg \
     -F outputencoding="utf-8" \
     -F outputformat="txt" \
     -F eclass="page" \
     http://michelle.ocrgrid.org/cgi-bin/weocr/submit_e2.cgi > result

cat result | sed  's/1/7/g' | sed 's/[OD]/0/g' | sed 's/[lIJj]/1/g' | sed 's/_/4/g' | sed 's/[Ss]/5/g' | sed 's/g/8/g' | sed 's/ //g'