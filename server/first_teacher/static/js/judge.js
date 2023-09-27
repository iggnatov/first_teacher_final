let groupNumber = 0;

var judgeApp = new Vue({
    el: '#judgedata',
    data: {
        judge: {},
    },
    created: function () {
        const vm = this;
        const personal = document.location.search.substring(1);
        console.log(personal);
        axios.get('~/judge?' + personal)
            .then(function (response) {
                vm.judge = response.data;
                console.log(response.data);
                groupNumber = vm.judge.group_number;
                console.log(groupNumber);

                // GET PARTICIPANTS 
                var participantApp = new Vue({
                    el: '#participants',
                    data: {
                        participants: [],
                        criterias: [],
                        scores: [],
                    },
                    created: function () {
                        const vp = this;
                        axios.get('/participants?' + 'group_number=' + groupNumber)
                            .then(function (response) {
                                vp.participants = response.data;
                                console.log(response.data);
                                console.log('participants', vp.participants[0].id);

                                axios.get('/criterias?' + 'tour=1')
                                    .then(function (response) {
                                        vp.criterias = response.data;
                                        console.log('criterisas', response.data);


                                    });

                                axios.get('/get_votes?' + personal)
                                    .then(function (response) {
                                        vp.scores = response.data;
                                        console.log('scores', response.data);

                                        function putValue() {
                                            for (let i = 0; i < 15; i++) {
                                                let elem = document.getElementById('result' + vp.participants[i].id);
                                                // console.log('elem', elem);
                                                for (let j = 0; j < 15; j++) {
                                                    if (vp.participants[i].id == vp.scores[i].participant) {
                                                        elem.innerHTML = vp.scores[i].score;
                                                    }
                                                }
                                            }
                                        };
                                        putValue();


                                    });


                            })
                    },


                    updated: function () {
                        let buttons = [];



                        // if (document.getElementById("criteria_21_1") !== null) {
                        //     criteria_21_1.oninput = function () {
                        //         valueCriteria_21_1.innerHTML = criteria_21_1.value;
                        //         pre_result_21.innerHTML = getResult21();
                        //     };

                        // };

                        // if (document.getElementById("criteria_21_2") !== null) {
                        //     criteria_21_2.oninput = function () {
                        //         valueCriteria_21_2.innerHTML = criteria_21_2.value;
                        //         pre_result_21.innerHTML = getResult21();
                        //     };

                        // };

                        // function getResult21() {
                        //     return Number(criteria_21_1.value) + Number(criteria_21_2.value);
                        // };
                        let ranges = [];
                        for (let i = 0; i < 31; i++) {
                            let ranges_criterias = [];
                            // let ranges_value_criterias = [];
                            for (let j = 1; j < 6; j++) {
                                need_id_string = "criteria_" + i + '_' + j;
                                need_value_id_string = "valueCriteria_" + i + '_' + j;
                                if (document.getElementById(need_id_string) !== null) {
                                    console.log('need_id_string', need_id_string);
                                    ranges_criterias[j] = document.getElementById(need_id_string);
                                    // ranges_value_criterias[j] = document.getElementById(need_value_id_string);
                                    console.log('ranges[i][j]', document.getElementById(need_id_string), document.getElementById(need_value_id_string));
                                    // need_id_string.oninput = function () {
                                    //     console.log('hi')
                                    //     need_value_id_string.innerHTML = need_id_string.value;
                                    //     // pre_result_21.innerHTML = getResult21();
                                    // };
                                    // function_body_string = "function () { " + need_value_id_string + ".innerHTML = " + need_id_string + ".value;};";
                                    function_body_string = need_value_id_string + ".innerHTML = " + need_id_string + ".value;";
                                    function_body = function_body_string;
                                    ranges_criterias[j].setAttribute("oninput", function_body);
                                }
                            };
                        };


                        for (let i = 0; i < 31; i++) {
                            need_id_string = "button" + i;

                            // console.log(need_id_string);
                            if (document.getElementById(need_id_string) !== null) {
                                buttons[i] = document.getElementById(need_id_string);
                                // console.log(need_id_string, buttons[i]);
                                flush_collapse_string = "#flush-collapse" + i;
                                buttons[i].setAttribute("data-bs-target", flush_collapse_string);
                                buttons[i].setAttribute("aria-controls", flush_collapse_string);
                            };


                        };
                        // for (let i = 0; i < 31; i++) {
                        //     for (let j = 1; j < 6; j++) {
                        //         ranges[i][j]
                        //         need_id_range = "criteria_" + i + '_' + j;
                        //         if (document.getElementById(need_id_range) !== null) {
                        //             console.log(need_id_range);
                        //             ranges[i][j] = document.getElementById(need_id_range);
                        //         };

                        //     };

                        // };
                    },

                });

            })
    },



});



// criteria_21_1.oninput = function () {
//     valueCriteria_21_1.innerHTML = criteria_21_1.value;
//     // result1.innerHTML = getResult1();
// };


// axios.get('/get_votes?' + 'jid=' + personal)
//     .then(function (response) {
//         vp.criterias = response.data;
//         console.log(response.data);

//     })