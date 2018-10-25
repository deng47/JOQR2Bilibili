#!/bin/bash

echo '{"font_size":0.4,"font_color":"#FFFFFF","background_alpha":0.5,"background_color":"#9C27B0","Stroke":"none","body":['

 tail -n +10 "$1" | while read -r line; do

    [ ! "$line" ] && continue
    line=$(echo "$line" | sed 's/<[^>]*>//g' | sed 's/align.*//g')
    time=$(echo "$line" | grep ' --> ' | sed 's/ --> /,/g')

    [ "$time" ] && [ ! "$pretime" ] && pretime="$time" && continue
<<<<<<< HEAD
=======

    [ "$time" ] && [ "$output" ] && from=$(echo "$pretime" | cut -d',' -f1 |  awk -F: '{ print ($1 * 3600) + ($2 * 60) + $3 }') && to=$(echo "$pretime" | cut -d',' -f2 |  awk -F: '{ print ($1 * 3600) + ($2 * 60) + $3 }') && output="{\"from\":$from,\"to\":$to,\"location\":2,\"content\":\"$text\"}" && echo "$output" && pretime='' && text=''
>>>>>>> 9e0f71f01c0cc878a2c67156e5188e0feff30677

    [ "$time" ] && [ "$output" ] && from=$(echo "$pretime" | cut -d',' -f1 |  awk -F: '{ print ($1 * 3600) + ($2 * 60) + $3 }') && to=$(echo "$pretime" | cut -d',' -f2 |  awk -F: '{ print ($1 * 3600) + ($2 * 60) + $3 }')  && output="{\"from\":$from,\"to\":$to,\"location\":2,\"content\":\"$text\"}" && echo "$output" && text='' && pretime="$time"

    [ "$time" ] && output="Yes"
    [ ! "$time" ] && text="$text $line"
done

echo "]}"
