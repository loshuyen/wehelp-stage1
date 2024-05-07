function func(...data){
    let middleName={};
    let middleNameArr=[];
    for (let name of data) {
        if (name.length === 2) {
            middleName[name]=name[1];
            middleNameArr.push(name[1]);
        } else if (name.length === 4) {
            middleName[name]=name[2];
            middleNameArr.push(name[2]);
        } else {
            middleName[name]=name[Math.trunc(name.length / 2)];
            middleNameArr.push(name[Math.trunc(name.length / 2)]);
        }
    }
    const middleNameCount = {};
    for (i=0; i<middleNameArr.length;i++) {
        middleNameCount[middleNameArr[i]]=0;
    }
    for (let word of middleNameArr) {
        if (middleNameCount.hasOwnProperty(word)) {
            middleNameCount[word]+=1;
        } 
    }
    let uniqueMiddleName = "";
    const entries = Object.entries(middleNameCount);
    for (const [key, val] of entries) {
        if (val === 1) {
            uniqueMiddleName = key;
        }
    }
    let uniqueName = "沒有";
    for (const [key, val] of Object.entries(middleName)) {
        if (val === uniqueMiddleName) {
            uniqueName = key;
        }
    }
    console.log(uniqueName);
}
console.log("==========TASK 3==========");
func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花 
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有 
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安