package cs108;

public final class BoundedIntQueueSlow implements BoundedIntQueue {
    private final int[] contents;
    private int size;

    public BoundedIntQueueSlow(int capacity) {
        if (!(capacity >= 0))
            throw new IllegalArgumentException(
                    "illegal capacity: " + capacity + " (must be >= 0)");
        contents = new int[capacity];
        size = 0;
    }

    @Override
    public int capacity() {
        return contents.length;
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    @Override
    public boolean isFull() {
        return size == capacity();
    }

    @Override
    public void addLast(int newElement) {
        if (isFull())
            throw new IllegalStateException("full queue");
        contents[size++] = newElement;

        assert 1 <= size && size <= capacity();
    }

    @Override
    public int removeFirst() {
        if (isEmpty())
            throw new IllegalStateException("empty queue");
        int first = contents[0];
        System.arraycopy(contents, 1, contents, 0, --size);
        assert 0 <= size && size < capacity();
        return first;
    }
}
