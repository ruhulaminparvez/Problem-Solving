const romanToInt = function (s) {
    const romanMap = new Map([
        ['I', 1],
        ['V', 5],
        ['X', 10],
        ['L', 50],
        ['C', 100],
        ['D', 500],
        ['M', 1000]
    ]);

    let ans = 0;
    for (let i = 0; i < s.length; i++) {
        const curr = romanMap.get(s[i]);
        const next = romanMap.get(s[i + 1]);
        if (curr < next) {
            ans -= curr;
        } else {
            ans += curr;
        }
    }
    return ans;
};

// test case
console.log(romanToInt('III')); // 3
console.log(romanToInt('IV')); // 4
console.log(romanToInt('IX')); // 9
console.log(romanToInt('LVIII')); // 58