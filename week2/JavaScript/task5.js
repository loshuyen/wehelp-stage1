function find(spaces, stat, n){
    let availableCar={};
    for (let i = 0; i < stat.length; i++) {
        if (stat[i]===1) {
            availableCar[i]=spaces[i];
        }
    }
    let spaceDiff={};    
    for (let car in availableCar) {
        if (availableCar[car]-n >= 0) {
            spaceDiff[car]=availableCar[car]-n;
        }
    }
    if (Object.keys(spaceDiff).length === 0) {
        console.log(-1);
        return;
    }
    let diff = [];
    for (let val of Object.values(spaceDiff)) {
        diff.push(val);
    }
    for (const [key, val] of Object.entries(spaceDiff)) {
        if (val === Math.min(...diff)) {
            console.log(key);
        }
    }
}
console.log("==========Task 5==========")
find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2); // print 5 
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1 
find([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2