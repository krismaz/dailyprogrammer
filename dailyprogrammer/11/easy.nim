#Nim 10.2
import os, times, strutils

#Note that we need to convert the timeinfo to a time object, and snap it back into the local calendar in order to recompute the weekday. I suspect there may be a smarter way to do this, but the time parsing code of the nim stdlib also does this
echo TimeInfo(year: 3.paramStr.parseInt, month: Month(2.paramStr.parseInt-1), monthday: 1.paramStr.parseInt).timeInfoToTime.getLocalTime.weekday