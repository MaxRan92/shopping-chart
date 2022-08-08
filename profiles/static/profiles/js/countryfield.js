/* jshint esversion: 11, jquery: true */
let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').attr('style', 'color: #aab7c4 !important');
}
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).attr('style', 'color: #aab7c4 !important');
    } else {
        $(this).attr('style', 'color: #ffffff');
    }
});