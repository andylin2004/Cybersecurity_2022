import java.util.Arrays;

boolean lastThree(int value) {
    return(value & 7) == 0;
}

boolean firstThree(int value) {
    return(value & 224) == 0;
}

int setLastThree(int secret, int original) {
    return secret | original;
}


//for code that runs one time place all code in setup.
void setup() {
    size(1200,600);
    PImage img = loadImage("data/cat.png");
    println(img.width,img.height);//to check size for display purposes.
    img.loadPixels();
    
    String message = "The message is encoded in a somewhat obvious way if you know how to decode";
    
    //convert the string into an array of ints in the range 0-3
    int[]parts = new int[message.length() * 4];
    int index = 0;
    for (int si = 0; si < message.length(); si++) {
        char c = message.charAt(si);
        int c1 = (128 + 64) & c;
        c1 = c1 >> 6;
        int c2 = (32 + 16) & c;
        c2 = c2 >> 4;
        int c3 = (8 + 4) & c;
        c3 = c3 >> 2;
        int c4 = (2 + 1) & c;
        println(c1,c2,c3,c4);
        parts[index * 4] = c1;
        parts[index * 4 + 1] = c2;
        parts[index * 4 + 2] = c3;
        parts[index * 4 + 3] = c4;
        index++;
}
    
    //add those values to the pixels!
    int count = 0;
    int numPixels = img.width * img.height;
    for (int i = 0; i < numPixels; i++) {
        color c = img.pixels[i];
        int red = (int)red(c);
        int green = (int)green(c);
        int blue = (int)blue(c);
        //when the red and blue end in 000, modify the last 2 bits of green.
        if (lastThree(red) && lastThree(blue)) {
            
            //clear the green data last 2 bits.
            green = (green & (128 + 64 + 32 + 16 + 8 + 4));
            if (count < parts.length) {
                //change the last 2 bits to the partial character
                green = (green | parts[count]);
                count++;
        } else{
                //when no more message, fix the blue so it doesn't have 000 at the end.
                blue= blue | 1;
        }
            img.pixels[i] = color(red,green,blue);
        }
}
    img.updatePixels();
    img.save("data/modifiedCat.png");
    
}
