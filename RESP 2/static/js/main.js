

var grafico_PM_25, grafico_PM_10;

var canvas_MP_25 = document.getElementById("MP25").getContext("2d");
var canvas_MP_10 = document.getElementById("MP10").getContext("2d");

const TimeLapses = 5000;



var data = [
    MP_25 = {
        label: "MP 2.5 ug/m3",
        data: [],
        lineTension: 0,
        borderColor: 'green',
        steppedLine: true
    },
    MP_10 = {
        label: "MP 10 ug/m3",
        data: [],
        lineTension: 0,
        borderColor: 'red',
        steppedLine: true
    }
]


var data_set_25 = {
    labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
    datasets: [data[0]]
};

var data_set_10 = {
    labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
    datasets: [data[1]]
};

const get_Data = (resp) => {
    data[0].data = resp[25];
    data[1].data = resp[10];
    data_set_25.datasets = [data[0]];
    data_set_10.datasets = [data[1]];
}


const GetJson = () => {
    $.getJSON("http://127.0.0.1:4000/get_data", function (data) {
        get_Data(data);
    });
};


const Grafico_PM_25 = () => {
    grafico_PM_25 = new Chart(canvas_MP_25, {
        type: 'line',
        data: data_set_25,
        options: { legend: { display: true, position: 'top', labels: { boxWidth: 75, fontColor: 'black' } } }
    });
    grafico_PM_25.render();
};


const Grafico_PM_10 = () => {
    grafico_PM_10 = new Chart(canvas_MP_10, {
        type: 'line',
        data: data_set_10,
        options: { legend: { display: true, position: 'top', labels: { boxWidth: 75, fontColor: 'black' } } }
    });
    grafico_PM_10.render();
};


const main = () => {
    GetJson();
    Grafico_PM_25();
    Grafico_PM_10();
    grafico_PM_25.render();
    grafico_PM_10.render();

};
setInterval(main, TimeLapses);