let rowtop = document.querySelector("#row_top");

// rowtop.addEventListener('click', () => {
//     alert("No mames los meros top");
// });

$('#row_top').slick({
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    arrows: false,
    dots: true
});