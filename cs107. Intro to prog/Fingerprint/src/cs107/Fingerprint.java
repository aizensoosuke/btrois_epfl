package cs107;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Provides tools to compare fingerprint.
 */
public class Fingerprint {

  /**
   * The number of pixels to consider in each direction when doing the linear
   * regression to compute the orientation.
   */
  public static final int ORIENTATION_DISTANCE = 16;

  /**
   * The maximum distance between two minutiae to be considered matching.
   */
  public static final int DISTANCE_THRESHOLD = 5;

  /**
   * The number of matching minutiae needed for two fingerprints to be considered
   * identical.
   */
  public static final int FOUND_THRESHOLD = 20;

  /**
   * The distance between two angle to be considered identical.
   */
  public static final int ORIENTATION_THRESHOLD = 20;

  /**
   * The offset in each direction for the rotation to test when doing the
   * matching.
   */
  public static final int MATCH_ANGLE_OFFSET = 2;

  /**
   * Returns true iff the pixel at position (row, col) is inside of the image
   * image.
   *
   * @param image the image
   * @param row   the row
   * @param col   the col
   * @returns whether or not pixel is in image
   */
  public static boolean isInside(boolean[][] image, int row, int col) {
    if (image == null || row < 0 || col < 0 || row >= image.length || col >= image[0].length)
      return false;
    return true;
  }

  /**
   * Returns the pixel at position (row, col) if it's in the image. Otherwise
   * returns false.
   *
   * @param image the image.
   * @param row   the row
   * @param col   the col
   * @return the resulting pixel
   */
  public static boolean getPixel(boolean[][] image, int row, int col) {
    return isInside(image, row, col) && image[row][col];
  }

  /**
   * Returns a deep copy of the image given as an argument.
   *
   * @param image the image to copy
   * @return the copy of the image
   */
  public static boolean[][] copyImage(boolean[][] image) {
    if (image == null)
      return null;

    boolean[][] copy = new boolean[image.length][image[0].length];

    for(int i = 0; i < image.length; i++)
      copy[i] = image[i].clone(); // works for 1D arrays

    return copy;
  }

  /**
   * Returns an array containing the value of the 8 neighbours of the pixel at
   * coordinates <code>(row, col)</code>.
   * <p>
   * The pixels are returned such that their indices corresponds to the following
   * diagram:<br>
   * ------------- <br>
   * | 7 | 0 | 1 | <br>
   * ------------- <br>
   * | 6 | _ | 2 | <br>
   * ------------- <br>
   * | 5 | 4 | 3 | <br>
   * ------------- <br>
   * <p>
   * If a neighbours is out of bounds of the image, it is considered white.
   * <p>
   * If the <code>row</code> or the <code>col</code> is out of bounds of the
   * image, the returned value should be <code>null</code>.
   *
   * @param image array containing each pixel's boolean value.
   * @param row   the row of the pixel of interest, must be between
   *              <code>0</code>(included) and
   *              <code>image.length</code>(excluded).
   * @param col   the column of the pixel of interest, must be between
   *              <code>0</code>(included) and
   *              <code>image[row].length</code>(excluded).
   * @return An array containing each neighbours' value.
   */
  public static boolean[] getNeighbours(boolean[][] image, int row, int col) {
    assert (image != null); // special case that is not expected (the image is supposed to have been checked
                            // earlier)
    int[] rows = { -1, -1, 0, 1, 1, 1, 0, -1 };
    int[] cols = { 0, 1, 1, 1, 0, -1, -1, -1 };
    boolean[] res = new boolean[8];

    if (!isInside(image, row, col))
      return null;

    for (int i = 0; i < 8; i++) {
      res[i] = getPixel(image, row + rows[i], col + cols[i]);
    }

    return res;
  }

  /**
   * Computes the number of black (<code>true</code>) pixels among the neighbours
   * of a pixel.
   *
   * @param neighbours array containing each pixel value. The array must respect
   *                   the convention described in
   *                   {@link #getNeighbours(boolean[][], int, int)}.
   * @return the number of black neighbours.
   */
  public static int blackNeighbours(boolean[] neighbours) {
    int count = 0;

    for (int i = 0; i < neighbours.length; i++) {
      if (neighbours[i])
        count++;
    }

    return count;
  }

  /**
   * Computes the number of white to black transitions among the neighbours of
   * pixel.
   *
   * @param neighbours array containing each pixel value. The array must respect
   *                   the convention described in
   *                   {@link #getNeighbours(boolean[][], int, int)}.
   * @return the number of white to black transitions.
   */
  public static int transitions(boolean[] neighbours) {
    int count = 0;

    for (int i = 0; i < neighbours.length; i++) {
      if (!neighbours[i] && neighbours[(i + 1) % neighbours.length])
        count++;
    }

    return count;
  }

  /**
   * Returns <code>true</code> if the images are identical and false otherwise.
   *
   * @param image1 array containing each pixel's boolean value.
   * @param image2 array containing each pixel's boolean value.
   * @return <code>True</code> if they are identical, <code>false</code>
   *         otherwise.
   */
  public static boolean identical(boolean[][] image1, boolean[][] image2) {
    assert (image1 != null || image2 != null); // images not empty

    if (image1.length != image2.length || image1[0].length != image2[0].length)
      return false;

    for (int i = 0; i < image1.length; i++) {
      for (int j = 0; j < image1[0].length; j++) {
        if (image1[i][j] != image2[i][j]) return false;
      }
    }

    return true;
  }

  /**
   * Internal method used by {@link #thin(boolean[][])}.
   *
   * @param image array containing each pixel's boolean value.
   * @param step  the step to apply, Step 0 or Step 1.
   * @return A new array containing each pixel's value after the step.
   */
  public static boolean[][] thinningStep(boolean[][] image, int step) {
    assert (image != null); // as usual
    assert (step == 0 || step == 1); // step must be 0 or 1

    boolean[][] res = copyImage(image);

    for (int i = 0; i < res.length; i++) {
      for (int j = 0; j < res[0].length; j++) {
        boolean[] neighbours = getNeighbours(image, i, j);
        if (image[i][j] && neighbours != null // ???
            && 2 <= blackNeighbours(neighbours) && blackNeighbours(neighbours) <= 6 && transitions(neighbours) == 1) {
          if (step == 0 && !(neighbours[0] && neighbours[2] && neighbours[4]) && !(neighbours[2] && neighbours[4] && neighbours[6]))
            res[i][j] = false;
          if (step == 1 && !(neighbours[0] && neighbours[2] && neighbours[6]) && !(neighbours[0] && neighbours[4] && neighbours[6]))
            res[i][j] = false;
        }
      }
    }

    return res;
  }

  /**
   * Compute the skeleton of a boolean image.
   *
   * @param image array containing each pixel's boolean value.
   * @return array containing the boolean value of each pixel of the image after
   *         applying the thinning algorithm.
   */
  public static boolean[][] thin(boolean[][] image) {
    assert (image != null); // as usual
    boolean[][] oldImage;
    boolean[][] res = copyImage(image);

    do {
      oldImage = copyImage(res);
      res = thinningStep(thinningStep(res, 0), 1);
    } while (!identical(res, oldImage));

    return res;
  }

  /**
   * Computes all pixels that are connected to the pixel at coordinate
   * <code>(row, col)</code> and within the given distance of the pixel.
   *
   * @param image    array containing each pixel's boolean value.
   * @param row      the first coordinate of the pixel of interest.
   * @param col      the second coordinate of the pixel of interest.
   * @param distance the maximum distance at which a pixel is considered.
   * @return An array where <code>true</code> means that the pixel is within
   *         <code>distance</code> and connected to the pixel at
   *         <code>(row, col)</code>.
   */
  public static boolean[][] connectedPixels(boolean[][] image, int row, int col, int distance) {
    assert (image != null); // as usual
    assert (isInside(image, row, col)); // minutia must be in image

    // coordinates for the cropped connected "square"
    int top = Math.max(row - distance, 0);
    int bot = Math.min(row + distance + 1, image.length);
    int left = Math.max(col - distance, 0);
    int right = Math.min(col + distance + 1, image[0].length);

    boolean[][] connected = new boolean[image.length][image[0].length];
    boolean[][] old;

    // init to false
    for (int i = 0; i < image.length; i++) {
      for (int j = 0; j < image[0].length; j++) {
          connected[i][j] = false;
      }
    }
    connected[row][col] = image[row][col]; // minutia

    do {
      old = copyImage(connected);
      for (int i = top; i < bot; i++) {
        for (int j = left; j < right; j++) {
          if (getPixel(image, i, j) && blackNeighbours(getNeighbours(connected, i, j)) > 0) {
            connected[i][j] = true;
          }
        }
      }
    } while (!identical(old, connected));

    return connected;
  }

  /**
   * Computes the slope of a minutia using linear regression.
   *
   * @param connectedPixels the result of
   *                        {@link #connectedPixels(boolean[][], int, int, int)}.
   * @param row             the row of the minutia.
   * @param col             the col of the minutia.
   * @return the slope.
   */
  public static double computeSlope(boolean[][] connectedPixels, int row, int col) {
    assert (connectedPixels != null); // there should at least be the minutia

    double sumX = 0;
    double sumY = 0;
    double sumXY = 0;

    for (int i = 0; i < connectedPixels.length; i++) {
      for (int j = 0; j < connectedPixels[0].length; j++) {
        if (connectedPixels[i][j]) {
          int x = j - col;
          int y = row - i;
          sumX += x*x;
          sumY += y*y;
          sumXY += x*y;
        }
      }
    }

    if (sumX == 0)
      return Double.POSITIVE_INFINITY;

    return sumX >= sumY ? sumXY / sumX : sumY / sumXY;
  }

  /**
   * Computes the orientation of a minutia in radians.
   * 
   * @param connectedPixels the result of
   *                        {@link #connectedPixels(boolean[][], int, int, int)}.
   * @param row             the row of the minutia.
   * @param col             the col of the minutia.
   * @param slope           the slope as returned by
   *                        {@link #computeSlope(boolean[][], int, int)}.
   * @return the orientation of the minutia in radians.
   */
  public static double computeAngle(boolean[][] connectedPixels, int row, int col, double slope) {
    assert (connectedPixels != null); // as usual
    assert (getPixel(connectedPixels, row, col)); // there must be a minutia at (row, col)

    double perpSlope;
    double angle;
    int abovePixels = 0;
    int belowPixels = 0;

    if(slope == Double.POSITIVE_INFINITY) {
      angle = -Math.PI / 2;
      perpSlope = 0;
    } else {
      angle = Math.atan(slope);
      perpSlope = -1 / slope;
    }

    for (int i = 0; i < connectedPixels.length; i++) {
      for(int j = 0; j < connectedPixels[0].length; j++) {
        if (getPixel(connectedPixels, i, j)) {
          int x = j - col;
          int y = row - i;
          if (y >= perpSlope * x)
            abovePixels += 1;
          else
            belowPixels += 1;
        }
      }
    }

    if((angle > 0 && belowPixels > abovePixels) || (angle < 0 && belowPixels < abovePixels))
      angle += Math.PI;

    return angle;
  }

  /**
   * Computes the orientation of the minutia that the coordinate <code>(row,
   * col)</code>.
   *
   * @param image    array containing each pixel's boolean value.
   * @param row      the first coordinate of the pixel of interest.
   * @param col      the second coordinate of the pixel of interest.
   * @param distance the distance to be considered in each direction to compute
   *                 the orientation.
   * @return The orientation in degrees.
   */
  public static int computeOrientation(boolean[][] image, int row, int col, int distance) {
    assert (image != null); // as usual

    boolean[][] connected = connectedPixels(image, row, col, distance);

    int angle = (int)Math.round(Math.toDegrees(computeAngle(connected, row, col, computeSlope(connected, row, col))));

    return angle < 0 ? angle + 360 : angle;
  }

  /**
   * Extracts the minutiae from a thinned image.
   *
   * @param image array containing each pixel's boolean value.
   * @return The list of all minutiae. A minutia is represented by an array where
   *         the first element is the row, the second is column, and the third is
   *         the angle in degrees.
   * @see #thin(boolean[][])
   */
  public static List<int[]> extract(boolean[][] image) {
    assert (image != null); // as usual

    List<int[]> res = new ArrayList<int[]>();

    for (int i = 1; i < image.length - 1; i++) {
      for(int j = 1; j < image[0].length - 1; j++ ) {
        int transitionCount = transitions(getNeighbours(image, i, j));
        if(getPixel(image, i, j) && (transitionCount == 1 || transitionCount == 3))
          res.add(new int[] {i, j, computeOrientation(image, i, j, ORIENTATION_DISTANCE)});
      }
    }

    return res;
  }

  /**
   * Applies the specified rotation to the minutia.
   *
   * @param minutia   the original minutia.
   * @param centerRow the row of the center of rotation.
   * @param centerCol the col of the center of rotation.
   * @param rotation  the rotation in degrees.
   * @return the minutia rotated around the given center.
   */
  public static int[] applyRotation(int[] minutia, int centerRow, int centerCol, int rotation) {
    int row = minutia[0];
    int col = minutia[1];
    int orientation = minutia[2];

    int x = col - centerCol;
    int y = centerRow - row;
    double angle = Math.toRadians(rotation);
    double newX = x*Math.cos(angle) - y*Math.sin(angle);
    double newY = x*Math.sin(angle) + y*Math.cos(angle);

    int newRow = (int)Math.round(centerRow - newY);
    int newCol = (int)Math.round(newX + centerCol);
    int newOrientation = (int) (orientation + rotation) % 360;

    return new int[] { newRow, newCol, newOrientation };
  }

  /**
   * Applies the specified translation to the minutia.
   *
   * @param minutia        the original minutia.
   * @param rowTranslation the translation along the rows.
   * @param colTranslation the translation along the columns.
   * @return the translated minutia.
   */
  public static int[] applyTranslation(int[] minutia, int rowTranslation, int colTranslation) {
    int row = minutia[0];
    int col = minutia[1];
    int orientation = minutia[2];

    return new int[] { row - rowTranslation, col - colTranslation, orientation };
  }

  /**
   * Computes the row, column, and angle after applying a transformation
   * (translation and rotation).
   *
   * @param minutia        the original minutia.
   * @param centerCol      the column around which the point is rotated.
   * @param centerRow      the row around which the point is rotated.
   * @param rowTranslation the vertical translation.
   * @param colTranslation the horizontal translation.
   * @param rotation       the rotation.
   * @return the transformed minutia.
   */
  public static int[] applyTransformation(int[] minutia, int centerRow, int centerCol, int rowTranslation,
      int colTranslation, int rotation) {
    return applyTranslation(applyRotation(minutia, centerRow, centerCol, rotation), rowTranslation, colTranslation);
  }

  /**
   * Computes the row, column, and angle after applying a transformation
   * (translation and rotation) for each minutia in the given list.
   *
   * @param minutiae       the list of minutiae.
   * @param centerCol      the column around which the point is rotated.
   * @param centerRow      the row around which the point is rotated.
   * @param rowTranslation the vertical translation.
   * @param colTranslation the horizontal translation.
   * @param rotation       the rotation.
   * @return the list of transformed minutiae.
   */
  public static List<int[]> applyTransformation(List<int[]> minutiae, int centerRow, int centerCol, int rowTranslation,
      int colTranslation, int rotation) {
    List<int[]> res = new ArrayList<int[]>();

    for(int[] minutia : minutiae) {
      res.add(applyTransformation(minutia, centerRow, centerCol, rowTranslation, colTranslation, rotation));
    }

    return res;
  }

  /**
   * Counts the number of overlapping minutiae.
   *
   * @param minutiae1      the first set of minutiae.
   * @param minutiae2      the second set of minutiae.
   * @param maxDistance    the maximum distance between two minutiae to consider
   *                       them as overlapping.
   * @param maxOrientation the maximum difference of orientation between two
   *                       minutiae to consider them as overlapping.
   * @return the number of overlapping minutiae.
   */
  public static int matchingMinutiaeCount(List<int[]> minutiae1, List<int[]> minutiae2, int maxDistance,
      int maxOrientation) {
    int matching = 0;

    for(int i = 0; i < minutiae1.size(); i++) {
      for(int j = 0; j < minutiae2.size(); j++) {
        double row1 = minutiae1.get(i)[0];
        double col1 = minutiae1.get(i)[1];
        double row2 = minutiae2.get(j)[0];
        double col2 = minutiae2.get(j)[1];

        double distance = Math.sqrt(Math.pow(row1 - row2, 2) + Math.pow(col1 - col2, 2));
        double orientation = Math.abs(minutiae1.get(i)[2] - minutiae2.get(j)[2]);

        if (distance <= maxDistance && orientation <= maxOrientation)
          matching++;
      }
    }

    return matching;
  }

  /**
   * Compares the minutiae from two fingerprints.
   *
   * @param minutiae1 the list of minutiae of the first fingerprint.
   * @param minutiae2 the list of minutiae of the second fingerprint.
   * @return Returns <code>true</code> if they match and <code>false</code>
   *         otherwise.
   */
  public static boolean match(List<int[]> minutiae1, List<int[]> minutiae2) {
    for(int i = 0; i < minutiae1.size(); i++) {
      for(int j = 0; j < minutiae2.size(); j++) {
        double computedRotation = minutiae2.get(j)[2] - minutiae1.get(i)[2];
        int centerRow = minutiae1.get(i)[0];
        int centerCol = minutiae1.get(i)[1];
        int rowTranslation = minutiae2.get(j)[0] - centerRow;
        int colTranslation = minutiae2.get(j)[1] - centerCol;

        for (int rotation = (int) Math.ceil(computedRotation - MATCH_ANGLE_OFFSET); rotation <= computedRotation + MATCH_ANGLE_OFFSET; rotation++) {
          List<int[]> transformedMinutiae2 = applyTransformation(minutiae2, centerRow, centerCol, rowTranslation, colTranslation, rotation);
          if (matchingMinutiaeCount(minutiae1, transformedMinutiae2, DISTANCE_THRESHOLD, ORIENTATION_THRESHOLD) >= FOUND_THRESHOLD)
            return true;
        }
      }
    }

    return false;
  }
}
