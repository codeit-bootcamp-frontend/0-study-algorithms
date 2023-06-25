class Node {
    constructor(item){
        this.item = item 
        this.next = null 
        this.prev = null 
    }
}

class Deque {
    constructor(){
        this.head = null 
        this.tail = null 
        this.size = 0 
    }
    pushFront(item){
        const newNode = new Node(item)
        if(this.getSize() === 0){
            this.head = newNode 
            this.tail = newNode 
        } else {
            newNode.next = this.head 
            this.head.prev = newNode 
            this.head = newNode
        }
        this.size += 1
    }
    pushBack(item){
        const newNode = new Node(item)
        if(this.getSize() === 0){
            this.head = newNode 
            this.tail = newNode
        } else {
            this.tail.next = newNode 
            newNode.prev = this.tail 
            this.tail = newNode
        }
        this.size += 1
    }
    popFront(){
        if(this.getSize() === 0){
            return -1
        } else if(this.getSize() === 1){
            const popedItem = this.head.item 
            this.head = null 
            this.tail = null 
            this.size -= 1 
            return popedItem
        } else if(this.getSize() === 2){
            const popedItem = this.head.item 
            this.head = this.head.next 
            this.tail.prev = null 
            this.size -= 1
            return popedItem 
        } else if(this.getSize() > 2){
            const popedItem = this.head.item 
            this.head.next.prev = null 
            this.head = this.head.next 
            this.size -= 1 
            return popedItem 
        }
    }
    popBack(){
        if(this.getSize() === 0){
            return -1 
        } else if(this.getSize() === 1){
            const popedItem = this.tail.item
            this.head = null
            this.tail = null
            this.size -= 1
            return popedItem
        } else if(this.getSize() === 2){
            const popedItem = this.tail.item
            this.tail = this.tail.prev
            this.head.next = null 
            this.size -= 1 
            return popedItem 
        } else if(this.getSize() > 2){
            const popedItem = this.tail.item 
            this.tail.prev.next = null 
            this.tail = this.tail.prev 
            this.size -= 1 
            return popedItem 
        }
    }
    getSize(){
        return this.size
    }
    isEmpty(){
        return this.getSize() ? 0 : 1 
    }
    getFront(){
        return this.getSize() ? this.head.item : -1 
    }
    getBack(){
        return this.getSize() ? this.tail.item : -1 
    }
}

function solution(rc, operations) {
    const mdq = new Deque() 
    const ldq = new Deque()
    const rdq = new Deque() 
    
    let answer = [[]]
    
    // 2차원 행렬 => 3개의 deque로 분리 
    for (let i = 0; i < rc.length; ++i) {
      const dq = new Deque();
      ldq.pushBack(rc[i][0]); // left pushBack
      for (let j = 1; j < rc[0].length - 1; ++j) {
        dq.pushBack(rc[i][j]);
      }
      rdq.pushBack(rc[i][rc[i].length - 1]); // right pushBack
      mdq.pushBack(dq); // main pushBack
    }
    
    // 분리한 각각의 deque에 operations 반영 
    for (let i = 0; i < operations.length; ++i) {
        if (operations[i] === "ShiftRow") {
          mdq.pushFront(mdq.popBack());
          ldq.pushFront(ldq.popBack());
          rdq.pushFront(rdq.popBack());
        } else if (operations[i] === "Rotate") {
          let sf = mdq.popFront();
          let sb = mdq.popBack();
          sf.pushFront(ldq.popFront());
          sb.pushBack(rdq.popBack());
          ldq.pushBack(sb.popFront());
          rdq.pushFront(sf.popBack());
          mdq.pushFront(sf);
          mdq.pushBack(sb);
        }
      }
    
    // 정답 도출 
    for (let i = 0; i < rc.length; ++i) {
    let arr = [];
    let temp = mdq.popFront();
    temp.pushFront(ldq.popFront());
    temp.pushBack(rdq.popFront());
    for (let j = 0; j < rc[0].length; ++j) {
      arr[j] = temp.popFront();
    }
    answer[i] = arr;
  }
    return answer 
}