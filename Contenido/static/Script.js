$(document).ready(function() {
    AOS.init();
    
    $('.card').on('click', function() {
        $('#bookCover').attr('src', this.querySelector('img').src);

        var bookId = $(this).attr('id');
        $.get(`https://www.googleapis.com/books/v1/volumes/${bookId}`, function(data) {
            $('#bookTitle').text(data.volumeInfo.title);
            $('#bookDescription').html(data.volumeInfo.description);
            $('#bookAuthors').html('<b>Autores</b>: ' + data.volumeInfo.authors.join(', '));

            $('#bookModal').modal('show');
        })
    })
}) 