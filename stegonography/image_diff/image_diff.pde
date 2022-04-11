boolean isGreenEncoded(int value) {
  int encodedNum = value & 3;
  return encodedNum > 0 && encodedNum <= 3;
}

void setup(){
  size(1200,600);
  PImage img1 = loadImage("cat.png");
  PImage img2 = loadImage("modifiedCat.png");
  PImage diffImage = createImage(1200, 600, RGB);
  img1.loadPixels();
  img2.loadPixels();
  diffImage.loadPixels();

  int numPixels = img1.width * img1.height;

  for (int i = 0; i<numPixels; i++){
    color img1C = img1.pixels[i];
    color img2C = img2.pixels[i];

    int red = abs((int)red(img1C) - (int)red(img2C));
    int green = abs((int)green(img1C) - (int)green(img2C));
    int blue = abs((int)blue(img1C) - (int)blue(img2C));
    
    if (isGreenEncoded(green)){
      diffImage.pixels[i] = color(153, 0, 255);
    }else{
      diffImage.pixels[i] = color(red, green, blue);
    }

  }

  diffImage.updatePixels();
  image(diffImage, 0, 0);
}
