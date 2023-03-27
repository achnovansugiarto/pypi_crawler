# cat data/package_names.txt| grep ^a >> a.txt
# input='a.txt'
input="data/package_names.txt"
while IFS= read -r line
do
  echo "=============\t\t\t $line \t\t\t================"
  python update_latest_json.py $line
  echo "===================================="
done < "$input"