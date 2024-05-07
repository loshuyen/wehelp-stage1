let hourOccupied={};
function book(consultants, hour, duration, criteria){
    requestHour=new Set();
    for (let i = hour; i < hour+duration; i++) {
        requestHour.add(i);
    }
    for (let i=0; i < consultants.length; i++) {
        if (!hourOccupied.hasOwnProperty(consultants[i].name)) {
            hourOccupied[consultants[i].name] = new Set();
        }
    }
    let candidates = new Set();
    for (let key in hourOccupied){
        const intersect = new Set([...requestHour].filter(value => hourOccupied[key].has(value)));
        if (intersect.size === 0) {
            candidates.add(key);
        }
    }
    if (candidates.size === 0) {
        console.log("No Service");
        return;
    }
    if (criteria === "rate") {
        let candidatesRate={};
        for (let candidate of candidates) {
            for (let consultant of consultants) {
                if (consultant.name === candidate) {
                    candidatesRate[candidate] = consultant.rate;
                }
            }
        }
        let rateArr = [];
        for ( let i in candidatesRate) {
            rateArr.push(candidatesRate[i]);
          }
        for ( let key in candidatesRate) {
            if (candidatesRate[key] === Math.max(...rateArr)) {
                console.log(key);
                hourOccupied[key] = new Set([...hourOccupied[key], ...requestHour]);
            }
        }
    }
    if (criteria === "price") {
        let candidatesPrice={};
        for (let candidate of candidates) {
            for (let consultant of consultants) {
                if (consultant.name === candidate) {
                    candidatesPrice[candidate] = consultant.price;
                }
            }
        }
        let priceArr = [];
        for ( let i in candidatesPrice) {
            priceArr.push(candidatesPrice[i]);
          }
        for ( let key in candidatesPrice) {
            if (candidatesPrice[key] === Math.min(...priceArr)) {
                console.log(key);
                hourOccupied[key] = new Set([...hourOccupied[key], ...requestHour]);
            }
        }
    }
}
const consultants=[
    {"name":"John", "rate":4.5, "price":1000}, {"name":"Bob", "rate":3, "price":1200}, {"name":"Jenny", "rate":3.8, "price":800}
];
console.log("==========TASK 2==========");
book(consultants, 15, 1, "price"); // Jenny 
book(consultants, 11, 2, "price"); // Jenny 
book(consultants, 10, 2, "price"); // John 
book(consultants, 20, 2, "rate"); // John 
book(consultants, 11, 1, "rate"); // Bob 
book(consultants, 11, 2, "rate"); // No Service 
book(consultants, 14, 3, "price"); // John