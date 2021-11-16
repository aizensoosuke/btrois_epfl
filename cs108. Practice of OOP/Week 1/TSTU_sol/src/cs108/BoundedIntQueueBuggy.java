package cs108;

public final class BoundedIntQueueBuggy implements BoundedIntQueue {
    private final int[] contents;
    private int size;
    private int headPos;

    public BoundedIntQueueBuggy(int capacity) {
        if (!(capacity >= 0))
            throw new IllegalArgumentException(
                    "illegal capacity: " + capacity + " (must be >= 0)");
        contents = new int[capacity + 1];
        size = 1;
        headPos = 0;
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
        headPos = (headPos + 1) % contents.length;
        contents[headPos] = newElement;
        size += 1;
        if (isFull())
            throw new IllegalArgumentException("full queue");
    }

    @Override
    public int removeFirst() {
        size -= 1;
        int tailPos = (headPos - size + contents.length) % contents.length;
        if (isEmpty())
            throw new IllegalArgumentException("empty queue");
        return contents[tailPos];
    }
}
