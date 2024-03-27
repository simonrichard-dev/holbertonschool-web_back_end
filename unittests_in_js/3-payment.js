const Utilis = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const total = Utilis.calculateNumber('SUM', totalAmount, totalShipping)
    console.log(`The total is: ${total}`);
}

module.exports = sendPaymentRequestToApi
