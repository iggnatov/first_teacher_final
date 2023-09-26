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
                    }
                });
            })
    }
});



// axios.get('/get_votes?' + 'jid=' + personal)
//     .then(function (response) {
//         vp.criterias = response.data;
//         console.log(response.data);

//     })