package cs108;


public final class BoundedIntQueueFastTest extends BoundedIntQueueTest {
    public BoundedIntQueueFastTest() {}

    @Override
    protected BoundedIntQueue newBoundedIntQueue(int capacity) {
        return new BoundedIntQueueFast(capacity);
    }
}
