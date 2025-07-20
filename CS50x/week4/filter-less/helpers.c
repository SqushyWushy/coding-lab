#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width]) {
  for (int i = 0; i < height; i++) {
    for (int j = 0; j < width; j++) {
      int red = image[i][j].rgbtRed;
      int green = image[i][j].rgbtGreen;
      int blue = image[i][j].rgbtBlue;

      int avg = round((red + green + blue) / 3.0);

      image[i][j].rgbtRed = avg;
      image[i][j].rgbtBlue = avg;
      image[i][j].rgbtGreen = avg;
    }
  }
  return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width]) {
  for (int i = 0; i < height; i++) {
    for (int j = 0; j < width; j++) {
      int red = image[i][j].rgbtRed;
      int blue = image[i][j].rgbtBlue;
      int green = image[i][j].rgbtGreen;

      double sepiaRed = 0.393 * red + 0.769 * green + 0.189 * blue;
      double sepiaGreen = 0.349 * red + 0.686 * green + 0.168 * blue;
      double sepiaBlue = 0.272 * red + 0.534 * green + 0.131 * blue;

      if (sepiaBlue > 255) {
        sepiaBlue = 255;
      }
      if (sepiaGreen > 255) {
        sepiaGreen = 255;
      }
      if (sepiaRed > 255) {
        sepiaRed = 255;
      }

      image[i][j].rgbtRed = round(sepiaRed);
      image[i][j].rgbtBlue = round(sepiaBlue);
      image[i][j].rgbtGreen = round(sepiaGreen);
    }
  }

  return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width]) {
  for (int i = 0; i < height; i++) {
    for (int j = 0; j < width / 2; j++) {
      // Swap the pixel at position j with the one at width - j - 1
      RGBTRIPLE temp = image[i][j];
      image[i][j] = image[i][width - j - 1];
      image[i][width - j - 1] = temp;
    }
  }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width]) {
  RGBTRIPLE copy[height][width];

  // Copy the original image into the temp copy
  for (int i = 0; i < height; i++) {
    for (int j = 0; j < width; j++) {
      copy[i][j] = image[i][j];
    }
  }

  // Loop through every pixel in the image
  for (int i = 0; i < height; i++) {
    for (int j = 0; j < width; j++) {
      int sumRed = 0;
      int sumGreen = 0;
      int sumBlue = 0;
      int count = 0;

      // Check all 3x3 neighbors around pixel (i, j)
      for (int di = -1; di <= 1; di++) {
        for (int dj = -1; dj <= 1; dj++) {
          int ni = i + di; // neighbor row
          int nj = j + dj; // neighbor column

          // Make sure neighbor is within image bounds
          if (ni >= 0 && ni < height && nj >= 0 && nj < width) {
            sumRed += copy[ni][nj].rgbtRed;
            sumGreen += copy[ni][nj].rgbtGreen;
            sumBlue += copy[ni][nj].rgbtBlue;
            count++;
          }
        }
      }

      // Set the blurred pixel value (rounded average)
      image[i][j].rgbtRed = round((float)sumRed / count);
      image[i][j].rgbtGreen = round((float)sumGreen / count);
      image[i][j].rgbtBlue = round((float)sumBlue / count);
    }
  }
  return;
}
