for VARIABLE in 0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p
do
    git pull
    git checkout main
    git merge update_latest/$VARIABLE
done