function unique(value, index, array) {
    return array.indexOf(value) === index;
}

function main() {
    // write your code here.
    // call functions `nextString`, `nextFloat` and `nextInt` 
    // to read the next token of input (ignoring whitespace)
    // Alternatively, you can create your own input parser functions
    // use console.log() to write to stdout

    const N = nextInt();
    const M = nextInt()
    var S = []
    var sCopy = []
    for (let i = 0; i < M; i++) {
        let str = nextString();
        sCopy.push(...str.split(''))
        S.push(str)
    }

    console.log(sCopy.filter(unique))
    const modulus = 998244353;

    function generateAllPossibilities(N, letters) {
        const allStrings = [];
        const space = 'abcdefghijklmnopqrstuvwxyz'

        const stack = [];
        stack.push(['', N]);

        while (stack.length > 0) {
            const [currentString, length] = stack.pop();

            if (length === 0) {
               // console.log('length is 0, i\'ve been told to print this ', currentString)
                allStrings.push(currentString);
            } else {
                console.log('length is not 0, i\'ve been told to print this ', currentString)
                for (let i = 0; i < space.length; i++) {
                    stack.push([currentString + space[i], length - 1]);
                }
            }
        }
        console.log(allStrings)
        return allStrings;
    }

    /**
     * matches substrings using regex and returns the count
     * @param {string} string the full string
     * @param {string} substrings partial string to look for
     * @returns {object} the count in which substring occurs in string
     */
    function countSubstrings(string, substrings) {
        const counts = {};
        substrings.forEach(someString => {
            counts[someString] = (string.match(new RegExp(someString, 'g')) || []).length;
        });
        return counts;
    }

    /**
    * Calculates the power of a number with the given base and exponent, considering a modulus.
    * @param {number} base - base number.
    * @param {number} exponent - exponent to raise the base by.
    * @param {number} modulus - modulus for the operation.
    * @returns {number} result of base raised to the power of the exponent, modulo global modulo.
    */
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

    const possibilitySpace = generateAllPossibilities(N, sCopy);

    let totalPower = 0;
    for (let i = 0; i < possibilitySpace.length; i++) {
        const string = possibilitySpace[i];
        const counts = countSubstrings(string, S);
        let totalCount = Object.values(counts).reduce((acc, cur) => acc + cur, 0);
        let power = calculatePower(2, totalCount);

        totalPower = (totalPower + power) % modulus;
    }
    console.log(totalPower)
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