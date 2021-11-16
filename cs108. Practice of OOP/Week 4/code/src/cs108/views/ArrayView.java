package cs108.views;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public final class ArrayView {
    public static void main(String[] args) {
        String[] a = new String[]{"b", "c", "a", "f", "e", "g", "d", "k", "m", "o"};
        List<String> l = Arrays.asList(a);

        // 1. Modification du tableau (à travers la vue)
        l.set(0, "z");
        System.out.println("1: " + Arrays.toString(a));

        // 2. Tri du tableau (à travers la vue)
        Collections.sort(l);
        System.out.println("2: " + Arrays.toString(a));

        // 3. Mélange d'une partie du tableau (à travers une vue de vue)
        List<String> l2 = l.subList(0, 5);
        Collections.shuffle(l2);
        System.out.println("3: " + Arrays.toString(a));

        // 4. Tentative de suppression d'un élément du tableau (lève UnsupportedOperationEx…)
        l.remove(0);
    }
}
