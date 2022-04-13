int getLastTwo(int value) {
  return value & 3;
}

void setup(){
  size(1200,600);
  PImage img1 = loadImage("data/space.png");
  PImage img2 = loadImage("data/modifiedSpace.png");
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
    int blue = ((int)blue(img1C) - (int)blue(img2C));

    if (img1C != img2C){
      println("r" + red);
      println("g" + green);
      println("b" + blue);
    }

    if (blue != 0){
      diffImage.pixels[i] = color(0, 0, 255);
    }else{
      diffImage.pixels[i] = color(0, 0, 0);
    }
  }

  diffImage.updatePixels();
  image(diffImage, 0, 0);
}
