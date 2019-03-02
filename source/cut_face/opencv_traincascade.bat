md xml
opencv_traincascade.exe -data xml -vec pos.vec -bg bg.txt -numPos 2000 -numNeg 7000 -numStages 13 -featureType LBP -mode ALL -w 24 -h 24
pause