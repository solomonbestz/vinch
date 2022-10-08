
$('.owl-carousel').owlCarousel({
    loop:true,
    autoplay: true,
    autoplayHoverPause: true,
    autoplayTimeout: 1000,
    margin:5,
    responsiveClass:true,
    responsive:{
        0:{
            items:2.5,
        },
        600:{
            items:4,
        },
        1000:{
            items:4.5,
        }
    }
})

document.getElementById('make-payment').addEventListener('click', function(e){
    submitFormData()
})

var form = document.getElementById('form')
  form.addEventListener('submit', function(e){
    e.preventDefault()
    console.log("form submitted.....")
    document.getElementById('form-button').classList.add("hidden");
    document.getElementById('payment-info').classList.remove("hidden")
  })

function submitFormData(){
    console.log('Payment Button Clicked')
}


