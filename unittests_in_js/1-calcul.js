/**
 *
 * @param {string} type
 * @param {number} a
 * @param {number} b
 * @returns the result of the operation
 */

function calculateNumber(type, a, b) {
  if (typeof a !== 'number' || typeof b !== 'number') {
    throw new Error('Invalid input');
  }
  if (type === 'SUM') {
    return Math.round(a) + Math.round(b);
  } else if (type === 'SUBSTRACT') {
    return Math.round(a) - Math.round(b);
  } else if (type === 'DIVIDE') {
      if (Math.round(b) === 0) {
          return 'Error';
      } else {
          return Math.round(a) / Math.round(b);
      }
  }
}

module.exports = calculateNumber;
