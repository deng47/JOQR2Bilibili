#!/bin/bash

echo '{"font_size":0.4,"font_color":"#FFFFFF","background_alpha":0.5,"background_color":"#9C27B0","Stroke":"none","body":['

 tail -n +10 "$1" | while read -r line; do
    [ ! "$line" ] && continue
    line=$(echo "$line" | sed 's/<[^>]*>//g' | sed 's/align.*//g')
    time=$(echo "$line" | grep ' --> ' | sed 's/ --> /,/g')

    [ "$time" ] && [ "$output" ] && from=$(echo "$time" | cut -d',' -f1 |  awk -F: '{ print ($1 * 3600) + ($2 * 60) + $3 }') && to=$(echo "$time" | cut -d',' -f2 |  awk -F: '{ print ($1 * 3600) + ($2 * 60) + $3 }') && output="{\"from\":$from,\"to\":$to,\"location\":2,\"content\":\"$text\"}" && echo "$output" && text=''

    [ "$time" ] && output="Dialogue: 0,$time,Default,,0,0,0,,"

    [ ! "$time" ] && text="$text $line"
done

echo "]}"
