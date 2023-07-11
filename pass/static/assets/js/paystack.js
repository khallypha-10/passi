var paymentForm = document.getElementById('paymentForm');
paymentForm.addEventListener('submit', payWithPaystack, false);
function payWithPaystack() {
  var handler = PaystackPop.setup({
    key: '{{ paystack_pub_key }}', // Replace with your public key
    email: document.getElementById('email-address').value,
    amount: document.getElementById('amount').value * 100, // the amount value is multiplied by 100 to convert to the lowest currency unit
    currency: 'NGN', // Use GHS for Ghana Cedis or USD for US Dollars
    ref: 'ref', // Replace with a reference you generated
    callback: function(response) {
      //this happens after the payment is completed successfully
      var reference = response.reference;
      alert('Payment complete! Reference: ' + reference);
      window.location.href = "{% url 'verify_payment' payment.ref %}";
      // Make an AJAX call to your server with the reference to verify the transaction
    },
    onClose: function() {
      alert('Transaction was not completed, window closed.');
    },
  });
  handler.openIframe();
}

