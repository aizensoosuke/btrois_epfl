package cs108;

import java.lang.IllegalArgumentException;
import java.lang.IllegalStateException;

/**
 * Working implementation of BoundedIntQueue.
 *
 * @author Yohan Abehssera
 * @author Michel Schinz (most comments)
 */
public class BoundedIntQueueOk implements BoundedIntQueue {

    private int [] queue;
    private int size;
    private int capacity;
    private int firstPosition;

    BoundedIntQueueOk(int _capacity) {
        if(_capacity < 0) {
            throw new IllegalArgumentException("Capacity must be non-negative.");
        }

        queue = new int[_capacity];
        size = 0;
        firstPosition = 0;
        capacity = _capacity;

        assert capacity == queue.length;
    }

    /**
     * Retourne la position du premier élément de la queue.
     *
     * @return firstPosition
     */
    private int firstPosition() {
        return firstPosition;
    }

    /**
     * Calcule et retourne la position du dernier élément de la queue à partir de
     *   - la position du
     * Cette position peut être supérieure ou inférieure à firstPosition !.
     *
     * @return lastPosition
     */
    private int lastPosition() {
        return (firstPosition() + size()) % capacity();
    }

    /**
     * Retourne la capacité de la queue, c-à-d le nombre maximum d'éléments
     * qu'elle peut contenir.
     *
     * @return la capacité de la queue.
     */
    public int capacity() {
        assert capacity >= 0;
        return capacity;
    }

    /**
     * Retourne la taille de la queue, c-à-d le nombre d'éléments qu'elle
     * contient.
     *
     * @return la taille de la queue.
     */
    public int size() {
        assert size >= 0;
        return size;
    }

    /**
     * Retourne vrai ssi la queue est vide, c-à-d que sa taille est nulle.
     *
     * @return vrai ssi la queue est vide.
     */
    public boolean isEmpty() {
        return size() == 0;
    }

    /**
     * Retourne vrai ssi la queue est pleine, c-à-d que sa taille est égale à sa
     * capacité.
     *
     * @return vrai ssi la queue est pleine.
     */
    public boolean isFull() {
        return size() == capacity();
    }

    /**
     * Ajoute l'élément donné en fin de queue.
     *
     * @param newElement
     *            l'élément à ajouter.
     * @throws java.lang.IllegalStateException
     *             si la queue est pleine.
     */
    public void addLast(int newElement) {
        if(isFull()) {
            throw new IllegalStateException("Full queue");
        }

        queue[lastPosition()] = newElement;

        size++;
        assert size() <= capacity();
    }

    /**
     * Supprime et retourne l'élément en début de la queue.
     *
     * @return l'élément en début de queue.
     * @throws java.lang.IllegalStateException
     *             si la queue est vide.
     */
    public int removeFirst() {
        if(isEmpty()) {
            throw new IllegalStateException("Empty queue");
        }

        int firstElement = queue[firstPosition()];

        size--;
        assert size() >= 0;

        if(firstPosition < capacity() - 1) {
            firstPosition++;
        }
        else {
            assert firstPosition == capacity() - 1;
            firstPosition = 0;
            assert lastPosition() >= firstPosition();
        }

        return firstElement;
    }
}
