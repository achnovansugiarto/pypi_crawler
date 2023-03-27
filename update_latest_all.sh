cat data/package_names.txt| grep ^$1 >> $1.txt
input="$1.txt"
while IFS= read -r line
do
  echo "=============\t\t\t $line \t\t\t================"
  python update_latest_json.py $line
  echo "===================================="
done < "$input"
rm $1.txt