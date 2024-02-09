
        $(document).ready(function () {
    // Gestionnaire d'événement pour le clic sur le bouton d'export
    $('#exportButton').click(function () {
        var numberOfRows = $('#numberOfRows').val();

        // Effectuer une requête AJAX vers votre vue Django pour déclencher l'export
        $.ajax({
            url: '/api/collecte',
            type: 'GET',
            data: { 'numberOfRows': numberOfRows },
            success: function (response) {
                // Créer un lien de téléchargement et le cliquer pour télécharger le fichier
                var downloadLink = document.createElement('a');
                downloadLink.href = 'data:text/csv;charset=utf-8,' + encodeURIComponent(response);
                downloadLink.download = 'collectes.csv';
                document.body.appendChild(downloadLink);
                downloadLink.click();
                document.body.removeChild(downloadLink);

                // Afficher le message de succès
                $('#exportMessage').text('Export CSV réussi !');
            },
            error: function (error) {
                // Afficher le message d'erreur
                $('#exportMessage').text('Erreur lors de l\'export des données : ' + error.statusText);
            }
        });
    });
});
