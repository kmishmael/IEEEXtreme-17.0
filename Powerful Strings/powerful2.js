function unique(value, index, array) {
    return array.indexOf(value) === index;
}

function main() {
    // write your code here.
    // call functions `nextString`, `nextFloat`, and `nextInt`
    // to read the next token of input (ignoring whitespace)
    // Alternatively, you can create your own input parser functions
    // use console.log() to write to stdout

    const N = nextInt();
    const M = nextInt();
    const substrings = [];
    

    for (let i = 0; i < M; i++) {
        const str = nextString();
        substrings.push(str);
    }

    const modulus = 998244353;

    function countSubstrings(string, substrings) {
        let totalCount = 0;
        substrings.forEach(sub => {
            let index = -1;
            while ((index = string.indexOf(sub, index + 1)) !== -1) {
                totalCount++;
            }
        });
        return totalCount;
    }

    function calculatePower(base, exponent) {
        if (modulus === 1) return 0;
        let res = 1;
        base = base % modulus;
        while (exponent > 0) {
            if (exponent % 2 === 1) {
                res = (res * base) % modulus;
            }
            exponent = exponent >> 1; // divide by 2
            base = (base * base) % modulus;
        }
        return res;
    }

    let totalPower = 0;
    const space = 'abcdefghijklmnopqrstuvwxyz';

    const stack = [];
    stack.push(['', N]);

    while (stack.length > 0) {
        const [currentString, length] = stack.pop();

        if (length === 0) {
            const totalCount = countSubstrings(currentString, substrings);
            const power = calculatePower(2, totalCount);
            totalPower = (totalPower + power) % modulus;
        } else {
            for (let i = 0; i < space.length; i++) {
                stack.push([currentString + space[i], length - 1]);
            }
        }
    }

    console.log(totalPower);
    return totalPower;
}


// default parsers for JS.
function nextInt() {
    return parseInt(nextString());
}

function nextFloat() {
    return parseFloat(nextString());
}

function nextString() {
    var next_string = "";
    clearWhitespaces();
    while (input_cursor < input_stdin.length && !isWhitespace(input_stdin[input_cursor])) {
        next_string += input_stdin[input_cursor];
        input_cursor += 1;
    }
    return next_string;
}

function nextChar() {
    clearWhitespaces();
    if (input_cursor < input_stdin.length) {
        return input_stdin[input_cursor++];
    } else {
        return '\0';
    }
}

process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_cursor = 0;
process.stdin.on('data', function (data) { input_stdin += data; });
process.stdin.on('end', function () { main(); });

function isWhitespace(character) {
    return ' \t\n\r\v'.indexOf(character) > -1;
}

function clearWhitespaces() {
    while (input_cursor < input_stdin.length && isWhitespace(input_stdin[input_cursor])) {
        // ignore the next whitespace character
        input_cursor += 1;
    }
}