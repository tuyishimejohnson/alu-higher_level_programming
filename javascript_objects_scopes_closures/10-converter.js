#!/usr/bin/node
exports.converter = function(base) {
  return function convertToBase(number) {
    return number === 0 ? '0' : (number < 0 ? '-' : '') + convert(Math.abs(number));

    function convert(number) {
      const digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
      const baseDigits = digits.slice(0, base);

      let result = '';
      while (number > 0) {
        result = baseDigits[number % base] + result;
        number = Math.floor(number / base);
      }
      return result;
    }
  };
};
