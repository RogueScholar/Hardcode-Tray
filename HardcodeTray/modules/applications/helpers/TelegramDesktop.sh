#!/usr/bin/env bash

for i in {1..99}; do
  convert ~/.local/share/TelegramDesktop/tdata/ticons/icon_22_0.png -page -4-4 -background none -flatten \( +page -fill "#f23c34" -stroke "#f23c34" -draw "circle 14,14, 14,21" \) \( +stroke -font Hack-Regular -pointsize 9 -gravity center -draw "fill black text 4,5 '$i'" \) ~/.local/share/TelegramDesktop/tdata/ticons/icon_22_"$i".png
  convert ~/.local/share/TelegramDesktop/tdata/ticons/iconmute_22_0.png -page -4-4 -background none -flatten \( +page -fill "#ececec" -stroke gray -draw "circle 14,14, 14,21" \) \( +stroke -font Helvetica -pointsize 9 -gravity center -draw "fill black text 4,5 '$i'" \) ~/.local/share/TelegramDesktop/tdata/ticons/iconmute_22_"$i".png
done
