# motion-photo-extractor  

Extract pictures and movies from Samsung GS7 motion photos. Adapted for python from github.com/MatthewAlner/motion-photo-extractor/.
Requires python>=3.5

## What this does  

It's a command line ruby script that splits your S7/S7 Edge motion photos in to a (now smaller) jpg and a mp4.  The files will be saved in the same folder the original image.  

## Example  

```bash
$ python motion-photo-extractor.py  #Splits everything in current directory

or

$ python motion-photo-extractor.py ./FolderA  /abs-path/FolderB  ./imageA.jpg  #Splits in each folder and additional files
```

## Options

$ motion-photo-extractor.py [options]

| Short | Long           | Description 
| ------|--------------- | -------------------- 
| -h    | --help         | Prints help
