# Xadrez Automatizado

# chess
Chess

O intuito do projeto é usar uma IA para reconhecer os movimentos de peças do Xadrez, e calcular através do stockfishchess, a melhor jogada possível, e então realizar a jogada, através de LEDs que sinalizam para onde as peças são movidas.

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

base64 negativas/1701128875.2898896.jpg | curl -d @- "https://detect.roboflow.com/chess-4jvm8/1?api_key=Yc9P3iOmEuSts3mFZLd3"
