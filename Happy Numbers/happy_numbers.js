var input_stdin = "";
var input_cursor = 0;

const split_and_square = (number, calls) => {
    calls++;
    if (number === 1) {
        return true;
    } else if (calls > 10) {
        return false;
    } else {
        let total = 0;
        for (let i = 0; i < `${number}`.length; i++) {
            const num = Number(`${number}`[i]);
            const num2 = num * num;
            total += num2;
        }
        return split_and_square(total, calls);
    }
}

const main = () => {
    let start_number = nextInt();
    let end_number = nextInt();

    let happy_nums = [];
    for (let i = start_number; i <= end_number; i++) {
        if (split_and_square(i, 0)) {
            happy_nums.push(i);
        }
    }

    console.log(happy_nums.length);
    //console.log(happy_nums);
}

process.stdin.resume();
//process.stdin.setEncoding('ascii');
process.stdin.on('data', function (data) {
    input_stdin += data;
});
process.stdin.on('end', function () { main(); });

// default parsers for JS.
function nextInt() {
    return parseInt(nextString());
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

function isWhitespace(character) {
    return ' \t\n\r\v'.indexOf(character) > -1;
}

function clearWhitespaces() {
    while (input_cursor < input_stdin.length && isWhitespace(input_stdin[input_cursor])) {
        // ignore the next whitespace character
        input_cursor += 1;
    }
}