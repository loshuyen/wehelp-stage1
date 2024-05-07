function getNumber(index) {
  seq = [];
  for (let i=0; i < index; i++) {
    for (let j=0; j < 3; j++) {
        seq.push(i*7+j*4)
    }
  }
  console.log(seq[index])
}
console.log("==========Task 4==========");
getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70
