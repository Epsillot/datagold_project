
        // Fonction pour initialiser le graphique avec Chart.js
        function initializeChart(labels, data) {
            var ctx = document.getElementById('myChart2').getContext('2d');

            var config2 = {
                type: 'bar',
                data: {
                    datasets: [{
                        data: data,
                        backgroundColor: [
                            'red', 'orange', 'blue', 'yellow', 'green'
                        ],
                        label: 'Dépense moyenne par panier'
                    }],
                    labels: labels
                },
                options: {
                    responsive: true
                }
            };

            var myChart2 = new Chart(ctx, config2);
        }

        // Fonction pour charger les données via AJAX
        $(document).ready(function () {
            $.ajax({
                url: '/graph_moyenne',
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    // Mettez à jour le contenu de la div avec les données renvoyées
                    // Vous pouvez utiliser ces données pour initialiser votre graphique
                    console.log('Données reçues :', data);

                    // Exemple de mise à jour de la div
                    $('#myChart2');

                    // Appeler la fonction pour initialiser le graphique avec Chart.js
                    initializeChart(data.labels, data.data);
                },
                error: function (error) {
                    console.log('Erreur lors du chargement des données :', error);
                }
            });
        });
