
def splitter(name):

    num = int(0)
    while(1):

        num1 = '{:06d}'.format(num)
        path = name
        path += "/frames/frame_"
        path += num1
        path += ".txt"

        try:
            with open(path) as f:

                lines = f.readlines()
                num += 1

                newpath1 = "/"
                newpath1 = str(name)
                newpath1 += "/detection/"
                newpath1 += num1 + ".txt"

                newpath2 = "/"
                newpath2 = str(name)
                newpath2 += "/classification/"
                newpath2 += num1 + ".txt"

                fd = open(newpath1, "w+")  # for detection
                fc = open(newpath2, "w+")  # for classification

                if len(lines) == 1:
                    vals = lines[0].split(' ')

                    if vals[0] != '0':     # need to be written in both classification and detection
                        for x in vals:
                            fc.write(x+" ")

                        vals[0] = '0'   # for detection
                        for x in vals:
                            fd.write(x+" ")

                    else:               # only write in detection
                        for x in vals:
                            fd.write(x+" ")
        except:
            break

        num += 1


if __name__ == "__main__":

    video_id = str(71023710613)
    splitter(video_id)



