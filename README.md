# chess
Chess

Install STOCKFISHCHESS https://stockfishchess.org/download/linux/

'
. install.sh
'

referencias

https://github.com/prashantdukecyfi/Chessboard-Detection
https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html
https://www.youtube.com/watch?v=XrCAvs9AePM

docker compose run opencv
cd app/

opencv_createsamples -info pos.dat -w 24 -h 24 -num 1000 -vec pos.vec

opencv_traincascade -data cascade/ -vec pos.vec -bg neg.txt -w 24 -h 24 -numPos 200 -numNeg 100

opencv_traincascade -data cascade/ -vec pos.vec -bg neg.txt -w 24 -h 24 -numPos 20 -numNeg 500 -numStages 10