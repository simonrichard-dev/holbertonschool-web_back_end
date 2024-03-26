// 1-calcul.test.js
const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {


    // SUM

  it('should return 4 when adding 1 and 3', function() {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
  });
  
  it('should return 4 when adding 1 and PI', function() {
    assert.strictEqual(calculateNumber('SUM', 1, Math.PI), 4);
  });

  it('should return 5 when adding 1 and 3.7', function() {
    assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
  });

  it('should return 5 when adding 1.2 and 3.7', function() {
    assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
  });

  it('should return 6 when adding 1.5 and 3.7', function() {
    assert.strictEqual(calculateNumber('SUM', 1.5, 3.7), 6);
  });

  it('should return -2 when adding 1 and -3', () => {
    assert.equal(calculateNumber('SUM', 1, -3), -2);
  });

  it('should return 2 when adding -1 and 3', () => {
    assert.equal(calculateNumber('SUM', -1, 3), 2);
  })

  it('should return undefined when missing first argument', () => {
    assert.equal(calculateNumber('', -1, 3), undefined);
  })

  it('should return undefined if first argument not correct', () => {
    assert.equal(calculateNumber('SEUM', -1, 3), undefined);
  })


  // SUBSTRACT

  it('should return -2 when substracting 1 and 3', function() {
    assert.strictEqual(calculateNumber('SUBSTRACT', 1, 3), -2);
  });
  
  it('should return -2 when substracting 1 and PI', function() {
    assert.strictEqual(calculateNumber('SUBSTRACT', 1, Math.PI), -2);
  });

  it('should return -3 when substracting 1 and 3.7', function() {
    assert.strictEqual(calculateNumber('SUBSTRACT', 1, 3.7), -3);
  });

  it('should return -3 when substracting 1.2 and 3.7', function() {
    assert.strictEqual(calculateNumber('SUBSTRACT', 1.2, 3.7), -3);
  });

  it('should return -2 when substracting 1.5 and 3.7', function() {
    assert.strictEqual(calculateNumber('SUBSTRACT', 1.5, 3.7), -2);
  });

  it('should return 4 when substracting 1 and -3', () => {
    assert.equal(calculateNumber('SUBSTRACT', 1, -3), 4);
  });

  it('should return -4 when substracting -1 and 3', () => {
    assert.equal(calculateNumber('SUBSTRACT', -1, 3), -4);
  })


  // DIVIDE

  it('should return 4 when divide 1 and 3', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 1, 3), 0.3333333333333333);
  });
  
  it('should return 4 when divide 1 and PI', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 1, Math.PI), 0.3333333333333333);
  });

  it('should return 5 when divide 1 and 3.7', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 1, 3.7), 0.25);
  });

  it('should return 5 when divide 1.2 and 3.7', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 1.2, 3.7), 0.25);
  });

  it('should return 6 when divide 1.5 and 3.7', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 1.5, 3.7), 0.5);
  });

  it('should return -2 when divide 1 and -3', () => {
    assert.equal(calculateNumber('DIVIDE', 1, -3), -0.3333333333333333);
  });

  it('should return 2 when divide -1 and 3', () => {
    assert.equal(calculateNumber('DIVIDE', -1, 3), -0.3333333333333333);
  })

  it('should return -Infinity when divide -1 and 0', () => {
    assert.equal(calculateNumber('DIVIDE', -1, 0), 'Error');
  })

  it('should return Infinity when divide 1 and 0', () => {
    assert.equal(calculateNumber('DIVIDE', 1, 0), 'Error');
  })

  it('should return NaN when divide 0 and 0', () => {
    assert.equal(calculateNumber('DIVIDE', 0, 0), 'Error');
  })
});
