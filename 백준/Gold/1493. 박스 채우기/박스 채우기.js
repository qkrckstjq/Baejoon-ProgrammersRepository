var input = require("fs").readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n");
var _a = input[0].split(' ').map(function (el) { return Number(el); }), len = _a[0], wid = _a[1], hei = _a[2];
var cube = input.slice(2).map(function (el) { return el.split(' ').map(function (item, idx) { return idx === 0 ? Number(Math.pow(2, item)) : Number(item); }); });
var answer = 0;
var NoMore;
var stack = [];
stack.push(len, wid, hei);
while (stack.length !== 0) {
    var l = stack.pop(), w = stack.pop(), h = stack.pop();
    NoMore = true;
    var Max = Math.min(l, w, h);
    for (var i = cube.length - 1; i >= 0; i--) {
        if (cube[i][0] <= Max && cube[i][1] !== 0) {
            answer++;
            cube[i][1]--;
            Max = cube[i][0];
            NoMore = false;
            break;
        }
    }
    if (NoMore)
        break;
    if (w - Max !== 0) {
        stack.push(Max, w - Max, Max);
    }
    if (l - Max !== 0) {
        stack.push(l - Max, w, Max);
    }
    if (h - Max !== 0) {
        stack.push(l, w, h - Max);
    }
}
console.log(NoMore ? -1 : answer);
