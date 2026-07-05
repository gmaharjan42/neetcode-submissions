class DynamicArray {
    private int capacity;
    private int size;
    private int[] arr;

    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this. size = 0;
        this.arr = new int[this.capacity];
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if (size == capacity) {
            resize();
    }
        arr[size] = n;
        size++;
    }

    public int popback() {
        int lastValue = arr[size - 1];
        size--;
        return lastValue;
    }

    private void resize() {
        int newCapacity = capacity * 2;
        int[] newArray = new int[newCapacity];
        for (int i = 0; i < size; i++){
            newArray[i] = arr[i];
        }
        capacity = newCapacity;
        arr = newArray;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return capacity;
    }
}
