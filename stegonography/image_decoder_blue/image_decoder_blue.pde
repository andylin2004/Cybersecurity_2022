import java.util.Arrays;

boolean lastThree(int value) {
    return(value & 7) == 0;
}

int getLast(int value) {
    return value & 1;
}

/**
*Extract the message given a list of the parts of each character.
*Every 4 values is one character.
*Loop over the list and assemble the characters, and append
*each character to an answer string.
*/
PImage reassemble(ArrayList<Integer> parts) {
    PImage result = createImage(600, 600, RGB);
    
    /**
    * loop through the parts list, and append the decoded characters to the ans String
    * You may use another loop or list if you need, but it can be done here.
    */
    
    for (int i = 0; i < parts.size() / 24; i++) {
        int[] array = new int[3];
        for (int h = 0; h < 3; h++){
          for (int v = 0; v < 8; v++) {
            int cPart = parts.get(i*24 + v + h*8);
            cPart = cPart << ((7 - v) * 2);
            array[h] += cPart;
          }
        }
        result.pixels[i] = color(array[0], array[1], array[2]);
    }
    
    result.updatePixels();
    return result;
}

//for code that runs one time place all code in setup.
void setup() {
    size(1200,600);
    PImage img = loadImage("data/modifiedSpace.png");
    img.loadPixels();
    
    ArrayList<Integer> data = new ArrayList<Integer>();
    int count = 0;
    int numPixels = img.width * img.height;
    for (int i = 0; i < numPixels; i++) {
        //extract the numbers from the special pixels add them to an ArrayList
        color c = img.pixels[i];
        int red = (int)red(c);
        int green = (int)green(c);
        int blue = (int)blue(c);
        
        //pixels that have red and blue values that end in 000 have secret hidden in the green channel
        // if (lastThree(red) && lastThree(green)) {
            //the last 2 bits of the green channel is 1/4 of a character
            //extract the last 2 bits of the green channel and store in part of value
            int partOfValue = getLast(blue);
            //add a 0,1,2 or 3 to the list of all the secret values
            data.add(partOfValue);
            count++;
    // }
        
    }
    
    image(reassemble(data), 0, 0);
}