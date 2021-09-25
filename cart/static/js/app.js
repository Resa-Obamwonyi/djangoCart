
function calculateSingleItemPrice() {
  var itemQuantity = document.getElementById("potatoQty");
  var itemPrice = document.getElementById("potatoPrice");
  var itemPrice = parseFloat(itemPrice.value);
  var itemQuantity = parseFloat(itemQuantity.value);
  var totalPrice = itemPrice * itemQuantity;
  document.getElementById("singleItemTotal").value = totalPrice;
}

function calculateSubTotal(){
  var grandTotal = 0.0
  var table = document.getElementById('cart-table');
    for (var r = 0, n = table.rows.length; r < n; r++) {
        for (var c = 0, m = table.rows[r].cells.length; c < m; c++) {
            // return table.rows[r].cells[c].innerHTML;
            var singleItemTotal = document.getElementById("singleItemTotal").value;
            grandTotal += singleItemTotal;
        }
    }
    document.getElementById("total").value = totalPrice;
}
