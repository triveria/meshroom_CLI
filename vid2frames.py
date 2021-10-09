import cv2 as cv
import os
import sys
import argparse

def check_save_dir(spath):
    if not os.path.exists(spath):
        os.makedirs(spath)
    if len(os.listdir(spath)) > 0:
        choice = input("Detected non-empty directory. Continue? (Y/n)")
        if str(choice).lower() != 'y':
            print('Terminating...')
            sys.exit(0)

def read_imgs(vpath, spath, rescale, w, h, skip):
    cap = cv.VideoCapture(vpath)

    height, width = cap.get(3), cap.get(4)
    rh = height*rescale if h is None else h
    rw = width *rescale if w is None else w
    new_shape     = tuple(map(int, (rh, rw)))

    fid = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if fid%(skip+1)==0:  
            img = cv.resize(frame, new_shape)
            ipath = os.path.join(spath, f'{fid}.jpg')
            cv.imwrite(ipath, img)
        fid += 1
    cv.destroyAllWindows()
    print('Done...')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('vpath')      ## video path
    parser.add_argument('spath')      ## save  path
    parser.add_argument('-r', '--rescale', type=float, default=1., help='Factor to rescale the frames')
    parser.add_argument('-s', '--skip'   , type=int,   default=0,  help='Interval between two fetched frames')
    parser.add_argument('--width'  , type=int, help='Reset width of the frames, will overwrite the rescaled width')
    parser.add_argument('--height' , type=int, help='Reset height of the frames, will overwrite the rescaled height')
    args = parser.parse_args()

    check_save_dir(args.spath)
    read_imgs(args.vpath, args.spath, args.rescale, args.width, args.height, args.skip)