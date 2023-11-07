// [ rows, columns ]
let gameCoordinates = [
    [ 2, 1 ],
    [ 4, 3 ],
    [ 6, 5 ],
    [ 8, 7 ],
    [ 10, 9 ],
  ];

  function transposeArray(array) {
    const newArray = [];

    for (let i = 0; i < array.length; i++) {
      newArray.push([]);

      for (let j = array[i].length - 1; j >= 0; j--) {
        newArray[i].push(array[i][j]);
      }
    };

    return newArray;
  }

  console.log(transposeArray(gameCoordinates));
  // [ [ 1, 2 ], [ 3, 4 ], [ 5, 6 ], [ 7, 8 ], [ 9, 10 ] ]
