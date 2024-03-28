const sinon = require('sinon');
const expect = require('chai').expect;
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

describe('Test for sendPaymentRequestToApi with stub', function() {
    it('Test the usage of Utils.calculateNumber fonction', function() {
        const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
        const consoleLogSpy = sinon.spy(console,'log');

        sendPaymentRequestToApi(100, 20);

        expect(stub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
        expect(consoleLogSpy.calledOnceWithExactly('The total is: 10')).to.be.true;

        stub.restore();
        consoleLogSpy.restore();
    });
});
