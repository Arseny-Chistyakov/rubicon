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

    // $('.card_add_basket').on('click','button[type="button"]',function (){
    //
    // let t_href = event.target;
    // console.log(t_href.value);
    //
    // $.ajax(
    //     {
    //         url:"/baskets/basket_add/" + t_href.value + "/",
    //         success: function (data){
    //             $('.card_add_basket').html(data.result)
    //         }
    //     }
    // )
    //
    // })
}