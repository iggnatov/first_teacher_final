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
                    },
                    created: function () {
                        const vp = this;
                        axios.get('/participants?' + 'group_number=' + groupNumber)
                            .then(function (response) {
                                vp.participants = response.data;
                                console.log(response.data);

                                axios.get('/criterias?' + 'tour=1')
                                    .then(function (response) {
                                        vp.criterias = response.data;
                                        console.log(response.data);
                                    })
                            })
                    }
                });
            })
    }
});
