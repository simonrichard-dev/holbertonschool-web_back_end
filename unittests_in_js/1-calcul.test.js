// 1-calcul.test.js
const assert = require('assert');
const calculateNumber = require('./1-calcul');


// SUM

describe('calculateNumber testing SUM', function() {

  it('returns the good result when add two pos numbers', function() {
    assert.equal(calculateNumber('SUM', 1, 2.8), 4);
    assert.equal(calculateNumber('SUM', 1, Math.PI), 4);
  });

  it('returns the good result when add a neg and a pos number', function() {
    assert.equal(calculateNumber('SUM', 1, -3), -2);
    assert.equal(calculateNumber('SUM', -1, 3), 2);
  });

  it('returns the good result add two neg numbers', function() {
    assert.equal(calculateNumber('SUM', -1, -3.7), -5);
    assert.equal(calculateNumber('SUM', -1.6, -3.7), -6);
  });

  it('Correctly returns an error for invalid input types', function() {
    assert.throws(() => calculateNumber('SUM', "a", 2), Error);
    assert.throws(() => calculateNumber('SUM', 2, "b"), Error);
  })
});


// SUBSTRACT

describe('calculateNumber testing SUBSTRACT', function() {

  it('returns the good result when substract two pos numbers', function() {
    assert.equal(calculateNumber('SUBSTRACT', 1, 3.2), -2);
    assert.equal(calculateNumber('SUBSTRACT', 6, 4), 2);
  });

  it('returns the good result when substract a neg and a pos number', function() {
    assert.equal(calculateNumber('SUBSTRACT', 1, -3), 4);
    assert.equal(calculateNumber('SUBSTRACT', -1, 3), -4);
  });

  it('returns the good result substract two neg numbers', function() {
    assert.equal(calculateNumber('SUBSTRACT', -1, -3.7), 3);
    assert.equal(calculateNumber('SUBSTRACT', -10, -4), -6);
  });

  it('Correctly returns an error for invalid input types', function() {
    assert.throws(() => calculateNumber('SUBSTRACT', "a", 2), Error);
    assert.throws(() => calculateNumber('SUBSTRACT', 2, "b"), Error);
  })
});


// DIVIDE

describe('calculateNumber testing DIVIDE', function() {

  it('returns the good result dividing two pos numbers', function() {
    assert.equal(calculateNumber('DIVIDE', 6, 2), 3);
    assert.equal(calculateNumber('DIVIDE', Math.PI, 1), 3);
  });

  it('returns the good result dividing a neg and a pos number', () => {
    assert.equal(calculateNumber('DIVIDE', -4, 2.2), -2);
    assert.equal(calculateNumber('DIVIDE', -1.6, 3.7), -0.5);
  });

  it('returns the good result dividing two neg numbers', function() {
    assert.equal(calculateNumber('DIVIDE', -4, -2.2), 2);
    assert.equal(calculateNumber('DIVIDE', -1.6, -3.7), 0.5);
  });

  it('Correctly returns an error for invalid input types', function() {
    assert.throws(() => calculateNumber('DIVIDE', "a", 2), Error);
    assert.throws(() => calculateNumber('DIVIDE', 2, "b"), Error);
  })
});
