var handles = ["SELECT Sub-Division","Bardhaman Sadar North", "Bardhaman Sadar South", "Kalna", "Katwa"];

$(function() {
  var options = '';
  for (var i = 0; i < handles.length; i++) {
      options += '<option value="' + handles[i] + '">' + handles[i] + '</option>';
  }
  $('#listBox').html(options);
});
function selct_block($val)
{
    if($val=='SELECT Sub-Division') {
   var options = '';
  $('#secondlist').html(options);
  }
 if($val=='Bardhaman Sadar North') {
   var sadarnorth = ["Ausgram I","Ausgram II","Bhatar","Galsi I","Galsi II", "Burdwan I", "Burdwan II"];
   $(function() {
  var options = '';
  for (var i = 0; i < sadarnorth.length; i++) {
      options += '<option value="' + sadarnorth[i] + '">' + sadarnorth[i] + '</option>';
  } 
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Bardhaman Sadar South') {
    var sadarsouth = ["Memari I", "Memari II", "Jamalpur", "Raina I", "Raina II", "Khandaghosh"];
   $(function() {
  var options = '';
  for (var i = 0; i < sadarsouth.length; i++) {
      options += '<option value="' + sadarsouth[i] + '">' + sadarsouth[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Kalna') {
    var kalna = ["Purbasthali I", "Purbasthali II", "Kalna I", "Kalna II", "Monteswar"];
   $(function() {
  var options = '';
  for (var i = 0; i < kalna.length; i++) {
      options += '<option value="' + kalna[i] + '">' + kalna[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Katwa') {
    var katwa = ["Mongalkote", "Ketugram I", "Ketugram II", "Katwa I", "Katwa II"];
   $(function() {
  var options = '';
  for (var i = 0; i < katwa.length; i++) {
      options += '<option value="' + katwa[i] + '">' + katwa[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
}