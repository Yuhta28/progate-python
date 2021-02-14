const sum = require('./sum');
Test('adds 1 + 2 to equal 3', () => {
    expect(sum(1, 2)).toBe(3);
});