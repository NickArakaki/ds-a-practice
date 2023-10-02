function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

function convertArrayToLinkedList(arr) {
  const ll = new ListNode(arr[0]);
  let currentPointer = ll;

  for (let i = 1; i < arr.length; i++) {
    currentPointer.next = new ListNode(arr[i]);
    currentPointer = currentPointer.next;
  }

  return ll;
}

function mergeList(list1, list2) {
  const mergedList = new ListNode();
  let currentPointer = mergedList;

  while (list1 && list2) {
    if (list1.val < list2.val) {
      currentPointer.next = list1;
      currentPointer = list1;
      list1 = list1.next;
    } else {
      currentPointer.next = list2;
      currentPointer = list2;
      list2 = list2.next;
    }
  }

  if (!list1) currentPointer.next = list2;
  if (!list2) currentPointer.next = list1;

  return mergedList.next;
}

const listOne = convertArrayToLinkedList([1, 3, 5]);
const listTwo = convertArrayToLinkedList([2, 4, 6]);
let finalList = mergeList(listOne, listTwo);

console.log(finalList);
