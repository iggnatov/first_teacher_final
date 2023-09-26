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
                vm.judge = response.data
                console.log(response.data)
                groupNumber = vm.judge.group_number;
                console.log(groupNumber);

                var participantApp = new Vue({
                    el: '#participants',
                    data: {
                        participants: [],
                    },
                    created: function () {
                        const vp = this;
                        console.log(groupNumber);
                        // console.log('F', judgeApp);
                        axios.get('/participants?' + 'group_number=' + groupNumber)
                            .then(function (response) {
                                vp.participants = response.data
                                console.log(response.data)
                                console.log(groupNumber)
                            })
                    }
                });
            })
    }
});

