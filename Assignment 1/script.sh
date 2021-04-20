#!/bin/bash
 
echo "----Question 2--------"
echo 'tac' | bash q2.sh 
echo 'hy' | bash q2.sh 
echo 'ger' | bash q2.sh 
echo 'kmdir' | bash q2.sh 
echo 'sl' | bash q2.sh 
echo 'coeh' | bash q2.sh 
echo 'qqqqq' | bash q2.sh 
 
echo "----Question 3--------"
bash q3.sh
 
echo "----Question 4--------"
echo '(1 (2) ((3)) (5) (((7 8 9)) ())' | bash q4.sh
echo '((1 2)(3 (4)))' | bash q4.sh
echo '((1 1.2)()(3.5 4))' | bash q4.sh
echo '(1 (2.1 3.2 (4.2)))' | bash q4.sh
echo '(1 2 3 4 5)' | bash q4.sh
 
echo "----Question 5--------"
echo 'Madam' | bash q5.sh
echo 'madam' | bash q5.sh
echo 'aaaaa' | bash q5.sh
echo 'aadaa' | bash q5.sh
echo 'aaddd' | bash q5.sh
echo 'cat' | bash q5.sh
 
echo "----Question 6--------"
bash q6.sh 2 3 4 
bash q6.sh 2 3 4 5 
bash q6.sh 2 4 5
bash q6.sh 5 3 2 3
bash q6.sh 3 3 3 3
 
echo "----Question 7--------"
echo 4 | bash q7.sh
 
echo "----Question 8--------"
echo "11 * 11 11 * mkdir test" > crontab_file
bash q8.sh crontab_file
echo "* * mkdir test" > crontab_file
bash q8.sh crontab_file
echo "30 08 10 cat * *" | bash q8.sh
 
echo "----Question 9--------"
echo '4539 3195 0343 6467'| bash q9.sh
echo '8273 1232 7352 0569'| bash q9.sh
echo '1234 1234 1234 1234'| bash q9.sh
echo '79927391783'| bash q9.sh
echo '874328923'| bash q9.sh
 
echo "----Question 10--------"
echo '+ 
5 
2 
20 
35 
7 
12' | bash q10.sh
echo "/
3
1
3
3" | bash q10.sh
echo "*
4
2
3
4
5" | bash q10.sh 
echo "*
2
40
40" | bash q10.sh 
echo "-
4
1
2
3
4" | bash q10.sh
