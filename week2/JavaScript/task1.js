function findAndPrint(messages, currentStation) {
  const stations = {
    'Songshan': 0,
    'Nanjing Sanmin': 1,
    'Taipei Arena': 2,
    'Nanjing Fuxing': 3,
    'Songjiang Nanjing': 4,
    'Zhongshan': 5,
    'Beimen': 6,
    'Ximen': 7,
    'Xiaonanmen': 8,
    'Chiang Kai-Shek Memorial Hall': 9,
    'Guting': 10,
    'Taipower Building': 11,
    'Gongguan': 12,
    'Wanlong': 13,
    'Jingmei': 14,
    'Dapinglin': 15,
    'Qizhang': 16,
    'Xindian City Hall': 17,
    'Xindian': 18,
    'Xiaobitan': 16,
  };
  let locations = {};
  for (let station in stations) {
    for (let name in messages) {
      if (messages[name].includes(station)) {
        locations[name] = stations[station];
      }
    }
  }
  const currentStationIndex = stations[currentStation];
  let distanceObj = {};
  for (let name in locations) {
    const d = Math.abs(locations[name] - currentStationIndex);
    if (
      currentStation === 'Xiaobitan' ||
      messages[name].includes('Xiaobitan')
    ) {
      distanceObj[name] = d + 1;
    } else {
      distanceObj[name] = d;
    }
  }
  let distanceArr = [];
  for (i in distanceObj) {
    distanceArr.push(distanceObj[i]);
  }
  for (key in distanceObj) {
    if (distanceObj[key] === Math.min(...distanceArr)) {
      console.log(key);
    }
  }
}
const messages = {
  Bob: "I'm at Ximen MRT station.",
  Mary: 'I have a drink near Jingmei MRT station.',
  Copper: 'I just saw a concert at Taipei Arena.',
  Leslie: "I'm at home near Xiaobitan station.",
  Vivian: "I'm at Xindian station waiting for you.",
};
console.log('==========TASK 1==========');
findAndPrint(messages, 'Wanlong'); // print Mary
findAndPrint(messages, 'Songshan'); // print Copper
findAndPrint(messages, 'Qizhang'); // print Leslie
findAndPrint(messages, 'Ximen'); // print Bob
findAndPrint(messages, 'Xindian City Hall'); // print Vivian
