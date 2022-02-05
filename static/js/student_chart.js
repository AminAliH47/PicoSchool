var ctx = document.getElementById("studentChart");
var present = document.getElementById("stuPresent").value;
var absent = document.getElementById("stuAbsent").value;
var plate = document.getElementById("stuPlate").value;
var studentChart = new Chart(ctx, {
    type: "doughnut",
    data: {
        labels: ["غایب", "حاضر", "حاضر (با تاخیر)"],
        datasets: [
            {
                data: [absent, present, plate],
                backgroundColor: ["#dc3545", "#28a745",'#ffc107'],
            },
        ],
    },
    options: {
        responsive: true,
        scales: {
            xAxes: [
                {
                    gridLines: {
                        display: false,
                    },
                },
            ],
            yAxes: [
                {
                    gridLines: {
                        display: false,
                    },
                },
            ],
        },
    },
});
