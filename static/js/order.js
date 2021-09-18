$(function(){
    $('.add_to_cart').click(function (){
       var product = $(this).data();
       addToCart(product.pid,product.img,product.product_name,product.product_price);
       window.location.href="Add_cart";
    });

    if ($('#cart-details').length) {
        displayCartDetails();
    }

    $('#cart-container').on('click', '.product-remove',function (){
        removeItem($(this).data('pid'));
    });
    $('#cart-container').on('change', '.input-product-qty',function (){
        updateItem($(this).data('pid'), $(this).val());
    });
});

function getCart(){
    return JSON.parse(localStorage.getItem('cartDetails') || "[]");
}
function addToCart(pid,img,product_name,product_price) {
    var cartIndex = getCartItemIndexByProduct(pid);
    if(cartIndex!=-1){
        return;
    }
    var cartDetails = getCart();
    cartDetails.push({
        pid,
        img,
        product_name,
        product_price,
        qty: 1
    });
    setCartToStorage(cartDetails);
}
function setCartToStorage(cartDetails){
    localStorage.setItem('cartDetails', JSON.stringify(cartDetails));
}

function removeItem(pid) {
    var cartDetails = getCart();
    var cartIndex = getCartItemIndexByProduct(pid);

    cartDetails.splice(cartIndex, 1);
    setCartToStorage(cartDetails);
    displayCartDetails();
}

function updateItem(pid, qty){
    var cartDetails = getCart();
    var cartIndex = getCartItemIndexByProduct(pid);

    cartDetails[cartIndex].qty = qty;
    setCartToStorage(cartDetails);
    displayCartDetails();
}

function getCartItemIndexByProduct(pid) {
    var cartDetails = getCart();
    return cartDetails.map(function(el){ return el.pid}).indexOf(pid);
}

function displayCartDetails() {
    var cartDetails = getCart();

    $('#cart-container').empty().html('');
    $('#checkout_total_amount').text(0);
    $('#checkout_total_item').text(0);
    if (!cartDetails.length){
        $('#cart-container').empty().html('<h3>No items are found</h3>');
        return;
    }

    var temp = $.trim($('#cart-details').html());
    var total_amount = 0;
    var total_qty = 0;
    var total_item_price;
    $.each(cartDetails, function (index, obj) {
        var x = temp.replace(/##product_name##/ig, obj.product_name);
        x = x.replace(/##img##/ig, obj.img);
        x = x.replace(/##product_price##/ig, obj.product_price);
        x = x.replace(/##qty##/ig, obj.qty);
        x = x.replace(/##pid##/ig, obj.pid);
        total_item_price = obj.qty * obj.product_price;
        total_qty += parseInt(obj.qty);
        total_amount += total_item_price;
        x = x.replace(/##total##/ig, total_item_price.toFixed(2));

        $('#cart-container').append(x);
    });

    $('#checkout_total_amount').text(total_amount.toFixed(2));
    $('#checkout_total_item').text(total_qty);
}
