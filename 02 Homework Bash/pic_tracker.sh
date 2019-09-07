#Create three folders called: JPG, PNG, TIFF
mkdir JPG PNG TIFF

#Locate all .jpg, .png, and .tiff files inside the folder and copy each into their respective folder.
find . -type f -iname *.jpg -exec cp {} JPG \;
find . -type f -iname *.png -exec cp {} PNG \;
find . -type f -iname *.tiff -exec cp {} TIFF \;

#Create a new file called PictureCounts.md
#Count how many times each file type occurs and log the results to the PictureCounts.md file.
find . -type f -iname *.jpg | wc -l >> PictureCounts.md
find . -type f -iname *.png | wc -l >> PictureCounts.md
find . -type f -iname *.tiff | wc -l >> PictureCounts.md

