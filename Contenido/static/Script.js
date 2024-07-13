$(document).ready(function() {
    console.log('ready')
    $('.card').on('click', function() {
        var bookId = $(this).attr('id');
        $.get(`https://www.googleapis.com/books/v1/volumes/${bookId}`, function(data) {
            $('#bookTitle').text(data.volumeInfo.title);
            $('#bookDescription').html(data.volumeInfo.description);
            $('#bookAuthors').text('Autores: ' + data.volumeInfo.authors.join(', '));
            $('#bookCover').attr('src', data.volumeInfo.imageLinks.medium);

            $('#bookModal').modal('show');
        })
    })
}) 