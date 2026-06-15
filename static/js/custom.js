function sendArticleComment(articleId) {
    var comment = $('#commentText').val();
    var parentId = $('#parent_id').val()
    $.get('/articles/add-article-comment', {
        article_comment: comment,
        article_id: articleId,
        parent_id: parentId
    }).then(res => {
            console.log(res);
            $('#comments_area').html(res);
            $('#commentText').val('');
            $('#parent_id').val('');
            if (parentId !== '' && parentId !== null) {
                $('html, body').animate({
                    scrollTop: $('#comment_single_box_' + parentId).offset().top
                }, 1000);
            } else {
                $('html, body').animate({
                    scrollTop: $('#comments_area').offset().top
                }, 1000);
            }
        }
    );
}



function fillParentId(parentId) {
    $('#parent_id').val(parentId);
    $('html, body').animate({
        scrollTop: $('#comment_form').offset().top
    }, 1000);
}

function filterProducts() {
    const filter_price = $('#sl2').val();
    const start_price = filter_price.split(',')[0];
    const end_price = filter_price.split(',')[1];
    $('#start_price').val(start_price);
    $('#end_price').val(end_price);
    $('#filter_form').submit()
}

function fillPage(page) {
    $('#page').val(page);
    $('#filter_form').submit();
}


function showLargeImage(imageSrc) {
    $('#main_image').attr('src', imageSrc);
    $('#show_large_image_modal').attr('href', imageSrc);
}

function addProductToOrder(productId) {
    const productCount = $('#product-count').val();
    $.get('/order/add-to-order?product_id=' + productId + '&count=' + productCount).then(res => {
        Swal.fire({
            title: "اعلان",
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: "#3085d6",

            confirmButtonText: res.confirm_button_text
        }).then(confirm => {
            if (res.status === 'not_auth' && res.isConfirmed) {
                window.location.href = '/login';
            }
        });
    });
}

function removeOrderDetail(detailId) {
    $.get('/user/remove-order-detail?detail_id=' + detailId).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    })
}

function changeOrderDetailCount(detailId , state){
        $.get('/user/change-order-detail?detail_id=' + detailId + '&state=' + state).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    })
}