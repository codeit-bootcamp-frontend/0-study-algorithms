class Heap {
  constructor() {
    this.heap = [];
  }
  peek = () => this.heap[0];
  getLeftChildIndex = (parent) => parent * 2 + 1;
  getRightChildIndex = (parent) => parent * 2 + 2;
  getParentIndex = (child) => Math.floor((child - 1) / 2);
  insert = (key, value) => {
    const node = { key, value };
    this.heap.push(node);
    this.heapifyUp();
  };
  remove = () => {
    const length = this.heap.length;
    const root = this.peek();

    if (length <= 0) return;
    if (length === 1) {
      this.heap = [];
    } else {
      this.heap[0] = this.heap.pop();
      this.heapifyDown();
    }
    return root;
  };
  heapifyUp = () => {
    let index = this.heap.length - 1;
    const insertedNode = this.heap[index];

    while (index) {
      const parent = this.getParentIndex(index);

      if (this.heap[parent].key > insertedNode.key) {
        this.heap[index] = this.heap[parent];
        index = parent;
      } else break;
    }
    this.heap[index] = insertedNode;
  };
  heapifyDown = () => {
    let index = 0;
    const length = this.heap.length;
    const root = this.heap[index];

    while (this.getLeftChildIndex(index) < length) {
      const leftChild = this.getLeftChildIndex(index);
      const rightChild = this.getRightChildIndex(index);

      let minChild;

      if (
        rightChild < length &&
        this.heap[rightChild].key < this.heap[leftChild].key
      ) {
        minChild = rightChild;
      } else {
        minChild = leftChild;
      }

      if (this.heap[minChild].key <= root.key) {
        this.heap[index] = this.heap[minChild];
        index = minChild;
      } else break;
    }

    this.heap[index] = root;
  };
}

class PriorityQueue extends Heap {
  constructor() {
    super();
  }
  enqueue = (priority, value) => {
    this.insert(priority, value);
  };
  dequeue = () => {
    return this.remove();
  };
  isEmpty = () => {
    return this.heap.length <= 0;
  };
}

function dijkstra(n, graph, start, end, traps) {
  const pq = new PriorityQueue();
  const visited = Array(n + 1)
    .fill(null)
    .map((_) => []);

  for (let i = 1; i < n + 1; i++) {
    for (let j = 0; j < 1 << traps.length; j++) {
      visited[i][j] = 0;
    }
  }

  pq.enqueue(0, [start, 0]);

  while (!pq.isEmpty()) {
    const curr = pq.dequeue();
    const weight = curr.key;
    const node = curr.value[0];
    let state = curr.value[1];

    if (node === end) {
      return weight;
    }

    if (visited[node][state]) {
      continue;
    }

    visited[node][state] = true;

    let currTrapped = false;
    const trapped = new Map();

    // 현재 node가 함정인지 아닌지 경우의 수
    for (let i = 0; i < traps.length; i++) {
      const bit = 1 << i;
      if (state & bit) {
        if (traps[i] === node) {
          state = state & ~bit;
        } else {
          trapped.set(traps[i], true);
        }
      } else {
        if (traps[i] === node) {
          state = state | bit;
          currTrapped = true;
          trapped.set(traps[i], true);
        }
      }
    }

    // 이동하려는 다음 node에 대해 함정인지 아닌지 경우의 수
    for (let next = 1; next < n + 1; next++) {
      if (next === node) {
        continue;
      }

      const nextTrapped = trapped.has(next) ? true : false;

      if (currTrapped === nextTrapped) {
        if (graph[node][next] !== Infinity) {
          pq.enqueue(weight + graph[node][next], [next, state]);
        }
      } else {
        if (graph[next][node] !== Infinity) {
          pq.enqueue(weight + graph[next][node], [next, state]);
        }
      }
    }
  }

  return Infinity;
}

function solution(n, start, end, roads, traps) {
  const graph = Array.from({ length: n + 1 }, () =>
    Array.from({ length: n + 1 }, () => Infinity)
  );

  roads.forEach(([v1, v2, w]) => (graph[v1][v2] = Math.min(graph[v1][v2], w)));

  return dijkstra(n, graph, start, end, traps);
}