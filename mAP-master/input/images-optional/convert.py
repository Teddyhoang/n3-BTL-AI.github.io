from glob import glob
import cv2
import numpy as np
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--path_input', required=True,
                help='path to input image')
ap.add_argument('-i', '--path_output', required=True,
                help='path to input image')               
args = ap.parse_args()

def check(path_txt):
        name = path_txt.split(".")[0]
        if os.path.isfile(name + '.jpg'):
                return True
        return False

for path_txt in glob.glob(args.path_input + "/*.txt"):
        no=[0,0,0,0,0]
        #print(path_txt)
        if check(path_txt):
                image = cv2.imread(path_txt.split(".")[0] + ".jpg")
                h,w = image.shape[:2]
                output=""
                with open(path_txt, "r") as stream:
                        for line in stream.readlines():
                                line = line.strip()
                                coord = line.split(" ")
                                a = coord[0]
                                num = int(line.split(' ',1)[0])
                                no[num]+=1
                                coord = [float(i) for i in coord[1:]]
                                box = np.array(coord) * np.array([w,h,w,h])
                                (centerX, centerY, width, height) = box.astype('int')
                                left = centerX - int(width/2)
                                top = centerY - int(height/2)
                                right = centerX + int(width/2)
                                bottom = centerY + int(height/2)
                                out1 = "{} {} {} {} {}\n".format(a, left, top, right, bottom)
                                output +=out1
                name_output = path_txt.split('/')[-1]
                print(name_output)
                with open(args.path_output + '/' + name_output, 'w') as stream_out:
                        stream_out.write(output)
                stream.close()
                stream_out.close()