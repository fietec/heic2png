from PIL import Image
import pillow_heif
import sys
import os

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("No input file provided!")
        exit(1)
    
    for input_file in sys.argv[1:]:
        heif_file = pillow_heif.read_heif(input_file)
        image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, "raw")
        if image == None:
            print("Failed to load image!")
            exit(1)
        print(f"Converting '{input_file}'..")
        filename = os.path.splitext(os.path.basename(input_file))[0] + ".png"
        path = os.path.join(os.getcwd(), filename)
        image.save(path, format("png"))
        os.startfile(path)
        os.remove(input_file)
