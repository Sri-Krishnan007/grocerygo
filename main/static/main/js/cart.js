function addToCart(productId) {
    let quantity = document.getElementById('quantity').value;
    // AJAX call to add item to cart
    fetch('/cart/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}',
        },
        body: JSON.stringify({ product_id: productId, quantity: quantity })
    }).then(response => {
        if (response.ok) {
            alert('Item added to cart!');
        }
    });
}
