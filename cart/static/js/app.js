
function calculateSingleItemPrice(e) {
  if (e == 'potatoes'){
    var itemQuantity = document.getElementById("potatoQty");
    var itemPrice = document.getElementById("potatoPrice");
    var totalId = 'potatoTotal';
  }

  if (e == 'carrots'){
    var itemQuantity = document.getElementById("carrotQty");
    var itemPrice = document.getElementById("carrotPrice");
    var totalId = 'carrotTotal';
  }

  if (e == 'onions'){
    var itemQuantity = document.getElementById("onionQty");
    var itemPrice = document.getElementById("onionPrice");
    var totalId = 'onionTotal';
  }
  
  var itemPrice = parseFloat(itemPrice.value) || 0;
  var itemQuantity = parseFloat(itemQuantity.value) || 0;
  var totalPrice = itemPrice * itemQuantity || 0;

  document.getElementById(totalId).value = totalPrice;
  calculateSubTotal();
}

function calculateSubTotal(){
  var  potatoTotal = parseFloat(document.getElementById("potatoTotal").value) || 0;
  var  carrotTotal = parseFloat(document.getElementById("carrotTotal").value) || 0;
  var  onionTotal = parseFloat(document.getElementById("onionTotal").value) || 0;

  var grandTotal = potatoTotal + carrotTotal + onionTotal;
  document.getElementById("total").value = grandTotal;

}
