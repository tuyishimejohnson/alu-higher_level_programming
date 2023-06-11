#!/usr/bin/node
exports.converter = function (base) {
  return function convertToBase(number) {
    if (number === 0) {
      return '0';
    }

    let result = '';
    while (number > 0) {
      result = (number % base) + result;
      number = Math.floor(number / base);
    }

    return result;
  };
};
