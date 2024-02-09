
        var config = {
            type: 'bar',
            data: {
                datasets: [{
                    data: {{ data|safe }},
                    backgroundColor: [
                        'red', 'orange', 'blue', 'yellow', 'green'
                    ],
                    label: 'Label'
                }],
                labels: {{ labels|safe }}
            },
            options: {
                responsive: true
            }
        };

        document.addEventListener('DOMContentLoaded', function () {
            var ctx = document.getElementById('myChart').getContext('2d');
            var myChart = new Chart(ctx, config);
        });

