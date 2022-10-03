window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        let t_href = event.target;
        $.ajax(
            {
                url: "/baskets/basket_edit/" + t_href.name + "/" + t_href.value + "/",
                success: function (data) {
                    $('.basket_list').html(data.result)
                }
            }
        )
    })

    $('.card-footer').on('click', 'button[type="button"]', function () {
        let t_href = event.target.value;
        console.log(t_href);
        $.ajax(
            {
                url: "/baskets/basket_add/" + t_href + "/",
                success: function (data) {
                    $('.card-footer').html(data.result)
                    alert('Товар добавлен в корзину!')
                },
            });
    })
}