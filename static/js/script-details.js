$(function(){
    let queryParams = getUrlVars();

   $("a[data-shop_cat='"+queryParams.product+"']").addClass("active");
});