package cs108.views;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public final class SublistView {
    public static void main(String[] args) {
        List<Integer> l = new ArrayList<>(List.of(5, 7, 1, 4, 2, 3, 6, 8));

        // 1. Création et affichage de la sous-liste
        List<Integer> subL = l.subList(2, 6);
        System.out.println("1a: " + l);
        System.out.println("1b: " + subL);

        // 2. Modification (tri) de la sous-liste
        Collections.sort(subL);
        System.out.println("2a: " + subL);
        System.out.println("2b: " + l);

        // 3. Modification (mélange aléatoire)
        Collections.shuffle(subL);
        System.out.println("3:  " + l);

        // 4. Effacement de la sous-liste
        subL.clear();
        System.out.println("4:  " + l);

        // 5. Insertion dans la sous-liste
        subL.addAll(List.of(0, 0, 0));
        System.out.println("5:  " + l);
    }
}
