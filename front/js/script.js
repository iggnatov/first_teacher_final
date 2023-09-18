criteria11.oninput = function () {
    valueCriteria11.innerHTML = criteria11.value;
    result1.innerHTML = getResult1();
};

criteria12.oninput = function () {
    valueCriteria12.innerHTML = criteria12.value;
    result1.innerHTML = getResult1();
};

criteria13.oninput = function () {
    valueCriteria13.innerHTML = criteria13.value;
    result1.innerHTML = getResult1();
};

criteria14.oninput = function () {
    valueCriteria14.innerHTML = criteria14.value;
    result1.innerHTML = getResult1();
};

criteria15.oninput = function () {
    valueCriteria15.innerHTML = criteria15.value;
    result1.innerHTML = getResult1();
};

function getResult1() {
    return Number(criteria11.value) + Number(criteria12.value) + Number(criteria13.value) + Number(criteria14.value) + Number(criteria15.value);
};





criteria21.oninput = function () {
    valueCriteria21.innerHTML = criteria21.value;
    result2.innerHTML = getResult2();
};

criteria22.oninput = function () {
    valueCriteria22.innerHTML = criteria22.value;
    result2.innerHTML = getResult2();
};

criteria23.oninput = function () {
    valueCriteria23.innerHTML = criteria23.value;
    result2.innerHTML = getResult2();
};

criteria24.oninput = function () {
    valueCriteria24.innerHTML = criteria24.value;
    result2.innerHTML = getResult2();
};

criteria25.oninput = function () {
    valueCriteria25.innerHTML = criteria25.value;
    result2.innerHTML = getResult2();
};

function getResult2() {
    return Number(criteria21.value) + Number(criteria22.value) + Number(criteria23.value) + Number(criteria24.value) + Number(criteria25.value);
};