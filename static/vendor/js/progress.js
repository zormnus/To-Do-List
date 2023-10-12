function getDataAndCreateChart(url, chartType) {
    const request = new XMLHttpRequest();
    request.open('GET', url, true);
    request.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            const parsedData = JSON.parse(request.responseText);
            createChart(parsedData, chartType);
        }
    };
    request.send();
}

function createChart(data, chartType) {
    const labels = [];
    let labelsData = [];
    for (const [key, value] of Object.entries(data)) {
        labels.push(key);
        labelsData.push(value);
    }
    labels.reverse();
    labelsData.reverse();

    const ctx = document.getElementById(`${chartType}Chart`).getContext('2d');
    const chartData = {
      labels: labels,
      datasets: [{
        label: 'Ваша активность',
        data: labelsData,
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        backgroundColor: chartType === 'pie' ? [
            'rgb(255, 99, 132)',
            'rgb(54, 162, 235)',
            'rgb(255, 205, 86)'
        ]: [],
        tension: 0.1
      }]
    };
    const chart = new Chart(ctx, {
        type: chartType,
        data: chartData,
    });
}

getDataAndCreateChart('http://127.0.0.1:8000/todo/tasks/recent_stats', 'line');
getDataAndCreateChart('http://127.0.0.1:8000/todo/tasks/fav_cats', 'pie');
