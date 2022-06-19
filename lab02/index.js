function display(val) {
    document.getElementById('result').value += val;
    return val;
}

function solve() {
    let str = document.getElementById('result').value;
    if (str.includes("+")) {
        let allValue = document.getElementById('result').value;
        let resultVal = eval(allValue);
        document.getElementById('result').value = resultVal;
        return resultVal;
    }
    else if (str.includes("-")) {
        let allValue = document.getElementById('result').value;
        let resultVal = eval(allValue);
        document.getElementById('result').value = resultVal;
        return resultVal;
    }
    else if (str.includes("*")) {
        let allValue = document.getElementById('result').value;
        let resultVal = eval(allValue);
        document.getElementById('result').value = resultVal;
        return resultVal;
    }
    else if (str.includes("/")) {
        let allValue = document.getElementById('result').value;
        let resultVal = eval(allValue);
        document.getElementById('result').value = resultVal;
        return resultVal;
    }
    else if (str.includes("^")) {
        let resultVal = Math.pow(str.substring(0, str.indexOf('^')), str.substring(str.indexOf('^') + 1));
        document.getElementById('result').value = resultVal;
        return resultVal;
    }
    else if (str.includes("sin")) {
        let allValue = document.getElementById('result').value;
        let n = 3;
        allValue = '' + allValue.slice(n);
        let resultVal = Math.sin(allValue);
        document.getElementById('result').value = resultVal;
        return resultVal;
    }
    else if (str.includes("cos")) {
        let allValue = document.getElementById('result').value;
        let n = 3;
        allValue = '' + allValue.slice(n);
        let resultVal = Math.cos(allValue);
        document.getElementById('result').value = resultVal;
        return resultVal;
    }
    else if (str.includes("tan")) {
        let allValue = document.getElementById('result').value;
        let n = 3;
        allValue = '' + allValue.slice(n);
        let resultVal = Math.tan(allValue);
        document.getElementById('result').value = resultVal;
        return resultVal;
    }
    else { 
        let allValue = document.getElementById('result').value;
        allValue = allValue.replace(str[0],"");
        let resultVal = Math.sqrt(allValue);
        document.getElementById('result').value = resultVal;
        return resultVal;
    }
}

function clearScreen() {
    document.getElementById('result').value = '';
}