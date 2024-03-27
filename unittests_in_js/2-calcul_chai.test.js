// 2-calcul_chai.test.js
const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

//SUM
describe('Tests for SUM', function() {
    it('should return 6 when adding 1 and 3', function() {
        expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });
  
    it('should return 4 when adding 1 and PI', function() {
        expect(calculateNumber('SUM', 1, Math.PI)).to.equal(4);
    });

     it('should return undefined when missing first argument', () => {
        expect(calculateNumber('', -1, 3)).to.equal(undefined);
    })

    it('should return undefined if first argument not correct', () => {
        expect(calculateNumber('SEUM', -1, 3)).to.equal(undefined);
    })
});

//SUBSTRACT
describe('Tests for SUBSTRACT', function() {
    it('should return 6 when adding 1 and 3', function() {
        expect(calculateNumber('SUBSTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('should return -2 when substracting 1 and PI', function() {
        expect(calculateNumber('SUBSTRACT', 1, Math.PI)).to.equal(-2);
    });

    it('should return 4 when substracting 1 and -3', () => {
        expect(calculateNumber('SUBSTRACT', 1, -3)).to.equal(4);
    });

    it('should return -4 when substracting -1 and 3', () => {
        expect(calculateNumber('SUBSTRACT', -1, 3)).to.equal(-4);
    })
});

//DIVIDE
describe('Tests for DIVIDE', function() {

    it('Correctly returns 0.2 when dividing 1.4 by 4.5', () => {
        expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('Correctly returns Error when dividing by 0', () => {
        expect(calculateNumber('DIVIDE', 3, 0)).to.equal('Error');
    });
});
