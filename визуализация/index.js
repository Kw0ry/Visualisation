const popBarId = $("#pop");


const popBar = new Chart(popBarId, {
    type: 'bar',
    data: {
        labels: names,
        datasets: [
            {
                label: 'course',
                data: values,
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderWidth: 1,
                borderColor: 'rgba(255, 99, 132, 1)'
            },
        ]
    },

})
