const sinon = require('sinon');
const expect = require('chai').expect;
const sendPaymentRequestToApi = require('./5-payment');

describe('test hooks on sendPaymentRequestToApi', () => {
    let a;
    let b;
    let spyConsole;

    beforeEach(function() {
        spyConsole = sinon.spy(console, 'log');
    });

    afterEach(function() {
        spyConsole.restore();
    })

    it('Uses a stub for Utils.calculateNumber', () => {
        a = 100;
        b = 20;
        sendPaymentRequestToApi(a, b);

        a = 10;
        b = 10;
        sendPaymentRequestToApi(a, b);

        expect(spyConsole.calledWithExactly(`The total is: ${a + b}`)).to.be.true;
  });
});
