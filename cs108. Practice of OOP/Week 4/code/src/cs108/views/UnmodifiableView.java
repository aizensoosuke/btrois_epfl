package cs108.views;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public final class UnmodifiableView {
    public static void main(String[] args) {
        List<Integer> ml = new ArrayList<>(Arrays.asList(5, 7, 1, 4, 2, 3, 6, 8));
        List<Integer> ul = Collections.unmodifiableList(ml);

        System.out.println(ml);
        System.out.println(ul);

        // Tentative de modification de la liste non modifiable
        ul.remove(0); // lève Unsupported…
        System.out.println(ul);

        // Modification de la liste modifiable
        ml.remove(0);
        System.out.println(ul);
    }
}
