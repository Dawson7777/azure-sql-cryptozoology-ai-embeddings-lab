for file in Screenshot\ *at*.png; do
  newname=$(echo "$file" | sed -E 's/Screenshot[[:space:]]+([0-9]{4}-[0-9]{2}-[0-9]{2})[[:space:]]+at[[:space:]]+([0-9]{1,2}\.[0-9]{2}\.[0-9]{2})[[:space:]]*([AP]M)\.png/Screenshot\1at\2\3.png/')
  if [ "$file" != "$newname" ]; then
    echo "Renaming: $file -> $newname"
    mv "$file" "$newname"
  fi
done
