import os

def main():
    path = "CyberSecurity-Notes"

    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

    for week in range(1,25):
        for day in range(1,4):
            path2 = "Week"
            path3 = "Day"
            try:
                os.makedirs(os.path.join('CyberSecurity-Notes', path2 + str(week), path3 + str(day)))
            except OSError:
                print ("Creation of the directory %s failed" % path)
            else:
                print ("Successfully created the directory %s " % path)

        


main()


