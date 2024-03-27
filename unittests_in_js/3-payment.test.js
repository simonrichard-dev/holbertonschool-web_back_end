const sinon = require('sinon');
const expect = require('chai').expect;
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('Test for sendPaymentRequestToApi', function() {
    it('Test the usage of Utilis.calculateNumber fonction', function() {
        const spy = sinon.spy(Utils, 'calculateNumber');
        sendPaymentRequestToApi(100, 20);

        expect(spy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
        expect(spy.returnValues[0]).to.equal(120);
        spy.restore();
    });
});
