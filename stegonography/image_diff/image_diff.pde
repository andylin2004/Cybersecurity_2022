int getLastTwo(int value) {
  return value & 3;
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

    if (img1C == img2C){
      diffImage.pixels[i] = color(255, 255, 255);
    }else{
      int green = abs((int)green(img1C) - (int)green(img2C));
      switch(getLastTwo(green)){
        case 0:
         diffImage.pixels[i] = color(255, 0, 0);
         break;
        case 1:
         diffImage.pixels[i] = color(0, 255, 0);
         break;
        case 2:
         diffImage.pixels[i] = color(0, 0, 255);
         break;
        case 3:
         diffImage.pixels[i] = color(231, 200, 146);
         break;
        default:
         diffImage.pixels[i] = color(255, 0, 255);
         break;
      }
    } 
  }

  diffImage.updatePixels();
  image(diffImage, 0, 0);
}
