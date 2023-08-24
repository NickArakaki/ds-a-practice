// """
// Given the head of a singly linked list, reverse the list, and return the reversed list.
// """

class Node {
  constructor(val, next) {
    (this.val = val == undefined ? 0 : val),
      (this.next = next == undefined ? null : next);
  }
}

function reverseList(head) {
  let prev = null;
  let curr = head;

  while (curr) {
    let next = curr.next;
    curr.next = prev;
    prev = curr;
    curr = next;
  }

  return prev;
}

let node4 = new Node(4);
let node3 = new Node(3, node4);
let node2 = new Node(2, node3);
let node1 = new Node(1, node2);

function printList(head) {
  while (head) {
    console.log(head);
    head = head.next;
  }
}

printList(node1);
reverseList(node1);
console.log("--------------------------");
printList(node4);
