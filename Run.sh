# $1 project name
if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
  else
    echo "Executing Project: $1"
    python vid2frames.py "/home/amos/workspace/DB/reconstruct/$1.mp4" "/home/amos/Programs/Meshroom-2021.1.0/caches/$1/0_Images" -s 3 -r 0.5
    python Meshroom_CLI-linux.py "/home/amos/Programs/Meshroom-2021.1.0/aliceVision/bin" "/home/amos/Programs/Meshroom-2021.1.0/caches/$1" "/home/amos/Programs/Meshroom-2021.1.0/caches/$1/0_Images"
fi

